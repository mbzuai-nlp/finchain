import random
from misc import companies, currencies

from decimal import Decimal, ROUND_HALF_UP
import random

def fmt_money(val):
    return f"${val.quantize(Decimal('0.1'), ROUND_HALF_UP)}"

def template_debt_to_equity_aggregate_debt():
    """
    1:Basic: Calculate debt-to-equity ratio given short-term and long-term debt, and equity.
    Capital-structure scenario with two reasoning steps:
      1. Aggregate short-term and long-term debt.
      2. Compute debt-to-equity ratio.
    """
    company, industry = random.choice(companies)
    multiplier = random.choice(["million", "billion"])

    # Generate numbers as Decimals for precise rounding
    st_debt = Decimal(random.randint(50, 50000)) / 100   # short-term debt
    lt_debt = Decimal(random.randint(50, 50000)) / 100   # long-term debt
    equity  = Decimal(random.randint(100, 100000)) / 100

    question = (
        f"{company}, a company in the {industry} sector, reports:\n"
        f"- Short-term debt: {fmt_money(st_debt)} {multiplier}\n"
        f"- Long-term debt: {fmt_money(lt_debt)} {multiplier}\n"
        f"- Shareholders' equity: {fmt_money(equity)} {multiplier}\n\n"
        "Calculate the debt-to-equity ratio (round to two decimal places)."
    )

    total_debt = st_debt + lt_debt
    ratio = (total_debt / equity).quantize(Decimal('0.01'), ROUND_HALF_UP)

    solution = (
        "Step 1: Compute total liabilities (short-term + long-term).\n"
        f"        = {fmt_money(st_debt)} {multiplier} + "
        f"{fmt_money(lt_debt)} {multiplier} = {fmt_money(total_debt)} {multiplier}\n"
        "Step 2: Debt-to-Equity = Total Liabilities ÷ Shareholders’ Equity.\n"
        f"        = {fmt_money(total_debt)} {multiplier} ÷ "
        f"{fmt_money(equity)} {multiplier} = {ratio}"
    )

    return question, solution

def template_debt_to_equity_after_buyback():
    """
    2:Basic: Calculate debt-to-equity ratio after a share buy-back.
    Capital-structure scenario with two reasoning steps:
      1. Adjust equity for a share buy-back.
      2. Compute debt-to-equity ratio using adjusted equity.
    """
    company, industry = random.choice(companies)
    multiplier = random.choice(["million", "billion"])

    debt      = Decimal(random.randint(100, 100000)) / 100  # total liabilities
    equity    = Decimal(random.randint(100, 100000)) / 100  # pre-buy-back equity
    buyback   = Decimal(random.randint(10, 5000)) / 100     # cash used for buy-back

    question = (
        f"{company}, operating in the {industry} sector, announces:\n"
        f"- Total liabilities: {fmt_money(debt)} {multiplier}\n"
        f"- Shareholders' equity (before buy-back): {fmt_money(equity)} {multiplier}\n"
        f"- It repurchased shares for {fmt_money(buyback)} {multiplier} in cash.\n\n"
        "After the buy-back, what is the debt-to-equity ratio (round to two decimal places)?"
    )

    adj_equity = equity - buyback
    ratio = (debt / adj_equity).quantize(Decimal('0.01'), ROUND_HALF_UP)

    solution = (
        "Step 1: Adjust equity for the cash buy-back.\n"
        f"        Adjusted Equity = {fmt_money(equity)} {multiplier} − "
        f"{fmt_money(buyback)} {multiplier} = {fmt_money(adj_equity)} {multiplier}\n"
        "Step 2: Debt-to-Equity = Total Liabilities ÷ Adjusted Equity.\n"
        f"        = {fmt_money(debt)} {multiplier} ÷ "
        f"{fmt_money(adj_equity)} {multiplier} = {ratio}"
    )

    return question, solution


def template_debt_to_equity_after_asset_sale():
    """
    3:Intermediate: Calculate debt-to-equity ratio after selling a non-core asset.
    Three-step reasoning:
      1. Find net sale proceeds.
      2. Reduce total debt by those proceeds.
      3. Compute the debt-to-equity ratio.
    """
    company, industry = random.choice(companies)
    unit = "million"   # keep everything in the same unit

    orig_debt = Decimal(random.randint(500, 50000)) / 100   # $m
    equity    = Decimal(random.randint(500, 80000)) / 100
    sale_price = Decimal(random.randint(100, 10000)) / 100
    trans_cost = Decimal(random.randint(  5,   500)) / 100   # costs of the sale

    question = (
        f"{company}, operating in the {industry} sector, reports:\n"
        f"- Total liabilities: {fmt_money(orig_debt)} {unit}\n"
        f"- Shareholders' equity: {fmt_money(equity)} {unit}\n"
        f"- It sells a non-core asset for {fmt_money(sale_price)} {unit}; "
        f"transaction costs are {fmt_money(trans_cost)} {unit}.\n"
        "All net proceeds are used immediately to repay debt.\n\n"
        "After the sale, what is the debt-to-equity ratio (round to two decimals)?"
    )

    # Step 1 – net proceeds
    net_proceeds = sale_price - trans_cost
    # Step 2 – adjust debt (cannot drop below zero)
    adj_debt = max(orig_debt - net_proceeds, Decimal("0"))
    # Step 3 – ratio
    ratio = (adj_debt / equity).quantize(Decimal('0.01'), ROUND_HALF_UP)

    solution = (
        "Step 1  Net proceeds = Sale price − Transaction costs\n"
        f"        = {fmt_money(sale_price)} − {fmt_money(trans_cost)} "
        f"= {fmt_money(net_proceeds)} {unit}\n"
        "Step 2  Adjusted Debt = max(Original Debt − Net proceeds, 0)\n"
        f"        = max({fmt_money(orig_debt)} − {fmt_money(net_proceeds)}, 0) "
        f"= {fmt_money(adj_debt)} {unit}\n"
        "Step 3  Debt-to-Equity = Adjusted Debt ÷ Equity\n"
        f"        = {fmt_money(adj_debt)} ÷ {fmt_money(equity)} "
        f"= {ratio}"
    )

    return question, solution

