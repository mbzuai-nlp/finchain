import random

# Named Entities
investor_names = ["Alice Johnson", "Michael Chen", "Nina Patel", "Carlos Rivera", "Olivia Thompson"]
company_names = [
    "JP Morgan Chase", "Goldman Sachs", "Wells Fargo", "Citibank", "Bank of America",
    "Morgan Stanley", "Capital One", "US Bancorp", "PNC Financial", "American Express"
]


def template_compliance_basic_fine_calculation():
    """1:Basic: Calculate total fine from multiple types of AML violations with tiered penalties"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    # Different types of violations with different fine rates
    violation_types = {
        "Failure to file SARs": random.randint(1, 3),
        "Structuring detection failure": random.randint(1, 2),
        "Incomplete customer due diligence": random.randint(1, 3)
    }

    fine_rates = {
        "Failure to file SARs": 100_000,
        "Structuring detection failure": 75_000,
        "Incomplete customer due diligence": 50_000
    }

    # Calculate total fine
    fine_breakdown = []
    total_fine = 0
    for v_type, count in violation_types.items():
        fine = count * fine_rates[v_type]
        fine_breakdown.append(f"{count} × ${fine_rates[v_type]} for {v_type} = ${fine}")
        total_fine += fine

    question = (
        f"{company} was found to have committed several types of AML violations:\n"
        + "\n".join([f"  - {v_type}: {count} instance(s)" for v_type, count in violation_types.items()]) +
        f"\nThe fine rates are:\n"
        + "\n".join([f"  - {v_type}: ${fine_rates[v_type]} per violation" for v_type in fine_rates]) +
        "\nWhat is the total fine?"
    )

    solution = (
        "Step 1: Calculate fine for each violation type:\n" +
        "\n".join([f"  - {line}" for line in fine_breakdown]) +
        f"\nStep 2: Add all fines together:\n  Total fine = ${total_fine}"
    )

    return question, solution



def template_compliance_basic_risk_score():
    """2:Basic: Risk score calculation"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    likelihood = random.randint(1, 5)
    impact = random.randint(1, 5)
    detectability = random.randint(1, 5)
    question = (
        f"{investor} assesses {company}'s compliance risk using a Risk Priority Number (RPN), calculated as:\n"
        f"  RPN = Likelihood × Impact × Detectability\n"
        f"Given: Likelihood = {likelihood}, Impact = {impact}, Detectability = {detectability}\n"
        f"What is the RPN?"
    )
    rpn = likelihood * impact * detectability
    solution = (
        f"Step 1: Multiply all risk factors:\n"
        f"  {likelihood} × {impact} × {detectability} = {rpn}\n"
        f"Answer: RPN = {rpn}"
    )
    return question, solution


def template_compliance_intermediate_delayed_compliance_fine():
    """3:Intermediate: Fine escalation with multiple delay types and tiered logic"""

    investor = random.choice(investor_names)
    company = random.choice(company_names)
    base_fine = 20000

    # Two types of delay
    reporting_delay = random.randint(1, 5)
    correction_delay = random.randint(0, 4)  # Optional second delay

    # Define tiered rates for each
    def fine_rate(days):
        if days == 0:
            return 0
        elif days <= 2:
            return random.randint(1000, 2000)
        elif days <= 4:
            return random.randint(3000, 5000)
        else:
            return random.randint(7000, 9000)

    reporting_fine_per_day = fine_rate(reporting_delay)
    correction_fine_per_day = fine_rate(correction_delay)

    reporting_penalty = reporting_delay * reporting_fine_per_day
    correction_penalty = correction_delay * correction_fine_per_day
    total_penalty = base_fine + reporting_penalty + correction_penalty

    # Optional administrative surcharge
    admin_fee = 2500 if correction_delay > 0 else 0
    total_due = total_penalty + admin_fee

    question = (
        f"{company} received a base AML fine of ${base_fine:,}.\n"
        f"It submitted its AML report {reporting_delay} days late and corrected discrepancies {correction_delay} days after the notice.\n"
        f"Penalty rates are tiered based on delay length:\n"
        f"- Reporting delay penalty: ${reporting_fine_per_day:,}/day\n"
        f"- Correction delay penalty: ${correction_fine_per_day:,}/day\n"
        f"An additional administrative fee of ${admin_fee:,} applies {'due to correction delay' if admin_fee else 'since all corrections were timely'}.\n"
        f"What is the total fine owed by {company}?"
    )

    solution = (
        f"Step 1: Reporting penalty = {reporting_delay} × ${reporting_fine_per_day:,} = ${reporting_penalty:,}\n"
        f"Step 2: Correction penalty = {correction_delay} × ${correction_fine_per_day:,} = ${correction_penalty:,}\n"
        f"Step 3: Add base fine: ${base_fine:,} + penalties (${reporting_penalty:,} + ${correction_penalty:,}) = ${total_penalty:,}\n"
        f"Step 4: Add administrative fee = ${admin_fee:,}\n"
        f"Total Fine = ${total_due:,}"
    )

    return question, solution



