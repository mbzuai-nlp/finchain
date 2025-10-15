// This object manages everything related to the chart view.
const ChartController = {
    chartInstance: null,
    yAxisMetric: 'chain_eval',
    highlightedIndex: null,

    // Color mapping for model categories for consistent styling
    categoryColors: {
        'Finance Specific': 'rgba(40, 167, 69, 0.8)',
        'Math Enhanced': 'rgba(255, 193, 7, 0.9)',
        'General Purpose Open': 'rgba(220, 53, 69, 0.8)'
    },

    /**
     * Prepares filtered data into the format Chart.js expects, adding "jitter".
     */
    prepareDatasets: function(filteredModels) {
        const datasets = {};
        const jitterStrength = 0.09;

        filteredModels.forEach(model => {
            if (!model.size_b) return;

            if (!datasets[model.category]) {
                datasets[model.category] = {
                    label: model.category,
                    data: [],
                    backgroundColor: this.categoryColors[model.category] || 'rgba(108, 117, 125, 0.7)',
                    pointRadius: 7,
                    pointHoverRadius: 10,
                };
            }

            datasets[model.category].data.push({
                x: model.size_b + (Math.random() - 0.5) * jitterStrength,
                y: model.scores[this.yAxisMetric],
                modelData: model,
            });
        });
        return Object.values(datasets);
    },

    /**
     * Creates or updates the chart with new data and settings.
     */
    update: function(filteredModels, allModels) {
        const canvas = document.getElementById('leaderboard-chart');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        if (this.chartInstance) {
            this.chartInstance.destroy();
        }

        const datasets = this.prepareDatasets(filteredModels);

        this.chartInstance = new Chart(ctx, {
            type: 'scatter',
            data: { datasets },
            plugins: [ChartDataLabels],
            options: {
                responsive: true,
                maintainAspectRatio: false,
                // --- NEW: ONHOVER LOGIC FOR CROSSHAIRS ---
                onHover: (event, elements) => {
                    const annotations = this.chartInstance.options.plugins.annotation.annotations;
                    // When a point is hovered
                    if (elements.length > 0) {
                        const hoveredPoint = elements[0].element.$context.raw;
                        // Update and show the crosshair lines and labels
                        annotations.hoverXLine.value = hoveredPoint.x;
                        annotations.hoverXLine.label.content = hoveredPoint.modelData.size_display;
                        annotations.hoverYLine.value = hoveredPoint.y;
                        annotations.hoverYLine.label.content = hoveredPoint.y.toFixed(2);
                        annotations.hoverXLine.display = true;
                        annotations.hoverYLine.display = true;
                    } else {
                        // Hide crosshairs when not hovering a point
                        annotations.hoverXLine.display = false;
                        annotations.hoverYLine.display = false;
                    }
                    this.chartInstance.update('none'); // Update chart without animation
                },
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom',
                        title: { display: true, text: 'Model Size (Billions of Parameters)', font: { size: 14 } }
                    },
                    y: {
                        title: { display: true, text: document.getElementById('y-axis-select').options[document.getElementById('y-axis-select').selectedIndex].text, font: { size: 14 } }
                    }
                },
                plugins: {
                    datalabels: {
                        display: 'auto', align: 'top', offset: 8,
                        font: { size: 10, weight: '500' }, color: '#555',
                        formatter: (value) => value.modelData.model_name
                    },
                    legend: { position: 'top' },
                    tooltip: {
                        callbacks: {
                            label: (context) => {
                                const model = context.raw.modelData;
                                return [
                                    `${model.model_name} (${model.size_display})`, `Category: ${model.category}`, `--------------------`,
                                    `ChainEval: ${model.scores.chain_eval.toFixed(2)}`, `ROUGE R₂: ${model.scores.rouge_r2.toFixed(2)}`,
                                    `BERTScore: ${model.scores.bertscore.toFixed(2)}`,
                                ];
                            }
                        }
                    },
                    annotation: {
                        annotations: this.getBenchmarkAnnotations(allModels)
                    },
                    zoom: {
                        pan: { enabled: true, mode: 'xy' },
                        zoom: { wheel: { enabled: true }, pinch: { enabled: true }, mode: 'xy' }
                    }
                },
                onClick: (event, elements) => {
                    if (elements.length > 0) {
                        const clickedIndex = elements[0].datasetIndex + '_' + elements[0].index;
                        this.highlightedIndex = this.highlightedIndex === clickedIndex ? null : clickedIndex;
                    } else {
                        if (this.chartInstance.isZoomedOrPanned()) {
                             this.chartInstance.resetZoom();
                        } else {
                            this.highlightedIndex = null;
                        }
                    }
                    this.chartInstance.update('none');
                },
                elements: {
                    point: {
                        radius: (context) => {
                            const currentIndex = context.datasetIndex + '_' + context.dataIndex;
                            return this.highlightedIndex === currentIndex ? 12 : 7;
                        },
                        borderWidth: (context) => {
                            const currentIndex = context.datasetIndex + '_' + context.dataIndex;
                            return this.highlightedIndex === currentIndex ? 4 : 1;
                        },
                        borderColor: (context) => {
                             const currentIndex = context.datasetIndex + '_' + context.dataIndex;
                             return this.highlightedIndex === currentIndex ? 'rgba(0, 0, 0, 0.5)' : 'rgba(255, 255, 255, 0.8)';
                        }
                    }
                }
            }
        });
    },

    /**
     * Generates annotation objects, NOW INCLUDING THE HIDDEN CROSSHAIRS.
     */
    getBenchmarkAnnotations: function(allModels) {
        const annotations = {
            // --- NEW: INITIAL DEFINITION FOR HOVER LINES ---
            hoverXLine: {
                type: 'line',
                scaleID: 'x',
                display: false, // Hidden by default
                borderColor: 'rgba(0, 0, 0, 0.5)',
                borderWidth: 1,
                borderDash: [4, 4],
                label: { enabled: true, content: '', position: 'start', backgroundColor: 'rgba(0, 0, 0, 0.7)' }
            },
            hoverYLine: {
                type: 'line',
                scaleID: 'y',
                display: false, // Hidden by default
                borderColor: 'rgba(0, 0, 0, 0.5)',
                borderWidth: 1,
                borderDash: [4, 4],
                label: { enabled: true, content: '', position: 'start', backgroundColor: 'rgba(0, 0, 0, 0.7)' }
            }
        };
        
        if (document.querySelector('[data-benchmark="gpt5"]').checked) {
            const gpt5 = allModels.find(m => m.model_name === "GPT-5");
            if (gpt5) {
                 annotations.gpt5Line = {
                    type: 'line', yMin: gpt5.scores[this.yAxisMetric], yMax: gpt5.scores[this.yAxisMetric],
                    borderColor: 'rgba(0, 123, 255, 0.5)', borderWidth: 2, borderDash: [6, 6],
                    label: { content: 'GPT-5', enabled: true, position: 'start', yAdjust: -15, backgroundColor: 'rgba(0, 123, 255, 0.7)' }
                };
            }
        }

        if (document.querySelector('[data-benchmark="best_open"]').checked) {
            const bestOpen = allModels
                .filter(m => m.category !== 'Frontier Proprietary' && m.size_b)
                .sort((a, b) => b.scores[this.yAxisMetric] - a.scores[this.yAxisMetric])[0];
            if (bestOpen) {
                annotations.bestOpenLine = {
                    type: 'line', yMin: bestOpen.scores[this.yAxisMetric], yMax: bestOpen.scores[this.yAxisMetric],
                    borderColor: 'rgba(220, 53, 69, 0.5)', borderWidth: 2, borderDash: [6, 6],
                    label: { content: `Best Open: ${bestOpen.model_name}`, enabled: true, position: 'end', yAdjust: 15, backgroundColor: 'rgba(220, 53, 69, 0.7)' }
                };
            }
        }
        return annotations;
    },

    /**
     * Initializes event listeners for the chart's specific controls.
     */
    initialize: function() {
        Chart.register(ChartDataLabels); // Register plugin globally

        const yAxisSelect = document.getElementById('y-axis-select');
        yAxisSelect.addEventListener('change', (e) => {
            this.yAxisMetric = e.target.value;
            window.renderDashboard();
        });

        const benchmarkToggles = document.querySelector('.benchmark-toggles');
        benchmarkToggles.addEventListener('change', () => {
             window.renderDashboard();
        });
    }
};

// Initialize the chart controller when the DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    ChartController.initialize();
});