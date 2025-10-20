import random
import math
import json
import argparse
import pathlib

# ---------------------------
# Helpers (formatting & draws)
# ---------------------------

def _fmt_money(x: float) -> str:
    return f"${x:,.2f}"

def _fmt_pct(p: float) -> str:
    return f"{p:.2f}%"

def _years_left(current_age: int, retirement_age: int) -> int:
    return max(1, retirement_age - current_age)

# Optional: set a seed for reproducibility in testing
# random.seed(42)

# ---------------------------------------------------
# EASY 1: Additional annual needed (NO investment returns)
# ---------------------------------------------------

def template_retirement_savings_simple():
    """1:Easy:Additional annual savings needed to hit a target, assuming NO investment returns (pure arithmetic)."""
    person_name = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    age = random.randint(30, 50)
    retirement_age = random.randint(60, 65)
    years_left = _years_left(age, retirement_age)

    target_savings = float(random.randint(2_000_000, 10_000_000))  # $
    current_savings = float(random.randint(200_000, 1_500_000))    # $
    annual_savings = float(random.randint(60_000, 250_000))        # $/year

    # Correct logic: extra needed beyond current annual_savings each year
    shortfall = max(0.0, target_savings - current_savings - annual_savings * years_left)
    extra_annual_needed = shortfall / years_left

    question = (
        f"{person_name}, aged {age}, plans to retire in {years_left} years with a goal of "
        f"{_fmt_money(target_savings)}. They currently have {_fmt_money(current_savings)} and "
        f"already save {_fmt_money(annual_savings)} at the end of each year. "
        f"Assuming no investment returns, how much MORE do they need to save per year "
        f"(in addition to the {_fmt_money(annual_savings)} they already save) to reach their goal?"
    )

    solution = (
        "Step 1: Compute the shortfall after accounting for current contributions (no returns).\n"
        f"  Shortfall S = Target − Current − (Annual × Years)\n"
        f"               = {_fmt_money(target_savings)} − {_fmt_money(current_savings)} − "
        f"({_fmt_money(annual_savings)} × {years_left}) = {_fmt_money(shortfall)}\n\n"
        "Step 2: Spread the remaining shortfall evenly across the years.\n"
        f"  Extra annual needed = S / Years = {_fmt_money(shortfall)} / {years_left} "
        f"= {_fmt_money(extra_annual_needed)} per year"
    )

    return question, solution

# ---------------------------------------------------
# EASY 2: Years needed to hit target (NO investment returns)
# ---------------------------------------------------

def template_retirement_years_to_target_simple():
    """2:Easy:Years required to hit a target with current savings and constant annual savings, assuming NO investment returns."""
    person_name = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    age = random.randint(25, 45)

    target_savings = float(random.randint(1_500_000, 6_000_000))  # $
    current_savings = float(random.randint(100_000, 800_000))     # $
    annual_savings = float(random.randint(80_000, 250_000))       # $/year

    remaining = max(0.0, target_savings - current_savings)
    if annual_savings <= 0:
        years_needed = math.inf  # Safeguard; won't occur by construction
    else:
        years_needed = math.ceil(remaining / annual_savings)

    question = (
        f"{person_name}, aged {age}, currently has {_fmt_money(current_savings)} saved and can set aside "
        f"{_fmt_money(annual_savings)} at the end of each year. Without assuming any investment returns, "
        f"how many years will it take to reach {_fmt_money(target_savings)}?"
    )

    solution = (
        "Step 1: Compute the remaining amount to reach the target.\n"
        f"  Remaining R = Target − Current = {_fmt_money(target_savings)} − {_fmt_money(current_savings)} "
        f"= {_fmt_money(remaining)}\n\n"
        "Step 2: Divide by annual savings and round up to a whole year.\n"
        f"  Years = ceil(R / Annual) = ceil({_fmt_money(remaining)} / {_fmt_money(annual_savings)}) = {years_needed} years"
    )

    return question, solution