# Weighted risk of regions
def template_compliance_intermediate_regional_risk_weighted_score():
    """4:Intermediate: Compute weighted risk score and evaluate monitoring requirement"""

    investor = random.choice(investor_names)
    company = random.choice(company_names)

    # Expanded region pool
    region_pool = ["North America", "South America", "Europe", "Asia", "Africa", "Middle East", "Oceania"]
    selected_regions = random.sample(region_pool, k=random.randint(4, 6))

    # Random weights and normalization
    raw_weights = [round(random.uniform(0.1, 0.6), 2) for _ in selected_regions]
    weight_sum = sum(raw_weights)
    weights = [round(w / weight_sum, 2) for w in raw_weights]
    weights[-1] = round(1.0 - sum(weights[:-1]), 2)  # Ensure total = 1.0

    # Assign risk scores to each region (1–10 scale)
    risks = [random.randint(3, 10) for _ in selected_regions]
    weighted_components = [round(w * r, 2) for w, r in zip(weights, risks)]
    weighted_risk = round(sum(weighted_components), 2)

    # Determine enhanced monitoring condition
    enhanced_monitoring_required = weighted_risk > 6.5

    # Determine if more than 30% of exposure is in high-risk regions (score ≥ 8)
    high_risk_weights = [weights[i] for i in range(len(selected_regions)) if risks[i] >= 8]
    high_risk_exposure = round(sum(high_risk_weights), 2)
    high_exposure_triggered = high_risk_exposure > 0.3

    # Final decision
    needs_monitoring = enhanced_monitoring_required or high_exposure_triggered

    question = (
        f"{company} is assessing its regional compliance risk exposure across the following regions:\n"
        f"Regions: {', '.join(selected_regions)}\n"
        f"Weights: {weights}\n"
        f"Risk Scores: {risks}\n"
        f"Determine:\n"
        f"1. The weighted average risk score\n"
        f"2. Whether enhanced monitoring is required based on the following rules:\n"
        f"   - Weighted risk score > 6.5 → Enhanced monitoring\n"
        f"   - If more than 30% of risk exposure is in regions with risk score ≥ 8 → Enhanced monitoring\n"
    )

    # Construct reasoning chain
    step1 = "Step 1: Multiply weight × risk for each region:"
    region_lines = [
        f"  {selected_regions[i]}: {weights[i]} × {risks[i]} = {weighted_components[i]}"
        for i in range(len(selected_regions))
    ]

    step2 = f"Step 2: Sum all weighted risks = {weighted_risk}"
    step3 = f"Step 3: Weighted score {'exceeds' if enhanced_monitoring_required else 'does not exceed'} 6.5 → {'✓' if enhanced_monitoring_required else '✗'}"

    step4 = (
        f"Step 4: High-risk regions (score ≥ 8): Exposure = {high_risk_exposure:.2f} → "
        f"{'✓ (over 30%)' if high_exposure_triggered else '✗ (not over 30%)'}"
    )

    step5 = (
        f"Final conclusion: {'Enhanced monitoring required' if needs_monitoring else 'Standard monitoring sufficient'}"
    )

    solution = "\n".join([step1] + region_lines + [step2, step3, step4, step5])

    return question, solution




