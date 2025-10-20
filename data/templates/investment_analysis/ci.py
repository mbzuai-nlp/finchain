import random

# Named entities for investors and projects
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
project_names = [
    "Tesla Gigafactory", "Apple iPhone Launch", "Amazon Web Services Expansion", "SpaceX Starship Development",
    "Google Data Center Build", "Microsoft Azure", "Netflix Content Production", "Uber Autonomous Driving Initiative",
    "Facebook Metaverse", "Samsung Semiconductor Factory"
]

# Template 1: Simple CI Calculation
def template_ci_simple_calculation():
    """1: Basic: Simple Compound Interest Calculation"""
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    principal = random.randint(1_000, 5_000)        # $P
    rate      = round(random.uniform(2, 10), 2)      # r %
    time      = random.randint(1, 5)                 # t years

    question = (
        f"{investor_name} invested ${principal} in {project_name}. "
        f"The investment grows at an annual interest rate of {rate:.2f}% "
        f"compounded annually over {time} years. Calculate the compound interest."
    )

    # --- Computation section --------------------------------------------------
    # 1. Full-precision compound amount
    compound_amount = principal * (1 + rate / 100) ** time       # float

    # 2. **Round what we will display**
    compound_amount_disp = round(compound_amount, 2)             # $A
    ci_disp              = round(compound_amount_disp - principal, 2)  # $CI
    # -------------------------------------------------------------------------

    solution = (
        f"Step 1: Compute the compound amount:\n"
        f"  Compound Amount = $ {principal} × (1 + {rate/100:.4f})^{time}"
        f" = $ {compound_amount_disp:.2f}\n\n"
        f"Step 2: Compute the compound interest:\n"
        f"  Compound Interest = $ {compound_amount_disp:.2f} − $ {principal}"
        f" = $ {ci_disp:.2f}"
    )

    return question, solution


# Template 2: CI with Quarterly Compounding
def template_ci_quarterly_compounding():
    """2: Basic: Compound Interest with Quarterly Compounding"""
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    # Parameters
    principal = random.randint(1_000, 7_000)          # $
    rate      = round(random.uniform(2, 8), 2)        # annual %, two decimals
    time      = random.randint(1, 3)                  # years
    n         = 4                                     # quarterly

    # ---------- Question ----------
    question = (
        f"{investor_name} invests ${principal} in {project_name}. "
        f"The account earns {rate:.2f}% interest per year, compounded quarterly, "
        f"for {time} years. What is the total compound interest earned "
    )

    # ---------- Solution ----------
    # Step 1: future (compound) amount – keep full precision
    future_value = principal * (1 + rate / (100 * n)) ** (n * time)
    # Step 2: compound interest
    ci = future_value - principal

    # Round only for display
    fv_display = f"${future_value:.2f}"
    ci_display = f"${ci:.2f}"

    solution = (
        "Step 1. Compute the future value with quarterly compounding:\n"
        "  n = 4 periods per year.\n"
        "  Future Value = P × (1 + r / (100 × n))^(n × t)\n"
        f"              = ${principal} × (1 + {rate:.2f}% / (100 × 4))^(4 × {time})\n"
        f"              = ${principal} × (1 + {rate / (100 * n):.4f})^{4*time}\n"
        f"              = {fv_display}\n\n"
        "Step 2. Find the compound interest earned:\n"
        f"  Compound Interest = Future Value − Principal\n"
        f"                   = {fv_display} − ${principal}\n"
        f"                   = {ci_display}"
    )

    return question, solution


