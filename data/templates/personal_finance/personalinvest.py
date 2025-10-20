import random
from typing import Tuple
import json
import argparse
import pathlib

# =========================
# Helpers for consistency
# =========================
def _rand_money(lo: float, hi: float) -> float:
    """Return a 2-decimal USD amount as float (rounded only for display)."""
    return round(random.uniform(lo, hi), 2)

def _rand_pct(lo: float, hi: float) -> float:
    """Return a percent value (0-100) with 2 decimals."""
    return round(random.uniform(lo, hi), 2)

def _fmt_money(x: float) -> str:
    return f"${x:,.2f}"

def _fmt_pct(p: float) -> str:
    return f"{p:.2f}%"

# Set a stable list of names
_PEOPLE = ["John", "Aisha", "Ravi", "Sara", "David"]

# ============================================================
# EASY 1 — Simple compound growth (compounded annually)
# ============================================================
def template_compound_growth_easy() -> Tuple[str, str]:
    """1:Easy:future value given principal, annual rate (%), and years."""
    person = random.choice(_PEOPLE)
    P = _rand_money(100_000, 500_000)          # USD
    r_pct = _rand_pct(5.0, 15.0)               # % per year
    n = random.randint(5, 15)                  # years
    r = r_pct / 100.0

    FV = P * (1 + r) ** n
    question = (
        f"{person} invests {_fmt_money(P)} in an index fund that compounds annually at "
        f"{_fmt_pct(r_pct)}. What will the investment be worth after {n} years?"
    )

    solution = (
        "Step 1: Convert the annual rate to decimal for computation:\n"
        f"  r = {r_pct:.2f}% = {r:.4f}\n\n"
        "Step 2: Use the compound interest formula FV = P × (1 + r)^n:\n"
        f"  FV = {_fmt_money(P)} × (1 + {r:.4f})^{n}\n"
        f"  FV = {_fmt_money(FV)}\n\n"
        "Answer: " + _fmt_money(FV)
    )
    return question, solution

# ============================================================
# EASY 2 — Portfolio allocation amounts summing to 100%
# ============================================================
def template_portfolio_allocation_easy() -> Tuple[str, str]:
    """2:Easy:allocate a lump sum across stocks/bonds/real estate by % weights."""
    person = random.choice(_PEOPLE)
    age = random.randint(25, 55)
    total = _rand_money(1_000_000, 5_000_000)  # USD
    # Draw two weights; the third becomes the remainder
    w_stock = _rand_pct(40.0, 60.0)
    w_bond  = _rand_pct(20.0, 40.0)
    # Ensure the remainder is non-negative and round to 2 decimals in display
    remainder = round(100.00 - w_stock - w_bond, 2)
    # Guard against tiny negative due to floating noise
    if remainder < 0:
        # Nudge bonds down so the sum hits 100.00
        w_bond = round(w_bond + remainder, 2)  # remainder is negative here
        remainder = round(100.00 - w_stock - w_bond, 2)
    w_real = remainder

    a_stock = total * (w_stock / 100.0)
    a_bond  = total * (w_bond  / 100.0)
    a_real  = total * (w_real  / 100.0)

    question = (
        f"{person}, aged {age}, has {_fmt_money(total)} to invest.\n"
        f"They choose {_fmt_pct(w_stock)} in stocks, {_fmt_pct(w_bond)} in bonds, and "
        f"{_fmt_pct(w_real)} in real estate (total 100.00%). "
        "How many dollars go into each category?"
    )

    solution = (
        "Step 1: Convert percentages to weights and multiply by the total:\n"
        f"  Stocks = {_fmt_money(total)} × {_fmt_pct(w_stock)} = {_fmt_money(a_stock)}\n"
        f"  Bonds  = {_fmt_money(total)} × {_fmt_pct(w_bond)}  = {_fmt_money(a_bond)}\n"
        f"  Real estate = {_fmt_money(total)} × {_fmt_pct(w_real)} = {_fmt_money(a_real)}\n\n"
        "Check: amounts sum to the total.\n"
        f"  Sum = {_fmt_money(a_stock + a_bond + a_real)} = {_fmt_money(total)} (OK)"
    )
    return question, solution

