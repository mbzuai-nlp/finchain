import random
import json
import math   # reserved for future numeric helpers if needed

###############################################################################
# Data Pools
###############################################################################
investor_names = ["Alice Wu", "Brad Johnson", "Carla Simmons", "Daniel Craig", "Eva Gonzalez"]
bond_issuers   = ["U.S. Treasury", "XYZ Corporation", "ABC Bank", "City of Metropolis", "Acme Corp"]

###############################################################################
# BASIC TEMPLATES (2 steps, single numeric answer)
###############################################################################

def template_bp_easy1():
    """
    1:Basic: Zero-Coupon Bond Price  (2 steps)
    Steps (2):
      1) Compute discount factor = 1 / (1 + r)^t
      2) Bond price = Face × discount factor   (answer)
    """
    issuer   = random.choice(bond_issuers)
    investor = random.choice(investor_names)
    F  = random.randint(1_000, 2_000)
    t  = random.randint(1, 5)
    r  = round(random.uniform(0.02, 0.10), 3)

    discount_factor = 1 / ((1 + r) ** t)
    price = F * discount_factor

    question = (
        f"{investor} considers a zero-coupon bond from {issuer} with face value ${F} maturing in {t} years. "
        f"If the required annual yield is {r*100:.2f} %, what is the bond’s price today?"
    )

    solution = (
        f"Step 1: Discount factor = 1 / (1 + {r:.3f})^{t} = {discount_factor:.5f}\n\n"
        f"Step 2 (answer): Price = ${F} × {discount_factor:.5f} = ${price:,.2f}"
    )
    return question, solution


def template_bp_easy2():
    """
    2:Basic: One-Year Coupon Bond Price  (2 steps)
    Steps (2):
      1) Discount (coupon + principal) one year
      2) Bond price   (answer)
    """
    issuer   = random.choice(bond_issuers)
    investor = random.choice(investor_names)
    F  = random.randint(1_000, 2_000)
    c  = round(random.uniform(0.02, 0.08), 3)     # coupon rate
    r  = round(random.uniform(0.02, 0.10), 3)

    C  = round(F * c, 2)
    CF = C + F
    price = CF / (1 + r)

    question = (
        f"{investor} is evaluating a 1-year bond from {issuer} (face ${F}, coupon {c*100:.2f} %). "
        f"Market yield is {r*100:.2f} %. What is its fair price?"
    )

    solution = (
        f"Step 1: Cash flow in 1 yr = ${C:,.2f} + ${F} = ${CF:,.2f}; "
        f"discount at 1 + r = 1 + {r:.3f}\n\n"
        f"Step 2 (answer): Price = ${CF:,.2f} / (1 + {r:.3f}) = ${price:,.2f}"
    )
    return question, solution

###############################################################################
# INTERMEDIATE TEMPLATES (3 steps, single numeric answer)
###############################################################################

def template_bp_medium1():
    """
    3:Intermediate: Multi-Year Coupon Bond Price  (3 steps)
    Steps (3):
      1) PV of coupons
      2) PV of face value
      3) Bond price = PVs sum   (answer)
    """
    issuer   = random.choice(bond_issuers)
    investor = random.choice(investor_names)
    F  = random.choice([1_000, 2_000])
    c  = round(random.uniform(0.03, 0.09), 3)
    n  = random.randint(2, 5)
    r  = round(random.uniform(0.02, 0.10), 3)

    C = round(F * c, 2)
    pv_cpn = sum(C / ((1 + r) ** t) for t in range(1, n + 1))
    pv_F   = F / ((1 + r) ** n)
    price  = pv_cpn + pv_F

    question = (
        f"{investor} needs the fair price of a bond from {issuer}: face ${F}, coupon {c*100:.2f} %, "
        f"{n} years to maturity, required yield {r*100:.2f} %. What is the bond’s price?"
    )

    solution = (
        f"Step 1: PV(coupons) = Σ C / (1 + r)^t = ${pv_cpn:,.2f}\n\n"
        f"Step 2: PV(face)    = ${F} / (1 + {r:.3f})^{n} = ${pv_F:,.2f}\n\n"
        f"Step 3 (answer): Price = ${pv_cpn:,.2f} + ${pv_F:,.2f} = ${price:,.2f}"
    )
    return question, solution


