import random
from typing import Tuple
import json
import argparse
import pathlib

# -----------------------
# Global settings & utils
# -----------------------

company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]
industry_names = ["automotive", "technology", "e-commerce", "aerospace", "internet services"]

RATIO_DP = 2         # decimals for ratios
MONEY_DP = 2         # decimals for money
MIN_EQUITY = 5_000   # hard floor to avoid division by zero / tiny equity

def fmt_usd(x: float) -> str:
    """Format money in USD with commas and 2 decimals."""
    return f"${x:,.2f}"

def round_money(x: float) -> float:
    return round(float(x), MONEY_DP)

def bound_ratio(liabilities: float, equity: float, rmin=0.2, rmax=3.0) -> bool:
    """Keep ratios in a realistic band to avoid pathological examples."""
    if equity <= 0:
        return False
    r = liabilities / equity
    return (rmin <= r <= rmax)

def sample_liab_equity(
    L_range: Tuple[float, float],
    E_range: Tuple[float, float],
    rmin=0.2,
    rmax=3.0,
    max_tries: int = 500
) -> Tuple[float, float]:
    """
    Sample liabilities and equity that lead to a realistic D/E ratio,
    with consistent precision.
    """
    for _ in range(max_tries):
        L = round_money(random.uniform(*L_range))
        E = max(round_money(random.uniform(*E_range)), MIN_EQUITY)
        if bound_ratio(L, E, rmin, rmax):
            return L, E
    # Fallback (rare): pick midpoints that satisfy the constraint.
    L_mid = sum(L_range)/2.0
    E_mid = max(sum(E_range)/2.0, MIN_EQUITY)
    # Nudge E so the ratio lands near 1 if needed
    if not bound_ratio(L_mid, E_mid, rmin, rmax):
        E_mid = max(L_mid, MIN_EQUITY)
    return round_money(L_mid), round_money(E_mid)

# ---------------------------------------------------
# EASY 1 — Debt-to-Equity Ratio (simple, single step)
# ---------------------------------------------------
def template_debt_to_equity_simple():
    """1:Easy:Compute basic D/E = Total Liabilities / Shareholders' Equity."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    # Smaller ranges for 'easy'
    total_liabilities, shareholders_equity = sample_liab_equity(
        L_range=(10_000, 50_000),
        E_range=(8_000, 30_000),
        rmin=0.3,
        rmax=2.5
    )

    question = (
        f"All amounts are in USD. Round the final ratio to {RATIO_DP} decimal places.\n\n"
        f"{company_name}, operating in the {industry} industry, has total liabilities of "
        f"{fmt_usd(total_liabilities)} and shareholders’ equity of {fmt_usd(shareholders_equity)}. "
        f"Calculate the company’s debt-to-equity (D/E) ratio."
    )

    de = round(total_liabilities / shareholders_equity, RATIO_DP)

    solution = (
        "Step 1 — Apply the definition of leverage:\n"
        "  D/E = Total Liabilities ÷ Shareholders’ Equity\n"
        f"      = {fmt_usd(total_liabilities)} ÷ {fmt_usd(shareholders_equity)}\n"
        f"      = {de:.{RATIO_DP}f}"
    )

    return question, solution

# ----------------------------------------------------------------
# EASY 2 — D/E with Convertible Debt converting fully into equity
# ----------------------------------------------------------------
def template_debt_to_equity_convertible_debt():
    """2:Easy:Compute current D/E and D/E after ALL convertible debt converts to equity."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    L, E = sample_liab_equity(L_range=(30_000, 100_000), E_range=(15_000, 60_000), rmin=0.3, rmax=2.5)
    max_conv = 0.4 * L
    convertible_debt = round_money(random.uniform(5_000, max(6_000, max_conv)))
    # Ensure convertible debt cannot exceed total liabilities
    convertible_debt = min(convertible_debt, L)

    de_before = round(L / E, RATIO_DP)
    L_after = round_money(L - convertible_debt)
    E_after = round_money(E + convertible_debt)
    de_after = round(L_after / E_after, RATIO_DP)

    question = (
        f"All amounts are in USD. Round ratios to {RATIO_DP} decimals.\n\n"
        f"{company_name}, a key player in the {industry} industry, reports total liabilities of "
        f"{fmt_usd(L)}, of which {fmt_usd(convertible_debt)} is convertible debt, and shareholders’ equity of {fmt_usd(E)}. "
        "If all convertible debt converts into equity, how does the D/E ratio change (before vs. after)?"
    )

    solution = (
        "Step 1 — Current leverage:\n"
        f"  D/E_before = {fmt_usd(L)} ÷ {fmt_usd(E)} = {de_before:.{RATIO_DP}f}\n\n"
        "Step 2 — Conversion mechanics (no cash flow): liabilities ↓ by the converted amount; equity ↑ by the same amount:\n"
        f"  Liabilities_after = {fmt_usd(L)} − {fmt_usd(convertible_debt)} = {fmt_usd(L_after)}\n"
        f"  Equity_after      = {fmt_usd(E)} + {fmt_usd(convertible_debt)} = {fmt_usd(E_after)}\n\n"
        "Step 3 — Recompute leverage:\n"
        f"  D/E_after = {fmt_usd(L_after)} ÷ {fmt_usd(E_after)} = {de_after:.{RATIO_DP}f}"
    )

    return question, solution

