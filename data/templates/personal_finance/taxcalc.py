import random
from decimal import Decimal, ROUND_HALF_UP
import json
import argparse
import pathlib

# ---------------------------
# Helpers for consistency
# ---------------------------

CURRENCY = "USD"
CURR = "$"

def q2(x):
    """Quantize to 2 decimal places with banker-friendly rounding."""
    return Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def money(x):
    """Format as currency with thousands separators and 2 decimals."""
    return f"{CURR}{q2(x):,.2f}"

def pct(x):
    """Format a percentage with 2 decimals."""
    return f"{Decimal(x).quantize(Decimal('0.01'))}%"

def rand_rate(min_pct, max_pct):
    """Generate a percentage as Decimal with exactly 2 decimals (avoids float artifacts)."""
    # produce an integer of basis points then divide by 100
    bps = random.randint(int(min_pct * 100), int(max_pct * 100))
    return Decimal(bps) / Decimal(100)

# Named entities
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]

# =========================================================
# EASY 1: Flat income tax (single rate)
# =========================================================
def template_income_tax_flat_easy():
    """1:Easy:Single-rate income tax on annual income."""
    person = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    annual_income = random.randint(500_000, 3_000_000)  # USD cents avoided; we print 2dp anyway
    rate = rand_rate(5.00, 30.00)

    tax_due = q2(Decimal(annual_income) * rate / Decimal(100))

    question = (
        f"({CURRENCY}) {person} has an annual income of {money(annual_income)}. "
        f"The applicable flat income tax rate is {pct(rate)}. "
        f"How much income tax will they owe for the year?"
    )

    solution = (
        "Step 1: Identify the tax base and rate (reasoning):\n"
        f"  Tax base is annual income = {money(annual_income)} and rate = {pct(rate)}.\n\n"
        "Step 2: Compute tax due as base × rate:\n"
        f"  Tax Due = {money(annual_income)} × {pct(rate)} = {money(tax_due)}"
    )
    return question, solution

# =========================================================
# EASY 2: Standard deduction then flat tax
# =========================================================
def template_income_tax_with_standard_deduction_easy():
    """2:Easy:Apply a standard deduction, then a single tax rate."""
    person = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    annual_income = random.randint(800_000, 3_500_000)
    # Standard deduction capped to avoid exceeding income
    max_std = max(50_000, int(annual_income * 0.25))
    standard_deduction = random.randint(50_000, max_std)
    rate = rand_rate(8.00, 25.00)

    taxable_income = max(0, annual_income - standard_deduction)
    tax_due = q2(Decimal(taxable_income) * rate / Decimal(100))

    question = (
        f"({CURRENCY}) {person} earns {money(annual_income)} per year and can claim a "
        f"standard deduction of {money(standard_deduction)}. The tax rate on the taxable "
        f"income is {pct(rate)}. What is the income tax owed?"
    )

    solution = (
        "Step 1: Determine the taxable income (reasoning: income reduced by standard deduction):\n"
        f"  Taxable Income = {money(annual_income)} − {money(standard_deduction)} = {money(taxable_income)}\n\n"
        "Step 2: Apply the flat tax rate to the taxable income (reasoning: policy applies rate to taxable base):\n"
        f"  Tax Due = {money(taxable_income)} × {pct(rate)} = {money(tax_due)}"
    )
    return question, solution

# =========================================================
# INTERMEDIATE 1: Itemized deductions (cap ensures solvability)
# =========================================================
def template_tax_with_itemized_deductions_intermediate():
    """3:Intermediate:Compute taxable income after itemized deductions and apply a single rate."""
    person = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    age = random.randint(25, 55)
    annual_income = random.randint(1_000_000, 5_000_000)
    # Cap deductions as a fraction of income for realism
    cap = max(100_000, int(annual_income * 0.35))
    deductions = random.randint(50_000, cap)
    rate = rand_rate(10.00, 30.00)

    taxable_income = max(0, annual_income - deductions)
    tax_due = q2(Decimal(taxable_income) * rate / Decimal(100))

    question = (
        f"({CURRENCY}) {person}, aged {age}, earns {money(annual_income)} annually and "
        f"has eligible itemized deductions totaling {money(deductions)}. "
        f"Their tax rate is {pct(rate)} on taxable income. "
        f"How much income tax do they owe after deductions?"
    )

    solution = (
        "Step 1: Establish taxable income (reasoning: income reduced by allowable deductions):\n"
        f"  Taxable Income = {money(annual_income)} − {money(deductions)} = {money(taxable_income)}\n\n"
        "Step 2: Apply the tax rate to taxable income (reasoning: tax computed on reduced base):\n"
        f"  Tax Due = {money(taxable_income)} × {pct(rate)} = {money(tax_due)}"
    )
    return question, solution