def template_compliance_advanced_composite_risk_rating():
    """5:Advanced: Compute and interpret composite risk rating with exposure-based decision logic"""

    investor = random.choice(investor_names)
    company = random.choice(company_names)

    all_categories = [
        "Customer", "Transaction", "Geography", "Product", "Delivery Channel", "Account Type"
    ]
    selected_categories = random.sample(all_categories, k=random.randint(4, 6))

    scores = [random.randint(1, 5) for _ in selected_categories]
    raw_weights = [round(random.uniform(0.1, 0.6), 2) for _ in selected_categories]
    weight_sum = sum(raw_weights)
    weights = [round(w / weight_sum, 2) for w in raw_weights]
    weights[-1] = round(1.0 - sum(weights[:-1]), 2)

    weighted_scores = [round(s * w, 2) for s, w, in zip(scores, weights)]
    composite = round(sum(weighted_scores), 2)

    # Tag risks and extract exposure info
    risk_tags = []
    high_risk_weight = 0
    for score, weight in zip(scores, weights):
        if score >= 4:
            tag = "High"
            high_risk_weight += weight
        elif score == 3:
            tag = "Medium"
        else:
            tag = "Low"
        risk_tags.append(tag)

    high_risk_exposure_pct = round(high_risk_weight * 100, 2)

    # Threshold-based conclusion
    composite_threshold = 3.5
    high_risk_flag = composite >= composite_threshold or high_risk_weight > 0.5
    final_rating = "High Risk" if high_risk_flag else "Moderate or Low Risk"

    # Question prompt
    question = (
        f"{investor} has assessed {company}'s risk profile using the following criteria:\n\n"
        + "Scores and weights:\n"
        + "\n".join([
            f"  {cat} Risk = {scores[i]} (weight: {weights[i]})"
            for i, cat in enumerate(selected_categories)
        ])
        + "\n\nCompute the composite risk score and determine whether the customer should be classified as High Risk using the following rules:\n"
        + "- Composite Score ≥ 3.5 → High Risk\n"
        + "- OR: If over 50% of weight is allocated to categories with High individual risk (score ≥ 4)"
    )

    # Step-by-step solution
    steps = []

    steps.append("Step 1: Multiply score × weight for each dimension:")
    for i in range(len(selected_categories)):
        steps.append(f"  {selected_categories[i]}: {scores[i]} × {weights[i]} = {weighted_scores[i]} → {risk_tags[i]} Risk")

    steps.append(f"\nStep 2: Sum of weighted scores = {composite}")
    steps.append(f"Step 3: Composite threshold check → {composite} {'≥' if composite >= composite_threshold else '<'} {composite_threshold} → {'✓' if composite >= composite_threshold else '✗'}")

    steps.append(f"Step 4: Weight in High-Risk dimensions = {high_risk_exposure_pct}%")
    steps.append(f"Step 5: Exposure threshold check → {high_risk_exposure_pct}% {'>' if high_risk_exposure_pct > 50 else '<='} 50% → {'✓' if high_risk_exposure_pct > 50 else '✗'}")

    steps.append("Final Risk Classification → " + final_rating)

    solution = "\n".join(steps)

    return question, solution




def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # ----------- Export All to JSONL -----------

    # List of template functions
    templates = [
        template_compliance_basic_fine_calculation,
        template_compliance_basic_risk_score,
        template_compliance_intermediate_delayed_compliance_fine,
        template_compliance_intermediate_regional_risk_weighted_score,
        template_compliance_advanced_composite_risk_rating
    ]

    # List to store all generated problems
    all_problems = []

    # Generate 10 problems for each template
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        
        for i in range(10):
            # Generate a unique seed for each problem
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            
            # Generate the problem and solution
            question, solution = template_func()
            
            # Create a JSON entry
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            
            # Add to the list of problems
            all_problems.append(problem_entry)
            
            # Reset the random seed
            random.seed()

    random.shuffle(all_problems)
    # Write all problems to a .jsonl file
    output_file = "../../testset/finance_regulation/compliance.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")


if __name__ == "__main__":
   main()