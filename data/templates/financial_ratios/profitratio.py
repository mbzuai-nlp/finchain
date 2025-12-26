import random
import json
import argparse
import pathlib

# Named entities for companies and industries
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]
industry_names = ["automotive", "technology", "e-commerce", "aerospace", "internet services"]

# ---------- formatting helpers ----------
def fmt_money(x: float) -> str:
    """Format currency consistently as $ with two decimals and commas."""
    return f"${x:,.2f}"

def fmt_pct(x: float) -> str:
    """Format percentages consistently with two decimals and a % sign."""
    return f"{x:.2f}%"

# ---------- Basic 1: Net Profit Margin ----------
def template_net_profit_margin_easy():
    """1:Basic:Net Profit Margin from revenue and net income."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    revenue = random.randint(80_000, 400_000)
    net_income = int(round(revenue * random.uniform(0.05, 0.25)))

    question = (
        f"{company}, operating in the {industry} industry, reported revenue of {fmt_money(revenue)} "
        f"and net income of {fmt_money(net_income)}. Calculate the company's net profit margin."
    )

    margin = (net_income / revenue) * 100

    solution = (
        "Step 1: Use Net Profit Margin = (Net Income ÷ Revenue) × 100.\n"
        f"Step 2: Plug in values = ({fmt_money(net_income)} ÷ {fmt_money(revenue)}) × 100.\n"
        f"Step 3: Compute = {fmt_pct(margin)}."
    )
    return question, solution

# ---------- Easy 2: Gross Profit Margin ----------
def template_gross_profit_margin_easy():
    """2:Basic:Gross Profit Margin from revenue and COGS."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    revenue = random.randint(120_000, 500_000)
    cogs = int(round(revenue * random.uniform(0.50, 0.80)))
    gross_profit = revenue - cogs
    gpm = (gross_profit / revenue) * 100

    question = (
        f"{company}, a {industry} company, recorded revenue of {fmt_money(revenue)} and cost of goods sold (COGS) "
        f"of {fmt_money(cogs)}. Calculate the Gross Profit Margin."
    )

    solution = (
        "Step 1: Gross Profit = Revenue − COGS.\n"
        f"        = {fmt_money(revenue)} − {fmt_money(cogs)} = {fmt_money(gross_profit)}.\n"
        "Step 2: Gross Profit Margin = (Gross Profit ÷ Revenue) × 100.\n"
        f"        = ({fmt_money(gross_profit)} ÷ {fmt_money(revenue)}) × 100 = {fmt_pct(gpm)}."
    )
    return question, solution

