import random
from math import ceil
import json
import argparse
import pathlib

# ----------------------------- #
# Helpers (formatting & checks) #
# ----------------------------- #

def fmt_usd(x: float) -> str:
    return f"${x:,.2f}"

def fmt_pct(x: float) -> str:
    # x is a percent number, e.g., 7.5 -> "7.50%"
    return f"{x:.2f}%"

def fmt_rate_dec(x: float) -> str:
    # x is a decimal monthly rate, e.g., 0.00625 -> "0.006250"
    return f"{x:.6f}"

def ensure_bounds_years_paid(total_years: int, max_paid: int = None) -> int:
    """Return a valid years_paid strictly less than total_years."""
    if max_paid is None or max_paid >= total_years:
        max_paid = max(1, total_years - 1)
    return random.randint(1, max_paid)

# Named entities for companies and industries
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]
industry_names = ["automotive", "technology", "e-commerce", "aerospace", "internet services"]

# ------------------------------------------------ #
# Basic 1: Loan Repayment with Simple Interest      #
# ------------------------------------------------ #
def template_loan_repayment_simple():
    """1:Basic:Simple interest, single repayment at maturity."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    loan_amount = float(random.randint(500_000, 5_000_000))           # USD
    interest_rate_pct = round(random.uniform(3.0, 12.0), 2)           # annual % (nominal)
    loan_term_years = random.randint(3, 15)

    r = interest_rate_pct / 100.0  # decimal annual rate

    question = (
        f"{company_name}, operating in the {industry} industry, takes a loan of {fmt_usd(loan_amount)} "
        f"at a fixed annual simple interest rate of {fmt_pct(interest_rate_pct)} for {loan_term_years} years. "
        f"Using simple interest, calculate the total amount repaid at the end of the term."
    )

    total_repayment = loan_amount * (1 + r * loan_term_years)

    solution = (
        "Step 1: Convert the annual simple interest rate to decimal: "
        f"{fmt_pct(interest_rate_pct)} = {r:.4f}.\n"
        "Step 2: Apply the simple interest total-repayment formula:\n"
        "        Total = Principal × (1 + r × t)\n"
        f"              = {fmt_usd(loan_amount)} × (1 + {r:.4f} × {loan_term_years})\n"
        f"              = {fmt_usd(total_repayment)}."
    )

    return question, solution

# ------------------------------------------------------- #
# Basic 2: Level-payment mortgage-style monthly installment #
# ------------------------------------------------------- #
def template_loan_repayment_monthly_installments():
    """2:Basic:Standard amortization monthly payment (no extras)."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    loan_amount = float(random.randint(1_000_000, 10_000_000))        # USD
    annual_rate_pct = round(random.uniform(4.0, 10.0), 2)              # %
    term_years = random.randint(5, 20)

    r_m = (annual_rate_pct / 100.0) / 12.0
    n = term_years * 12

    question = (
        f"{company_name}, a leading company in the {industry} industry, borrows {fmt_usd(loan_amount)} "
        f"at an annual interest rate of {fmt_pct(annual_rate_pct)} to be repaid over {term_years} years "
        "via equal monthly installments. Compute the monthly payment."
    )

    # Monthly payment (M) = P * [ r(1+r)^n / ((1+r)^n - 1) ]
    numerator = r_m * (1 + r_m) ** n
    denominator = (1 + r_m) ** n - 1
    monthly_payment = loan_amount * (numerator / denominator)

    solution = (
        "Step 1: Convert to monthly rate and number of payments:\n"
        f"        r_m = {fmt_pct(annual_rate_pct)} / 12 = {fmt_rate_dec(r_m)} ;  n = {n} months.\n"
        "Step 2: Apply the amortization formula:\n"
        "        M = P × [ r_m(1+r_m)^n / ((1+r_m)^n − 1) ]\n"
        f"          = {fmt_usd(loan_amount)} × [ {fmt_rate_dec(r_m)}(1+{fmt_rate_dec(r_m)})^{n} / "
        f"((1+{fmt_rate_dec(r_m)})^{n} − 1) ]\n"
        f"          = {fmt_usd(monthly_payment)}."
    )

    return question, solution

