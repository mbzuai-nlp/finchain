import random
import math
import json

###############################################################################
# Data Pools
###############################################################################
investor_names = ["Alice Wu", "Brad Johnson", "Carla Simmons", "Daniel Craig", "Eva Gonzalez"]
underlying_assets = [
    "Apple Inc.", "Tesla Inc.", "Amazon.com Inc.", "Microsoft Corp.", "Netflix Inc.",
    "Google LLC", "Meta Platforms", "Nvidia Corp.", "Disney Co.", "Coca-Cola Co."
]

###############################################################################
# BASIC TEMPLATES (2 steps, single numeric answer)
###############################################################################

def template_op_easy1():
    """
    1:Basic: Intrinsic Value of a Call  (2 steps)
      1) Compare S and K
      2) Intrinsic = max(S-K,0)   (answer)
    """
    investor = random.choice(investor_names)
    asset = random.choice(underlying_assets)
    S = round(random.uniform(80, 150), 2)
    K = round(random.uniform(70, 160), 2)

    intrinsic = max(S - K, 0)
    itm = "in the money" if S > K else "out of the money"

    question = (
        f"{investor} holds a call on {asset}: strike ${K:.2f}, spot ${S:.2f}. "
        f"What is its intrinsic value?"
    )

    solution = (
        f"Step 1: S = ${S:.2f} vs K = ${K:.2f} → option is {itm}.\n\n"
        f"Step 2 (answer): Intrinsic = max(S−K,0) = max(${S:.2f}−${K:.2f},0) = ${intrinsic:.2f}"
    )
    return question, solution


def template_op_easy2():
    """
    2:Basic: Intrinsic Value of a Put  (2 steps)
      1) Compare S and K
      2) Intrinsic = max(K-S,0)   (answer)
    """
    investor = random.choice(investor_names)
    asset = random.choice(underlying_assets)
    S = round(random.uniform(80, 150), 2)
    K = round(random.uniform(70, 160), 2)

    intrinsic = max(K - S, 0)
    itm = "in the money" if S < K else "out of the money"

    question = (
        f"{investor} holds a put on {asset}: strike ${K:.2f}, spot ${S:.2f}. "
        f"What is its intrinsic value?"
    )

    solution = (
        f"Step 1: S = ${S:.2f} vs K = ${K:.2f} → option is {itm}.\n\n"
        f"Step 2 (answer): Intrinsic = max(K−S,0) = max(${K:.2f}−${S:.2f},0) = ${intrinsic:.2f}"
    )
    return question, solution

###############################################################################
# INTERMEDIATE TEMPLATES (3 steps, single numeric answer)
###############################################################################

def template_op_medium1():
    """
    3:Intermediate: 1-Period Binomial Call Price  (3 steps)
      1) Payoffs in up/down states
      2) Risk-neutral probability
      3) Present-value of expected payoff   (answer)
    """
    investor = random.choice(investor_names)
    asset = random.choice(underlying_assets)
    S0 = round(random.uniform(90, 120), 2)
    K  = round(random.uniform(80, 130), 2)
    u  = round(random.uniform(1.1, 1.3), 2)
    d  = round(random.uniform(0.7, 0.9), 2)
    r  = round(random.uniform(0.02, 0.08), 3)

    Su, Sd = round(S0*u,2), round(S0*d,2)
    Cu, Cd = max(Su-K,0), max(Sd-K,0)
    p = ((1+r) - d) / (u - d)
    PV = (p*Cu + (1-p)*Cd) / (1+r)

    question = (
        f"{investor} prices a call on {asset} via a 1-period binomial model: "
        f"S0=${S0:.2f}, K=${K:.2f}, u={u}, d={d}, r={r*100:.2f} %. "
        f"What is the option’s fair value?"
    )

    solution = (
        f"Step 1: Payoffs ⇒ Cu=max({Su}−{K},0)=${Cu:.2f}, Cd=max({Sd}−{K},0)=${Cd:.2f}\n\n"
        f"Step 2: Risk-neutral p = [(1+r)−d]/(u−d) = {p:.3f}\n\n"
        f"Step 3 (answer): Price = [p·Cu+(1−p)·Cd]/(1+r) = ${PV:.2f}"
    )
    return question, solution


