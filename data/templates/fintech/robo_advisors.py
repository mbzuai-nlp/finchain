import random
import json
import math   # used in some calculations

###############################################################################
# Data Pools
###############################################################################
investor_names = ["Alice Wu", "Brad Johnson", "Carla Simmons", "Daniel Craig", "Eva Gonzalez"]
robo_advisors  = ["BetterWealth", "SmartInvest", "RoboMax", "WealthBot", "AlgoAdvisor"]

###############################################################################
# BASIC TEMPLATES (2 steps, single numeric answer)
###############################################################################

def template_ra_easy1():
    """
    1:Basic: Net Portfolio Value After Advisory Fee (single answer)
    Variables:
      • Portfolio value (V)
      • Annual advisory fee rate (f)
    Steps (2):
      1) Fee = V × f
      2) Net portfolio value after fee = V − Fee  (answer)
    """
    investor = random.choice(investor_names)
    advisor  = random.choice(robo_advisors)
    value    = random.randint(5_000, 50_000)
    fee_rate = round(random.uniform(0.0025, 0.01), 4)   # 0.25 %–1 %

    fee       = value * fee_rate
    net_value = value - fee

    question = (
        f"{investor} has ${value:,} managed by {advisor}, which charges an annual advisory fee "
        f"of {fee_rate*100:.2f}%. What will the portfolio be worth **after** the fee is deducted?"
    )

    solution = (
        f"Step 1: Fee = ${value:,} × {fee_rate:.4f} = ${fee:,.2f}\n\n"
        f"Step 2 (answer): Net value = ${value:,} − ${fee:,.2f} = ${net_value:,.2f}"
    )

    return question, solution


def template_ra_easy2():
    """
    2:Basic: One-Year Ending Value After Fee (single answer)
    Variables:
      • Portfolio value (V)
      • Gross return (g)
      • Advisory fee rate (f)
    Steps (2):
      1) Ending value before fee = V × (1 + g)
      2) Ending value after fee = Ending value × (1 − f)  (answer)
    """
    investor = random.choice(investor_names)
    advisor  = random.choice(robo_advisors)
    value        = random.randint(10_000, 100_000)
    gross_return = round(random.uniform(-0.05, 0.12), 3)  # −5 % to 12 %
    fee_rate     = round(random.uniform(0.003, 0.01), 4)

    end_before_fee = value * (1 + gross_return)
    end_after_fee  = end_before_fee * (1 - fee_rate)

    question = (
        f"{investor}'s portfolio at {advisor} is worth ${value:,}. Over the next year it earns a "
        f"gross return of {gross_return*100:.2f}%. {advisor} charges {fee_rate*100:.2f}% of assets as its fee. "
        f"What will the portfolio be worth **after fees**?"
    )

    solution = (
        f"Step 1: Ending value before fee = ${value:,} × (1 + {gross_return:.3f}) "
        f"= ${end_before_fee:,.2f}\n\n"
        f"Step 2 (answer): Ending value after fee = ${end_before_fee:,.2f} × (1 − {fee_rate:.4f}) "
        f"= ${end_after_fee:,.2f}"
    )

    return question, solution

###############################################################################
# INTERMEDIATE TEMPLATES (3 steps, single numeric answer)
###############################################################################

def template_ra_medium1():
    """
    3:Intermediate: Equity Trade Needed for Rebalance (single answer)
    Scenario:
      • Two-asset portfolio (Equities / Bonds)
      • Current values given
      • Target allocation given
    Steps (3):
      1) Compute total portfolio value
      2) Calculate target equity dollar amount
      3) Buy/sell amount of equities needed to hit target  (answer)
    """
    investor = random.choice(investor_names)
    advisor  = random.choice(robo_advisors)
    equities_val = random.randint(20_000, 60_000)
    bonds_val    = random.randint(10_000, 40_000)
    target_equity_pct = random.choice([0.6, 0.7, 0.8])   # 60 %, 70 %, 80 %

    total_val        = equities_val + bonds_val
    target_equity_val = total_val * target_equity_pct
    equity_trade      = target_equity_val - equities_val  # +ve buy, −ve sell

    question = (
        f"{investor}'s portfolio with {advisor} currently holds ${equities_val:,} in equities and "
        f"${bonds_val:,} in bonds. The target allocation is {target_equity_pct*100:.0f}% equities. "
        f"How many dollars of equities should be "
        f"{'bought' if equity_trade>0 else 'sold'} to reach the target exactly?"
    )

    solution = (
        f"Step 1: Total value = ${equities_val:,} + ${bonds_val:,} = ${total_val:,}\n\n"
        f"Step 2: Target equity value = {target_equity_pct*100:.0f}% × ${total_val:,} "
        f"= ${target_equity_val:,.2f}\n\n"
        f"Step 3 (answer): Equity trade = ${target_equity_val:,.2f} − ${equities_val:,} "
        f"= {'+' if equity_trade>=0 else '−'}${abs(equity_trade):,.2f}"
    )

    return question, solution


