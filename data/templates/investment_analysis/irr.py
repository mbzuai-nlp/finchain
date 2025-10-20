import random
import numpy as np

# Named entities for investors and projects
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
project_names = [
    "Tesla Gigafactory", "Apple iPhone Launch", "Amazon Web Services Expansion", "SpaceX Starship Development",
    "Google Data Center Build", "Microsoft Azure", "Netflix Content Production", "Uber Autonomous Driving Initiative",
    "Facebook Metaverse", "Samsung Semiconductor Factory"
]

# ------------------------------------------------------------------
# Template 1: IRR with selling (exit) costs
# ------------------------------------------------------------------
def template_irr_net_sale_proceeds():
    """
    1: Basic: IRR where the year-1 inflow is a sale price minus selling costs.
    Two reasoning steps:
      1) Compute net proceeds.
      2) Compute IRR from net proceeds and initial investment.
    """
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    investment   = random.randint(10_000, 50_000)
    sale_price   = random.randint(20_000, 70_000)
    sell_cost    = random.randint(500, 5_000)

    # Ensure positive net gain > investment so IRR is positive
    # (Regenerate sale_price if needed.)
    if sale_price - sell_cost <= investment:
        sale_price = investment + sell_cost + random.randint(1_000, 20_000)

    net_proceeds = sale_price - sell_cost
    irr_ratio    = net_proceeds / investment - 1
    irr_percent  = round(irr_ratio * 100, 2)

    question = (
        f"{investor_name} invested ${investment:,.0f} in {project_name}. "
        f"After 1 year, the project is sold for ${sale_price:,.0f}, but ${sell_cost:,.0f} "
        f"in selling costs must be paid. What is the internal rate of return (IRR)?"
    )

    solution = (
        "Step 1 (Compute net sale proceeds at Year 1):\n"
        f"     Net Proceeds = ${sale_price:,.0f} - ${sell_cost:,.0f} = ${net_proceeds:,.0f}\n\n"
        "Step 2 (Solve IRR for a 1-year investment):\n"
        f"     IRR = (${net_proceeds:,.0f} ÷ ${investment:,.0f}) - 1 = {irr_ratio:.6f}\n\n"
        f"Final: IRR = {irr_percent:.2f}%"
    )

    return question, solution


# ------------------------------------------------------------------
# Template 2: IRR with after-tax proceeds on the gain
# ------------------------------------------------------------------
def template_irr_after_tax():
    """
    2: Basic: IRR where exit is taxed on the gain (sale - basis).
    Two reasoning steps:
      1) Compute after-tax cash flow (sale - tax_on_gain).
      2) Compute IRR.
    """
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    investment  = random.randint(10_000, 50_000)  # tax basis
    sale_price  = random.randint(20_000, 80_000)
    tax_rate_bp = random.choice([10, 15, 20, 25, 30, 35, 40])  # %
    tax_rate    = tax_rate_bp / 100.0

    # Ensure gain > 0 so tax makes sense & IRR positive
    if sale_price <= investment:
        sale_price = investment + random.randint(5_000, 30_000)

    gain        = sale_price - investment
    tax         = gain * tax_rate
    after_tax   = sale_price - tax
    irr_ratio   = after_tax / investment - 1
    irr_percent = round(irr_ratio * 100, 2)

    question = (
        f"{investor_name} invested ${investment:,.0f} (tax basis) in {project_name}. "
        f"After 1 year, it is sold for ${sale_price:,.0f}. The tax on the gain is {tax_rate_bp}% "
        f"of (Sale Price - Initial Investment). What is the internal rate of return (IRR) after tax?"
    )

    solution = (
        "Step 1 (Compute after-tax proceeds at Year 1):\n"
        f"     Gain = ${sale_price:,.0f} - ${investment:,.0f} = ${gain:,.0f}\n"
        f"     Tax  = {tax_rate_bp}% × ${gain:,.0f} = ${tax:,.2f}\n"
        f"     After-Tax Proceeds = ${sale_price:,.0f} - ${tax:,.2f} = ${after_tax:,.2f}\n\n"
        "Step 2 (Solve IRR for a 1-year investment):\n"
        f"     IRR = (${after_tax:,.2f} ÷ ${investment:,.0f}) - 1 = {irr_ratio:.6f}\n\n"
        f"Final: IRR = {irr_percent:.2f}%"
    )

    return question, solution

