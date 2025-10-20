import random

investor_names = ["John Doe", "Alice Johnson", "Michael Chen", "Emily Davis", "Robert Lee"]
company_names = ["JP Morgan", "Goldman Sachs", "Bank of America", "Citigroup", "Wells Fargo", "Morgan Stanley"]

# ----------------------- BASIC QUESTIONS -----------------------

def template_basel_basic_leverage_ratio_test():
    """1:Basic: Leverage Ratio Computation"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    tier1 = round(random.uniform(5, 10), 2)
    total_exposure = round(random.uniform(100, 200), 2)
    ratio = round((tier1 / total_exposure) * 100, 2)

    question = (
        f"{investor} is assessing {company}'s leverage ratio. "
        f"The bank has Tier 1 capital of ${tier1} million and total exposure of ${total_exposure} million. "
        f"What is the leverage ratio and does it meet the Basel III minimum of 3%?"
    )

    solution = (
        f"Step 1: Leverage Ratio = (Tier 1 / Total Exposure) × 100\n"
        f"        = ({tier1} / {total_exposure}) × 100 = {ratio:.2f}%\n"
        f"Step 2: Compare with Basel minimum of 3% → {'Yes' if ratio >= 3 else 'No'}"
    )

    return question, solution


def template_basel_basic_tier_composition_analysis():
    """2:Basic: Capital Ratio Decomposition"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    tier1 = round(random.uniform(5, 10), 2)
    tier2 = round(random.uniform(2, 5), 2)
    rwa = round(random.uniform(70, 120), 2)
    total_ratio = round(((tier1 + tier2) / rwa) * 100, 2)
    tier1_ratio = round((tier1 / rwa) * 100, 2)

    question = (
        f"{investor} examines {company}'s capital composition. The Tier 1 capital is ${tier1} million, Tier 2 is ${tier2} million, "
        f"and risk-weighted assets are ${rwa} million. Calculate the total capital ratio and Tier 1 ratio."
    )

    solution = (
        f"Step 1: Tier 1 Ratio = ({tier1} / {rwa}) × 100 = {tier1_ratio:.2f}%\n"
        f"Step 2: Total Capital Ratio = ({round(tier1 + tier2, 2)} / {rwa}) × 100 = {total_ratio:.2f}%"
    )
    return question, solution

# ----------------------- INTERMEDIATE QUESTIONS -----------------------