# ---------- Intermediate 1: Operating Profit (EBIT) Margin ----------
def template_operating_margin_intermediate():
    """3:Intermediate:Compute Operating Profit (EBIT) and Operating Margin from revenue, COGS, and Opex."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    revenue = random.randint(200_000, 800_000)
    cogs = int(round(revenue * random.uniform(0.45, 0.70)))
    # Opex will be 10%–25% of revenue but not exceeding (revenue - cogs - a buffer)
    max_opex_allowed = max(10_000, revenue - cogs - 10_000)
    opex = int(round(min(max_opex_allowed, revenue * random.uniform(0.10, 0.25))))
    ebit = revenue - cogs - opex
    # If randomization produced marginally low EBIT, nudge opex down to ensure positivity
    if ebit <= 0:
        opex = max(0, opex + ebit - 1)  # reduce opex so that ebit = 1 at least
        ebit = revenue - cogs - opex
    opm = (ebit / revenue) * 100

    question = (
        f"{company} in the {industry} sector reported: Revenue {fmt_money(revenue)}, COGS {fmt_money(cogs)}, "
        f"and Operating Expenses {fmt_money(opex)}. Calculate (a) Operating Profit (EBIT) and "
        f"(b) Operating Profit Margin."
    )

    solution = (
        "Step 1: EBIT = Revenue − COGS − Operating Expenses.\n"
        f"        = {fmt_money(revenue)} − {fmt_money(cogs)} − {fmt_money(opex)} = {fmt_money(ebit)}.\n"
        "Step 2: Operating Profit Margin = (EBIT ÷ Revenue) × 100.\n"
        f"        = ({fmt_money(ebit)} ÷ {fmt_money(revenue)}) × 100 = {fmt_pct(opm)}."
    )
    return question, solution

# ---------- Intermediate 2: Compare Gross vs Net Profit Margins ----------
def template_dual_margin_intermediate():
    """4:Intermediate:Compute both Gross Profit Margin and Net Profit Margin."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    revenue = random.randint(250_000, 900_000)
    cogs = int(round(revenue * random.uniform(0.50, 0.75)))
    # Net income 5%–20% of revenue to keep realistic and below gross profit
    net_income = int(round(revenue * random.uniform(0.05, 0.20)))
    # Ensure net income <= gross profit
    gross_profit = revenue - cogs
    if net_income > gross_profit:
        net_income = int(round(gross_profit * random.uniform(0.50, 0.90)))

    gpm = (gross_profit / revenue) * 100
    npm = (net_income / revenue) * 100

    question = (
        f"{company} ({industry}) reported revenue of {fmt_money(revenue)}, COGS of {fmt_money(cogs)}, "
        f"and net income of {fmt_money(net_income)}. Calculate (a) the Gross Profit Margin and (b) the Net Profit Margin."
    )

    solution = (
        "Step 1: Gross Profit = Revenue − COGS = "
        f"{fmt_money(revenue)} − {fmt_money(cogs)} = {fmt_money(gross_profit)}.\n"
        "Step 2: Gross Profit Margin = (Gross Profit ÷ Revenue) × 100 = "
        f"({fmt_money(gross_profit)} ÷ {fmt_money(revenue)}) × 100 = {fmt_pct(gpm)}.\n"
        "Step 3: Net Profit Margin = (Net Income ÷ Revenue) × 100 = "
        f"({fmt_money(net_income)} ÷ {fmt_money(revenue)}) × 100 = {fmt_pct(npm)}."
    )
    return question, solution

# ---------- Advanced: Hit a Target Net Profit Margin ----------
def template_target_net_margin_advanced():
    """5:Advanced:Current Net Profit Margin vs a higher target margin."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    revenue = random.randint(300_000, 1_200_000)
    # Current net income 6%–18% of revenue
    net_income = int(round(revenue * random.uniform(0.06, 0.18)))
    current_margin = (net_income / revenue) * 100

    # Ensure target > current by 1–8 p.p., capped reasonably
    lift = random.uniform(1.0, 8.0)
    target_margin = min(current_margin + lift, 40.0)  # cap target at 40% for realism
    required_net_income = (target_margin / 100.0) * revenue
    additional_needed = max(0.0, required_net_income - net_income)

    question = (
        f"{company}, a {industry} company, reported revenue of {fmt_money(revenue)} and net income of "
        f"{fmt_money(net_income)}. Management set a target net profit margin of {fmt_pct(target_margin)}. "
        "Compute: (a) the current net profit margin, (b) the required net income to meet the target, and "
        "(c) the additional net income needed."
    )

    solution = (
        "Step 1: Current Net Profit Margin = (Net Income ÷ Revenue) × 100 = "
        f"({fmt_money(net_income)} ÷ {fmt_money(revenue)}) × 100 = {fmt_pct(current_margin)}.\n"
        "Step 2: Required Net Income to hit target = (Target Margin × Revenue) ÷ 100 = "
        f"({fmt_pct(target_margin)} × {fmt_money(revenue)}) ÷ 100 = {fmt_money(required_net_income)}.\n"
        "Step 3: Additional Net Income Needed = Required − Current = "
        f"{fmt_money(required_net_income)} − {fmt_money(net_income)} = {fmt_money(additional_needed)}."
    )
    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_net_profit_margin_easy,
        template_gross_profit_margin_easy,
        template_operating_margin_intermediate,
        template_dual_margin_intermediate,
        template_target_net_margin_advanced,
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
    parser = argparse.ArgumentParser(description="Generate profitability ratio problems.")
    parser.add_argument("--output_file", type=str, default="profitratio_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
