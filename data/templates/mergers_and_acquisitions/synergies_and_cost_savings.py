import random
import json

# Named entities for investors and companies
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = ["Apple", "Google", "Microsoft", "Amazon", "Facebook", "Tesla", "Netflix", "Walmart", "JP Morgan", "Berkshire Hathaway"]

# Basic Level Question 1: Synergy Cost Reduction via % Savings
def template_synergy_basic_cost_reduction():
    """1:Basic: Calculate annual cost savings from percentage cost reduction"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)
    cost_base_a = random.randint(50, 200)          # in $ million
    cost_base_b = random.randint(50, 200)          # in $ million
    synergy_pct = random.randint(5, 20)            # %

    question = (
        f"{investor} is evaluating a merger between {company_a} and {company_b}. "
        f"{company_a} has an annual operating cost base of ${cost_base_a} million, and "
        f"{company_b} has ${cost_base_b} million. "
        f"Eliminating redundant operations is expected to cut costs by {synergy_pct}% "
        f"of the combined cost base. "
        f"Calculate the annual cost savings from the merger."
    )

    total_cost = cost_base_a + cost_base_b                              # $ million
    savings = round(total_cost * synergy_pct / 100, 2)                  # $ million, 2 dp
    savings_str = f"{savings:.2f}"

    solution = (
        "Step 1 – Compute the combined cost base:\n"
        f"         Total Cost = ${cost_base_a} million + ${cost_base_b} million"
        f" = ${total_cost} million\n\n"
        "Step 2 – Compute the cost savings:\n"
        f"         Savings = Total Cost × {synergy_pct}%"
        f" = ${total_cost} million × {synergy_pct}% = ${savings_str} million\n\n"
        f"Hence, the annual cost savings from the merger is ${savings_str} million."
    )

    return question, solution


# Basic Level Question 2: Fixed Cost Savings from Eliminating Redundant Expenses
def template_synergy_basic_fixed_savings():
    """2:Basic: Calculate total fixed annual cost savings by summing individual savings"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)
    saving_a = random.randint(5, 20)   # $ million
    saving_b = random.randint(5, 20)   # $ million

    question = (
        f"{investor} expects that the merger between {company_a} and {company_b} will cut duplicate "
        f"administrative costs. {company_a} can save ${saving_a} million annually and "
        f"{company_b} can save ${saving_b} million annually. "
        f"Calculate the total fixed annual cost savings from the merger."
    )

    total_fixed_savings = saving_a + saving_b    # $ million

    solution = (
        "Step 1 – Identify the annual savings for each company:\n"
        f"         Savings for {company_a} = ${saving_a} million\n"
        f"         Savings for {company_b} = ${saving_b} million\n\n"
        "Step 2 – Sum the savings:\n"
        f"         Total Fixed Savings = ${saving_a} million + ${saving_b} million"
        f" = ${total_fixed_savings} million\n\n"
        f"Thus, the merger yields total annual fixed cost savings of ${total_fixed_savings} million."
    )

    return question, solution

