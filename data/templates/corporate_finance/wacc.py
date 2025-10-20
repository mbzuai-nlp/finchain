import random
from misc import companies, currencies

def template_easy_wacc():
    """
    1:Basic: Compute WACC with given equity, debt, costs, and tax rate.
    Easy WACC: 2-step solution (weights → WACC).
    Returns (question, solution).
    """

    company_name, industry = random.choice(companies)
    currency = "$"
    unit = random.choice(["million", "billion"])

    # inputs (2-dp precision)
    equity_val = round(random.uniform(20, 80), 2)
    debt_val   = round(random.uniform(10, 60), 2)
    r_e        = round(random.uniform(6, 12), 2)   # %
    r_d        = round(random.uniform(3, 8), 2)    # %
    tax_pct    = round(random.uniform(20, 35), 2)  # %

    total_cap  = round(equity_val + debt_val, 2)

    # weights (4-dp, used consistently)
    w_e = round(equity_val / total_cap, 4)
    w_d = round(debt_val   / total_cap, 4)

    # WACC (2-dp) – uses rounded weights
    wacc = round(w_e * r_e + w_d * r_d * (1 - tax_pct/100), 2)

    # ---------- QUESTION ----------
    question = (
        f"{company_name} (a {industry} firm) reports:\n"
        f"- Equity value = {currency}{equity_val} {unit}\n"
        f"- Debt value   = {currency}{debt_val} {unit}\n"
        f"- Cost of equity = {r_e}%\n"
        f"- Cost of debt   = {r_d}%\n"
        f"- Tax rate       = {tax_pct}%\n\n"
        f"Compute the company’s weighted average cost of capital (WACC)."
    )

    # ---------- SOLUTION ----------
    solution = (
        f"Step 1 – Capital weights:\n"
        f"      Total capital V = {currency}{equity_val} + {currency}{debt_val} = {currency}{total_cap}\n"
        f"      Equity weight (E/V) = {w_e:.4f}\n"
        f"      Debt weight   (D/V) = {w_d:.4f}\n\n"
        f"Step 2 – WACC:\n"
        f"      WACC = (E/V)·r_e + (D/V)·r_d·(1 – T)\n"
        f"           = {w_e:.4f} × {r_e}% + {w_d:.4f} × {r_d}% × (1 – {tax_pct}%)\n"
        f"           = {wacc}%"
    )

    return question, solution

def template_easy_capm_wacc():
    """
    2:Basic: Compute WACC using CAPM for cost of equity.
    Easy CAPM-based WACC: 2-step solution (cost of equity → WACC).
    Returns (question, solution).
    """

    company_name, industry = random.choice(companies)
    currency = "$"

    # inputs
    E = round(random.uniform(40, 90), 2)
    D = round(random.uniform(15, 45), 2)
    beta   = round(random.uniform(0.8, 1.4), 2)
    r_f    = round(random.uniform(2.0, 4.0), 2)
    r_m    = round(random.uniform(8.0, 10.0), 2)
    r_d    = round(random.uniform(4.0, 7.0), 2)
    tax_pct = round(random.uniform(25, 30), 2)

    V = round(E + D, 2)

    # Step 1 result
    r_e = round(r_f + beta * (r_m - r_f), 2)

    # weights (4-dp)
    w_e = round(E / V, 4)
    w_d = round(D / V, 4)

    # Step 2 result
    wacc = round(w_e * r_e + w_d * r_d * (1 - tax_pct/100), 2)

    # ---------- QUESTION ----------
    question = (
        f"{company_name} (industry: {industry}) has the following data:\n"
        f"- Equity = {currency}{E} million, Debt = {currency}{D} million\n"
        f"- Beta = {beta}, Risk-free rate = {r_f}%, Market return = {r_m}%\n"
        f"- Cost of debt = {r_d}%, Tax rate = {tax_pct}%\n\n"
        f"Using CAPM for the cost of equity, calculate the WACC."
    )

    # ---------- SOLUTION ----------
    solution = (
        f"Step 1 – Cost of equity via CAPM:\n"
        f"      r_e = r_f + β·(r_m – r_f) = {r_f}% + {beta} × ({r_m}% – {r_f}%) = {r_e}%\n\n"
        f"Step 2 – WACC:\n"
        f"      Weights: E/V = {w_e:.4f}, D/V = {w_d:.4f}; V = {currency}{V}\n"
        f"      WACC = {w_e:.4f} × {r_e}% + {w_d:.4f} × {r_d}% × (1 – {tax_pct}%) = {wacc}%"
    )

    return question, solution