def template_op_medium2():
    """
    4:Intermediate: ROI on a Long Call Position  (3 steps)
      1) Intrinsic payoff at expiration
      2) Net profit or loss = payoff − premium
      3) Return on investment (%) = (net P/L ÷ premium) × 100   (answer)
    """
    investor = random.choice(investor_names)
    asset    = random.choice(underlying_assets)

    K      = round(random.uniform(90, 110), 2)    # strike
    premium = round(random.uniform(2, 10), 2)     # upfront cost
    S_T    = round(random.uniform(80, 130), 2)    # price at expiry

    payoff   = max(S_T - K, 0)
    net_pl   = payoff - premium
    roi_pct  = (net_pl / premium) * 100  # can be negative

    question = (
        f"{investor} pays a ${premium:.2f} premium for a call on {asset} (strike ${K:.2f}). "
        f"At expiration the stock is ${S_T:.2f}. What is the return on investment (ROI) "
        f"expressed as a percentage of the premium paid?"
    )

    solution = (
        f"Step 1: Payoff = max(S_T − K, 0) = max({S_T} − {K}, 0) = ${payoff:.2f}\n\n"
        f"Step 2: Net P/L = Payoff − Premium = ${payoff:.2f} − ${premium:.2f} = ${net_pl:.2f}\n\n"
        f"Step 3 (answer): ROI = ({net_pl:.2f} ÷ {premium:.2f}) × 100 = {roi_pct:.2f}%"
    )

    return question, solution


###############################################################################
# ADVANCED TEMPLATE (4 steps, single numeric answer)
###############################################################################

def template_op_hard1():
    """
    5:Advanced: Black-Scholes Call Price  (4 steps)
      1) Compute d1
      2) Compute d2
      3) Φ(d1), Φ(d2)
      4) Call price = S0Φ(d1) − Ke^{−rT}Φ(d2)   (answer)
    """
    def Φ(x):   # standard normal CDF
        return 0.5*(1+math.erf(x/math.sqrt(2)))

    investor = random.choice(investor_names)
    asset = random.choice(underlying_assets)
    S0   = round(random.uniform(90,150),2)
    K    = round(random.uniform(80,140),2)
    r    = round(random.uniform(0.01,0.05),3)
    σ    = round(random.uniform(0.1,0.4),3)
    T    = round(random.uniform(0.5,2),2)

    d1 = (math.log(S0/K)+(r+0.5*σ**2)*T)/(σ*math.sqrt(T))
    d2 = d1-σ*math.sqrt(T)
    Nd1, Nd2 = Φ(d1), Φ(d2)
    C = S0*Nd1 - K*math.exp(-r*T)*Nd2

    question = (
        f"{investor} wants a Black-Scholes price for a call on {asset}: "
        f"S0=${S0}, K=${K}, r={r:.3f}, σ={σ:.3f}, T={T} yr. "
        f"Estimate the call value."
    )

    solution = (
        f"Step 1: d1 = [ln(S0/K)+(r+σ²/2)T]/(σ√T) ≈ {d1:.4f}\n"
        f"Step 2: d2 = d1 − σ√T ≈ {d2:.4f}\n"
        f"Step 3: Φ(d1) ≈ {Nd1:.4f}, Φ(d2) ≈ {Nd2:.4f}\n"
        f"Step 4 (answer): C = {S0}·Φ(d1) − {K}·e^(−rT)·Φ(d2) ≈ ${C:.2f}"
    )
    return question, solution

###############################################################################
# MAIN
###############################################################################

def main():
    templates = [
        template_op_easy1,
        template_op_easy2,
        template_op_medium1,
        template_op_medium2,
        template_op_hard1
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
            random.seed()  # reset RNG to system state

    random.shuffle(problems)
    out = "../../testset/financial_markets/option_pricing.jsonl"
    with open(out, "w") as f:
        for p in problems:
            f.write(json.dumps(p)); f.write("\n")

    print(f"Generated {len(problems)} problems → {out}")


if __name__ == "__main__":
    main()