def template_ra_medium2():
    """
    4:Intermediate: Projected Value with Monthly Contributions (single answer)
    Variables:
      • Monthly contribution (C)
      • Annual expected return (r)
      • Years (t)
      • Advisory fee (f)
    Steps (3):
      1) FV of ordinary annuity with monthly compounding
      2) Fee at end = FV × f
      3) Net projected value = FV − fee  (answer)
    """
    investor = random.choice(investor_names)
    advisor  = random.choice(robo_advisors)
    monthly_contrib = random.randint(200, 600)
    years           = random.choice([5, 10, 15])
    annual_return   = round(random.uniform(0.04, 0.08), 3)
    fee_rate        = round(random.uniform(0.0025, 0.0075), 4)  # 0.25 %–0.75 %

    months        = years * 12
    monthly_rate  = annual_return / 12
    fv_before_fee = monthly_contrib * (((1 + monthly_rate) ** months - 1) / monthly_rate)
    net_value     = fv_before_fee * (1 - fee_rate)

    question = (
        f"{investor} will contribute ${monthly_contrib} each month to {advisor} for {years} years. "
        f"Expected return is {annual_return*100:.2f}% (compounded monthly) and the advisory fee is "
        f"{fee_rate*100:.2f}% per year. What is the projected portfolio value "
        f"**after fees** at the end of {years} years?"
    )

    solution = (
        f"Step 1: FV before fees = ${monthly_contrib} × [((1 + {monthly_rate:.5f})^{months} − 1) / "
        f"{monthly_rate:.5f}] = ${fv_before_fee:,.2f}\n\n"
        f"Step 2: Fee = {fee_rate*100:.2f}% × ${fv_before_fee:,.2f} = ${fv_before_fee*fee_rate:,.2f}\n\n"
        f"Step 3 (answer): Net projected value = ${fv_before_fee:,.2f} − fee = ${net_value:,.2f}"
    )

    return question, solution

###############################################################################
# ADVANCED TEMPLATE (4 steps, single numeric answer)
###############################################################################

def template_ra_hard1():
    """
    5:Advanced: Tax Savings from Tax-Loss Harvesting  (3 steps, single answer)
    Scenario:
      • Investor sells ETF at a loss and buys a similar one
      • Loss offsets ordinary income at marginal tax rate (m)
    Steps (3):
      1) Realised capital loss
      2) Apply marginal rate to find tax savings
      3) State the tax savings amount   (answer)
    """
    investor = random.choice(investor_names)
    advisor  = random.choice(robo_advisors)
    shares        = random.randint(50, 200)
    cost_basis    = round(random.uniform(50, 120), 2)
    current_price = round(cost_basis * random.uniform(0.60, 0.95), 2)
    marginal_rate = random.choice([0.22, 0.24, 0.32])   # 22 %, 24 %, 32 %

    realised_loss = (current_price - cost_basis) * shares      # negative number
    tax_savings   = -realised_loss * marginal_rate             # positive

    question = (
        f"{investor} owns {shares} shares of an ETF bought at ${cost_basis:.2f} each, now trading at "
        f"${current_price:.2f}.  If the shares are sold to harvest the loss and {investor}'s marginal tax "
        f"rate is {marginal_rate*100:.0f} %, how much tax can be saved this year?"
    )

    solution = (
        f"Step 1: Realised loss = ({current_price:.2f} − {cost_basis:.2f}) × {shares} "
        f"= ${realised_loss:,.2f}\n\n"
        f"Step 2: Tax savings = (−Loss) × marginal rate = "
        f"${-realised_loss:,.2f} × {marginal_rate:.2f} = ${tax_savings:,.2f}\n\n"
        f"Step 3 (answer): ${tax_savings:,.2f}"
    )

    return question, solution


###############################################################################
# MAIN
###############################################################################

def main():
    """
    Generate 10 instances of each Robo-Advisor template and save to JSONL.
    """
    templates = [
        template_ra_easy1,
        template_ra_easy2,
        template_ra_medium1,
        template_ra_medium2,
        template_ra_hard1
    ]

    problems = []
    for template_func in templates:
        id_   = template_func.__doc__.split(':')[0].strip()
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
            random.seed()  # restore system RNG state

    random.shuffle(problems)
    outfile = "../../testset/fintech/robo_advisors.jsonl"
    with open(outfile, "w") as f:
        for p in problems:
            f.write(json.dumps(p))
            f.write("\n")

    print(f"Successfully generated {len(problems)} problems → {outfile}")


if __name__ == "__main__":
    main()
