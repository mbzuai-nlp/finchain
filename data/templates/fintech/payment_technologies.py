import random
import json
import math   # used for a few percentage-rate calculations

###############################################################################
# Data Pools
###############################################################################
user_names = ["Alice Wu", "Brad Johnson", "Carla Simmons", "Daniel Craig", "Eva Gonzalez"]
merchant_names = ["Cafe Aroma", "TechZone", "FashionHub", "BookNook", "GreenGrocer"]
payment_platforms = ["PayWave", "QuickPay", "TapX", "FlexiPay", "ZenoPay"]

###############################################################################
# BASIC TEMPLATES (2 steps, single numeric answer)
###############################################################################

def template_pt_easy1():
    """
    1:Basic: Card Processing Net Amount (single answer)
    Variables:
      • Sale amount (A)
      • Merchant discount rate (m)
    Steps (2):
      1) Fee = A × m
      2) Net amount merchant receives = A − Fee  (answer)
    """
    merchant = random.choice(merchant_names)
    platform = random.choice(payment_platforms)
    amount   = round(random.uniform(20, 500), 2)
    mdr      = round(random.uniform(0.015, 0.03), 4)   # 1.5 %–3 %

    fee = amount * mdr
    net = amount - fee

    question = (
        f"{merchant} processes a ${amount:.2f} card payment through {platform}. "
        f"The platform charges a merchant-discount rate of {mdr*100:.2f}%. "
        f"How much money does {merchant} receive **after** the fee is deducted?"
    )

    solution = (
        f"Step 1: Fee = ${amount:.2f} × {mdr:.4f} = ${fee:.2f}\n\n"
        f"Step 2 (answer): Net amount = ${amount:.2f} − ${fee:.2f} = ${net:.2f}"
    )

    return question, solution


def template_pt_easy2():
    """
    2:Basic: Buy-Now-Pay-Later Equal Installments (single answer)
    Variables:
      • Purchase price (P)
      • Number of installments (n)
      • Service fee rate (f)
    Steps (2):
      1) Total due = P × (1 + f)
      2) Installment payment = Total due ÷ n  (answer)
    """
    user      = random.choice(user_names)
    merchant  = random.choice(merchant_names)
    platform  = random.choice(payment_platforms)
    purchase  = round(random.uniform(100, 2000), 2)
    n_inst    = random.choice([4, 6, 12])
    fee_rate  = round(random.uniform(0.00, 0.08), 3)   # 0 %–8 %

    total_due = purchase * (1 + fee_rate)
    installment = total_due / n_inst

    question = (
        f"{user} uses {platform}'s Buy-Now-Pay-Later option at {merchant} to purchase "
        f"items totaling ${purchase:.2f}. The service fee is {fee_rate*100:.2f}% of the purchase price, "
        f"spread evenly over {n_inst} installments. What is each installment amount?"
    )

    solution = (
        f"Step 1: Total amount owed = ${purchase:.2f} × (1 + {fee_rate:.3f}) = ${total_due:.2f}\n\n"
        f"Step 2 (answer): Installment = ${total_due:.2f} ÷ {n_inst} = ${installment:.2f}"
    )

    return question, solution

###############################################################################
# INTERMEDIATE TEMPLATES (3 steps, single numeric answer)
###############################################################################

def template_pt_medium1():
    """
    3:Intermediate: Effective Fee Rate on Batch (single answer)
    Scenario:
      • Platform charges $0.30 + 2.5 % per transaction
      • Several transaction amounts provided
    Steps (3):
      1) Compute fee for each transaction
      2) Sum all fees and total sales
      3) Effective fee rate = Total fees ÷ Total sales  (answer)
    """
    merchant = random.choice(merchant_names)
    platform = random.choice(payment_platforms)
    per_tx_fee = 0.30
    pct_fee    = 0.025
    num_tx = random.randint(4, 7)
    tx_amounts = [round(random.uniform(5, 120), 2) for _ in range(num_tx)]

    fees = [per_tx_fee + amt * pct_fee for amt in tx_amounts]
    total_fees  = sum(fees)
    total_sales = sum(tx_amounts)
    eff_rate = total_fees / total_sales

    tx_lines = "\n".join([f"  • ${amt:.2f}" for amt in tx_amounts])
    question = (
        f"{merchant} processes these amounts via {platform} ($0.30 + 2.5% each):\n"
        f"{tx_lines}\n\n"
        f"What is the **effective fee rate** (percentage of total sales taken as fees) for this batch?"
    )

    fee_lines = "\n".join(
        [f"  • Fee on ${amt:.2f} = $0.30 + 2.5% × ${amt:.2f} = ${fee:.2f}"
         for amt, fee in zip(tx_amounts, fees)]
    )
    solution = (
        f"Step 1:\n{fee_lines}\n\n"
        f"Step 2: Totals ⇒ Fees ${total_fees:.2f}, Sales ${total_sales:.2f}\n\n"
        f"Step 3 (answer): Effective rate = ${total_fees:.2f} ÷ ${total_sales:.2f} "
        f"= {eff_rate*100:.2f}%"
    )

    return question, solution