def template_bp_medium2():
    """
    4:Intermediate: Yield to Maturity of a 2-Year Bond  (3 steps)
    Steps (3):
      1) Formulate price equation → quadratic in (1+r)
      2) Solve quadratic for (1+r)
      3) Yield to maturity r = root − 1   (answer)
    """
    issuer   = random.choice(bond_issuers)
    investor = random.choice(investor_names)
    F  = 1_000
    c  = round(random.uniform(0.03, 0.08), 3)
    C  = round(F * c, 2)

    # Hidden true yield to create a consistent price
    true_r = round(random.uniform(0.02, 0.10), 3)
    P = round(C / (1 + true_r) + (C + F) / ((1 + true_r) ** 2), 2)

    # Quadratic coefficients for x = 1 + r:   P x² − (C+F) x − C = 0
    A = P
    B = -(C + F)
    C_coef = -C
    discr = B**2 - 4 * A * C_coef
    x_root = (-B - discr ** 0.5) / (2 * A)      # economically relevant root
    ytm = x_root - 1

    question = (
        f"{investor} is analysing a 2-year ${F} bond from {issuer} with "
        f"{c*100:.2f} % coupons (${C:.2f}). It trades at ${P:,.2f}. "
        f"Estimate its yield to maturity."
    )

    solution = (
        f"Step 1: Price equation → P(1+r)² − (C+F)(1+r) − C = 0\n\n"
        f"Step 2: Solve quadratic with A={A:.2f}, B={B:.2f}, C={C_coef:.2f}, "
        f"disc={discr:.2f} ⇒ root x = {x_root:.5f}\n\n"
        f"Step 3 (answer): Yield r = x − 1 = {ytm*100:.2f} %"
    )
    return question, solution

def template_bp_hard1():
    """
    5:Advanced: Dirty Price of a Semi-Annual Coupon Bond  (4 steps)
    Steps (4):
      1) PV of all future semi-annual coupons
      2) PV of face value → Clean price
      3) Accrued interest since last coupon
      4) Dirty price = Clean + Accrued   (answer)
    """
    issuer   = random.choice(bond_issuers)
    investor = random.choice(investor_names)
    F   = 1_000
    q   = round(random.uniform(0.03, 0.08), 3)        # annual coupon rate
    C_sa = round(F * q / 2, 2)                        # semi-annual coupon
    years = random.randint(2, 5)
    r_sa  = round(random.uniform(0.015, 0.05), 3)     # semi-annual yield
    periods = years * 2

    # Step 1 & 2: Clean price
    pv_cpn = sum(C_sa / ((1 + r_sa) ** t) for t in range(1, periods + 1))
    pv_F   = F / ((1 + r_sa) ** periods)
    clean  = pv_cpn + pv_F

    # Step 3: Accrued interest
    months_since = random.randint(1, 5)               # months into current half-year
    accrued = C_sa * (months_since / 6)

    # Step 4: Dirty price
    dirty = clean + accrued

    question = (
        f"{investor} reviews a semi-annual coupon bond from {issuer}:\n"
        f"  • Face ${F}\n"
        f"  • Coupon {q*100:.2f} % (⇒ ${C_sa:.2f} twice a year)\n"
        f"  • {years} years to maturity\n"
        f"  • Semi-annual yield {r_sa*100:.2f} %\n"
        f"  • {months_since} months since the last coupon.\n\n"
        f"What is the bond’s **dirty (invoice) price**?"
    )

    solution = (
        f"Step 1: PV(coupons) = Σ C/(1+r)^t = ${pv_cpn:,.2f}\n\n"
        f"Step 2: PV(face) = ${F} / (1+{r_sa:.3f})^{periods} = ${pv_F:,.2f}\n"
        f"        Clean price = ${clean:,.2f}\n\n"
        f"Step 3: Accrued = C × (months/6) = ${C_sa:.2f} × {months_since}/6 = ${accrued:,.2f}\n\n"
        f"Step 4 (answer): Dirty price = ${clean:,.2f} + ${accrued:,.2f} = ${dirty:,.2f}"
    )
    return question, solution

###############################################################################
# MAIN
###############################################################################

def main():
    """
    Generate 10 instances of each bond-pricing template and save to JSONL.
    """
    templates = [
        template_bp_easy1,
        template_bp_easy2,
        template_bp_medium1,
        template_bp_medium2,
        template_bp_hard1
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
            random.seed()  # reset RNG state

    random.shuffle(problems)
    outfile = "../../testset/financial_markets/bond_pricing.jsonl"
    with open(outfile, "w") as f:
        for p in problems:
            f.write(json.dumps(p))
            f.write("\n")

    print(f"Successfully generated {len(problems)} problems → {outfile}")


if __name__ == "__main__":
    main()
