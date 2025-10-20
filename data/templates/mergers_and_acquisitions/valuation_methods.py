import random
import json

# Named entities for investors and US companies
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = [
    "Apple", "Microsoft", "Amazon", "Google", "Facebook",
    "Tesla", "Netflix", "Walmart", "Boeing", "Coca-Cola"
]

# Template 1: Basic Comparable Company Analysis using Revenue Multiple
def template_comparable_revenue_valuation():
    """1:Basic: Comparable Company Analysis using Revenue Multiple"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    revenue = random.randint(50, 200)                 # in $ million
    revenue_multiple = round(random.uniform(2, 5), 2)
    net_debt = random.randint(5, 20)                  # in $ million

    question = (
        f"{investor} is evaluating the acquisition of {company}. "
        f"The company generated revenue of ${revenue} million. "
        f"Comparable companies trade at a revenue multiple of {revenue_multiple}×. "
        f"Given the company's net debt is ${net_debt} million, calculate the estimated equity value."
    )

    # Step 1: Enterprise Value
    ev = round(revenue * revenue_multiple, 2)         # $ million
    # Step 2: Equity Value
    equity_value = round(ev - net_debt, 2)            # $ million

    solution = (
        f"Step 1: Calculate Enterprise Value (EV):\n"
        f"  EV = ${revenue} million × {revenue_multiple} = "
        f"${ev:.2f} million\n\n"
        f"Step 2: Calculate Equity Value:\n"
        f"  Equity Value = ${ev:.2f} million − ${net_debt} million = "
        f"${equity_value:.2f} million"
    )
    return question, solution


# Template 2: Basic Valuation using EBITDA Multiple
def template_ebitda_multiple_valuation():
    """2:Basic: Valuation using EBITDA Multiple"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    ebitda = random.randint(10, 100)                  # in $ million
    ebitda_multiple = round(random.uniform(5, 10), 2)
    net_debt = random.randint(10, 30)                 # in $ million

    question = (
        f"{investor} is considering acquiring {company}. "
        f"The company's EBITDA is ${ebitda} million, and the industry average EBITDA multiple is "
        f"{ebitda_multiple}×. With a net debt of ${net_debt} million, calculate the implied equity value."
    )

    # Step 1: Enterprise Value
    ev = round(ebitda * ebitda_multiple, 2)           # $ million
    # Step 2: Equity Value
    equity_value = round(ev - net_debt, 2)            # $ million

    solution = (
        f"Step 1: Calculate Enterprise Value (EV):\n"
        f"  EV = ${ebitda} million × {ebitda_multiple} = "
        f"${ev:.2f} million\n\n"
        f"Step 2: Calculate Equity Value:\n"
        f"  Equity Value = ${ev:.2f} million − ${net_debt} million = "
        f"${equity_value:.2f} million"
    )
    return question, solution


# Comparable EBITDA Multiple → Net Debt Computation → Equity Value
def template_comp_ebitda_multiple_with_net_debt():
    """3:Intermediate: EV from EBITDA multiple; compute Net Debt; Equity Value"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    ebitda = round(random.uniform(20, 120), 2)
    multiple = round(random.uniform(6, 12), 2)
    total_debt = round(random.uniform(30, 90), 2)
    cash = round(random.uniform(5, 40), 2)

    question = (
        f"{investor} is considering acquiring {company}. The company reported EBITDA of ${ebitda:.2f} million. "
        f"Comparable companies trade at an EBITDA multiple of {multiple:.2f}×. "
        f"Total debt is ${total_debt:.2f} million and cash is ${cash:.2f} million. "
        f"Calculate the implied equity value."
    )

    ev = round(ebitda * multiple, 2)
    net_debt = round(total_debt - cash, 2)
    equity_value = round(ev - net_debt, 2)

    solution = (
        f"Step 1: Enterprise Value (EV) = ${ebitda:.2f} million × {multiple:.2f} = ${ev:.2f} million\n\n"
        f"Step 2: Net Debt = ${total_debt:.2f} million − ${cash:.2f} million = ${net_debt:.2f} million\n\n"
        f"Step 3: Equity Value = ${ev:.2f} million − ${net_debt:.2f} million = ${equity_value:.2f} million"
    )
    return question, solution

# DCF (PV of FCFs) → PV of Terminal Value → Equity Value
def template_dcf_three_year_terminal_to_equity():
    """4:Intermediate: PV of 3 FCFs; PV of terminal value; Equity Value (subtract Net Debt)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    fcf1 = round(random.uniform(8, 20), 2)
    fcf2 = round(random.uniform(9, 22), 2)
    fcf3 = round(random.uniform(10, 24), 2)
    wacc_pct = round(random.uniform(8, 12), 2)   # %
    g_pct = round(random.uniform(2, 4), 2)       # %
    total_debt = round(random.uniform(40, 100), 2)
    cash = round(random.uniform(5, 40), 2)

    r = wacc_pct / 100
    g = g_pct / 100

    # PV of FCFs
    pv_fcf1 = fcf1 / (1 + r) ** 1
    pv_fcf2 = fcf2 / (1 + r) ** 2
    pv_fcf3 = fcf3 / (1 + r) ** 3
    pv_fcfs = round(pv_fcf1 + pv_fcf2 + pv_fcf3, 2)

    # Terminal value at end of year 3
    fcf4 = fcf3 * (1 + g)
    tv = fcf4 / (r - g)
    pv_tv = round(tv / (1 + r) ** 3, 2)

    net_debt = round(total_debt - cash, 2)
    equity_value = round(pv_fcfs + pv_tv - net_debt, 2)

    question = (
        f"{investor} is valuing {company} using a 3-year DCF. Free cash flows are "
        f"${fcf1:.2f} million, ${fcf2:.2f} million, and ${fcf3:.2f} million for Years 1–3. "
        f"The discount rate (WACC) is {wacc_pct:.2f}%, and the terminal growth rate is {g_pct:.2f}%. "
        f"Total debt is ${total_debt:.2f} million and cash is ${cash:.2f} million. "
        f"Calculate the implied equity value."
    )

    solution = (
        f"Step 1: PV of FCFs = ${fcf1:.2f}/(1+{r:.2f})^1 + ${fcf2:.2f}/(1+{r:.2f})^2 + ${fcf3:.2f}/(1+{r:.2f})^3 "
        f"= ${pv_fcfs:.2f} million\n\n"
        f"Step 2: Terminal Value = (${fcf3:.2f} × (1+{g:.2f})) / ({r:.2f} − {g:.2f}) = ${tv:.2f} million; "
        f"PV(TV) = ${pv_tv:.2f} million\n\n"
        f"Step 3: Equity Value = ${pv_fcfs:.2f} million + ${pv_tv:.2f} million − ${net_debt:.2f} million "
        f"= ${equity_value:.2f} million"
    )
    return question, solution