# ================================================================
# 1. Sale -> Selling Costs -> Tax on Gain -> IRR (1-year)
# Steps: (1) Net Sale  (2) After-Tax Proceeds  (3) IRR
# ================================================================
def template_irr_after_tax_net_sale_cost():
    """
    3: Intermediate:
    1. Sale -> Selling Costs -> Tax on Gain -> IRR (1-year)
    Steps: (1) Net Sale  (2) After-Tax Proceeds  (3) IRR
    """
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    investment = random.randint(10_000, 50_000)
    sale_price = random.randint(investment + 5_000, investment + 50_000)
    sell_cost  = random.randint(500, 5_000)
    tax_rate_bp = random.choice([10,15,20,25,30,35,40])

    net_sale = sale_price - sell_cost
    gain     = net_sale - investment
    if gain <= 0:  # force positive gain
        sale_price = investment + sell_cost + random.randint(1_000, 20_000)
        net_sale   = sale_price - sell_cost
        gain       = net_sale - investment

    tax_rate  = tax_rate_bp / 100
    tax       = gain * tax_rate
    after_tax = net_sale - tax
    irr_ratio = after_tax / investment - 1
    irr_percent = round(irr_ratio * 100, 2)

    question = (
        f"{investor_name} invested ${investment:,.0f} in {project_name}. "
        f"After 1 year, the project is sold for ${sale_price:,.0f}. Selling costs are ${sell_cost:,.0f}. "
        f"Capital gains tax is {tax_rate_bp}% of (Net Sale Proceeds - Initial Investment). "
        "What is the internal rate of return (IRR) after tax?"
    )

    solution = (
        "Step 1 (Net sale proceeds after selling costs):\n"
        f"     Net Sale = ${sale_price:,.0f} - ${sell_cost:,.0f} = ${net_sale:,.2f}\n\n"
        "Step 2 (After-tax proceeds):\n"
        f"     Gain = ${net_sale:,.2f} - ${investment:,.0f} = ${gain:,.2f}\n"
        f"     Tax  = {tax_rate_bp}% * ${gain:,.2f} = ${tax:,.2f}\n"
        f"     After-Tax Proceeds = ${net_sale:,.2f} - ${tax:,.2f} = ${after_tax:,.2f}\n\n"
        "Step 3 (Solve IRR for 1-year investment):\n"
        f"     IRR = (${after_tax:,.2f} / ${investment:,.0f}) - 1 = {irr_ratio:.6f}\n\n"
        f"Final: IRR = {irr_percent:.2f}%"
    )

    return question, solution

# ================================================================
# 4. Semiannual Coupon Reinvested to Year-End -> IRR
# Steps: (1) Coupon  (2) Reinvest & Add Par  (3) IRR
# ================================================================
def template_irr_bond_coupon_reinvest():
    """
    4: Intermediate:
    Semiannual Coupon Reinvested to Year-End -> IRR
    Steps: (1) Coupon  (2) Reinvest & Add Par  (3) IRR
    """
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    face = 10_000
    coupon_rate_bp = random.choice([4,5,6,7,8,9])  # annual coupon %
    reinv_rate_bp  = random.choice([3,4,5,6])      # simple annual reinvest %
    coupon_rate = coupon_rate_bp / 100
    reinv_rate  = reinv_rate_bp  / 100

    coupon_6mo = face * coupon_rate / 2
    coupon_fv  = coupon_6mo * (1 + reinv_rate * 0.5)  # simple pro‑rata
    total_cash = face + coupon_fv

    # Choose a purchase price below total cash so IRR not negative
    price = random.randint(int(total_cash * 0.7), int(total_cash * 0.99))

    irr_ratio   = total_cash / price - 1
    irr_percent = round(irr_ratio * 100, 2)

    question = (
        f"{investor_name} pays ${price:,.0f} to buy a 1-year ${face:,.0f} par bond issued by {project_name}. "
        f"The bond has a {coupon_rate_bp}% annual coupon paid semiannually. "
        f"The 6-month coupon is reinvested at a simple annual rate of {reinv_rate_bp}% "
        "for the remaining 6 months until maturity, when par is repaid. "
        "What is the internal rate of return (IRR) based on the cash received at maturity?"
    )

    solution = (
        "Step 1 (Compute 6-month coupon payment):\n"
        f"     Coupon = {coupon_rate_bp}% * ${face:,.0f} / 2 = ${coupon_6mo:,.2f}\n\n"
        "Step 2 (Grow coupon to Year 1 at reinvest rate and add par):\n"
        f"     Reinvested Coupon = ${coupon_6mo:,.2f} * [1 + {reinv_rate_bp}% * 0.5] = ${coupon_fv:,.2f}\n"
        f"     Total Year-1 Cash = ${face:,.0f} + ${coupon_fv:,.2f} = ${total_cash:,.2f}\n\n"
        "Step 3 (Solve IRR for 1-year holding):\n"
        f"     IRR = (${total_cash:,.2f} / ${price:,.0f}) - 1 = {irr_ratio:.6f}\n\n"
        f"Final: IRR = {irr_percent:.2f}%"
    )

    return question, solution