def template_debt_to_equity_bond_and_buyback():
    """
    4:Intermediate: Calculate debt-to-equity ratio after issuing new bonds and a share buy-back.
    Three-step reasoning:
      1. Add new bond issue to total debt.
      2. Subtract buy-back cash from equity.
      3. Compute the debt-to-equity ratio.
    """
    company, industry = random.choice(companies)
    unit = "million"

    debt      = Decimal(random.randint(800, 100000)) / 100   # $m
    equity    = Decimal(random.randint(800, 120000)) / 100
    new_bond  = Decimal(random.randint( 50,  30000)) / 100   # $m
    buy_back  = Decimal(random.randint( 20,  20000)) / 100   # $m

    question = (
        f"{company}, active in the {industry} sector, reports:\n"
        f"- Existing liabilities: {fmt_money(debt)} {unit}\n"
        f"- Shareholders' equity: {fmt_money(equity)} {unit}\n"
        f"- It will issue new bonds worth {fmt_money(new_bond)} {unit}.\n"
        f"- It will repurchase shares for {fmt_money(buy_back)} {unit} in cash.\n\n"
        "After completing both transactions, calculate the debt-to-equity ratio "
        "(round to two decimals)."
    )

    # Step 1 – adjust debt
    new_debt = debt + new_bond
    # Step 2 – adjust equity
    new_equity = equity - buy_back
    # Step 3 – ratio
    ratio = (new_debt / new_equity).quantize(Decimal('0.01'), ROUND_HALF_UP)

    solution = (
        "Step 1  Adjusted Debt = Existing Debt + New Bond Issue\n"
        f"        = {fmt_money(debt)} + {fmt_money(new_bond)} "
        f"= {fmt_money(new_debt)} {unit}\n"
        "Step 2  Adjusted Equity = Existing Equity − Share Buy-Back\n"
        f"        = {fmt_money(equity)} − {fmt_money(buy_back)} "
        f"= {fmt_money(new_equity)} {unit}\n"
        "Step 3  Debt-to-Equity = Adjusted Debt ÷ Adjusted Equity\n"
        f"        = {fmt_money(new_debt)} ÷ {fmt_money(new_equity)} "
        f"= {ratio}"
    )

    return question, solution


def template_debt_to_equity_bond_repay_buyback():
    """
    5:Advanced: Calculate debt-to-equity ratio after issuing bonds, repaying debt, and a share buy-back.
    Four-step reasoning:
      1. Add bond issue to debt.
      2. Subtract repayment from debt.
      3. Subtract buy-back from equity.
      4. Compute debt-to-equity ratio.
    """
    company, industry = random.choice(companies)
    unit = "million"

    orig_debt   = Decimal(random.randint(800, 120000)) / 100   # $m
    orig_equity = Decimal(random.randint(800, 120000)) / 100
    new_bond    = Decimal(random.randint(50, 30000))  / 100
    repayment   = Decimal(random.randint(20, 20000))  / 100
    buyback     = Decimal(random.randint(20, 15000))  / 100

    question = (
        f"{company}, active in the {industry} sector, reports:\n"
        f"- Existing liabilities: {fmt_money(orig_debt)} {unit}\n"
        f"- Shareholders' equity: {fmt_money(orig_equity)} {unit}\n"
        f"- It will issue new bonds worth {fmt_money(new_bond)} {unit}.\n"
        f"- It will repay {fmt_money(repayment)} {unit} of existing debt.\n"
        f"- It plans a share buy-back costing {fmt_money(buyback)} {unit}.\n\n"
        "After all three actions, calculate the debt-to-equity ratio (round to two decimals)."
    )

    # Step 1 – add bond issue
    debt_step1 = orig_debt + new_bond
    # Step 2 – subtract repayment
    debt_step2 = debt_step1 - repayment
    # Step 3 – adjust equity for buy-back
    equity_adj = orig_equity - buyback
    # Step 4 – ratio
    ratio = (debt_step2 / equity_adj).quantize(Decimal('0.01'), ROUND_HALF_UP)

    solution = (
        "Step 1  Adjust debt for the new bond issue:\n"
        f"        {fmt_money(orig_debt)} + {fmt_money(new_bond)} = {fmt_money(debt_step1)} {unit}\n"
        "Step 2  Subtract the scheduled debt repayment:\n"
        f"        {fmt_money(debt_step1)} − {fmt_money(repayment)} = {fmt_money(debt_step2)} {unit}\n"
        "Step 3  Adjust equity for the share buy-back:\n"
        f"        {fmt_money(orig_equity)} − {fmt_money(buyback)} = {fmt_money(equity_adj)} {unit}\n"
        "Step 4  Debt-to-Equity = Adjusted Debt ÷ Adjusted Equity\n"
        f"        = {fmt_money(debt_step2)} ÷ {fmt_money(equity_adj)} = {ratio}"
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
        template_debt_to_equity_aggregate_debt,
        template_debt_to_equity_after_buyback,
        template_debt_to_equity_after_asset_sale,
        template_debt_to_equity_bond_and_buyback,
        template_debt_to_equity_bond_repay_buyback,
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
    output_file = "../../testset/corporate_finance/capital_structure.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