# ---------------------------------------------------------------- #
# Intermediate 1: Extra fixed annual principal prepayment           #
# ---------------------------------------------------------------- #
def template_loan_repayment_with_extra_payments():
    """3:Intermediate:Monthly amortization + fixed extra payment once per year on principal."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    loan_amount = float(random.randint(2_000_000, 10_000_000))
    annual_rate_pct = round(random.uniform(5.0, 10.0), 2)
    term_years = random.randint(5, 25)
    extra_annual = float(random.randint(100_000, 500_000))

    r_m = (annual_rate_pct / 100.0) / 12.0
    n = term_years * 12

    # monthly payment without rounding for simulation accuracy
    M = loan_amount * (r_m * (1 + r_m) ** n) / ((1 + r_m) ** n - 1)

    # Simulate month-by-month and apply extra at the end of each year
    balance = loan_amount
    months = 0
    total_interest_paid = 0.0

    while balance > 1e-8:
        # monthly interest
        interest = balance * r_m
        principal = min(M - interest, balance)
        balance -= principal
        total_interest_paid += interest
        months += 1

        # extra principal once every 12 months (end-of-year)
        if months % 12 == 0 and balance > 0:
            balance = max(0.0, balance - extra_annual)

    new_months = months
    original_months = n
    reduction_months = max(0, original_months - new_months)
    red_years, red_months = divmod(reduction_months, 12)
    new_years, new_rem_months = divmod(new_months, 12)

    question = (
        f"{company_name} in the {industry} industry borrows {fmt_usd(loan_amount)} at "
        f"{fmt_pct(annual_rate_pct)} for {term_years} years (equal monthly payments). "
        f"The company also pays an extra {fmt_usd(extra_annual)} toward principal at the end of every year. "
        "Find the new payoff time and how much sooner the loan is repaid compared with the original schedule."
    )

    solution = (
        "Step 1: Compute the standard monthly payment (no extras):\n"
        f"        r_m = {fmt_pct(annual_rate_pct)} / 12 = {fmt_rate_dec(r_m)} ;  n = {n}\n"
        "        M = P × [ r_m(1+r_m)^n / ((1+r_m)^n − 1) ]\n"
        f"          = {fmt_usd(loan_amount)} × [ {fmt_rate_dec(r_m)}(1+{fmt_rate_dec(r_m)})^{n} / "
        f"((1+{fmt_rate_dec(r_m)})^{n} − 1) ]\n"
        f"          = {fmt_usd(M)}.\n"
        "Step 2: Amortize month-by-month and subtract the extra principal once every 12 months.\n"
        f"        Payoff occurs after {new_months} months → {new_years} years and {new_rem_months} months.\n"
        "Step 3: Compare to the original term:\n"
        f"        Original = {original_months} months, New = {new_months} months → "
        f"reduction = {reduction_months} months ({red_years} years and {red_months} months)."
    )

    return question, solution

# --------------------------------------------------------------- #
# Intermediate 2: Refinancing after some years (new loan term)    #
# --------------------------------------------------------------- #
def template_loan_repayment_with_refinancing():
    """4:Intermediate:Compute remaining balance after years_paid of the original loan, then compute new monthly payment for a specified new (refinance) term at a lower rate."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    P = float(random.randint(3_000_000, 15_000_000))  # Original principal
    orig_rate_pct = round(random.uniform(5.0, 10.0), 2)
    orig_term_years = random.randint(10, 30)          # ORIGINAL total term (given in question!)
    years_paid = ensure_bounds_years_paid(orig_term_years)
    new_rate_pct = round(random.uniform(3.0, 7.0), 2)
    new_term_years = random.randint(5, 20)            # Term of the REFINANCED loan

    r_m = (orig_rate_pct / 100.0) / 12.0
    n = orig_term_years * 12
    p = years_paid * 12

    # Original monthly payment
    M = P * (r_m * (1 + r_m) ** n) / ((1 + r_m) ** n - 1)

    # Remaining balance after p payments: B_p = P(1+r)^p − M[(1+r)^p − 1]/r
    Bp = P * (1 + r_m) ** p - M * ((1 + r_m) ** p - 1) / r_m
    Bp = max(0.0, Bp)

    # New monthly payment with new rate and new term
    r_new = (new_rate_pct / 100.0) / 12.0
    n_new = new_term_years * 12
    M_new = Bp * (r_new * (1 + r_new) ** n_new) / ((1 + r_new) ** n_new - 1)

    question = (
        f"{company_name}, a company in the {industry} industry, originally borrowed {fmt_usd(P)} "
        f"at {fmt_pct(orig_rate_pct)} for {orig_term_years} years. After paying for {years_paid} years, "
        f"it plans to refinance the remaining balance at {fmt_pct(new_rate_pct)} for a new term of {new_term_years} years. "
        "Calculate the new monthly payment after refinancing."
    )

    solution = (
        "Step 1: Original monthly payment:\n"
        f"        r_m = {fmt_pct(orig_rate_pct)} / 12 = {fmt_rate_dec(r_m)} ;  n = {n}\n"
        "        M = P × [ r_m(1+r_m)^n / ((1+r_m)^n − 1) ]\n"
        f"          = {fmt_usd(P)} × [ {fmt_rate_dec(r_m)}(1+{fmt_rate_dec(r_m)})^{n} / "
        f"((1+{fmt_rate_dec(r_m)})^{n} − 1) ]\n"
        f"          = {fmt_usd(M)}.\n"
        "Step 2: Remaining balance after p payments (p = years_paid × 12):\n"
        "        B_p = P(1+r_m)^p − M[(1+r_m)^p − 1]/r_m\n"
        f"          = {fmt_usd(P)}(1+{fmt_rate_dec(r_m)})^{p} − {fmt_usd(M)}[(1+{fmt_rate_dec(r_m)})^{p} − 1]/{fmt_rate_dec(r_m)}\n"
        f"          = {fmt_usd(Bp)}.\n"
        "Step 3: New monthly payment with new rate & term:\n"
        f"        r_new = {fmt_pct(new_rate_pct)} / 12 = {fmt_rate_dec(r_new)} ;  n_new = {n_new}\n"
        "        M_new = B_p × [ r_new(1+r_new)^{n_new} / ((1+r_new)^{n_new} − 1) ]\n"
        f"          = {fmt_usd(Bp)} × [ {fmt_rate_dec(r_new)}(1+{fmt_rate_dec(r_new)})^{n_new} / "
        f"((1+{fmt_rate_dec(r_new)})^{n_new} − 1) ]\n"
        f"          = {fmt_usd(M_new)}."
    )

    return question, solution

