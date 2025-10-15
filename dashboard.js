document.addEventListener('DOMContentLoaded', () => {

    // --- STATE MANAGEMENT ---
    let state = {
        // MODIFIED: Full dataset is the default
        models: finchainData,
        // MODIFIED: Default filter is now 'all'
        activeCategory: 'all',
        searchQuery: '',
        sort: { by: 'chain_eval', order: 'desc' }
    };

    // --- DOM ELEMENT REFERENCES ---
    const tableBody = document.getElementById('leaderboard-body');
    const categoryFilters = document.querySelector('.category-filters');
    const searchInput = document.getElementById('search-input');
    const tableHeaders = document.querySelectorAll('.leaderboard-table thead th');

    // --- GLOBAL RENDER FUNCTION ---
    window.renderDashboard = () => {
        let processedModels;

        // --- MODIFIED: Simplified filter logic ---
        if (state.activeCategory === 'all') {
            processedModels = [...state.models]; // Show all models
        } else {
            // Show only a specific category
            processedModels = state.models.filter(model => model.category === state.activeCategory);
        }

        if (state.searchQuery) {
            processedModels = processedModels.filter(model =>
                model.model_name.toLowerCase().includes(state.searchQuery.toLowerCase())
            );
        }
        
        renderTable(processedModels);
        ChartController.update(processedModels, finchainData);
    };

    // --- TABLE-SPECIFIC RENDER FUNCTION (Unchanged) ---
    const renderTable = (modelsToRender) => {
        modelsToRender.sort((a, b) => {
            let valA, valB;
            if (['chain_eval', 'rouge_r2', 'rouge_rl', 'bertscore'].includes(state.sort.by)) {
                valA = a.scores[state.sort.by];
                valB = b.scores[state.sort.by];
            } else {
                valA = state.sort.by === 'size_b' ? (a.size_b || 0) : a.model_name.toLowerCase();
                valB = state.sort.by === 'size_b' ? (b.size_b || 0) : b.model_name.toLowerCase();
            }
            if (valA < valB) return state.sort.order === 'asc' ? -1 : 1;
            if (valA > valB) return state.sort.order === 'asc' ? 1 : -1;
            return 0;
        });

        tableBody.innerHTML = '';
        if (modelsToRender.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding: 2rem;">No models match the current filters.</td></tr>`;
            return;
        }

        const rankEmojis = ['🥇', '🥈', '🥉'];
        modelsToRender.forEach((model, index) => {
            const row = document.createElement('tr');
            row.style.cursor = 'pointer';
            row.addEventListener('click', () => showModal(model));
            row.innerHTML = `
                <td>${rankEmojis[index] || index + 1}</td>
                <td class="model-name">${model.model_name}</td>
                <td>${model.size_display}</td>
                <td title="Std Dev: ±${model.scores.chain_eval_std.toFixed(2)}">${model.scores.chain_eval.toFixed(2)}</td>
                <td title="Std Dev: ±${model.scores.rouge_r2_std.toFixed(2)}">${model.scores.rouge_r2.toFixed(2)}</td>
                <td title="Std Dev: ±${model.scores.rouge_rl_std.toFixed(2)}">${model.scores.rouge_rl.toFixed(2)}</td>
                <td title="Std Dev: ±${model.scores.bertscore_std.toFixed(2)}">${model.scores.bertscore.toFixed(2)}</td>
            `;
            tableBody.appendChild(row);
        });
    };

    // --- EVENT LISTENERS (Unchanged) ---
    categoryFilters.addEventListener('click', (e) => {
        if (e.target.tagName === 'BUTTON') {
            categoryFilters.querySelector('.active').classList.remove('active');
            e.target.classList.add('active');
            state.activeCategory = e.target.dataset.category;
            window.renderDashboard();
        }
    });

    searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        window.renderDashboard();
    });

    tableHeaders.forEach(header => {
        const keyMap = {
            'Model': 'model_name', 'Size': 'size_b', 'ChainEval ↑': 'chain_eval',
            'ROUGE R₂ ↑': 'rouge_r2', 'ROUGE Rₗ ↑': 'rouge_rl', 'BERTScore ↑': 'bertscore'
        };
        const sortKey = keyMap[header.textContent];
        if (sortKey) {
            header.addEventListener('click', () => {
                if (state.sort.by === sortKey) {
                    state.sort.order = state.sort.order === 'desc' ? 'asc' : 'desc';
                } else {
                    state.sort.by = sortKey;
                    state.sort.order = 'desc';
                }
                window.renderDashboard();
            });
        }
    });
    
    // --- MODAL FUNCTIONALITY & CSS INJECTION (Unchanged) ---
    const showModal = (model) => {
        const existingModal = document.querySelector('.modal-overlay');
        if (existingModal) existingModal.remove();
        const modalOverlay = document.createElement('div');
        modalOverlay.className = 'modal-overlay';
        const modalContent = document.createElement('div');
        modalContent.className = 'modal-content';
        modalContent.innerHTML = `
            <button class="modal-close">&times;</button>
            <h2>${model.model_name}</h2>
            <p><strong>Category:</strong> ${model.category} &nbsp;|&nbsp; <strong>Size:</strong> ${model.size_display}</p>
            <hr>
            <h3>Performance Scores</h3>
            <ul>
                <li><strong>ChainEval:</strong> ${model.scores.chain_eval.toFixed(2)} (±${model.scores.chain_eval_std.toFixed(2)})</li>
                <li><strong>ROUGE R₂:</strong> ${model.scores.rouge_r2.toFixed(2)} (±${model.scores.rouge_r2_std.toFixed(2)})</li>
                <li><strong>ROUGE Rₗ:</strong> ${model.scores.rouge_rl.toFixed(2)} (±${model.scores.rouge_rl_std.toFixed(2)})</li>
                <li><strong>BERTScore:</strong> ${model.scores.bertscore.toFixed(2)} (±${model.scores.bertscore_std.toFixed(2)})</li>
            </ul>
            <a href="${model.source_link}" target="_blank" rel="noopener noreferrer" class="modal-link">Learn More at Source</a>
        `;
        modalOverlay.appendChild(modalContent);
        document.body.appendChild(modalOverlay);
        modalOverlay.addEventListener('click', e => {
            if (e.target === modalOverlay) modalOverlay.remove();
        });
        modalContent.querySelector('.modal-close').addEventListener('click', () => modalOverlay.remove());
    };

    const injectModalCSS = () => {
        if (document.getElementById('modal-styles')) return;
        const style = document.createElement('style');
        style.id = 'modal-styles';
        style.textContent = `
            .modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.6); display: flex; align-items: center; justify-content: center; z-index: 1000; backdrop-filter: blur(5px); }
            .modal-content { background: white; padding: 2rem 2.5rem; border-radius: 12px; width: 90%; max-width: 500px; position: relative; box-shadow: 0 10px 30px rgba(0,0,0,0.2); animation: modal-fade-in 0.3s ease-out; }
            @keyframes modal-fade-in { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
            .modal-close { position: absolute; top: 10px; right: 15px; font-size: 2rem; background: none; border: none; cursor: pointer; color: #aaa; line-height: 1; }
            .modal-content h2 { margin-top: 0; } .modal-content hr { margin: 1rem 0; } .modal-content ul { padding-left: 20px; }
            .modal-link { display: inline-block; margin-top: 1.5rem; padding: 0.6rem 1.2rem; background-color: #007bff; color: white; text-decoration: none; border-radius: 8px; font-weight: 500; transition: background-color 0.2s; }
            .modal-link:hover { background-color: #0056b3; }
        `;
        document.head.appendChild(style);
    };

    // --- INITIALIZATION ---
    injectModalCSS();
    window.renderDashboard(); // Initial render
});