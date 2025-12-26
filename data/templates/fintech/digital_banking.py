import random
import json
import math  # amortisation math

###############################################################################
# Data Pools
###############################################################################
user_names = [
    "Alice Wu",
    "Brad Johnson",
    "Carla Simmons",
    "Daniel Craig",
    "Eva Gonzalez",
]

digital_banks = [
    "NeoBank",
    "FinEdge",
    "CloudBank",
    "BrightPay",
    "MobileMoney",
]

###############################################################################
# EASY TEMPLATES (2 true reasoning steps, single final answer)
###############################################################################


def template_db_easy1():
    """1:Basic: Simple‑Interest Ending Balance (single value)
    Variables:
      • Principal (P)
      • Annual simple interest (r)
      • Time in years (t)
    Steps (2):
      1) Interest = P × r × t
      2) Ending balance = P + interest (answer)
    Returns → (question, solution)
    """
    user = random.choice(user_names)
    bank = random.choice(digital_banks)
    principal = random.randint(500, 5_000)
    rate = round(random.uniform(0.01, 0.05), 3)
    years = random.randint(1, 3)

    interest = principal * rate * years
    ending_balance = principal + interest

    question = (
        f"{user} deposits $${principal} into a simple‑interest savings account at {bank}. "
        f"The account pays {rate*100:.2f}% per year. "
        f"How much money will be in the account after {years} year(s)? Give the ending balance in dollars."
    )

    solution = (
        f"Step 1: Interest = P × r × t = $${principal} × {rate:.3f} × {years} = $${interest:.2f}\n\n"
        f"Step 2 (answer): Ending balance = $${principal} + $${interest:.2f} = $${ending_balance:.2f}"
    )

    return question, solution


def template_db_easy2():
    """2:Basic: Mobile‑Transfer Total Deduction (single value)
    Variables:
      • Transfer amount (A)
      • Fee rate (f)
    Steps (2):
      1) Fee = A × f
      2) Total deduction = A + fee (answer)
    """
    user = random.choice(user_names)
    bank = random.choice(digital_banks)
    amount = round(random.uniform(50, 500), 2)
    fee_rate = round(random.uniform(0.005, 0.02), 3)

    fee = amount * fee_rate
    total = amount + fee

    question = (
        f"{user} uses {bank}'s app to transfer $${amount:.2f}. "
        f"The platform charges a {fee_rate*100:.2f}% fee. "
        f"What is the TOTAL amount that will be deducted from {user}'s account?"
    )

    solution = (
        f"Step 1: Fee = $${amount:.2f} × {fee_rate:.3f} = $${fee:.2f}\n\n"
        f"Step 2 (answer): Total deduction = $${amount:.2f} + $${fee:.2f} = $${total:.2f}"
    )

    return question, solution

###############################################################################
# INTERMEDIATE TEMPLATES (3 genuine reasoning steps, single final answer)
###############################################################################


def template_db_medium1():
    """3:Intermediate: Future Value of Monthly Deposits (single value)
    Variables:
      • Monthly deposit (D)
      • Annual nominal rate (r)
      • Number of months (n)
    Steps (3):
      1) Monthly rate = r / 12
      2) Plug values into FV‑of‑annuity formula (symbolic)
      3) Evaluate FV numerically (answer)
    """
    user = random.choice(user_names)
    bank = random.choice(digital_banks)
    monthly_deposit = random.randint(50, 300)
    annual_rate = round(random.uniform(0.02, 0.06), 3)
    months = random.choice([12, 24, 36])

    monthly_rate = annual_rate / 12
    fv = monthly_deposit * (((1 + monthly_rate) ** months - 1) / monthly_rate)

    question = (
        f"{user} sets up a $${monthly_deposit} monthly deposit at {bank}, "
        f"earning {annual_rate*100:.2f}% APR compounded monthly. "
        f"What will the account balance be after {months} months?"
    )

    solution = (
        f"Step 1: Monthly rate = {annual_rate:.3f} / 12 = {monthly_rate:.5f}\n\n"
        f"Step 2: FV = D × [((1 + r)^n − 1) / r] (plugging symbols, not yet solved)\n\n"
        f"Step 3 (answer): FV = $${monthly_deposit} × (((1 + {monthly_rate:.5f})^{months} − 1) / {monthly_rate:.5f}) ≈ $${fv:,.2f}"
    )

    return question, solution
    

