import random
import json
import argparse
import pathlib

# Named entities for companies and industries
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon.com", "SpaceX", "Google LLC"]
industry_names = ["automotive", "technology", "e-commerce", "aerospace", "internet services"]

def _pct():
    """Helper: two-decimal percentage as float."""
    return round(random.uniform(10, 50), 2)

def _fmt_money(x: float) -> str:
    """Format money consistently to 2 decimals (USD)."""
    return f"${x:,.2f}"

def _fmt_pct(x: float) -> str:
    return f"{x:.2f}%"

# ----------------------------
# EASY 1: Budget Allocation Simple
# ----------------------------
def template_budget_allocation_simple():
    """1:Easy:Split a quarterly budget between Marketing (given %) and Operations (remainder)."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)
    total_budget = float(random.randint(500_000, 5_000_000))  # quarterly USD
    marketing_percentage = round(random.uniform(10, 50), 2)

    marketing_allocation = total_budget * (marketing_percentage / 100.0)
    operations_allocation = total_budget - marketing_allocation

    question = (
        f"{company_name}, operating in the {industry} industry, has a quarterly budget of "
        f"{_fmt_money(total_budget)}. The company plans to allocate {_fmt_pct(marketing_percentage)} "
        f"to Marketing and the remainder to Operations. How much goes to each?"
    )

    solution = (
        "Step 1 (Identify): Marketing share is a fixed percent, Operations is the remainder.\n"
        f"Step 2 (Compute Marketing): {_fmt_pct(marketing_percentage)} × {_fmt_money(total_budget)} "
        f"= {_fmt_money(marketing_allocation)}.\n"
        f"Step 3 (Compute Operations): Total − Marketing = {_fmt_money(total_budget)} − "
        f"{_fmt_money(marketing_allocation)} = {_fmt_money(operations_allocation)}.\n"
        f"Check: {_fmt_money(marketing_allocation)} + {_fmt_money(operations_allocation)} "
        f"= {_fmt_money(total_budget)} (matches total)."
    )

    return question, solution

# ----------------------------
# EASY 2: Budget Reallocation Due to Costs
# ----------------------------
def template_budget_reallocation_due_to_costs():
    """2:Easy:Move a given % of Marketing to Operations; report new budgets."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)
    marketing_budget = float(random.randint(500_000, 3_000_000))
    operations_budget = float(random.randint(1_000_000, 5_000_000))
    reallocation_percentage = round(random.uniform(5, 25), 2)

    reallocated_amount = marketing_budget * (reallocation_percentage / 100.0)
    new_marketing_budget = marketing_budget - reallocated_amount
    new_operations_budget = operations_budget + reallocated_amount

    question = (
        f"{company_name} ({industry}) allocated {_fmt_money(marketing_budget)} to Marketing and "
        f"{_fmt_money(operations_budget)} to Operations for this quarter. Due to cost pressures, "
        f"{_fmt_pct(reallocation_percentage)} of the Marketing budget must be shifted to Operations. "
        f"What are the new Marketing and Operations budgets?"
    )

    solution = (
        "Step 1 (Reallocated amount): "
        f"{_fmt_pct(reallocation_percentage)} × {_fmt_money(marketing_budget)} = {_fmt_money(reallocated_amount)}.\n"
        "Step 2 (New budgets):\n"
        f"  Marketing: {_fmt_money(marketing_budget)} − {_fmt_money(reallocated_amount)} "
        f"= {_fmt_money(new_marketing_budget)}.\n"
        f"  Operations: {_fmt_money(operations_budget)} + {_fmt_money(reallocated_amount)} "
        f"= {_fmt_money(new_operations_budget)}.\n"
        f"Check: {_fmt_money(new_marketing_budget)} + {_fmt_money(new_operations_budget)} "
        f"= {_fmt_money(marketing_budget + operations_budget)} (total unchanged)."
    )

    return question, solution