# Template 3: CI with Rate and Total Amount Known
def template_ci_rate_and_total_known():
    """3: Intermediate: Compound Interest with nominal rate, time, and frequency known"""

    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    # ---------- Parameters ----------
    total_amount = random.randint(5_000, 15_000)           # Final amount A ($)
    rate         = round(random.uniform(2, 10), 2)         # Nominal annual rate %
    time         = random.randint(1, 5)                    # Years
    freq_name, n = random.choice(
        [("semi‑annually", 2), ("quarterly", 4), ("monthly", 12)]
    )

    # ---------- Question ----------
    question = (
        f"{investor_name} received a total amount of ${total_amount:,.2f} "
        f"from their investment in {project_name}. "
        f"The investment grew at a nominal annual interest rate of {rate:.2f}% "
        f"compounded {freq_name} for {time} years. "
        f"Calculate the compound interest earned (in dollars)."
    )

    # ---------- Reasoning ----------
    # Step 1 – Periodic rate and (rounded) growth factor  ❱❱ same 6‑dp precision in calc & print
    periodic_rate = round(rate / 100 / n, 6)               # r_p
    growth_factor = round((1 + periodic_rate) ** (n * time), 6)

    # Step 2 – Principal P  ❱❱ uses the rounded growth_factor above
    principal = round(total_amount / growth_factor, 2)     # 2‑dp dollars

    # Step 3 – Compound interest CI  ❱❱ uses same rounded principal
    ci = round(total_amount - principal, 2)

    # ---------- Solution ----------
    solution = (
        f"Step 1 – Find the periodic rate and growth factor\n"
        f"  Periodic rate  = {rate:.2f}% ÷ {n} = {periodic_rate*100:.4f}%\n"
        f"  Growth factor  = (1 + {periodic_rate:.6f})^{n*time} = {growth_factor:.6f}\n\n"
        f"Step 2 – Compute the initial principal\n"
        f"  P = A ÷ growth factor = "
        f"${total_amount:,.2f} ÷ {growth_factor:.6f} = ${principal:,.2f}\n\n"
        f"Step 3 – Calculate the compound interest\n"
        f"  CI = A − P = ${total_amount:,.2f} − ${principal:,.2f} = ${ci:,.2f}"
    )

    return question, solution


def template_ci_half_yearly_variable_rate():
    """4: Intermediate: compound interest, semi‑annual compounding, rate changes mid‑way"""

    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    principal     = random.randint(2_000, 8_000)             # $P
    first_years   = random.randint(1, 3)                     # years at rate1
    second_years  = random.randint(1, 3)                     # years at rate2
    time          = first_years + second_years               # total years
    rate1         = round(random.uniform(3, 7), 2)           # first‑phase rate %
    rate2         = round(random.uniform(7, 10), 2)          # second‑phase rate %
    n             = 2                                        # semi‑annual compounding

    # ---------- Question ----------
    question = (
        f"{investor_name} invested ${principal} in {project_name}. "
        f"For the first {first_years} year{'s' if first_years>1 else ''} the investment earned "
        f"{rate1:.2f}% per annum, compounded semi‑annually. "
        f"After that, the rate changed to {rate2:.2f}% per annum (still compounded semi‑annually) "
        f"for another {second_years} year{'s' if second_years>1 else ''}. "
        f"How much **compound interest** is earned in total after {time} years?"
    )

    # ---------- Calculation ----------
    # Step 1: grow through the first phase
    amount_after_phase1 = principal * (1 + rate1 / (100 * n)) ** (n * first_years)

    # Step 2: grow through the second phase
    amount_exact        = amount_after_phase1 * (1 + rate2 / (100 * n)) ** (n * second_years)
    amount              = round(amount_exact, 2)

    # Step 3: compute compound interest
    ci                  = round(amount - principal, 2)

    # ---------- Solution ----------
    solution = (
        "Step 1 – Value after the first phase:\n"
        f"  $A₁ = $P × (1 + r₁/n)^(n·t₁)\n"
        f"      = ${principal} × (1 + {rate1:.2f}% ÷ (100×{n}))^{n*first_years}\n"
        f"      = ${amount_after_phase1:.2f}\n\n"
        "Step 2 – Value after the second phase:\n"
        f"  $A₂ = $A₁ × (1 + r₂/n)^(n·t₂)\n"
        f"      = ${amount_after_phase1:.2f} × (1 + {rate2:.2f}% ÷ (100×{n}))^{n*second_years}\n"
        f"      = ${amount:.2f}\n\n"
        "Step 3 – Compound interest earned:\n"
        f"  $CI = $A₂ – $P = ${amount:.2f} – ${principal} = ${ci:.2f}\n\n"
        f"**Answer : ${ci:.2f}**"
    )

    return question, solution