def template_db_medium2():
    """4:Intermediate: Highest-Spend Dollar Amount  (3 steps)
    Steps (3):
      1) Sum spending per category
      2) Identify the category with the maximum total
      3) Report that maximum dollar amount   (answer)
    """
    user = random.choice(user_names)
    categories = ["Food Delivery","Streaming","Ride-Hailing","Online Shopping","Subscriptions"]
    tx = [(random.choice(categories), round(random.uniform(5,120),2)) for _ in range(random.randint(4,7))]

    # Step-1 aggregation
    spend = {}
    for c,a in tx:
        spend[c] = spend.get(c,0)+a

    # Step-2 find maximum
    top_cat, top_amt = max(spend.items(), key=lambda x: x[1])

    # --- craft Q&A ---
    tx_lines = "\n".join(f"  • {c}: $${a:.2f}" for c,a in tx)
    question = (
        f"{user}'s wallet log shows:\n{tx_lines}\n\n"
        f"What is the DOLLAR AMOUNT of the category with the highest total spend?"
    )

    spend_lines = "\n".join(f"  {c}: $${spend[c]:.2f}" for c in spend)
    solution = (
        f"Step 1: Aggregate spending\n{spend_lines}\n\n"
        f"Step 2: Highest category = {top_cat} with $${top_amt:.2f}\n\n"
        f"Step 3 (answer): $${top_amt:.2f}"
    )
    return question, solution


###############################################################################
# ADVANCED TEMPLATE (4 genuine steps, single final answer)
###############################################################################


def template_db_hard1():
    """5:Advanced: Loan Payoff Months After Extra Payment  (4 steps)"""
    user = random.choice(user_names)
    bank = random.choice(digital_banks)
    principal     = random.randint(5_000, 15_000)
    annual_rate   = round(random.uniform(0.04, 0.09), 3)
    years         = random.choice([2,3,4])
    months_total  = years*12
    extra_month   = random.randint(6, months_total//2)
    extra_payment = random.randint(500, 2_000)

    i = annual_rate/12
    payment = principal*i / (1-(1+i)**(-months_total))

    # amortise to extra-payment month
    bal = principal
    for _ in range(extra_month):
        bal -= (payment - bal*i)

    bal_after_extra = bal - extra_payment

    # remaining months solution
    rem_months = 0 if bal_after_extra<=0 else math.ceil(
        math.log(payment/(payment-bal_after_extra*i), 1+i)
    )

    question = (
        f"{user} borrows $${principal} from {bank} at {annual_rate*100:.2f}% APR for {years} years. "
        f"The monthly payment is kept constant.  After {extra_month} months an extra $${extra_payment} "
        f"lump sum is paid.  How many **MONTHS** remain on the loan thereafter?"
    )

    solution = (
        f"Step 1: Monthly payment = P·i / (1−(1+i)^−n) = $${payment:,.2f}\n\n"
        f"Step 2: Balance just before extra payment ≈ $${bal:,.2f}; "
        f"after extra payment = $${bal_after_extra:,.2f}\n\n"
        f"Step 3: Remaining months satisfy\n"
        f"        payment = bal·i / (1−(1+i)^−m)  →  "
        f"m = ln[p/(p−bal·i)] / ln(1+i)\n\n"
        f"Step 4 (answer): m ≈ {rem_months} month(s)"
    )
    return question, solution


###############################################################################
# MAIN – Generate JSONL test‑set
###############################################################################

def main():
    templates = [
        template_db_easy1,
        template_db_easy2,
        template_db_medium1,
        template_db_medium2,
        template_db_hard1,
    ]

    all_problems = []
    for template_func in templates:
        id_ = template_func.__doc__.split(" – ")[0].split(":")[0].strip()
        level = template_func.__doc__.split(" – ")[0].split(":")[1].strip()

        for _ in range(10):
            seed = random.randint(1_000_000_000, 4_000_000_000)
            random.seed(seed)
            question, solution = template_func()
            all_problems.append(
                {
                    "seed": seed,
                    "id": id_,
                    "level": level,
                    "question": question,
                    "solution": solution,
                }
            )
            random.seed()  # reset RNG

    random.shuffle(all_problems)

    outfile = "../../testset/fintech/digital_banking.jsonl"
    with open(outfile, "w") as f:
        for p in all_problems:
            f.write(json.dumps(p))
            f.write("\n")

    print(f"Created {len(all_problems)} problems → {outfile}")


if __name__ == "__main__":
    main()