# ---------------------------------------------------------------
# Template 5 · Fractional-year sale → net sale → tax → IRR
# ---------------------------------------------------------------
def template_irr_fractional_net_tax():
    """
    5: Advanced:
    4-step annualized IRR with a partial-year holding, selling costs, and tax.
      Step 1  Convert holding period (months) to years.
      Step 2  Compute net sale proceeds (sale price – selling costs).
      Step 3  Compute tax on the gain and derive after-tax proceeds.
      Step 4  Solve annualized IRR.
    """
    investor_name = random.choice(investor_names)
    project_name  = random.choice(project_names)

    investment = random.randint(10_000, 60_000)
    months     = random.choice([6, 9, 15, 18, 21, 24])
    sale_price = random.randint(investment + 5_000, investment + 70_000)
    sell_cost  = random.randint(500, 5_000)
    tax_rate_bp = random.choice([20, 25, 30, 35])
    tax_rate = tax_rate_bp / 100

    years = months / 12
    net_sale = sale_price - sell_cost
    gain     = net_sale - investment
    if gain <= 0:                            # ensure positive gain
        sale_price = investment + sell_cost + random.randint(3_000, 15_000)
        net_sale   = sale_price - sell_cost
        gain       = net_sale - investment

    tax        = gain * tax_rate
    after_tax  = net_sale - tax
    irr_ratio  = (after_tax / investment) ** (1 / years) - 1
    irr_percent = round(irr_ratio * 100, 2)

    # ---------- Question ----------
    question = (
        f"{investor_name} invested ${investment:,.0f} in {project_name}. "
        f"The project is sold after {months} months for ${sale_price:,.0f}. "
        f"Selling costs total ${sell_cost:,.0f}. Capital-gains tax is {tax_rate_bp}% of "
        "(Net Sale Proceeds − Initial Investment). What is the annualized internal rate of return (IRR)?"
    )

    # ---------- Solution ----------
    solution = (
        "Step 1 (Convert holding period to years):\n"
        f"     {months} months ÷ 12 = {years:.4f} years\n\n"
        "Step 2 (Compute net sale proceeds):\n"
        f"     Net Sale = ${sale_price:,.0f} − ${sell_cost:,.0f} = ${net_sale:,.2f}\n\n"
        "Step 3 (Compute after-tax proceeds):\n"
        f"     Gain = ${net_sale:,.2f} − ${investment:,.0f} = ${gain:,.2f}\n"
        f"     Tax  = {tax_rate_bp}% × ${gain:,.2f} = ${tax:,.2f}\n"
        f"     After-Tax Proceeds = ${net_sale:,.2f} − ${tax:,.2f} = ${after_tax:,.2f}\n\n"
        "Step 4 (Solve annualized IRR):\n"
        f"     (1 + IRR)^{years:.4f} = ${after_tax:,.2f} / ${investment:,.0f}\n"
        f"     IRR = ({after_tax / investment:.6f})^(1/{years:.4f}) − 1 = {irr_ratio:.6f}\n\n"
        f"Final: IRR = {irr_percent:.2f}%"
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
        template_irr_net_sale_proceeds,
        template_irr_after_tax,
        template_irr_after_tax_net_sale_cost,
        template_irr_bond_coupon_reinvest,
        template_irr_fractional_net_tax
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
    output_file = "../../testset/investment_analysis/irr.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem, ensure_ascii=False))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()