def template_pt_medium2():
    """
    4:Intermediate: Cross-Border Payment Conversion and Fees (single answer)
    Variables:
      • Sale amount in EUR (E)
      • Mid-market EUR/USD rate (R)
      • Platform spread (s)
      • Fixed processing fee (f)
    Steps (3):
      1) Platform conversion rate = R × (1 − s)
      2) Convert amount to USD
      3) Net USD received after fee  (answer)
    """
    merchant = random.choice(merchant_names)
    platform = random.choice(payment_platforms)
    amount_eur = round(random.uniform(50, 1000), 2)
    mid_rate   = round(random.uniform(1.10, 1.20), 4)
    spread     = round(random.uniform(0.015, 0.03), 4)   # 1.5 %–3 %
    fixed_fee  = round(random.uniform(0, 5), 2)

    conv_rate = mid_rate * (1 - spread)
    usd_before_fee = amount_eur * conv_rate
    net_usd = usd_before_fee - fixed_fee

    question = (
        f"{merchant} receives a €{amount_eur:.2f} payment through {platform}. "
        f"The mid-market EUR/USD rate is {mid_rate}. {platform} applies a "
        f"{spread*100:.2f}% spread and charges a ${fixed_fee:.2f} fixed fee. "
        f"How many USD will {merchant} receive **after** conversion and fees?"
    )

    solution = (
        f"Step 1: Conversion rate = {mid_rate} × (1 − {spread:.4f}) = {conv_rate:.4f}\n\n"
        f"Step 2: USD before fee = €{amount_eur:.2f} × {conv_rate:.4f} = ${usd_before_fee:.2f}\n\n"
        f"Step 3 (answer): Net USD = ${usd_before_fee:.2f} − ${fixed_fee:.2f} = ${net_usd:.2f}"
    )

    return question, solution

###############################################################################
# ADVANCED TEMPLATE (4 steps, single numeric answer)
###############################################################################

def template_pt_hard1():
    """
    5:Advanced: Effective Monthly Fee Rate (single answer)
    Scenario:
      • $50 subscription
      • 1.7 % on first $10 000 sales, 1.4 % thereafter
      • $0.08 per transaction
      • N transactions averaging A dollars
    Steps (4):
      1) Compute total sales and tier split
      2) Calculate variable percentage fees
      3) Add flat per-transaction fees and subscription
      4) Effective fee rate = Total fees ÷ Total sales  (answer)
    """
    merchant = random.choice(merchant_names)
    platform = random.choice(payment_platforms)
    n_tx   = random.randint(300, 800)
    avg_tx = round(random.uniform(20, 100), 2)
    sub_fee = 50.00
    flat_fee = 0.08
    tier_cap = 10_000
    tier1_rate = 0.017
    tier2_rate = 0.014

    total_sales = n_tx * avg_tx
    tier1_sales = min(total_sales, tier_cap)
    tier2_sales = max(0, total_sales - tier_cap)

    var_fee = tier1_sales * tier1_rate + tier2_sales * tier2_rate
    flat_total = n_tx * flat_fee
    total_fees = sub_fee + var_fee + flat_total
    eff_rate = total_fees / total_sales

    question = (
        f"{merchant} uses {platform}'s pricing:\n"
        f"  • $50 monthly subscription\n"
        f"  • 1.7% on first $10 000 sales, 1.4% thereafter\n"
        f"  • $0.08 per transaction\n\n"
        f"In a month with {n_tx} sales averaging ${avg_tx:.2f}, "
        f"what is the **effective fee rate** on total sales?"
    )

    solution = (
        f"Step 1: Total sales = {n_tx} × ${avg_tx:.2f} = ${total_sales:,.2f}\n"
        f"        Tiered split ⇒ ${tier1_sales:,.2f} at 1.7%, ${tier2_sales:,.2f} at 1.4%\n\n"
        f"Step 2: Variable fees = 1.7% × ${tier1_sales:,.2f} + 1.4% × ${tier2_sales:,.2f}\n"
        f"        = ${tier1_sales * tier1_rate:,.2f} + ${tier2_sales * tier2_rate:,.2f}"
        f" = ${var_fee:,.2f}\n\n"
        f"Step 3: Flat fees = {n_tx} × $0.08 = ${flat_total:,.2f}; "
        f"Add subscription ${sub_fee:.2f} ⇒ Total fees ${total_fees:,.2f}\n\n"
        f"Step 4 (answer): Effective rate = ${total_fees:,.2f} ÷ ${total_sales:,.2f} "
        f"= {eff_rate*100:.2f}%"
    )

    return question, solution

###############################################################################
# MAIN
###############################################################################

def main():
    """
    Generate 10 instances of each Payment-Technologies template and save to JSONL.
    """
    templates = [
        template_pt_easy1,
        template_pt_easy2,
        template_pt_medium1,
        template_pt_medium2,
        template_pt_hard1
    ]

    problems = []
    for template_func in templates:
        id_ = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        for _ in range(10):
            seed = random.randint(1_000_000_000, 4_000_000_000)
            random.seed(seed)
            q, a = template_func()
            problems.append({
                "seed": seed,
                "id": id_,
                "level": level,
                "question": q,
                "solution": a
            })
            random.seed()  # reset RNG state

    random.shuffle(problems)
    outfile = "../../testset/fintech/payment_technologies.jsonl"
    with open(outfile, "w") as f:
        for p in problems:
            f.write(json.dumps(p))
            f.write("\n")

    print(f"Successfully generated {len(problems)} problems → {outfile}")


if __name__ == "__main__":
    main()