def template_basel_intermediate_capital_buffer_requirement():
    """3:Intermediate: Evaluate if a bank meets Basel III capital buffer requirements with randomized inputs"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    # Random minimum capital ratio and buffer (varied difficulty)
    min_ratio = round(random.uniform(7.5, 9.0), 1)
    buffer_required = round(random.uniform(1.5, 3.0), 1)
    required_total = round(min_ratio + buffer_required, 2)

    # Randomize the bank's ratio to be slightly above or below the requirement
    if random.random() < 0.5:
        # Case: Meets the requirement
        total_ratio = round(random.uniform(required_total, required_total + 1.0), 2)
        meets_requirement = True
    else:
        # Case: Does not meet the requirement
        total_ratio = round(random.uniform(required_total - 1.5, required_total - 0.01), 2)
        meets_requirement = False

    question = (
        f"{investor} is examining whether {company} meets the capital conservation buffer requirements. "
        f"The bank's capital adequacy ratio is {total_ratio}%. "
        f"Under Basel III, the minimum ratio is {min_ratio}% and the buffer required is {buffer_required}%. "
        f"Does the bank meet the full requirement?"
    )

    solution = (
        f"Step 1: Calculate Total Required Ratio = Minimum + Buffer = {min_ratio}% + {buffer_required}% = {required_total}%\n"
        f"Step 2: Compare Bank’s Ratio: {total_ratio}% {'>=' if meets_requirement else '<'} {required_total}%\n\n"
        f"Step 3: Conclusion: {'Yes' if meets_requirement else 'No'}, the bank {'meets' if meets_requirement else 'does not meet'} the full capital requirement."
    )

    return question, solution


def template_basel_intermediate_rwa_increase_effect():
    """4:Intermediate+: Analyze capital adequacy with changes in both capital and RWA, and interpret the direction and cause of change"""

    investor = random.choice(investor_names)
    company = random.choice(company_names)

    # Initial values
    capital_initial = round(random.uniform(10, 20), 2)
    rwa_initial = round(random.uniform(80, 100), 2)
    ratio_initial = round((capital_initial / rwa_initial) * 100, 2)

    # Changes
    capital_change_type = random.choice(["increase", "decrease", "same"])
    rwa_change_type = random.choice(["increase", "decrease", "same"])

    # Apply changes to capital
    if capital_change_type == "increase":
        capital_new = round(capital_initial + random.uniform(1, 5), 2)
    elif capital_change_type == "decrease":
        capital_new = round(capital_initial - random.uniform(1, 5), 2)
    else:
        capital_new = capital_initial

    # Apply changes to RWA
    if rwa_change_type == "increase":
        rwa_new = round(rwa_initial + random.uniform(5, 20), 2)
    elif rwa_change_type == "decrease":
        rwa_new = round(rwa_initial - random.uniform(5, 20), 2)
    else:
        rwa_new = rwa_initial

    ratio_new = round((capital_new / rwa_new) * 100, 2)
    direction = (
        "increased" if ratio_new > ratio_initial else
        "decreased" if ratio_new < ratio_initial else
        "remained the same"
    )

    # Analyze reasons
    effect_clauses = []
    if capital_new > capital_initial:
        effect_clauses.append("Capital increased, pushing the ratio upward")
    elif capital_new < capital_initial:
        effect_clauses.append("Capital decreased, pushing the ratio downward")

    if rwa_new > rwa_initial:
        effect_clauses.append("RWA increased, pushing the ratio downward")
    elif rwa_new < rwa_initial:
        effect_clauses.append("RWA decreased, pushing the ratio upward")

    effect_analysis = "; ".join(effect_clauses)

    # Optional compliance check
    threshold = 8.0
    compliance = "compliant" if ratio_new >= threshold else "non-compliant"

    question = (
        f"{investor} is analyzing capital adequacy trends at {company}.\n"
        f"Initially:\n"
        f"  - Capital = ${capital_initial} million\n"
        f"  - Risk-Weighted Assets (RWA) = ${rwa_initial} million\n"
        f"  - Capital Adequacy Ratio = {ratio_initial:.2f}%\n\n"
        f"After changes:\n"
        f"  - Capital {capital_change_type}d to ${capital_new} million\n"
        f"  - RWA {rwa_change_type}d to ${rwa_new} million\n\n"
        f"Question: How did the capital adequacy ratio change, and what contributed to the change?"
    )

    solution = (
        f"Step 1: Recalculate the new ratio = ({capital_new} / {rwa_new}) × 100 = {ratio_new:.2f}%\n"
        f"Step 2: Compare with initial ratio = {ratio_initial:.2f}% → Ratio has {direction}.\n"
        f"Step 3: Analyze effects:\n"
        f"  - {effect_analysis}\n"
        f"Step 4: Compliance check → New ratio {ratio_new:.2f}% {'>=' if ratio_new >= threshold else '<'} {threshold}% → {compliance.upper()} with Basel minimum.\n"
        f"Conclusion: The capital adequacy ratio has {direction}. {effect_analysis}. The bank is {compliance} with Basel capital requirements."
    )

    return question, solution



# ----------------------- ADVANCED QUESTIONS -----------------------

def template_basel_advanced_multiple_requirements_check():
    """5:Advanced: Multi-metric Basel III compliance check with interpretive steps"""

    investor = random.choice(investor_names)
    company = random.choice(company_names)

    # Capital & RWA
    tier1 = round(random.uniform(4.5, 8.5), 2)
    tier2 = round(random.uniform(1.0, 3.5), 2)
    rwa_credit = round(random.uniform(40, 60), 2)
    rwa_market = round(random.uniform(20, 30), 2)
    rwa_operational = round(random.uniform(10, 20), 2)
    rwa_total = round(rwa_credit + rwa_market + rwa_operational, 2)

    # Leverage
    exposure = round(random.uniform(150, 250), 2)

    # Liquidity
    hqla = round(random.uniform(100, 160), 2)
    outflows_operational = round(random.uniform(40, 60), 2)
    outflows_contingent = round(random.uniform(50, 90), 2)
    total_outflows = round(outflows_operational + outflows_contingent, 2)

    # Requirements
    capital_required = 8 + 2.5  # 8% minimum + 2.5% buffer
    leverage_required = 3.0  # 3%
    lcr_required = 100.0  # 100%

    # Ratios
    capital_ratio = round((tier1 + tier2) / rwa_total * 100, 2)
    leverage_ratio = round(tier1 / exposure * 100, 2)
    lcr = round(hqla / total_outflows * 100, 2)

    question = (
        f"{investor} is assessing whether {company} complies with key Basel III thresholds. The bank's financials are as follows:\n\n"
        f"• Tier 1 Capital = ${tier1}M\n"
        f"• Tier 2 Capital = ${tier2}M\n"
        f"• Risk-Weighted Assets (RWA):\n"
        f"    - Credit Risk = ${rwa_credit}M\n"
        f"    - Market Risk = ${rwa_market}M\n"
        f"    - Operational Risk = ${rwa_operational}M\n"
        f"    - Total RWA = ${rwa_total}M\n"
        f"• Total Exposure = ${exposure}M\n"
        f"• High-Quality Liquid Assets (HQLA) = ${hqla}M\n"
        f"• Net Cash Outflows:\n"
        f"    - Operational = ${outflows_operational}M\n"
        f"    - Contingent = ${outflows_contingent}M\n"
        f"    - Total = ${total_outflows}M\n\n"
        f"Regulatory minimums:\n"
        f"• Capital Ratio ≥ {capital_required}% (including buffer)\n"
        f"• Leverage Ratio ≥ {leverage_required}%\n"
        f"• LCR ≥ {lcr_required}%\n\n"
        f"Does {company} meet all three Basel III requirements? Provide reasoning for each component."
    )

    solution = (
        f"Step 1: Capital Adequacy Ratio = ({tier1 + tier2} / {rwa_total}) × 100 = {capital_ratio:.2f}%\n"
        f"  → {'✓ Meets' if capital_ratio >= capital_required else '✗ Fails'} the required minimum of {capital_required}%\n\n"
        f"Step 2: Leverage Ratio = ({tier1} / {exposure}) × 100 = {leverage_ratio:.2f}%\n"
        f"  → {'✓ Meets' if leverage_ratio >= leverage_required else '✗ Fails'} the required minimum of {leverage_required}%\n\n"
        f"Step 3: Liquidity Coverage Ratio (LCR) = ({hqla} / {total_outflows}) × 100 = {lcr:.2f}%\n"
        f"  → {'✓ Meets' if lcr >= lcr_required else '✗ Fails'} the required minimum of {lcr_required}%\n\n"
        f"Conclusion: "
        + (
            "✓ All Basel III requirements are satisfied."
            if (capital_ratio >= capital_required and leverage_ratio >= leverage_required and lcr >= lcr_required)
            else "✗ The bank fails to meet one or more Basel III thresholds."
        )
    )

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
        template_basel_basic_leverage_ratio_test,
        template_basel_basic_tier_composition_analysis,
        template_basel_intermediate_capital_buffer_requirement,
        template_basel_intermediate_rwa_increase_effect,
        template_basel_advanced_multiple_requirements_check
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
    output_file = "../../testset/finance_regulation/basel.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")


if __name__ == "__main__":
   main()