# -------------------------------------------------------------
# INTERMEDIATE 1 — D/E after primary equity capital injection
# -------------------------------------------------------------
def template_debt_to_equity_capital_injection():
    """3:Intermediate:Compute D/E before and after a primary equity raise (no change to liabilities)."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    L, E = sample_liab_equity(L_range=(100_000, 500_000), E_range=(60_000, 300_000), rmin=0.4, rmax=2.5)
    # Injection between 10% and 60% of current equity for a meaningful but not extreme change
    injection = round_money(random.uniform(0.10 * E, 0.60 * E))

    de_before = round(L / E, RATIO_DP)
    E_after = round_money(E + injection)
    de_after = round(L / E_after, RATIO_DP)

    question = (
        f"All amounts are in USD. Round ratios to {RATIO_DP} decimals.\n\n"
        f"{company_name} in the {industry} industry has total liabilities of {fmt_usd(L)} and shareholders’ equity of {fmt_usd(E)}. "
        f"The firm plans to raise {fmt_usd(injection)} in new equity (primary issue). "
        "What is the D/E ratio before and after the capital injection?"
    )

    solution = (
        "Step 1 — Baseline leverage:\n"
        f"  D/E_before = {fmt_usd(L)} ÷ {fmt_usd(E)} = {de_before:.{RATIO_DP}f}\n\n"
        "Step 2 — Equity raise (no change to liabilities):\n"
        f"  Equity_after = {fmt_usd(E)} + {fmt_usd(injection)} = {fmt_usd(E_after)}\n\n"
        "Step 3 — New leverage:\n"
        f"  D/E_after = {fmt_usd(L)} ÷ {fmt_usd(E_after)} = {de_after:.{RATIO_DP}f}"
    )

    return question, solution

# -----------------------------------------------------------------------
# INTERMEDIATE 2 — D/E after partial debt repayment and new borrowing
# -----------------------------------------------------------------------
def template_debt_to_equity_debt_repayment():
    """4:Intermediate:Compute D/E before and after simultaneous debt repayment and new borrowing."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    L, E = sample_liab_equity(L_range=(200_000, 1_000_000), E_range=(120_000, 500_000), rmin=0.4, rmax=2.5)
    repay = round_money(random.uniform(0.05 * L, 0.30 * L))   # repay 5–30% of L
    borrow = round_money(random.uniform(0.05 * L, 0.35 * L))  # borrow 5–35% of L

    de_before = round(L / E, RATIO_DP)
    L_after = round_money(L - repay + borrow)
    de_after = round(L_after / E, RATIO_DP)

    question = (
        f"All amounts are in USD. Round ratios to {RATIO_DP} decimals.\n\n"
        f"{company_name} in the {industry} sector has {fmt_usd(L)} in total liabilities and {fmt_usd(E)} in shareholders’ equity. "
        f"It repays {fmt_usd(repay)} of existing debt and takes {fmt_usd(borrow)} in new borrowing. "
        "Compute the D/E ratio before and after these changes."
    )

    solution = (
        "Step 1 — Baseline leverage:\n"
        f"  D/E_before = {fmt_usd(L)} ÷ {fmt_usd(E)} = {de_before:.{RATIO_DP}f}\n\n"
        "Step 2 — Adjust liabilities for both transactions:\n"
        f"  Liabilities_after = {fmt_usd(L)} − {fmt_usd(repay)} + {fmt_usd(borrow)} = {fmt_usd(L_after)}\n\n"
        "Step 3 — New leverage (equity unchanged):\n"
        f"  D/E_after = {fmt_usd(L_after)} ÷ {fmt_usd(E)} = {de_after:.{RATIO_DP}f}"
    )

    return question, solution

