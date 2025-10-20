import random
import json
import argparse
import pathlib

# Named entities for companies and industries
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]
industry_names = ["automotive", "technology", "e-commerce", "aerospace", "internet services"]

def _usd(x: float) -> str:
    """Format a number as USD with 2 decimals and thousands separators."""
    return f"${x:,.2f}"

def _pct(x: float) -> str:
    """Format a percent value with 2 decimals and % sign."""
    return f"{x:.2f}%"

# =========================
# EASY (2 templates)
# =========================

def template_asset_turnover_simple():
    """1:Easy:Simple Asset Turnover Ratio from sales and total assets."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_sales = round(random.uniform(50_000, 500_000), 2)
    total_assets = round(random.uniform(100_000, 1_000_000), 2)

    question = (
        f"{company_name}, operating in the {industry} industry, generated total sales of "
        f"{_usd(total_sales)} and reported total assets of {_usd(total_assets)}. "
        f"Calculate the company's Asset Turnover Ratio (unitless)."
    )

    asset_turnover = round(total_sales / total_assets, 2)

    solution = (
        "Step 1 (Identify formula): Asset Turnover = Total Sales ÷ Total Assets (unitless).\n"
        f"Step 2 (Apply values): {_usd(total_sales)} ÷ {_usd(total_assets)} = {asset_turnover:.2f}.\n"
        "Step 3 (Interpret): Each dollar of assets generated "
        f"{asset_turnover:.2f} dollars of sales."
    )

    return question, solution


def template_asset_turnover_compare_two_periods():
    """2:Easy:Compare Asset Turnover across two periods with assets changing and sales constant."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_sales = round(random.uniform(100_000, 1_000_000), 2)
    assets_last_year = round(random.uniform(200_000, 2_000_000), 2)
    asset_change = round(random.uniform(10_000, 200_000), 2)
    assets_this_year = round(assets_last_year + asset_change, 2)

    question = (
        f"{company_name} in the {industry} industry recorded sales of {_usd(total_sales)} in both Year 1 and Year 2. "
        f"In Year 1, total assets were {_usd(assets_last_year)}. In Year 2, total assets increased by "
        f"{_usd(asset_change)} to {_usd(assets_this_year)}. Compute the Asset Turnover Ratio for each year "
        "and state which year had the higher ratio."
    )

    t_last = round(total_sales / assets_last_year, 2)
    t_this = round(total_sales / assets_this_year, 2)
    winner = "Year 1" if t_last > t_this else ("Year 2" if t_this > t_last else "Both equal")

    solution = (
        "Step 1 (Formula): Asset Turnover = Sales ÷ Total Assets.\n"
        f"Year 1: {_usd(total_sales)} ÷ {_usd(assets_last_year)} = {t_last:.2f}\n"
        f"Year 2: {_usd(total_sales)} ÷ {_usd(assets_this_year)} = {t_this:.2f}\n"
        "Step 2 (Reason): With sales constant, higher assets dilute turnover.\n"
        f"Conclusion: {winner} has the higher Asset Turnover."
    )

    return question, solution

# =========================
# INTERMEDIATE (2 templates)
# =========================

def template_asset_turnover_average_assets():
    """3:Intermediate:Use Average Total Assets (beginning & ending) to compute Asset Turnover."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_sales = round(random.uniform(300_000, 1_500_000), 2)
    beginning_assets = round(random.uniform(400_000, 2_000_000), 2)
    # Ensure ending assets not wildly off; keep within a sensible band
    ending_assets = round(beginning_assets * random.uniform(0.8, 1.3), 2)
    average_assets = round((beginning_assets + ending_assets) / 2, 2)

    question = (
        f"{company_name} ({industry}) reported total sales of {_usd(total_sales)} this year. "
        f"Beginning total assets were {_usd(beginning_assets)} and ending total assets were {_usd(ending_assets)}. "
        "Compute the Asset Turnover Ratio using Average Total Assets."
    )

    turnover = round(total_sales / average_assets, 2)

    solution = (
        "Step 1 (Use appropriate base): Seasonal/level changes mean we use Average Total Assets.\n"
        f"Average Assets = ({_usd(beginning_assets)} + {_usd(ending_assets)}) / 2 = {_usd(average_assets)}\n"
        "Step 2 (Apply formula): Asset Turnover = Sales ÷ Average Assets.\n"
        f"{_usd(total_sales)} ÷ {_usd(average_assets)} = {turnover:.2f}\n"
        "Step 3 (Interpret): This normalizes for asset changes across the year."
    )

    return question, solution


def template_asset_turnover_with_depreciation():
    """4:Intermediate:Asset Turnover after depreciation adjustment (assets decrease; sales given)."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_sales = round(random.uniform(200_000, 1_500_000), 2)
    total_assets = round(random.uniform(500_000, 3_000_000), 2)
    max_dep = min(500_000.00, total_assets * 0.8)  # guardrail to keep adjusted assets positive
    depreciation = round(random.uniform(50_000, max_dep), 2)
    adjusted_assets = round(total_assets - depreciation, 2)

    question = (
        f"{company_name}, operating in {industry}, generated {_usd(total_sales)} in sales this year and held "
        f"total assets of {_usd(total_assets)}. Due to depreciation of {_usd(depreciation)}, total assets decline "
        f"to {_usd(adjusted_assets)}. Compute the Asset Turnover Ratio before and after depreciation."
    )

    t_before = round(total_sales / total_assets, 2)
    t_after = round(total_sales / adjusted_assets, 2)

    direction = "increases" if t_after > t_before else ("decreases" if t_after < t_before else "does not change")

    solution = (
        "Step 1 (Before): Asset Turnover = Sales ÷ Total Assets.\n"
        f"{_usd(total_sales)} ÷ {_usd(total_assets)} = {t_before:.2f}\n"
        "Step 2 (After adjustment): Reduce assets for depreciation.\n"
        f"Adjusted Assets = {_usd(total_assets)} − {_usd(depreciation)} = {_usd(adjusted_assets)}\n"
        f"Turnover After = {_usd(total_sales)} ÷ {_usd(adjusted_assets)} = {t_after:.2f}\n"
        f"Step 3 (Reason): With sales unchanged and assets lower, turnover {direction}."
    )

    return question, solution