# 1. DCF: PV of FCFs → PV of TV → EV → Equity Value
def template_dcf_3yr_gordon_to_equity():
    """5:Advanced: PV FCFs; PV TV; Enterprise Value; Equity Value"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    fcf1 = round(random.uniform(8, 20), 2)
    fcf2 = round(random.uniform(9, 22), 2)
    fcf3 = round(random.uniform(10, 24), 2)
    wacc_pct = round(random.uniform(8, 12), 2)
    g_pct = round(random.uniform(2, 4), 2)
    total_debt = round(random.uniform(40, 100), 2)
    cash = round(random.uniform(5, 40), 2)

    r = wacc_pct / 100
    g = g_pct / 100

    pv_fcf1 = fcf1 / (1 + r) ** 1
    pv_fcf2 = fcf2 / (1 + r) ** 2
    pv_fcf3 = fcf3 / (1 + r) ** 3
    pv_fcfs = round(pv_fcf1 + pv_fcf2 + pv_fcf3, 2)

    fcf4 = fcf3 * (1 + g)
    tv = fcf4 / (r - g)
    pv_tv = round(tv / (1 + r) ** 3, 2)

    ev = round(pv_fcfs + pv_tv, 2)
    net_debt = round(total_debt - cash, 2)
    equity_value = round(ev - net_debt, 2)

    question = (
        f"{investor} is valuing {company} using a 3-year DCF. Free cash flows are "
        f"${fcf1:.2f} million, ${fcf2:.2f} million, and ${fcf3:.2f} million for Years 1–3. "
        f"The discount rate (WACC) is {wacc_pct:.2f}%, and the terminal growth rate is {g_pct:.2f}%. "
        f"Total debt is ${total_debt:.2f} million and cash is ${cash:.2f} million. "
        f"Calculate the implied equity value."
    )

    solution = (
        f"Step 1: PV of FCFs = ${fcf1:.2f}/(1+{r:.2f})^1 + ${fcf2:.2f}/(1+{r:.2f})^2 + ${fcf3:.2f}/(1+{r:.2f})^3 = ${pv_fcfs:.2f} million\n\n"
        f"Step 2: Terminal Value = (${fcf3:.2f} × (1+{g:.2f})) / ({r:.2f} − {g:.2f}) = ${tv:.2f} million; PV(TV) = ${pv_tv:.2f} million\n\n"
        f"Step 3: Enterprise Value = ${pv_fcfs:.2f} million + ${pv_tv:.2f} million = ${ev:.2f} million\n\n"
        f"Step 4: Equity Value = ${ev:.2f} million − ${net_debt:.2f} million = ${equity_value:.2f} million"
    )
    return question, solution

def main():
    """
    Generate 10 instances of each valuation template (5 functions) with different random seeds
    and save the generated QA pairs along with step-by-step solutions to a JSONL file.
    """
    templates = [
        template_comparable_revenue_valuation,
        template_ebitda_multiple_valuation,
        template_comp_ebitda_multiple_with_net_debt,
        template_dcf_three_year_terminal_to_equity,
        template_dcf_3yr_gordon_to_equity
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
    output_file = "../../testset/mergers_and_acquisitions/valuation_methods.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
    main()
