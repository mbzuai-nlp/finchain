import random
import json

###############################################################################
# Data Pools
###############################################################################
investor_names = ["Alice Wu", "Brad Johnson", "Carla Simmons", "Daniel Craig", "Eva Gonzalez"]
currency_pairs = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "USD/CHF", "NZD/USD", "EUR/GBP", "EUR/JPY", "GBP/JPY"
]

###############################################################################
# BASIC TEMPLATES (2 steps, single numeric answer)
###############################################################################

def template_fx_easy1():
    """
    1:Basic: Simple Currency Conversion  (2 steps)
      1) Decide whether to multiply or divide by the quoted rate
      2) Perform the calculation to obtain the converted amount   (answer)
    """
    investor = random.choice(investor_names)
    pair     = random.choice(["EUR/USD", "GBP/USD", "USD/JPY"])
    amount   = round(random.uniform(500, 5_000), 2)

    if pair == "EUR/USD":
        rate = round(random.uniform(1.05, 1.20), 4)
        question = (
            f"{investor} wants to convert €{amount:.2f} to US dollars. "
            f"The EUR/USD rate is {rate}. How many USD will {investor} receive?"
        )
        converted = amount * rate
        solution = (
            f"Step 1: EUR/USD is quoted as USD per EUR, so multiply euros by the rate.\n\n"
            f"Step 2 (answer): USD = €{amount:.2f} × {rate} = ${converted:.2f}"
        )

    elif pair == "GBP/USD":
        rate = round(random.uniform(1.15, 1.40), 4)
        question = (
            f"{investor} wants to convert £{amount:.2f} to US dollars. "
            f"The GBP/USD rate is {rate}. How many USD will {investor} receive?"
        )
        converted = amount * rate
        solution = (
            f"Step 1: GBP/USD is USD per GBP, so multiply pounds by the rate.\n\n"
            f"Step 2 (answer): USD = £{amount:.2f} × {rate} = ${converted:.2f}"
        )

    else:  # USD/JPY
        rate = round(random.uniform(100, 150), 2)
        question = (
            f"{investor} wants to convert ${amount:.2f} to Japanese yen. "
            f"The USD/JPY rate is {rate}. How many JPY will {investor} receive?"
        )
        converted = amount * rate
        solution = (
            f"Step 1: USD/JPY is JPY per USD, so multiply dollars by the rate.\n\n"
            f"Step 2 (answer): JPY = ${amount:.2f} × {rate} = ¥{converted:.2f}"
        )

    return question, solution


def template_fx_easy2():
    """
    2:Basic: Pip Value Calculation  (2 steps)
    Steps (2):
      1) Identify pip size
      2) Pip value = pip size × position   (answer)
    """
    investor = random.choice(investor_names)
    pair = random.choice(["EUR/USD", "GBP/USD", "USD/JPY"])
    lot = random.choice([10_000, 50_000, 100_000])

    if pair in ["EUR/USD", "GBP/USD"]:
        pip = 0.0001
        value = pip * lot
        question = (
            f"{investor} trades {lot} units of {pair}. One pip is 0.0001. "
            f"How much is one-pip movement worth in USD?"
        )
        solution = (
            f"Step 1: Pip size = 0.0001\n"
            f"Step 2 (answer): Value = 0.0001 × {lot} = ${value:.2f} per pip"
        )
    else:  # USD/JPY
        pip = 0.01
        value = pip * lot
        question = (
            f"{investor} trades {lot} units of {pair}. One pip is 0.01. "
            f"How much is one-pip movement worth in JPY?"
        )
        solution = (
            f"Step 1: Pip size = 0.01\n"
            f"Step 2 (answer): Value = 0.01 × {lot} = ¥{value:.2f} per pip"
        )
    return question, solution

###############################################################################
# INTERMEDIATE TEMPLATES (3 steps, single numeric answer)
###############################################################################

def template_fx_medium1():
    """
    3:Intermediate: Profit/Loss on a Forex Trade  (3 steps)
    Steps (3):
      1) Pip difference
      2) Pip value
      3) P/L = pip diff × pip value   (answer)
    """
    investor = random.choice(investor_names)
    pair = random.choice(["EUR/USD", "GBP/USD", "USD/JPY"])
    lot = random.choice([10_000, 100_000])

    if pair in ["EUR/USD", "GBP/USD"]:
        open_ = round(random.uniform(1.05, 1.20), 4)
        close = round(open_ + random.uniform(-0.01, 0.02), 4)
        pip = 0.0001
        pip_diff = (close - open_) / pip
        pip_val = pip * lot
        pl = pip_diff * pip_val
        question = (
            f"{investor} buys {pair} ({lot} units) at {open_} and closes at {close}. "
            f"1 pip = 0.0001. What is the P/L in USD?"
        )
        solution = (
            f"Step 1: Pip diff = ({close} − {open_}) / 0.0001 = {pip_diff:.1f} pips\n\n"
            f"Step 2: Pip value = 0.0001 × {lot} = ${pip_val:.2f}\n\n"
            f"Step 3 (answer): P/L = {pip_diff:.1f} × ${pip_val:.2f} = ${pl:.2f}"
        )
    else:  # USD/JPY
        open_ = round(random.uniform(105, 120), 2)
        close = round(open_ + random.uniform(-1, 2), 2)
        pip = 0.01
        pip_diff = (close - open_) / pip
        pip_val = pip * lot
        pl = pip_diff * pip_val
        question = (
            f"{investor} buys {pair} ({lot} units) at {open_} and closes at {close}. "
            f"1 pip = 0.01. What is the P/L in JPY?"
        )
        solution = (
            f"Step 1: Pip diff = ({close} − {open_}) / 0.01 = {pip_diff:.1f} pips\n\n"
            f"Step 2: Pip value = 0.01 × {lot} = ¥{pip_val:.2f}\n\n"
            f"Step 3 (answer): P/L = {pip_diff:.1f} × ¥{pip_val:.2f} = ¥{pl:.2f}"
        )
    return question, solution


