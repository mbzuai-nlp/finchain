import random
import json

# Named entities for investors and companies (US companies)
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = ["Apple", "Microsoft", "Amazon", "Google", "Facebook", "Tesla", "JPMorgan", "Walmart", "Boeing", "Coca-Cola"]

# ---------------------- Basic Questions ---------------------- #
def template_integration_synergy_calculation():
    """1: Basic: Integration Synergy Savings Calculation"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    # Duplicate operational costs (in million dollars)
    cost_a = random.randint(50, 200)
    cost_b = random.randint(50, 200)

    # Synergy reduction rate (percentage, 2 d.p.)
    synergy_rate = round(random.uniform(25, 35), 2)

    question = (
        f"{investor} oversaw the merger of {company_a} and {company_b}. "
        f"Before integration, {company_a} incurred duplicate operational costs of "
        f"${cost_a} million and {company_b} incurred duplicate costs of ${cost_b} million. "
        f"Post‑integration, these costs are expected to fall by {synergy_rate}%. "
        f"Calculate the total cost savings achieved by the merger."
    )

    total_cost = cost_a + cost_b
    savings = round(total_cost * synergy_rate / 100, 2)

    solution = (
        "Step 1 – Total duplicate cost:\n"
        f"  ${cost_a} million + ${cost_b} million = ${total_cost} million\n\n"
        "Step 2 – Cost savings from synergy:\n"
        f"  ${total_cost} million × {synergy_rate}% = ${savings} million\n\n"
        f"Therefore, the total cost savings is ${savings} million."
    )
    return question, solution


def template_valuation_adjustment_after_integration():
    """2: Basic: Valuation Adjustment After Integration"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    # Pre‑merger valuations (in million dollars)
    valuation_a = random.randint(500, 3000)
    valuation_b = random.randint(500, 3000)

    # Integration premium percentage (2 d.p.)
    premium = round(random.uniform(5, 15), 2)

    combined = valuation_a + valuation_b
    premium_value = round(combined * premium / 100, 2)
    post_valuation = round(combined + premium_value, 2)

    question = (
        f"{investor} oversaw the merger of {company_a} and {company_b}. "
        f"Before the merger, {company_a} was valued at ${valuation_a} million and "
        f"{company_b} at ${valuation_b} million. With an expected integration premium of "
        f"{premium}%, calculate the post‑merger valuation."
    )

    solution = (
        "Step 1 – Combined pre‑merger valuation:\n"
        f"  ${valuation_a} million + ${valuation_b} million = ${combined} million\n\n"
        "Step 2 – Premium value:\n"
        f"  ${combined} million × {premium}% = ${premium_value} million\n\n"
        "Step 3 – Post‑merger valuation:\n"
        f"  ${combined} million + ${premium_value} million = ${post_valuation} million"
    )
    return question, solution


def template_integration_cost_reduction():
    """3:Intermediate: Net Cost Reduction"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)
    op_cost_a = random.randint(50, 300)          # in million $
    op_cost_b = random.randint(50, 300)
    reduction_percent = round(random.uniform(20, 40), 2)
    integration_cost = random.randint(20, 100)   # in million $

    total_overlap      = op_cost_a + op_cost_b
    potential_saving   = round(total_overlap * reduction_percent / 100, 2)
    net_saving         = round(potential_saving - integration_cost, 2)

    # ---------- QUESTION ----------
    question = (
        f"{investor} managed the merger of {company_a} and {company_b}. "
        f"The overlapping operating costs were ${op_cost_a} million for {company_a} and "
        f"${op_cost_b} million for {company_b}. Cost synergies are projected to reduce these "
        f"overlaps by {reduction_percent:.2f}%, but the merger also requires a one‑time "
        f"integration cost of ${integration_cost} million. "
        f"Calculate the **net cost reduction** achieved by the merger (in million dollars)."
    )

    # ---------- SOLUTION ----------
    solution = (
        f"Step 1 – Total overlapping cost:\n"
        f"  ${op_cost_a:.2f} m + ${op_cost_b:.2f} m = ${total_overlap:.2f} m\n\n"
        f"Step 2 – Potential saving from synergies:\n"
        f"  ${total_overlap:.2f} m × {reduction_percent:.2f}% = ${potential_saving:.2f} m\n\n"
        f"Step 3 – Net cost reduction (subtract integration cost):\n"
        f"  ${potential_saving:.2f} m − ${integration_cost:.2f} m = "
        f"${net_saving:.2f} m\n\n"
        f"Therefore, the merger delivers a net cost reduction of "
        f"${net_saving:.2f} million."
    )
    return question, solution

# ───────────────────────────────────────────────────────────
# Revenue Synergy – Net Annual Gain
# ───────────────────────────────────────────────────────────
def template_revenue_synergy_net_gain():
    """4:Intermediate: Net annual revenue gain from cross‑selling synergies"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    rev_a = random.randint(200, 800)     # annual overlapping revenue, $ million
    rev_b = random.randint(200, 800)
    synergy_pct = round(random.uniform(5, 15), 2)        # % uplift from cross‑selling
    cannibal_pct = round(random.uniform(1, 5), 2)        # % revenue cannibalised

    total_overlap = rev_a + rev_b
    gross_synergy = round(total_overlap * synergy_pct / 100, 2)
    net_gain      = round(gross_synergy - total_overlap * cannibal_pct / 100, 2)

    # ---------- QUESTION ----------
    question = (
        f"{investor} is analysing revenue synergies after the merger of {company_a} and {company_b}. "
        f"The overlapping product lines generate ${rev_a} million and ${rev_b} million in annual revenue, respectively. "
        f"Cross‑selling is expected to boost this overlap by {synergy_pct:.2f}%, while {cannibal_pct:.2f}% of the revenue will be lost to cannibalisation. "
        f"Calculate the **net additional annual revenue** created by the merger (in million dollars)."
    )

    # ---------- SOLUTION ----------
    solution = (
        f"Step 1 – Total overlapping revenue:\n"
        f"  ${rev_a:.2f} m + ${rev_b:.2f} m = ${total_overlap:.2f} m\n\n"
        f"Step 2 – Gross synergy gain:\n"
        f"  ${total_overlap:.2f} m × {synergy_pct:.2f}% = ${gross_synergy:.2f} m\n\n"
        f"Step 3 – Net additional revenue (subtract cannibalisation):\n"
        f"  ${gross_synergy:.2f} m − "
        f"${total_overlap:.2f} m × {cannibal_pct:.2f}% = ${net_gain:.2f} m\n\n"
        f"The merger delivers a net additional annual revenue of ${net_gain:.2f} million."
    )
    return question, solution