# Net First‑Year Savings after Synergies and Integration Cost
def template_synergy_complex_net_savings():
    """3:Intermediate: calculate net first‑year cost savings (synergy % – integration cost)"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    # Annual operating cost bases ($ million)
    cost_base_a = random.randint(70, 250)
    cost_base_b = random.randint(70, 250)

    # Synergy and one‑time integration assumptions
    synergy_pct = random.randint(8, 20)            # %
    integration_cost = random.randint(5, 30)       # $ million, paid in year 1

    question = (
        f"{investor} is analysing a merger between {company_a} and {company_b}. "
        f"{company_a} has an annual operating cost base of ${cost_base_a} million, while "
        f"{company_b} has ${cost_base_b} million. Eliminating overlap is expected to cut "
        f"{synergy_pct}% of the combined cost base, but a one‑time integration cost of "
        f"${integration_cost} million will be incurred in the first year. "
        f"Calculate the **net first‑year cost savings** from the merger."
    )

    # --- three‑step reasoning ---
    total_cost   = cost_base_a + cost_base_b                        # $ million
    gross_save   = round(total_cost * synergy_pct / 100, 2)         # $ million
    net_save     = round(gross_save - integration_cost, 2)          # $ million
    gross_str    = f"{gross_save:.2f}"
    net_str      = f"{net_save:.2f}"

    solution = (
        "Step 1 – Combined cost base:\n"
        f"         ${cost_base_a} million + ${cost_base_b} million = ${total_cost} million\n\n"
        "Step 2 – Gross synergy savings:\n"
        f"         ${total_cost} million × {synergy_pct}% = ${gross_str} million\n\n"
        "Step 3 – Net first‑year savings after integration cost:\n"
        f"         ${gross_str} million − ${integration_cost} million "
        f"= ${net_str} million\n\n"
        f"The net first‑year cost savings are **${net_str} million**."
    )

    return question, solution

# Multi‑Category Savings (Procurement % + Fixed IT Cuts)
def template_synergy_complex_multi_category():
    """4:Intermediate: total annual savings from two distinct synergy buckets"""
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    # Procurement spend ($ million)
    procurement_a = random.randint(30, 120)
    procurement_b = random.randint(30, 120)
    procurement_pct = random.randint(7, 15)        # % saving on combined procurement

    # IT rationalisation fixed saving ($ million)
    it_fixed_save = random.randint(8, 25)

    question = (
        f"{investor} anticipates two key synergy buckets after merging {company_a} and {company_b}: "
        f"(1) a {procurement_pct}% reduction on their combined procurement spend, and "
        f"(2) fixed savings of ${it_fixed_save} million annually from consolidating IT systems. "
        f"{company_a} currently spends ${procurement_a} million on procurement and "
        f"{company_b} spends ${procurement_b} million. "
        f"Calculate the **total annual cost savings** once both synergy buckets are realised."
    )

    # --- three‑step reasoning ---
    combined_procurement = procurement_a + procurement_b            # $ million
    procurement_save     = round(combined_procurement *
                                 procurement_pct / 100, 2)          # $ million
    total_save           = round(procurement_save + it_fixed_save, 2)  # $ million
    procurement_str = f"{procurement_save:.2f}"
    total_str       = f"{total_save:.2f}"

    solution = (
        "Step 1 – Combined procurement spend:\n"
        f"         ${procurement_a} million + ${procurement_b} million "
        f"= ${combined_procurement} million\n\n"
        "Step 2 – Procurement synergy savings:\n"
        f"         ${combined_procurement} million × {procurement_pct}% "
        f"= ${procurement_str} million\n\n"
        "Step 3 – Total annual savings:\n"
        f"         Procurement Savings ${procurement_str} million + "
        f"IT Savings ${it_fixed_save} million = ${total_str} million\n\n"
        f"Therefore, total annual cost savings amount to **${total_str} million**."
    )

    return question, solution


# Net After‑Tax Savings with Integration Amortisation
def template_synergy_complex_after_tax():
    """
    5:Advanced: net annual cost savings after tax and integration amortisation
    """
    investor = random.choice(investor_names)
    company_a, company_b = random.sample(company_names, 2)

    # Input assumptions
    cost_base_a      = random.randint(80, 300)            # $ million
    cost_base_b      = random.randint(80, 300)            # $ million
    synergy_pct      = random.randint(8, 20)              # %
    integration_cost = random.randint(20, 80)             # $ million one‑time
    amort_years      = random.choice([4, 5, 6])           # years
    tax_rate         = random.choice([20, 25, 30, 35])    # %

    question = (
        f"{investor} is analysing a merger between {company_a} and {company_b}. "
        f"{company_a} has an annual operating cost base of ${cost_base_a} million, "
        f"while {company_b} has ${cost_base_b} million. Eliminating overlaps is expected to "
        f"save {synergy_pct}% of the combined cost base. A one‑time integration cost of "
        f"${integration_cost} million will be amortised straight‑line over {amort_years} years. "
        f"The combined entity faces a corporate tax rate of {tax_rate}%. "
        f"Calculate the **net annual cost savings after tax** for the first full year."
    )

    # --- 4‑step reasoning ---
    total_cost         = cost_base_a + cost_base_b
    gross_savings      = round(total_cost * synergy_pct / 100, 2)
    annual_integration = round(integration_cost / amort_years, 2)
    net_after_tax      = round((gross_savings - annual_integration) *
                               (1 - tax_rate / 100), 2)

    g_str  = f"{gross_savings:.2f}"
    a_str  = f"{annual_integration:.2f}"
    n_str  = f"{net_after_tax:.2f}"

    solution = (
        "Step 1 – Combined cost base:\n"
        f"         ${cost_base_a} million + ${cost_base_b} million "
        f"= ${total_cost} million\n\n"
        "Step 2 – Gross synergy savings:\n"
        f"         ${total_cost} million × {synergy_pct}% = ${g_str} million\n\n"
        "Step 3 – Amortised integration cost and pre‑tax net:\n"
        f"         Annual integration = ${integration_cost} million ÷ {amort_years} "
        f"years = ${a_str} million\n"
        f"         Pre‑tax net = ${g_str} million − ${a_str} million "
        f"= ${float(gross_savings - annual_integration):.2f} million\n\n"
        "Step 4 – After‑tax net savings:\n"
        f"         (${float(gross_savings - annual_integration):.2f} million) × "
        f"(1 − {tax_rate}%) = ${n_str} million\n\n"
        f"Therefore, the net annual cost savings after tax are **${n_str} million**."
    )

    return question, solution



def main():
    """
    Generate one instance for each of the five merger synergy cost saving templates and write the results to a JSONL file.
    """
    # List of template functions
    templates = [
        template_synergy_basic_cost_reduction,
        template_synergy_basic_fixed_savings,
        template_synergy_complex_net_savings,
        template_synergy_complex_multi_category,
        template_synergy_complex_after_tax
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
    output_file = "../../testset/mergers_and_acquisitions/synergies_and_cost_savings.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
    main()