# ------------------------------------------------------------------
# INTERMEDIATE 1: Future value with returns (current + contributions)
# ------------------------------------------------------------------

def template_retirement_investment_returns():
    """3:Intermediate:Future value at retirement with annual return r, combining (a) current savings growth and (b) end-of-year contributions (ordinary annuity)."""
    person_name = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    current_age = random.randint(30, 50)
    retirement_age = random.randint(60, 65)
    years_left = _years_left(current_age, retirement_age)

    current_savings = float(random.randint(300_000, 2_000_000))
    annual_savings = float(random.randint(80_000, 300_000))
    r_pct = round(random.uniform(4.0, 9.0), 2)        # %
    r = r_pct / 100.0                                 # decimal

    fv_current = current_savings * (1 + r) ** years_left
    annuity_factor = ((1 + r) ** years_left - 1) / r
    fv_contribs = annual_savings * annuity_factor
    total_fv = fv_current + fv_contribs

    question = (
        f"{person_name}, aged {current_age}, has {_fmt_money(current_savings)} now and contributes "
        f"{_fmt_money(annual_savings)} at the end of each year. If investments earn an average of {_fmt_pct(r_pct)} "
        f"annually, how much will {person_name} have in {years_left} years at retirement?"
    )

    solution = (
        "Step 1: Define the annual return as a decimal.\n"
        f"  r = {_fmt_pct(r_pct)} = {r:.4f}\n\n"
        "Step 2: Grow the current balance to retirement.\n"
        f"  FV(current) = Current × (1 + r)^n = {_fmt_money(current_savings)} × (1 + {r:.4f})^{years_left} "
        f"= {_fmt_money(fv_current)}\n\n"
        "Step 3: Future value of end-of-year contributions (ordinary annuity).\n"
        f"  AF = ((1 + r)^n − 1) / r = ((1 + {r:.4f})^{years_left} − 1) / {r:.4f}\n"
        f"  FV(contribs) = Annual × AF = {_fmt_money(annual_savings)} × AF = {_fmt_money(fv_contribs)}\n\n"
        "Step 4: Total future value.\n"
        f"  Total FV = FV(current) + FV(contribs) = {_fmt_money(fv_current)} + {_fmt_money(fv_contribs)} "
        f"= {_fmt_money(total_fv)}"
    )

    return question, solution

# ---------------------------------------------------------
# INTERMEDIATE 2: Inflation adjustment of a real target
# ---------------------------------------------------------

def template_retirement_inflation_adjustment():
    """4:Intermediate:Convert a target expressed in today's dollars into the nominal amount needed at retirement using inflation g."""
    person_name = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    current_age = random.randint(30, 50)
    retirement_age = random.randint(60, 65)
    years_left = _years_left(current_age, retirement_age)

    target_today = float(random.randint(2_500_000, 12_000_000))
    g_pct = round(random.uniform(2.0, 5.0), 2)
    g = g_pct / 100.0

    nominal_needed = target_today * (1 + g) ** years_left

    question = (
        f"{person_name}, aged {current_age}, wants {_fmt_money(target_today)} in today’s purchasing power. "
        f"If retirement is in {years_left} years and inflation averages {_fmt_pct(g_pct)} per year, "
        f"what nominal amount will be needed at retirement to match {_fmt_money(target_today)} today?"
    )

    solution = (
        "Step 1: Express inflation as a decimal.\n"
        f"  g = {_fmt_pct(g_pct)} = {g:.4f}\n\n"
        "Step 2: Inflate today’s target to retirement.\n"
        f"  Nominal needed = Target_today × (1 + g)^n "
        f"= {_fmt_money(target_today)} × (1 + {g:.4f})^{years_left} = {_fmt_money(nominal_needed)}"
    )

    return question, solution

# -------------------------------------------------------------------------
# ADVANCED: Early retirement feasibility (pre/post returns + withdrawals)
# -------------------------------------------------------------------------