# ───────────────────────────────────────────────────────────
# Supply‑Chain Consolidation – Net NPV Benefit
# ───────────────────────────────────────────────────────────
def template_supply_chain_npv_net_benefit():
    """
    5:Advanced: Net present value (NPV) of supply‑chain savings minus integration cost.
    4‑step reasoning: Net present value (NPV) of supply‑chain savings minus integration cost.
    Returns (question, solution)
    """
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    spend_a = random.randint(300, 800)          # $ million annual supply cost
    spend_b = random.randint(300, 800)
    reduction_pct   = round(random.uniform(8, 18), 2)     # % annual saving
    years           = random.randint(3, 5)                # savings horizon
    discount_rate   = round(random.uniform(5, 12), 2)     # %
    integration_cost = random.randint(50, 200)            # $ million

    total_spend      = spend_a + spend_b
    annual_saving    = round(total_spend * reduction_pct / 100, 2)
    r                = discount_rate / 100
    pv_factor        = (1 - (1 + r) ** (-years)) / r
    npv_savings      = round(annual_saving * pv_factor, 2)
    net_npv_benefit  = round(npv_savings - integration_cost, 2)

    # ----- QUESTION -----
    question = (
        f"{investor} is assessing supply‑chain synergies after {company_a} merged with {company_b}. "
        f"Their annual supply‑chain spends are ${spend_a} million and ${spend_b} million, respectively. "
        f"Synergy initiatives should cut these costs by {reduction_pct:.2f}% for the next {years} years, "
        f"and the appropriate discount rate is {discount_rate:.2f}%. Implementing the program costs "
        f"${integration_cost} million up‑front. "
        f"Calculate the **net present value (NPV) benefit** of the program (in million dollars)."
    )

    # ----- SOLUTION -----
    solution = (
        f"Step 1 – Combined annual spend:\n"
        f"  ${spend_a:.2f} m + ${spend_b:.2f} m = ${total_spend:.2f} m\n\n"
        f"Step 2 – Annual synergy saving:\n"
        f"  ${total_spend:.2f} m × {reduction_pct:.2f}% = ${annual_saving:.2f} m\n\n"
        f"Step 3 – NPV of savings over {years} years:\n"
        f"  PV factor = (1 − (1 + {r:.4f})^{-{years}}) / {r:.4f} = {pv_factor:.4f}\n"
        f"  NPV savings = ${annual_saving:.2f} m × {pv_factor:.4f} = ${npv_savings:.2f} m\n\n"
        f"Step 4 – Net NPV benefit (subtract integration cost):\n"
        f"  ${npv_savings:.2f} m − ${integration_cost:.2f} m = ${net_npv_benefit:.2f} m\n\n"
        f"The program’s net present value benefit is **${net_npv_benefit:.2f} million**."
    )
    return question, solution

# ----------------------------- Main ----------------------------- #
def main():
    """
    Generate multiple instances for each financial integration template and write the results to a JSONL file.
    """
    # List of template functions
    templates = [
        template_integration_synergy_calculation,
        template_valuation_adjustment_after_integration,
        template_integration_cost_reduction,
        template_revenue_synergy_net_gain,
        template_supply_chain_npv_net_benefit
    ]
    
    # List to store all generated problems
    all_problems = []
    
    # Generate one instance per template
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        
        # Set a unique random seed for reproducibility
        for i in range(10):
        # Generate a unique seed for each problem
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            
            # Generate the question and solution
            question, solution = template_func()
            
            # Create a JSON entry for the problem
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            
            all_problems.append(problem_entry)
            
            # Reset random seed after each instance
            random.seed()
    
    random.shuffle(all_problems)
    # Write all problems to a JSONL file
    output_file = "../../testset/mergers_and_acquisitions/post-merger_integration.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
    main()
