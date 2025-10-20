import random
import json

# Named entities for investors and companies
investor_names = ["Alice Johnson", "Bob Smith", "Catherine Lee", "Daniel Brown", "Eva Green"]
company_names = ["Apple Inc.", "Google LLC", "Microsoft Corp.", "Amazon.com Inc.", "Tesla Inc."]

import random

# assume `investor_names` and `company_names` are predefined lists
# ---------------------------------------------------------------
# 1: Basic – Calculate Working Capital
# ---------------------------------------------------------------
def template_due_diligence_working_capital():
    """
    1: Basic: Calculate Working Capital
    An investor evaluates a company's liquidity by computing its working capital.
    """
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    # Generate current assets and liabilities; ensure positive working capital
    current_assets = random.randint(20_000, 50_000)
    current_liabilities = random.randint(10_000, current_assets - 5_000)

    question = (
        f"{investor} is conducting due diligence on {company}. "
        f"The company reports current assets of ${current_assets} "
        f"and current liabilities of ${current_liabilities}. "
        f"Calculate the working capital."
    )

    working_capital = current_assets - current_liabilities

    solution = (
        "Step 1: Recall the formula for Working Capital:\n"
        "        Working Capital = Current Assets - Current Liabilities.\n"
        f"Step 2: Substitute the given values: "
        f"${current_assets} - ${current_liabilities} = ${working_capital}.\n"
        f"Therefore, the working capital is ${working_capital}."
    )

    return question, solution


# ---------------------------------------------------------------
# 2: Basic – Calculate Market Capitalization using P/E Ratio
# ---------------------------------------------------------------
def template_due_diligence_pe_valuation():
    """
    2: Basic: Calculate Market Capitalization using P/E Ratio
    An investor assesses a company's valuation by computing its market capitalization
    from its net income and P/E ratio.
    """
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    net_income = random.randint(500, 2_000)        # in millions
    pe_ratio   = round(random.uniform(10, 25), 1)

    question = (
        f"{investor} is reviewing {company} as a potential acquisition target. "
        f"The company reported a net income of ${net_income} million "
        f"and has a Price/Earnings (P/E) ratio of {pe_ratio}. "
        f"Calculate the market capitalization."
    )

    market_cap = round(net_income * pe_ratio, 2)   # in millions, 2‑dp precision

    solution = (
        "Step 1: Recall the market‑capitalization formula:\n"
        "        Market Capitalization = Net Income × P/E Ratio.\n"
        f"Step 2: Substitute the values: "
        f"${net_income} million × {pe_ratio} = ${market_cap:,.2f} million.\n"
        f"Therefore, the market capitalization is ${market_cap:,.2f} million."
    )

    return question, solution


def template_due_diligence_synergy_estimation():
    """
    3:Intermediate: Estimate Net First‑Year Synergy Benefit from a Merger
    """
    investor = random.choice(investor_names)
    company1 = random.choice(company_names)
    company2 = random.choice([c for c in company_names if c != company1])

    revenue1 = random.randint(100_000, 500_000)
    revenue2 = random.randint(100_000, 500_000)
    synergy_rate = round(random.uniform(0.03, 0.07), 4)          # 3 %–7 %
    integration_cost = random.randint(50_000, 150_000)           # one‑time cost

    question = (
        f"{investor} is considering the merger of {company1} and {company2}. "
        f"{company1} has an annual revenue of ${revenue1}, and {company2} has an annual revenue of "
        f"${revenue2}. The merger is expected to realise synergies at a rate of "
        f"{synergy_rate*100:.1f}% of the combined revenue. A one‑time integration cost of "
        f"${integration_cost} will be amortised over one year. "
        f"Calculate the net first‑year synergy benefit."
    )

    # Calculations
    combined_revenue = revenue1 + revenue2
    annual_synergy = round(combined_revenue * synergy_rate, 2)
    net_first_year_synergy = round(annual_synergy - integration_cost, 2)

    solution = (
        "Step 1: Calculate the combined revenue:\n"
        f"        ${revenue1} + ${revenue2} = ${combined_revenue}.\n"
        "Step 2: Compute the annual synergy benefit:\n"
        f"        ${combined_revenue} × {synergy_rate:.4f} = ${annual_synergy}.\n"
        "Step 3: Subtract the amortised integration cost to obtain the net first‑year synergy benefit:\n"
        f"        ${annual_synergy} − ${integration_cost} = ${net_first_year_synergy}.\n"
        f"Therefore, the net first‑year synergy benefit is ${net_first_year_synergy}."
    )

    return question, solution