# --------------------------------------------------------------------------------
# ADVANCED — Scenario analysis: new DEBT vs. new EQUITY (compare both outcomes)
# --------------------------------------------------------------------------------
def template_debt_to_equity_scenario_analysis():
    """5:Advanced:Compute baseline D/E, then compare two financing scenarios: (1) Issue new debt; (2) Issue new equity."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    L, E = sample_liab_equity(L_range=(300_000, 1_500_000), E_range=(200_000, 1_000_000), rmin=0.4, rmax=2.5)
    issue_debt = round_money(random.uniform(0.08 * L, 0.40 * L))
    issue_equity = round_money(random.uniform(0.08 * E, 0.40 * E))

    de_base = round(L / E, RATIO_DP)

    # Scenario 1: new debt
    L_s1 = round_money(L + issue_debt)
    de_s1 = round(L_s1 / E, RATIO_DP)

    # Scenario 2: new equity
    E_s2 = round_money(E + issue_equity)
    de_s2 = round(L / E_s2, RATIO_DP)

    question = (
        f"All amounts are in USD. Round ratios to {RATIO_DP} decimals.\n\n"
        f"{company_name} ({industry}) currently has total liabilities of {fmt_usd(L)} and shareholders’ equity of {fmt_usd(E)}. "
        f"The firm is evaluating two financing options:\n"
        f"  • Scenario 1: Issue {fmt_usd(issue_debt)} of new debt.\n"
        f"  • Scenario 2: Issue {fmt_usd(issue_equity)} of new equity.\n"
        "Compute the D/E ratio under each scenario and compare them to the baseline."
    )

    solution = (
        "Step 1 — Baseline leverage:\n"
        f"  D/E_base = {fmt_usd(L)} ÷ {fmt_usd(E)} = {de_base:.{RATIO_DP}f}\n\n"
        "Step 2 — Scenario 1 (issue debt): liabilities increase, equity unchanged:\n"
        f"  D/E_S1 = {fmt_usd(L_s1)} ÷ {fmt_usd(E)} = {de_s1:.{RATIO_DP}f}\n\n"
        "Step 3 — Scenario 2 (issue equity): equity increases, liabilities unchanged:\n"
        f"  D/E_S2 = {fmt_usd(L)} ÷ {fmt_usd(E_s2)} = {de_s2:.{RATIO_DP}f}\n\n"
        "Interpretation: Issuing debt raises D/E (more leverage), while issuing equity lowers D/E (less leverage), "
        "holding other items constant."
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_debt_to_equity_simple,
        template_debt_to_equity_convertible_debt,
        template_debt_to_equity_capital_injection,
        template_debt_to_equity_debt_repayment,
        template_debt_to_equity_scenario_analysis,
    ]
    
    all_problems = []
    
    for template_func in templates:
        doc_parts = template_func.__doc__.split(':')
        id, level = doc_parts[0].strip(), doc_parts[1].strip()
        
        for i in range(num_instances):
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            
            question, solution = template_func()
            
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            
            all_problems.append(problem_entry)
            
            random.seed()
    
    random.shuffle(all_problems)

    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate leverage ratio problems.")
    parser.add_argument("--output_file", type=str, default="levratio_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