# ----------------------------
# INTERMEDIATE 1: Budget Adjustment for New Project
# ----------------------------
def template_budget_adjustment_new_project():
    """3:Intermediate:Allocate % to R&D and Marketing; Operations is remainder. Then add an extra amount to R&D taken from Operations."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_budget = float(random.randint(3_000_000, 10_000_000))  # quarterly USD
    r_and_d_percentage = round(random.uniform(15, 30), 2)
    marketing_percentage = round(random.uniform(20, 40), 2)

    # Base allocations
    r_and_d_budget = total_budget * (r_and_d_percentage / 100.0)
    marketing_budget = total_budget * (marketing_percentage / 100.0)
    operations_budget = total_budget - r_and_d_budget - marketing_budget

    # Ensure the additional R&D draw cannot exceed available operations budget
    # Pick additional up to 80% of ops (at least $200k to keep it meaningful if possible)
    max_draw = max(200_000.0, 0.8 * operations_budget)
    additional_r_and_d = float(random.randint(200_000, int(max_draw))) if max_draw >= 200_000 else 0.0

    new_r_and_d_budget = r_and_d_budget + additional_r_and_d
    new_operations_budget = operations_budget - additional_r_and_d

    question = (
        f"{company_name} in the {industry} industry has a quarterly budget of {_fmt_money(total_budget)}. "
        f"It allocates {_fmt_pct(r_and_d_percentage)} to R&D, {_fmt_pct(marketing_percentage)} to Marketing, "
        "and the remainder to Operations. Mid-quarter, an additional allocation to R&D is required for a new project, "
        f"funded by reducing Operations by {_fmt_money(additional_r_and_d)}. What are the new R&D and Operations budgets?"
    )

    solution = (
        "Step 1 (Base allocations):\n"
        f"  R&D = {_fmt_pct(r_and_d_percentage)} × {_fmt_money(total_budget)} = {_fmt_money(r_and_d_budget)}.\n"
        f"  Marketing = {_fmt_pct(marketing_percentage)} × {_fmt_money(total_budget)} = {_fmt_money(marketing_budget)}.\n"
        f"  Operations = Total − R&D − Marketing = {_fmt_money(total_budget)} − {_fmt_money(r_and_d_budget)} − "
        f"{_fmt_money(marketing_budget)} = {_fmt_money(operations_budget)}.\n"
        "Step 2 (Feasibility): The additional R&D draw comes from Operations and does not exceed it.\n"
        f"Step 3 (Adjust):\n"
        f"  New R&D = {_fmt_money(r_and_d_budget)} + {_fmt_money(additional_r_and_d)} = {_fmt_money(new_r_and_d_budget)}.\n"
        f"  New Operations = {_fmt_money(operations_budget)} − {_fmt_money(additional_r_and_d)} = {_fmt_money(new_operations_budget)}.\n"
        "Check: Marketing unchanged; totals still sum to the original budget."
    )

    return question, solution

# ----------------------------
# INTERMEDIATE 2: Budget Cut Reforecast (replaces profit-based template)
# ----------------------------
def template_budget_cut_reforecast():
    """4:Intermediate:Company faces a % cut to the total quarterly budget but keeps the same allocation percentages."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)

    total_budget = float(random.randint(5_000_000, 20_000_000))  # quarterly USD
    r_and_d_percentage = round(random.uniform(10, 25), 2)
    marketing_percentage = round(random.uniform(20, 40), 2)
    cut_percentage = round(random.uniform(5, 20), 2)

    # Base allocations
    base_r_and_d = total_budget * (r_and_d_percentage / 100.0)
    base_marketing = total_budget * (marketing_percentage / 100.0)
    base_operations = total_budget - base_r_and_d - base_marketing

    # After cut
    new_total_budget = total_budget * (1 - cut_percentage / 100.0)
    new_r_and_d = new_total_budget * (r_and_d_percentage / 100.0)
    new_marketing = new_total_budget * (marketing_percentage / 100.0)
    new_operations = new_total_budget - new_r_and_d - new_marketing

    question = (
        f"{company_name}, a {industry} company, has a quarterly budget of {_fmt_money(total_budget)}. "
        f"It allocates {_fmt_pct(r_and_d_percentage)} to R&D, {_fmt_pct(marketing_percentage)} to Marketing, "
        "and the remainder to Operations. A budget cut of "
        f"{_fmt_pct(cut_percentage)} is imposed, while keeping the same allocation percentages. "
        "What are the new budgets for R&D, Marketing, and Operations?"
    )

    solution = (
        "Step 1 (Current allocations):\n"
        f"  R&D = {_fmt_pct(r_and_d_percentage)} × {_fmt_money(total_budget)} = {_fmt_money(base_r_and_d)}.\n"
        f"  Marketing = {_fmt_pct(marketing_percentage)} × {_fmt_money(total_budget)} = {_fmt_money(base_marketing)}.\n"
        f"  Operations = Total − R&D − Marketing = {_fmt_money(base_operations)}.\n"
        "Step 2 (Apply cut to total):\n"
        f"  New Total = {_fmt_money(total_budget)} × (1 − {_fmt_pct(cut_percentage)}) = {_fmt_money(new_total_budget)}.\n"
        "Step 3 (Reapply percentages to new total):\n"
        f"  New R&D = {_fmt_pct(r_and_d_percentage)} × {_fmt_money(new_total_budget)} = {_fmt_money(new_r_and_d)}.\n"
        f"  New Marketing = {_fmt_pct(marketing_percentage)} × {_fmt_money(new_total_budget)} = {_fmt_money(new_marketing)}.\n"
        f"  New Operations = New Total − New R&D − New Marketing = {_fmt_money(new_operations)}.\n"
        "Check: New components sum to the new total."
    )

    return question, solution