# ============================================================
# INTERMEDIATE 1 — Retirement withdrawals (closed-form)
# ============================================================
def template_withdrawals_intermediate() -> Tuple[str, str]:
    """3:Intermediate:Remaining balance after n years with end-of-year withdrawals."""
    person = random.choice(_PEOPLE)
    age = random.randint(40, 60)
    P = _rand_money(1_000_000, 5_000_000)
    r_pct = _rand_pct(4.0, 8.0)
    r = r_pct / 100.0
    n = random.randint(5, 20)
    # Choose a sustainable withdrawal heuristic (2%–6% of initial per year)
    W = _rand_money(P * 0.02, P * 0.06)

    # Closed-form remaining balance after n years (end-of-year withdrawals)
    factor = (1 + r) ** n
    annuity_factor = (factor - 1) / r
    balance = P * factor - W * annuity_factor

    question = (
        f"{person}, aged {age}, has {_fmt_money(P)} invested in a fund compounding "
        f"annually at {_fmt_pct(r_pct)}. They plan to withdraw {_fmt_money(W)} at the "
        f"end of each year for {n} years. What will the account balance be "
        f"after {n} years (assume withdrawals at year-end)?"
    )

    solution = (
        "Step 1: Compute the growth factor and annuity factor (withdrawals at year-end):\n"
        f"  (1 + r)^n = (1 + {r:.4f})^{n} = {factor:.6f}\n"
        f"  Annuity factor = ((1 + r)^n - 1) / r = ({factor:.6f} - 1) / {r:.4f} = {annuity_factor:.6f}\n\n"
        "Step 2: Apply the closed-form for remaining balance:\n"
        f"  Balance_n = P*(1+r)^n - W*AnnuityFactor\n"
        f"            = {_fmt_money(P)}×{factor:.6f} - {_fmt_money(W)}×{annuity_factor:.6f}\n"
        f"            = {_fmt_money(balance)}\n\n"
        "Answer: " + _fmt_money(balance)
    )
    return question, solution

# ============================================================
# INTERMEDIATE 2 — Next-year range with volatility band
# ============================================================
def template_volatility_band_intermediate() -> Tuple[str, str]:
    """4:Intermediate:Apply a baseline growth, then an expected ±volatility band."""
    person = random.choice(_PEOPLE)
    age = random.randint(30, 50)
    P = _rand_money(500_000, 3_000_000)
    g_pct = _rand_pct(5.0, 20.0)    # baseline growth next year
    v_pct = _rand_pct(5.0, 15.0)    # expected fluctuation band
    g = g_pct / 100.0
    v = v_pct / 100.0

    base = P * (1 + g)
    upper = base * (1 + v)
    lower = base * (1 - v)

    question = (
        f"{person}, aged {age}, holds {_fmt_money(P)} in equities. Assume next year’s "
        f"baseline growth is {_fmt_pct(g_pct)}. Given an expected market volatility band "
        f"of ±{_fmt_pct(v_pct)} around that baseline, what range of values is plausible "
        "by the end of next year?"
    )

    solution = (
        "Step 1: Apply baseline growth to get next year’s base value:\n"
        f"  Base = {_fmt_money(P)} × (1 + {g:.4f}) = {_fmt_money(base)}\n\n"
        "Step 2: Apply the ±volatility band to the base:\n"
        f"  Upper = {_fmt_money(base)} × (1 + {v:.4f}) = {_fmt_money(upper)}\n"
        f"  Lower = {_fmt_money(base)} × (1 - {v:.4f}) = {_fmt_money(lower)}\n\n"
        "Answer: Range = " + _fmt_money(lower) + " to " + _fmt_money(upper)
    )
    return question, solution