def template_retirement_early():
    """5:Advanced:Early retirement feasibility. Pre-retirement growth at r_pre, contributions (ordinary annuity), then withdrawals for N years with post-retirement return r_post."""
    person_name = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    current_age = random.randint(30, 50)
    early_retire_age = random.randint(max(current_age + 5, 50), 60)
    years_until_ret = _years_left(current_age, early_retire_age)

    current_savings = float(random.randint(400_000, 2_500_000))
    annual_savings = float(random.randint(100_000, 350_000))

    r_pre_pct = round(random.uniform(4.0, 8.0), 2)
    r_pre = r_pre_pct / 100.0

    r_post_pct = round(max(1.0, r_pre_pct * 0.75), 2)  # conservative, at least 1%
    r_post = r_post_pct / 100.0

    annual_withdrawal = float(random.randint(250_000, 900_000))
    life_expectancy = random.randint(max(early_retire_age + 15, 75), 90)
    retirement_years = max(1, life_expectancy - early_retire_age)

    # Future value at retirement
    fv_current = current_savings * (1 + r_pre) ** years_until_ret
    af_pre = ((1 + r_pre) ** years_until_ret - 1) / r_pre
    fv_contribs = annual_savings * af_pre
    total_at_retirement = fv_current + fv_contribs

    # Capital required to fund withdrawals for retirement_years at r_post
    # PV of ordinary annuity: W * [1 - (1 + r_post)^(-N)] / r_post
    required_capital = annual_withdrawal * (1 - (1 + r_post) ** (-retirement_years)) / r_post
    surplus = total_at_retirement - required_capital

    question = (
        f"{person_name}, currently {current_age}, wants to retire at {early_retire_age}. "
        f"They have {_fmt_money(current_savings)} now and can save {_fmt_money(annual_savings)} at the end of each year. "
        f"Assume pre-retirement returns of {_fmt_pct(r_pre_pct)} and post-retirement returns of {_fmt_pct(r_post_pct)}. "
        f"If they plan to withdraw {_fmt_money(annual_withdrawal)} each year for {retirement_years} years "
        f"(life expectancy {life_expectancy}), will their savings be sufficient?"
    )

    solution = (
        "Step 1: Convert returns to decimals.\n"
        f"  r_pre = {_fmt_pct(r_pre_pct)} = {r_pre:.4f},  r_post = {_fmt_pct(r_post_pct)} = {r_post:.4f}\n\n"
        "Step 2: Project savings to retirement.\n"
        f"  FV(current) = {_fmt_money(current_savings)} × (1 + {r_pre:.4f})^{years_until_ret} = {_fmt_money(fv_current)}\n"
        f"  AF_pre = ((1 + r_pre)^{years_until_ret} − 1) / r_pre\n"
        f"  FV(contribs) = {_fmt_money(annual_savings)} × AF_pre = {_fmt_money(fv_contribs)}\n"
        f"  Total at retirement = {_fmt_money(total_at_retirement)}\n\n"
        "Step 3: Capital required for withdrawals (PV of annuity).\n"
        f"  Required = W × [1 − (1 + r_post)^(-N)] / r_post\n"
        f"           = {_fmt_money(annual_withdrawal)} × [1 − (1 + {r_post:.4f})^{-{retirement_years}}] / {r_post:.4f}\n"
        f"           = {_fmt_money(required_capital)}\n\n"
        "Step 4: Compare.\n"
        f"  Surplus/Shortfall = Total − Required = {_fmt_money(total_at_retirement)} − {_fmt_money(required_capital)} "
        f"= {_fmt_money(surplus)}\n\n"
        + (
            "Result: The plan is feasible with a projected surplus."
            if surplus >= 0 else
            "Result: The plan is NOT feasible as-is; consider higher savings, later retirement, lower withdrawals, or different asset mix."
        )
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_retirement_savings_simple,
        template_retirement_years_to_target_simple,
        template_retirement_investment_returns,
        template_retirement_inflation_adjustment,
        template_retirement_early,
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
    parser = argparse.ArgumentParser(description="Generate retirement savings problems.")
    parser.add_argument("--output_file", type=str, default="saveretire_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