def template_due_diligence_after_tax_interest_cost():
    """
    4:Intermediate: Calculate After‑Tax Annual Interest Cost of New Debt
    """
    investor = random.choice(investor_names)
    company  = random.choice(company_names)

    debt_amount   = random.randint(200_000, 800_000)                 # new debt issued
    interest_rate = round(random.uniform(0.03, 0.08), 4)            # 3 %–8 %
    tax_rate      = round(random.uniform(0.20, 0.35), 2)            # 20 %–35 %

    question = (
        f"{investor} plans to finance the acquisition of {company} with ${debt_amount} of new debt at an "
        f"annual interest rate of {interest_rate*100:.2f}%. The corporate tax rate is {tax_rate*100:.0f}%. "
        f"Calculate the after‑tax annual interest cost."
    )

    # Calculations
    annual_interest     = round(debt_amount * interest_rate, 2)
    tax_shield          = round(annual_interest * tax_rate, 2)
    after_tax_interest  = round(annual_interest - tax_shield, 2)

    solution = (
        "Step 1: Compute the annual interest expense:\n"
        f"        ${debt_amount} × {interest_rate:.4f} = ${annual_interest}.\n"
        "Step 2: Compute the tax shield on interest:\n"
        f"        ${annual_interest} × {tax_rate:.2f} = ${tax_shield}.\n"
        "Step 3: Subtract the tax shield to obtain the after‑tax annual interest cost:\n"
        f"        ${annual_interest} − ${tax_shield} = ${after_tax_interest}.\n"
        f"Therefore, the after‑tax annual interest cost is ${after_tax_interest}."
    )

    return question, solution

# ------------------ Advanced Due Diligence Question ------------------

def template_due_diligence_dcf_valuation():
    """
    5:Advanced: 5‑year DCF enterprise‑value calculation
    5‑year DCF enterprise‑value template that satisfies:
      • $ before every cash figure
      • 2‑decimal rounding applied immediately and used consistently
      • No bold / highlighting in Q&A
    """
    investor        = random.choice(investor_names)
    company         = random.choice(company_names)

    fcf_year1       = random.randint(200_000, 1_000_000)            # Year‑1 FCF
    g               = round(random.uniform(0.03, 0.07), 4)          # Growth 3‑7 %
    r               = round(random.uniform(0.10, 0.15), 4)          # Discount 10‑15 %
    g_term          = round(random.uniform(0.02, 0.04), 4)          # Terminal 2‑4 %
    years           = 5

    # ---------- Question ----------
    question = (
        f"{investor} is evaluating {company} for acquisition and wants to perform a DCF valuation. "
        f"The company's Year‑1 free cash flow (FCF) is ${fcf_year1:,}. "
        f"FCF is expected to grow {g*100:.2f}% per year for the next {years-1} years. "
        f"The discount rate is {r*100:.2f}%, and the terminal growth rate beyond Year‑{years} is "
        f"{g_term*100:.2f}%. Calculate the enterprise value of the company."
    )

    # ---------- Forecast period ----------
    pv_lines, pv_sum = [], 0.00
    for t in range(1, years + 1):
        fcf_t = fcf_year1 * (1 + g) ** (t - 1)
        pv_t  = round(fcf_t / (1 + r) ** t, 2)      # round immediately
        pv_sum += pv_t
        pv_lines.append(
            f"Year {t}:  FCF = ${fcf_year1:,} × (1+{g:.4f})^{t-1} = ${fcf_t:,.2f}; "
            f"PV = ${fcf_t:,.2f} / (1+{r:.4f})^{t} = ${pv_t:,.2f}"
        )
    pv_sum = round(pv_sum, 2)

    # ---------- Terminal value ----------
    fcf_N   = fcf_year1 * (1 + g) ** (years - 1)
    tv      = round((fcf_N * (1 + g_term)) / (r - g_term), 2)
    pv_tv   = round(tv / (1 + r) ** years, 2)

    # ---------- Enterprise value ----------
    ev = round(pv_sum + pv_tv, 2)

    # ---------- Solution ----------
    solution = (
        "Step 1 – Discount forecast‑period FCFs:\n"
        + "\n".join(pv_lines) +
        f"\n\nStep 2 – Terminal value at end of Year {years}:\n"
        f"        TV = [FCF_{years} × (1 + g_T)] / (r – g_T)\n"
        f"           = [${fcf_N:,.2f} × (1 + {g_term:.4f})] / "
        f"({r:.4f} – {g_term:.4f}) = ${tv:,.2f}\n"
        f"Step 3 – Present value of TV: ${tv:,.2f} / (1+{r:.4f})^{years} = ${pv_tv:,.2f}\n"
        f"Step 4 – Enterprise value: ΣPV_FCF (${pv_sum:,.2f}) + PV_TV (${pv_tv:,.2f}) "
        f"= ${ev:,.2f}\n\n"
        f"Estimated enterprise value: ${ev:,.2f}"
    )

    return question, solution


# ------------------ Main Method ------------------

def main():
    """
    Generate 5 due diligence QA pairs and save the results to a JSON file.
    There are two basic, two intermediate, and one advanced question.
    """
    templates = [
        template_due_diligence_working_capital,
        template_due_diligence_pe_valuation,
        template_due_diligence_synergy_estimation,
        template_due_diligence_after_tax_interest_cost,
        template_due_diligence_dcf_valuation
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
    output_file = "../../testset/mergers_and_acquisitions/due_diligence.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
    main()