# ------------------------------------------------------------------------- #
# Advanced: Lump-sum early payoff (keep same monthly payment, shorten term) #
# ------------------------------------------------------------------------- #
def template_loan_repayment_early_payoff():
    """5:Advanced:After a lump-sum payment at time t, continue paying the SAME monthly payment (no recast)."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    P = float(random.randint(5_000_000, 20_000_000))
    rate_pct = round(random.uniform(4.0, 9.0), 2)
    term_years = random.randint(10, 30)
    years_paid = ensure_bounds_years_paid(term_years, max_paid=min(15, term_years-1))
    lump_sum = float(random.randint(1_000_000, 5_000_000))

    r_m = (rate_pct / 100.0) / 12.0
    n = term_years * 12
    p = years_paid * 12

    # Original monthly payment
    M = P * (r_m * (1 + r_m) ** n) / ((1 + r_m) ** n - 1)

    # Remaining balance after p payments
    Bp = P * (1 + r_m) ** p - M * ((1 + r_m) ** p - 1) / r_m
    Bp = max(0.0, Bp)

    # Scenario A (no early payoff): total remaining interest
    remaining_installments = n - p
    total_payments_remaining = M * remaining_installments
    interest_without = total_payments_remaining - Bp

    # Scenario B (make lump-sum now, keep SAME M, shorten term)
    B_after = max(0.0, Bp - lump_sum)

    months_b = 0
    interest_with = 0.0
    balance = B_after

    while balance > 1e-8:
        interest = balance * r_m
        principal = min(M - interest, balance)
        balance -= principal
        interest_with += interest
        months_b += 1

        # Guard against pathological near-zero interest situations
        if months_b > n:  # should not happen, but prevents infinite loop
            break

    months_saved = max(0, (n - p) - months_b)
    saved_years, saved_months = divmod(months_saved, 12)

    interest_saved = max(0.0, interest_without - interest_with)

    question = (
        f"{company_name} in the {industry} industry borrowed {fmt_usd(P)} at {fmt_pct(rate_pct)} for {term_years} years. "
        f"After {years_paid} years of regular payments, the company makes a lump-sum payment of {fmt_usd(lump_sum)} and then "
        "continues paying the same monthly amount. How much interest is saved, and by how many months is the payoff accelerated "
        "compared with staying on schedule?"
    )

    solution = (
        "Step 1: Original monthly payment:\n"
        f"        r_m = {fmt_pct(rate_pct)} / 12 = {fmt_rate_dec(r_m)} ;  n = {n}\n"
        "        M = P × [ r_m(1+r_m)^n / ((1+r_m)^n − 1) ]\n"
        f"          = {fmt_usd(P)} × [ {fmt_rate_dec(r_m)}(1+{fmt_rate_dec(r_m)})^{n} / "
        f"((1+{fmt_rate_dec(r_m)})^{n} − 1) ]\n"
        f"          = {fmt_usd(M)}.\n"
        "Step 2: Remaining balance after p payments (p = years_paid × 12):\n"
        "        B_p = P(1+r_m)^p − M[(1+r_m)^p − 1]/r_m\n"
        f"          = {fmt_usd(P)}(1+{fmt_rate_dec(r_m)})^{p} − {fmt_usd(M)}[(1+{fmt_rate_dec(r_m)})^{p} − 1]/{fmt_rate_dec(r_m)}\n"
        f"          = {fmt_usd(Bp)}.\n"
        "Step 3: Scenario A — stay on schedule:\n"
        f"        Remaining installments = {n - p};  Total payments remaining = {fmt_usd(total_payments_remaining)}\n"
        f"        Interest remaining (A) = {fmt_usd(interest_without)}.\n"
        "Step 4: Scenario B — make lump-sum now, keep M the same:\n"
        f"        New balance = B_p − lump_sum = {fmt_usd(Bp)} − {fmt_usd(lump_sum)} = {fmt_usd(B_after)}\n"
        "        Amortize with the same M until balance reaches 0 to find new payoff time and interest.\n"
        f"        New months to finish = {months_b}; Interest (B) = {fmt_usd(interest_with)}.\n"
        "Step 5: Savings and acceleration:\n"
        f"        Interest saved = (A) − (B) = {fmt_usd(interest_without)} − {fmt_usd(interest_with)} = {fmt_usd(interest_saved)}\n"
        f"        Months saved = {(n - p)} − {months_b} = {months_saved} "
        f"({saved_years} years and {saved_months} months)."
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_loan_repayment_simple,
        template_loan_repayment_monthly_installments,
        template_loan_repayment_with_extra_payments,
        template_loan_repayment_with_refinancing,
        template_loan_repayment_early_payoff,
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
    parser = argparse.ArgumentParser(description="Generate loan repayment problems.")
    parser.add_argument("--output_file", type=str, default="loanrepay_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