# =========================
# ADVANCED (1 template)
# =========================

def template_asset_turnover_investment_vs_sales_push():
    """5:Advanced:Two strategic scenarios: (1) Add new investment and simultaneous depreciation (assets change). (2) Push sales by a specified percentage with assets held at current level."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_sales = round(random.uniform(500_000, 2_500_000), 2)
    total_assets = round(random.uniform(800_000, 3_000_000), 2)

    new_investment = round(random.uniform(100_000, 500_000), 2)
    depreciation = round(random.uniform(50_000, min(200_000.00, total_assets * 0.5)), 2)

    sales_increase_pct = round(random.uniform(10.0, 50.0), 2)
    new_sales = round(total_sales * (1 + sales_increase_pct / 100.0), 2)

    # Scenario 1 assets
    adjusted_assets = round(total_assets + new_investment - depreciation, 2)

    question = (
        f"{company_name} in the {industry} industry reported total sales of {_usd(total_sales)} and total assets of "
        f"{_usd(total_assets)}. The firm is evaluating two options:\n"
        f"• Scenario 1 (CapEx with wear): Invest {_usd(new_investment)} in assets while recognizing depreciation of "
        f"{_usd(depreciation)} on existing assets.\n"
        f"• Scenario 2 (Sales push): Increase sales by {_pct(sales_increase_pct)} with assets held at {_usd(total_assets)}.\n"
        "For each scenario, compute the Asset Turnover Ratio and compare to the current turnover."
    )

    t_current = round(total_sales / total_assets, 2)
    t_s1 = round(total_sales / adjusted_assets, 2)
    t_s2 = round(new_sales / total_assets, 2)

    s1_dir = "higher" if t_s1 > t_current else ("lower" if t_s1 < t_current else "the same as")
    s2_dir = "higher" if t_s2 > t_current else ("lower" if t_s2 < t_current else "the same as")

    solution = (
        "Step 1 (Current benchmark):\n"
        f"Current Turnover = {_usd(total_sales)} ÷ {_usd(total_assets)} = {t_current:.2f}\n\n"
        "Step 2 (Scenario 1 — CapEx with wear):\n"
        f"Adjusted Assets = {_usd(total_assets)} + {_usd(new_investment)} − {_usd(depreciation)} = {_usd(adjusted_assets)}\n"
        f"Turnover S1 = {_usd(total_sales)} ÷ {_usd(adjusted_assets)} = {t_s1:.2f} → {s1_dir} current.\n\n"
        "Step 3 (Scenario 2 — Sales push):\n"
        f"New Sales = {_usd(new_sales)}\n"
        f"Turnover S2 = {_usd(new_sales)} ÷ {_usd(total_assets)} = {t_s2:.2f} → {s2_dir} current.\n\n"
        "Reasoning: Increasing assets (with sales fixed) typically lowers turnover; raising sales (with assets fixed) raises turnover."
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_asset_turnover_simple,
        template_asset_turnover_compare_two_periods,
        template_asset_turnover_average_assets,
        template_asset_turnover_with_depreciation,
        template_asset_turnover_investment_vs_sales_push,
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
    parser = argparse.ArgumentParser(description="Generate efficiency ratio problems.")
    parser.add_argument("--output_file", type=str, default="effratio_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
