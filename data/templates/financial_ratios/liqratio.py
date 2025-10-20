import random
from decimal import Decimal, ROUND_HALF_UP
import json
import argparse
import pathlib

# ----------------------------
# Helpers for consistency
# ----------------------------
def q2(x) -> Decimal:
    """Quantize to 2 decimals with ROUND_HALF_UP for financial-style rounding."""
    return Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def money(x) -> str:
    """Format number as USD with thousands separators and 2 decimals."""
    return f"${q2(x):,}"

def ratio2(numer, denom) -> Decimal:
    """Compute a ratio with 2-decimal precision (dimensionless)."""
    return q2(Decimal(numer) / Decimal(denom))

def ensure_quick_assets_reasonable(ca: int, inv: int, prepaids: int) -> tuple[int, int]:
    """
    If inventories + prepaids are too large (leading to negative or near-zero quick assets),
    resample inventories to keep scenarios realistic for teaching.
    """
    max_inv_pre = int(0.85 * ca)  # keep some quick assets positive
    total = inv + prepaids
    if total > max_inv_pre:
        # Reduce inventories so that inv + prepaids ≤ 85% of CA
        inv = max(0, max_inv_pre - prepaids)
    return inv, prepaids

# Named entities for companies and industries
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]
industry_names = ["automotive", "technology", "e-commerce", "aerospace", "internet services"]

# ==========================================================
# EASY (2): Current Ratio; Quick Ratio
# ==========================================================

def template_current_ratio_simple():
    """1:Easy:Simple Current Ratio using current assets and current liabilities."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    ca = random.randint(5_000, 50_000)
    cl = random.randint(2_000, 25_000)

    question = (
        f"{company}, operating in the {industry} industry, has current assets of {money(ca)} "
        f"and current liabilities of {money(cl)}. Calculate the current ratio (to two decimals)."
    )

    current_ratio = ratio2(ca, cl)

    solution = (
        "Step: Apply the formula Current Ratio = Current Assets ÷ Current Liabilities.\n"
        f"  = {money(ca)} ÷ {money(cl)} = {current_ratio:.2f}"
    )
    return question, solution


def template_quick_ratio_simple():
    """2:Easy:Quick Ratio (acid-test) = (Current Assets − Inventories) ÷ Current Liabilities."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    ca = random.randint(10_000, 100_000)
    inv = random.randint(2_000, 30_000)
    cl = random.randint(5_000, 50_000)

    # Keep the prompt realistic (avoid > ~CA inventories for simple cases)
    inv = min(inv, int(0.8 * ca))

    question = (
        f"{company}, a major player in the {industry} industry, reports current assets of {money(ca)}, "
        f"inventories of {money(inv)}, and current liabilities of {money(cl)}. "
        f"Calculate the quick ratio (to two decimals)."
    )

    quick_ratio = ratio2(Decimal(ca) - Decimal(inv), cl)

    solution = (
        "Step: Apply Quick Ratio = (Current Assets − Inventories) ÷ Current Liabilities.\n"
        f"  = ({money(ca)} − {money(inv)}) ÷ {money(cl)} = {quick_ratio:.2f}"
    )
    return question, solution

# ==========================================================
# INTERMEDIATE (2): Both Ratios; Quick-Ratio to Target
# ==========================================================