def template_fx_medium2():
    """
    4:Intermediate: Cross-Currency Conversion  (3 steps)
    Steps (3):
      1) Note EUR/USD and GBP/USD rates
      2) Cross rate EUR/GBP = (EUR/USD) ÷ (GBP/USD)
      3) GBP received = EUR amount × cross rate   (answer)
    """
    investor = random.choice(investor_names)
    eur_usd = round(random.uniform(1.05, 1.20), 4)
    gbp_usd = round(random.uniform(1.15, 1.35), 4)
    amt_eur = round(random.uniform(500, 2_000), 2)

    cross = eur_usd / gbp_usd
    gbp = amt_eur * cross

    question = (
        f"{investor} has €{amt_eur:.2f} and knows:\n"
        f"  EUR/USD = {eur_usd}\n"
        f"  GBP/USD = {gbp_usd}\n"
        f"Calculate how many pounds (£) they receive when converting directly using the implied "
        f"EUR/GBP cross rate."
    )

    solution = (
        f"Step 1: Given EUR/USD = {eur_usd}, GBP/USD = {gbp_usd}\n\n"
        f"Step 2: Cross rate EUR/GBP = {eur_usd} ÷ {gbp_usd} = {cross:.4f}\n\n"
        f"Step 3 (answer): GBP = €{amt_eur:.2f} × {cross:.4f} = £{gbp:.2f}"
    )
    return question, solution

###############################################################################
# ADVANCED TEMPLATE (4 steps, single numeric answer)
###############################################################################

def template_fx_hard1():
    """
    5:Advanced: Triangular Arbitrage  (4 steps)
    Steps (4):
      1) USD → EUR
      2) EUR → GBP
      3) GBP → USD
      4) Net profit/loss in USD   (answer)
    """
    investor = random.choice(investor_names)
    usd_eur = round(random.uniform(0.80, 0.95), 4)
    eur_gbp = round(random.uniform(0.80, 0.90), 4)
    gbp_usd = round(random.uniform(1.25, 1.40), 4)
    start_usd = round(random.uniform(1_000, 3_000), 2)

    eur = start_usd * usd_eur
    gbp = eur * eur_gbp
    final_usd = gbp * gbp_usd
    pnl = final_usd - start_usd

    question = (
        f"{investor} spots these rates:\n"
        f"  USD/EUR = {usd_eur}\n"
        f"  EUR/GBP = {eur_gbp}\n"
        f"  GBP/USD = {gbp_usd}\n"
        f"If they start with ${start_usd:.2f} and trade USD→EUR→GBP→USD, "
        f"what is the profit or loss in USD?"
    )

    solution = (
        f"Step 1: USD→EUR  → €{eur:.2f}\n"
        f"Step 2: EUR→GBP  → £{gbp:.2f}\n"
        f"Step 3: GBP→USD  → ${final_usd:.2f}\n\n"
        f"Step 4 (answer): P/L = ${final_usd:.2f} − ${start_usd:.2f} = ${pnl:.2f}"
    )
    return question, solution

###############################################################################
# MAIN
###############################################################################

def main():
    templates = [
        template_fx_easy1,
        template_fx_easy2,
        template_fx_medium1,
        template_fx_medium2,
        template_fx_hard1
    ]

    problems = []
    for tmpl in templates:
        id_   = tmpl.__doc__.split(":")[0].strip()
        level = tmpl.__doc__.split(":")[1].strip()

        for _ in range(10):
            seed = random.randint(1_000_000_000, 4_000_000_000)
            random.seed(seed)
            q, a = tmpl()
            problems.append(
                {"seed": seed,
                 "id": id_,
                 "level": level,
                 "question": q,
                 "solution": a}
            )
            random.seed()  # restore RNG

    random.shuffle(problems)
    out = "../../testset/financial_markets/forex_trading.jsonl"
    with open(out, "w") as f:
        for p in problems:
            f.write(json.dumps(p)); f.write("\n")

    print(f"Generated {len(problems)} problems → {out}")


if __name__ == "__main__":
    main()