# ----------------------------
# ADVANCED: Budget Long-Term Growth (compound over years)
# ----------------------------
def template_budget_long_term_growth():
    """5:Advanced:Quarterly budget is projected to grow with annual compound growth over N years."""
    company_name = random.choice(company_names)
    industry = random.choice(industry_names)
    current_quarterly_budget = float(random.randint(10_000_000, 50_000_000))
    annual_growth_rate = round(random.uniform(5, 15), 2)
    r_and_d_percentage = round(random.uniform(15, 30), 2)
    marketing_percentage = round(random.uniform(20, 40), 2)
    number_of_years = 3  # long-term horizon

    # Compound growth assumption: the quarterly budget scales with revenue at the given annual growth rate.
    future_quarterly_budget = current_quarterly_budget * (1 + annual_growth_rate / 100.0) ** number_of_years

    future_r_and_d_budget = future_quarterly_budget * (r_and_d_percentage / 100.0)
    future_marketing_budget = future_quarterly_budget * (marketing_percentage / 100.0)
    future_operations_budget = future_quarterly_budget - future_r_and_d_budget - future_marketing_budget

    question = (
        f"{company_name} ({industry}) is planning a 3-year horizon. Its current quarterly budget is "
        f"{_fmt_money(current_quarterly_budget)}. Assuming the quarterly budget grows with annual compound growth of "
        f"{_fmt_pct(annual_growth_rate)}, and allocations remain {_fmt_pct(r_and_d_percentage)} to R&D, "
        f"{_fmt_pct(marketing_percentage)} to Marketing, and the remainder to Operations, "
        "what will the **quarterly** budgets for each category be after 3 years?"
    )

    solution = (
        "Step 1 (Quarterly budget after 3 years):\n"
        f"  Future Quarterly Budget = {_fmt_money(current_quarterly_budget)} × "
        f"(1 + {_fmt_pct(annual_growth_rate)})^{number_of_years} = {_fmt_money(future_quarterly_budget)}.\n"
        "Step 2 (Category allocations applied to that future quarterly budget):\n"
        f"  R&D = {_fmt_pct(r_and_d_percentage)} × {_fmt_money(future_quarterly_budget)} = {_fmt_money(future_r_and_d_budget)}.\n"
        f"  Marketing = {_fmt_pct(marketing_percentage)} × {_fmt_money(future_quarterly_budget)} = {_fmt_money(future_marketing_budget)}.\n"
        f"  Operations = Future Quarterly − R&D − Marketing = {_fmt_money(future_operations_budget)}.\n"
        "Check: R&D + Marketing + Operations equals the future quarterly total (up to rounding)."
    )

    return question, solution

def generate_templates(output_file: str, num_instances: int):
    """
    Generate instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_budget_allocation_simple,
        template_budget_reallocation_due_to_costs,
        template_budget_adjustment_new_project,
        template_budget_cut_reforecast,
        template_budget_long_term_growth,
    ]
    
    all_problems = []
    
    for template_func in templates:
        doc_parts = template_func.__doc__.split(':')
        id, level = doc_parts[0], doc_parts[1]
        
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
    parser = argparse.ArgumentParser(description="Generate budget problems.")
    parser.add_argument("--output_file", type=str, default="budget_problems.jsonl", help="Output JSONL file path.")
    parser.add_argument("--num_instances", type=int, default=10, help="Number of instances to generate per template.")
    args = parser.parse_args()
    
    generate_templates(args.output_file, args.num_instances)