def template_weighted_debt_wacc():
    """
    3:Intermediate: Compute WACC with two debt tranches.
    WACC with two debt tranches.
    3 reasoning steps:
      1. Weighted average cost of debt
      2. Capital structure weights
      3. WACC
    Returns (question, solution).
    """
    company_name, industry = random.choice(companies)
    currency = "$"
    unit = random.choice(["million", "billion"])

    # Inputs
    equity_val   = round(random.uniform(40, 120), 2)
    debt_senior  = round(random.uniform(20, 60), 2)
    debt_sub     = round(random.uniform(10, 40), 2)
    r_e          = round(random.uniform(6, 11), 2)
    r_d_senior   = round(random.uniform(3, 6), 2)
    r_d_sub      = round(random.uniform(6, 9), 2)
    tax_pct      = round(random.uniform(22, 30), 2)

    # Step 1 – average cost of debt
    total_debt = round(debt_senior + debt_sub, 2)
    w_senior   = round(debt_senior / total_debt, 4)
    w_sub      = round(debt_sub   / total_debt, 4)
    r_d_avg    = round(w_senior * r_d_senior + w_sub * r_d_sub, 2)

    # Step 2 – capital weights
    V   = round(equity_val + total_debt, 2)
    w_e = round(equity_val / V, 4)
    w_d = round(total_debt / V, 4)

    # Step 3 – WACC
    wacc = round(w_e * r_e + w_d * r_d_avg * (1 - tax_pct / 100), 2)

    # Question
    question = (
        f"{company_name} (industry: {industry}) reports:\n"
        f"- Equity = {currency}{equity_val} {unit}\n"
        f"- Senior debt = {currency}{debt_senior} {unit} at {r_d_senior}%\n"
        f"- Subordinated debt = {currency}{debt_sub} {unit} at {r_d_sub}%\n"
        f"- Cost of equity = {r_e}%\n"
        f"- Corporate tax rate = {tax_pct}%\n\n"
        f"Calculate the company’s weighted average cost of capital (WACC)."
    )

    # Solution
    solution = (
        f"Step 1 – Weighted average cost of debt:\n"
        f"      Total debt = {currency}{debt_senior} + {currency}{debt_sub} = {currency}{total_debt}\n"
        f"      Weights: senior = {w_senior:.4f}, sub = {w_sub:.4f}\n"
        f"      r_d(avg) = {w_senior:.4f}×{r_d_senior}% + {w_sub:.4f}×{r_d_sub}% = {r_d_avg}%\n\n"
        f"Step 2 – Capital structure weights:\n"
        f"      V = {currency}{equity_val} + {currency}{total_debt} = {currency}{V}\n"
        f"      Equity weight = {w_e:.4f}, Debt weight = {w_d:.4f}\n\n"
        f"Step 3 – WACC:\n"
        f"      WACC = {w_e:.4f}×{r_e}% + {w_d:.4f}×{r_d_avg}%×(1 – {tax_pct}%) = {wacc}%"
    )

    return question, solution

def template_pref_capm_wacc():
    """
    4:Intermediate: Compute WACC with preferred stock and CAPM-based equity.
    WACC with preferred stock and CAPM-based equity.
    3 reasoning steps:
      1. Cost of equity via CAPM
      2. Capital structure weights (equity, preferred, debt)
      3. WACC
    Returns (question, solution).
    """
    company_name, industry = random.choice(companies)
    currency = "$"

    # Inputs
    E = round(random.uniform(50, 120), 2)   # equity
    P = round(random.uniform(10, 30), 2)    # preferred
    D = round(random.uniform(20, 60), 2)    # debt
    beta   = round(random.uniform(0.9, 1.4), 2)
    r_f    = round(random.uniform(2.0, 4.0), 2)
    r_m    = round(random.uniform(8.0, 10.0), 2)
    r_p    = round(random.uniform(6.0, 8.0), 2)   # preferred dividend yield
    r_d    = round(random.uniform(4.0, 7.0), 2)
    tax_pct = round(random.uniform(24, 30), 2)

    # Step 1 – cost of equity
    r_e = round(r_f + beta * (r_m - r_f), 2)

    # Step 2 – weights
    V   = round(E + P + D, 2)
    w_e = round(E / V, 4)
    w_p = round(P / V, 4)
    w_d = round(D / V, 4)

    # Step 3 – WACC
    wacc = round(w_e * r_e + w_p * r_p + w_d * r_d * (1 - tax_pct / 100), 2)

    # Question
    question = (
        f"{company_name} operates in {industry} and provides:\n"
        f"- Equity (E) = {currency}{E} million\n"
        f"- Preferred stock (P) = {currency}{P} million at {r_p}%\n"
        f"- Debt (D) = {currency}{D} million at {r_d}%\n"
        f"- Beta = {beta}, Risk-free rate = {r_f}%, Market return = {r_m}%\n"
        f"- Corporate tax rate = {tax_pct}%\n\n"
        f"Using CAPM for the cost of equity, calculate the WACC."
    )

    # Solution
    solution = (
        f"Step 1 – Cost of equity via CAPM:\n"
        f"      r_e = r_f + β·(r_m – r_f) = {r_f}% + {beta}×({r_m}% – {r_f}%) = {r_e}%\n\n"
        f"Step 2 – Capital weights:\n"
        f"      V = {currency}{E} + {currency}{P} + {currency}{D} = {currency}{V}\n"
        f"      E/V = {w_e:.4f}, P/V = {w_p:.4f}, D/V = {w_d:.4f}\n\n"
        f"Step 3 – WACC:\n"
        f"      WACC = {w_e:.4f}×{r_e}% + {w_p:.4f}×{r_p}% + "
        f"{w_d:.4f}×{r_d}%×(1 – {tax_pct}%) = {wacc}%"
    )

    return question, solution