# =========================================================
# INTERMEDIATE 2: Capital gains tax (ensure sale > purchase)
# =========================================================
def template_capital_gains_tax_intermediate():
    """4:Intermediate:Capital gains tax on sale of shares. Ensures sale price > purchase price."""
    person = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    company = random.choice(company_names)
    current_age = random.randint(30, 55)
    purchase_price = random.randint(300_000, 1_000_000)
    # Ensure a positive gain
    sale_price = random.randint(purchase_price + 10_000, purchase_price + random.randint(100_000, 1_000_000))
    cap_gains_rate = rand_rate(10.00, 20.00)

    capital_gain = sale_price - purchase_price
    tax_due = q2(Decimal(capital_gain) * cap_gains_rate / Decimal(100))

    question = (
        f"({CURRENCY}) {person}, aged {current_age}, sold shares of {company} for {money(sale_price)}. "
        f"They purchased the shares for {money(purchase_price)}. The capital gains tax rate is {pct(cap_gains_rate)}. "
        f"What is their capital gains tax liability?"
    )

    solution = (
        "Step 1: Determine the capital gain (reasoning: gain is sale proceeds minus cost basis):\n"
        f"  Capital Gain = {money(sale_price)} − {money(purchase_price)} = {money(capital_gain)}\n\n"
        "Step 2: Apply the capital gains tax rate to the gain (reasoning: tax levied on gains only):\n"
        f"  Tax Due = {money(capital_gain)} × {pct(cap_gains_rate)} = {money(tax_due)}"
    )
    return question, solution

# =========================================================
# ADVANCED: Double taxation relief on foreign income
# =========================================================
def template_double_taxation_relief_advanced():
    """5:Advanced:Compute home-country tax on foreign income, foreign tax paid, the relief (min rule), and net liability after relief."""
    person = random.choice(["John", "Aisha", "Ravi", "Sara", "David"])
    foreign_country = random.choice(["UAE", "USA", "UK", "Canada", "Australia"])
    age = random.randint(30, 60)
    foreign_income = random.randint(1_000_000, 5_000_000)
    home_rate = rand_rate(15.00, 30.00)
    foreign_rate = rand_rate(5.00, 20.00)

    home_tax_due = q2(Decimal(foreign_income) * home_rate / Decimal(100))
    foreign_tax_paid = q2(Decimal(foreign_income) * foreign_rate / Decimal(100))
    relief = min(home_tax_due, foreign_tax_paid)
    net_liability = q2(home_tax_due - relief)

    question = (
        f"({CURRENCY}) {person}, aged {age}, earns foreign income of {money(foreign_income)} from {foreign_country}. "
        f"The home-country tax rate on foreign income is {pct(home_rate)}, and tax paid in {foreign_country} is {pct(foreign_rate)}. "
        f"Compute the eligible double taxation relief and the net home-country tax liability."
    )

    solution = (
        "Step 1: Compute home-country tax on the foreign income (reasoning: home policy applies to worldwide income):\n"
        f"  Home Tax = {money(foreign_income)} × {pct(home_rate)} = {money(home_tax_due)}\n\n"
        "Step 2: Determine foreign tax paid (reasoning: credit cannot exceed home tax on same income):\n"
        f"  Foreign Tax Paid = {money(foreign_income)} × {pct(foreign_rate)} = {money(foreign_tax_paid)}\n\n"
        "Step 3: Compute relief using the minimum rule (reasoning: lesser of home tax and foreign tax on the same income):\n"
        f"  Relief = min({money(home_tax_due)}, {money(foreign_tax_paid)}) = {money(relief)}\n\n"
        "Step 4: Net home-country liability after relief (reasoning: home tax minus allowable credit):\n"
        f"  Net Liability = {money(home_tax_due)} − {money(relief)} = {money(net_liability)}"
    )
    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_income_tax_flat_easy,
        template_income_tax_with_standard_deduction_easy,
        template_tax_with_itemized_deductions_intermediate,
        template_capital_gains_tax_intermediate,
        template_double_taxation_relief_advanced,
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
    parser = argparse.ArgumentParser(description="Generate tax calculation problems.")
    parser.add_argument("--output_file", type=str, default="taxcalc_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