def template_both_ratios_intermediate():
    """3:Intermediate:Compute Current and Quick Ratios (prepaid expenses excluded from quick assets)."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    ca = random.randint(20_000, 200_000)
    inv = random.randint(5_000, 50_000)
    pre = random.randint(1_000, 20_000)
    cl = random.randint(10_000, 100_000)

    inv, pre = ensure_quick_assets_reasonable(ca, inv, pre)

    question = (
        f"{company}, operating in the {industry} sector, reports: "
        f"current assets {money(ca)}, inventories {money(inv)}, prepaid expenses {money(pre)}, "
        f"and current liabilities {money(cl)}. "
        f"Calculate (i) the current ratio and (ii) the quick ratio (to two decimals)."
    )

    current_ratio = ratio2(ca, cl)
    quick_ratio = ratio2(Decimal(ca) - Decimal(inv) - Decimal(pre), cl)

    solution = (
        "Step 1: Current Ratio = Current Assets ÷ Current Liabilities\n"
        f"  = {money(ca)} ÷ {money(cl)} = {current_ratio:.2f}\n\n"
        "Step 2: Quick Ratio excludes inventories and prepaid expenses:\n"
        "  Quick Ratio = (Current Assets − Inventories − Prepaid Expenses) ÷ Current Liabilities\n"
        f"  = ({money(ca)} − {money(inv)} − {money(pre)}) ÷ {money(cl)} = {quick_ratio:.2f}"
    )
    return question, solution


def template_quick_ratio_reach_target_intermediate():
    """4:Intermediate:Given a minimum quick ratio requirement, compute additional quick assets needed."""
    company = random.choice(company_names)
    industry = random.choice(industry_names)
    ca = random.randint(50_000, 500_000)
    inv = random.randint(10_000, 100_000)
    pre = random.randint(2_000, 25_000)
    cl = random.randint(25_000, 250_000)
    target = q2(random.uniform(1.10, 2.20))

    inv, pre = ensure_quick_assets_reasonable(ca, inv, pre)

    question = (
        f"{company}, in the {industry} industry, has current assets {money(ca)}, inventories {money(inv)}, "
        f"prepaid expenses {money(pre)}, and current liabilities {money(cl)}. "
        f"The firm must maintain a minimum quick ratio of {target:.2f}. "
        f"How much additional cash or marketable securities are required to meet this requirement?"
    )

    quick_assets_now = Decimal(ca) - Decimal(inv) - Decimal(pre)
    required_quick_assets = q2(target * Decimal(cl))
    gap = q2(required_quick_assets - quick_assets_now)
    additional_needed = max(Decimal("0.00"), gap)

    current_quick_ratio = ratio2(quick_assets_now, cl)

    solution = (
        "Step 1: Compute current quick ratio:\n"
        f"  Quick Assets = {money(ca)} − {money(inv)} − {money(pre)} = {money(quick_assets_now)}\n"
        f"  Quick Ratio = {money(quick_assets_now)} ÷ {money(cl)} = {current_quick_ratio:.2f}\n\n"
        "Step 2: Compute the required quick assets to hit the target:\n"
        f"  Required Quick Assets = {target:.2f} × {money(cl)} = {money(required_quick_assets)}\n\n"
        "Step 3: Additional quick assets needed (if any):\n"
        f"  = Required Quick Assets − Current Quick Assets\n"
        f"  = {money(required_quick_assets)} − {money(quick_assets_now)} = {money(additional_needed)}"
        + (" (already compliant; need $0.00)" if additional_needed == Decimal("0.00") else "")
    )

    return question, solution

# ==========================================================
# ADVANCED (1): Full breakdown + target quick ratio
# ==========================================================

def template_liquidity_minimum_quick_ratio_advanced():
    """5:Advanced:Full balance sheet breakdown — compute Current Ratio, Quick Ratio, and additional quick assets needed to meet a minimum quick ratio threshold."""
    # Balance sheet components
    cash = random.randint(25_000, 200_000)
    mkt = random.randint(5_000, 50_000)      # Marketable securities
    ar  = random.randint(20_000, 150_000)    # Accounts receivable
    inv = random.randint(15_000, 100_000)    # Inventory
    pre = random.randint(1_000, 10_000)      # Prepaid expenses
    cl  = random.randint(30_000, 300_000)    # Current liabilities
    target = q2(random.uniform(1.30, 2.50))  # Minimum Quick Ratio

    # Keep inventories + prepaids reasonable relative to total CA
    total_ca = cash + mkt + ar + inv + pre
    inv, pre = ensure_quick_assets_reasonable(total_ca, inv, pre)

    question = (
        "A company's balance sheet shows:\n"
        f"  • Cash: {money(cash)}\n"
        f"  • Marketable securities: {money(mkt)}\n"
        f"  • Accounts receivable: {money(ar)}\n"
        f"  • Inventory: {money(inv)}\n"
        f"  • Prepaid expenses: {money(pre)}\n"
        f"  • Current liabilities: {money(cl)}\n\n"
        f"(i) Compute the Current Ratio and Quick Ratio (both to two decimals).\n"
        f"(ii) If the firm must maintain a minimum Quick Ratio of {target:.2f}, "
        "how much additional cash or marketable securities are required?"
    )

    current_assets = Decimal(cash + mkt + ar + inv + pre)
    quick_assets   = Decimal(cash + mkt + ar)  # exclude inventory & prepaids
    current_ratio  = ratio2(current_assets, cl)
    quick_ratio    = ratio2(quick_assets, cl)

    required_quick_assets = q2(target * Decimal(cl))
    additional_needed = max(Decimal("0.00"), q2(required_quick_assets - quick_assets))

    solution = (
        "Step 1: Current Ratio\n"
        f"  Current Assets = {money(cash)} + {money(mkt)} + {money(ar)} + {money(inv)} + {money(pre)} = {money(current_assets)}\n"
        f"  Current Ratio = {money(current_assets)} ÷ {money(cl)} = {current_ratio:.2f}\n\n"
        "Step 2: Quick Ratio (exclude inventory & prepaids)\n"
        f"  Quick Assets = {money(cash)} + {money(mkt)} + {money(ar)} = {money(quick_assets)}\n"
        f"  Quick Ratio = {money(quick_assets)} ÷ {money(cl)} = {quick_ratio:.2f}\n\n"
        "Step 3: Amount needed to meet the minimum Quick Ratio\n"
        f"  Required Quick Assets = {target:.2f} × {money(cl)} = {money(required_quick_assets)}\n"
        f"  Additional cash/marketable securities needed = {money(required_quick_assets)} − {money(quick_assets)} = {money(additional_needed)}"
        + (" (already compliant; need $0.00)" if additional_needed == Decimal("0.00") else "")
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds
    and write the results to a JSON file.
    """
    templates = [
        template_current_ratio_simple,
        template_quick_ratio_simple,
        template_both_ratios_intermediate,
        template_quick_ratio_reach_target_intermediate,
        template_liquidity_minimum_quick_ratio_advanced,
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
    parser = argparse.ArgumentParser(description="Generate liquidity ratio problems.")
    parser.add_argument("--output_file", type=str, default="liqratio_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