def template_inflation_adjusted_capm_wacc():
    """
    5:Advanced: Compute WACC with inflation-adjusted market return and CAPM equity.
    WACC with inflation-adjusted market return and CAPM equity.
    4 reasoning steps:
      1. Adjust market return for inflation.
      2. Calculate cost of equity via CAPM.
      3. Calculate average cost of debt from two tranches.
      4. Calculate WACC.
    Returns (question, solution).
    """

    company_name, industry = random.choice(companies)
    currency = "$"

    # Inputs
    E = round(random.uniform(60, 120), 2)
    D1 = round(random.uniform(15, 40), 2)
    D2 = round(random.uniform(15, 40), 2)
    beta = round(random.uniform(0.9, 1.3), 2)
    r_f = round(random.uniform(2.0, 4.0), 2)
    mkt_nominal = round(random.uniform(9.0, 12.0), 2)
    inflation = round(random.uniform(1.0, 3.0), 2)
    r_d1 = round(random.uniform(3.0, 5.0), 2)
    r_d2 = round(random.uniform(5.0, 7.0), 2)
    tax_pct = round(random.uniform(25, 30), 2)

    # Step 1 – real market return
    mkt_real = round(((1 + mkt_nominal/100) / (1 + inflation/100) - 1) * 100, 2)

    # Step 2 – CAPM equity cost
    r_e = round(r_f + beta * (mkt_real - r_f), 2)

    # Step 3 – average cost of debt
    total_debt = round(D1 + D2, 2)
    w_d1 = round(D1 / total_debt, 4)
    w_d2 = round(D2 / total_debt, 4)
    r_d_avg = round(w_d1 * r_d1 + w_d2 * r_d2, 2)

    # Step 4 – WACC
    V = round(E + total_debt, 2)
    w_e = round(E / V, 4)
    w_d = round(total_debt / V, 4)
    wacc = round(w_e * r_e + w_d * r_d_avg * (1 - tax_pct/100), 2)

    # Question
    question = (
        f"{company_name} ({industry}) reports:\n"
        f"- Equity = {currency}{E} million\n"
        f"- Debt A = {currency}{D1} million at {r_d1}%\n"
        f"- Debt B = {currency}{D2} million at {r_d2}%\n"
        f"- Beta = {beta}, Risk-free rate = {r_f}%, Nominal market return = {mkt_nominal}%\n"
        f"- Inflation rate = {inflation}%\n"
        f"- Corporate tax rate = {tax_pct}%\n\n"
        f"Calculate the WACC using inflation-adjusted CAPM for equity."
    )

    # Solution
    solution = (
        f"Step 1 – Inflation-adjusted market return:\n"
        f"      r_m(real) = ((1 + {mkt_nominal}/100) / (1 + {inflation}/100) - 1) × 100 = {mkt_real}%\n\n"
        f"Step 2 – Cost of equity via CAPM:\n"
        f"      r_e = {r_f}% + {beta}×({mkt_real}% – {r_f}%) = {r_e}%\n\n"
        f"Step 3 – Weighted average cost of debt:\n"
        f"      Total debt = {currency}{D1} + {currency}{D2} = {currency}{total_debt}\n"
        f"      Weights: {w_d1:.4f}, {w_d2:.4f}\n"
        f"      r_d(avg) = {w_d1:.4f}×{r_d1}% + {w_d2:.4f}×{r_d2}% = {r_d_avg}%\n\n"
        f"Step 4 – WACC:\n"
        f"      Weights: E/V = {w_e:.4f}, D/V = {w_d:.4f}\n"
        f"      WACC = {w_e:.4f}×{r_e}% + {w_d:.4f}×{r_d_avg}%×(1 – {tax_pct}%) = {wacc}%"
    )

    return question, solution



def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # List of template functions
    templates = [
        template_easy_wacc,
        template_easy_capm_wacc,
        template_weighted_debt_wacc,
        template_pref_capm_wacc,
        template_inflation_adjusted_capm_wacc
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
    output_file = "../../testset/corporate_finance/wacc.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()