# Template 5: CI with Varying Compounding Frequencies
def template_ci_with_additional_deposit():
    """5: Advanced: Compound Interest with a Mid‑Term Additional Deposit (needs 4 steps)"""
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    # --- parameters ---
    principal = random.randint(2000, 8000)          # initial $
    rate      = round(random.uniform(3, 10), 2)     # % p.a.
    time      = random.randint(3, 7)                # total years (≥3 so a mid‑deposit makes sense)
    n         = random.choice([1, 2, 4, 12])        # compounds per year

    deposit   = random.randint(500, 4000)           # extra $
    deposit_time = random.randint(1, time - 1)      # year when deposit is made (strictly inside the horizon)

    # ------------------ QUESTION ------------------
    question = (
        f"{investor_name} initially invested ${principal} in {project_name} at an annual "
        f"rate of {rate:.2f}%, compounded {n} times a year, for a total of {time} years. "
        f"Exactly {deposit_time} years after the start, they added an extra ${deposit}"
        f"to the same account under the same rate and compounding frequency. "
        f"Calculate the total compound interest earned by the end of the {time} years."
    )

    # ------------------ SOLUTION ------------------
    # Step 1 – periodic rate
    periodic_rate = round(rate / (100 * n), 4)

    # Step 2 – grow the original principal for the full period
    periods_principal = n * time
    fv_principal = round(principal * (1 + periodic_rate) ** periods_principal, 2)

    # Step 3 – grow the later deposit for the remaining (time - deposit_time) years
    remaining_years = time - deposit_time
    periods_deposit = n * remaining_years
    fv_deposit = round(deposit * (1 + periodic_rate) ** periods_deposit, 2)

    # Step 4 – combine amounts and find compound interest
    total_future_value = round(fv_principal + fv_deposit, 2)
    total_contributions = principal + deposit
    compound_interest = round(total_future_value - total_contributions, 2)

    solution = (
        "Step 1 – Periodic rate:\n"
        f"  r = {rate:.2f}% / (100 × {n}) = {periodic_rate:.4f}\n\n"
        "Step 2 – Future value of the original principal:\n"
        f"  Periods = {n} × {time} = {periods_principal}\n"
        f"  FV₁ = ${principal} × (1 + {periodic_rate:.4f})^{periods_principal} = "
        f"${fv_principal:.2f}\n\n"
        "Step 3 – Future value of the additional deposit:\n"
        f"  Remaining years = {time} − {deposit_time} = {remaining_years}\n"
        f"  Periods = {n} × {remaining_years} = {periods_deposit}\n"
        f"  FV₂ = ${deposit} × (1 + {periodic_rate:.4f})^{periods_deposit} = "
        f"${fv_deposit:.2f}\n\n"
        "Step 4 – Total compound interest:\n"
        f"  Total FV = FV₁ + FV₂ = ${fv_principal:.2f} + ${fv_deposit:.2f} = "
        f"${total_future_value:.2f}\n"
        f"  Contributions = ${principal} + ${deposit} = ${total_contributions}\n"
        f"  **Compound Interest = Total FV − Contributions = "
        f"${total_future_value:.2f} − ${total_contributions} = ${compound_interest:.2f}**"
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
        template_ci_simple_calculation,
        template_ci_quarterly_compounding,
        template_ci_rate_and_total_known,
        template_ci_half_yearly_variable_rate,
        template_ci_with_additional_deposit
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
    output_file = "../../testset/investment_analysis/ci.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem, ensure_ascii=False))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()