# ============================================================
# ADVANCED — Diversification risk impact (numeric)
# ============================================================
def template_diversification_risk_advanced() -> Tuple[str, str]:
    """5:Advanced:Compute risk change after adding a new asset given vols & correlation."""
    person = random.choice(_PEOPLE)
    age = random.randint(35, 55)

    # Existing dollar amounts
    A_s = _rand_money(1_000_000, 5_000_000)
    A_b = _rand_money(500_000, 3_000_000)
    A_re = _rand_money(1_000_000, 5_000_000)

    # New asset amount
    A_new = _rand_money(500_000, 2_000_000)

    # Annualized vols (in %)
    vol_s_pct  = _rand_pct(15.0, 25.0)
    vol_b_pct  = _rand_pct(4.0, 10.0)
    vol_re_pct = _rand_pct(10.0, 18.0)
    vol_new_pct = _rand_pct(10.0, 22.0)

    # Pairwise correlations among existing assets (plausible ranges)
    rho_sb  = round(random.uniform(0.10, 0.40), 2)
    rho_sre = round(random.uniform(0.30, 0.60), 2)
    rho_bre = round(random.uniform(0.05, 0.30), 2)

    # Correlation of NEW asset with the *existing portfolio as a whole*
    rho_port_new = round(random.uniform(-0.50, 0.50), 2)

    # --- Step 1: Existing portfolio weights and volatility ---
    A_total_existing = A_s + A_b + A_re
    ws = A_s / A_total_existing
    wb = A_b / A_total_existing
    wre = A_re / A_total_existing

    # Convert vols to decimals
    sig_s  = vol_s_pct  / 100.0
    sig_b  = vol_b_pct  / 100.0
    sig_re = vol_re_pct / 100.0
    sig_new = vol_new_pct / 100.0

    # Variance of 3-asset portfolio:
    var_port = (
        (ws**2) * (sig_s**2) +
        (wb**2) * (sig_b**2) +
        (wre**2) * (sig_re**2) +
        2*ws*wb  * rho_sb  * sig_s * sig_b +
        2*ws*wre * rho_sre * sig_s * sig_re +
        2*wb*wre * rho_bre * sig_b * sig_re
    )
    sig_port = var_port ** 0.5  # existing portfolio stdev

    # --- Step 2: Combine existing portfolio with new asset ---
    A_total_all = A_total_existing + A_new
    w_port = A_total_existing / A_total_all
    w_new  = A_new / A_total_all

    var_total = (
        (w_port**2) * (sig_port**2) +
        (w_new**2)  * (sig_new**2) +
        2*w_port*w_new*rho_port_new*sig_port*sig_new
    )
    sig_total = var_total ** 0.5

    # Percentage change in volatility after diversification
    delta_pct = (sig_total / sig_port - 1.0) * 100.0

    question = (
        f"{person}, aged {age}, holds a portfolio of {_fmt_money(A_s)} in stocks, "
        f"{_fmt_money(A_b)} in bonds, and {_fmt_money(A_re)} in real estate. They plan to add "
        f"{_fmt_money(A_new)} to a new asset class.\n\n"
        "Annualized volatilities (stdevs):\n"
        f"  Stocks: {_fmt_pct(vol_s_pct)}, Bonds: {_fmt_pct(vol_b_pct)}, Real estate: {_fmt_pct(vol_re_pct)}, "
        f"New asset: {_fmt_pct(vol_new_pct)}\n"
        "Correlations among existing assets:\n"
        f"  ρ(S,B)={rho_sb:.2f}, ρ(S,RE)={rho_sre:.2f}, ρ(B,RE)={rho_bre:.2f}\n"
        f"Correlation of the new asset with the *existing portfolio as a whole*: ρ(Port,New)={rho_port_new:.2f}\n\n"
        "Question: Compute the portfolio’s annualized volatility before and after adding the new asset, "
        "and the percentage change in risk."
    )

    solution = (
        "Step 1: Compute existing-portfolio weights by dollars:\n"
        f"  w_S={ws:.4f}, w_B={wb:.4f}, w_RE={wre:.4f}\n\n"
        "Step 2: Convert volatilities to decimals and compute existing variance:\n"
        f"  σ_S={sig_s:.4f}, σ_B={sig_b:.4f}, σ_RE={sig_re:.4f}\n"
        "  Var_port = Σ w_i^2 σ_i^2 + 2 ΣΣ w_i w_j ρ_ij σ_i σ_j\n"
        f"          = {var_port:.6f}\n"
        f"  σ_port = √Var_port = {sig_port:.6f} ⇒ {_fmt_pct(sig_port*100)}\n\n"
        "Step 3: Combine portfolio with the new asset using 2-asset variance:\n"
        f"  Weights: w_port={w_port:.4f}, w_new={w_new:.4f};  σ_new={sig_new:.4f};  ρ(Port,New)={rho_port_new:.2f}\n"
        "  Var_total = w_port^2 σ_port^2 + w_new^2 σ_new^2 + 2 w_port w_new ρ σ_port σ_new\n"
        f"            = {var_total:.6f}\n"
        f"  σ_total = √Var_total = {sig_total:.6f} ⇒ {_fmt_pct(sig_total*100)}\n\n"
        "Step 4: Percent change in volatility:\n"
        f"  Δ% = (σ_total / σ_port − 1) × 100 = {delta_pct:.2f}%\n\n"
        "Answer: Existing vol = " + _fmt_pct(sig_port*100) +
        ", New vol = " + _fmt_pct(sig_total*100) +
        f", Change = {delta_pct:.2f}%"
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_compound_growth_easy,
        template_portfolio_allocation_easy,
        template_withdrawals_intermediate,
        template_volatility_band_intermediate,
        template_diversification_risk_advanced,
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
    parser = argparse.ArgumentParser(description="Generate personal investment problems.")
    parser.add_argument("--output_file", type=str, default="personalinvest_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
