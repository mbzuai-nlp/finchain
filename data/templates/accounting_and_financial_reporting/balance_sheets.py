import random

company_names = ["Microsoft", "Apple", "NVIDIA", "Amazon", "Alphabet", "Meta Platforms", "Berkshire Hathaway", "Eli Lilly", "Broadcom", "Visa", "JPMorgan Chase", "Tesla", "Walmart", "Mastercard", "UnitedHealth"]


bank_names = ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Goldman Sachs", 
              "Morgan Stanley", "PNC Financial Services", "Capital One"]

# Template 1 (basic)
def template_cash_accounts_payable():
    """
    1:Basic: Cash and Accounts Payable

    Scenario:
        A company needs to assess its net cash position after settling its accounts payable.
        Given the company's available cash and outstanding accounts payable, the goal is 
        to compute the net cash position using:

            Net Cash Position = Cash - Accounts Payable

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the net cash position after paying off accounts payable.
            - str: A step-by-step solution explaining the calculation.
    """
    company_name = random.choice(company_names)
    cash = random.randint(5000, 20000)
    accounts_payable = random.randint(2000, 10000)
    net_cash = cash - accounts_payable

    question = (
        f"{company_name} has ${cash} in cash and ${accounts_payable} in accounts payable. Calculate the net cash position "
        f"of the company after paying off all its accounts payable."
    ).replace("$-", "-$")

    solution = (
        f"Step 1. Net Cash Position = Cash - Accounts Payable\n"
        f"                          = ${cash} - ${accounts_payable} = ${net_cash}"
    ).replace("$-", "-$")

    return question, solution

# Template 2 (basic)
def template_balance_sheet_equation():
    """
    2:Basic: Balance Sheet Equation

    Scenario:
        A company's financial position is assessed using the balance sheet equation.
        Given the company's assets and liabilities, the goal is to compute the equity 
        using the fundamental accounting equation: 

            Equity = Assets - Liabilities

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the company's equity.
            - str: A step-by-step solution explaining the calculation.
    """
    company_name = random.choice(company_names)
    assets = random.randint(10000, 50000)
    liabilities = random.randint(5000, 30000)
    equity = assets - liabilities

    question = (
        f"{company_name} has ${assets} in assets and ${liabilities} in liabilities. Using the balance sheet equation, "
        f"calculate the company's equity."
    ).replace("$-", "-$")

    solution = (
        f"Step 1. Equity = Assets - Liabilities\n"
        f"               = ${assets} - ${liabilities} = ${equity}"
    ).replace("$-", "-$")

    return question, solution


# Template 6 (intermediate)
def template_inventory_turnover_days():
    """
    3:Intermediate: Inventory Turnover Days

    Scenario: A company's Inventory Turnover Days measures how quickly it sells and 
        replaces its inventory over a period (usually a year). 
        It reflects how many days, on average, items remain in stock before being sold.
        This metric is especially useful in:
            - Assessing operational efficiency
            - Managing working capital
            - Identifying slow-moving or overstocked inventory

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the inventory turnover days.
            - str: A step-by-step solution explaining the calculation.
    """
    company_name = random.choice(company_names)
    opening_inventory = random.randint(10000, 20000)
    purchases = random.randint(20000, 40000)
    closing_inventory = random.randint(10000, 25000)

    average_inventory = round((opening_inventory + closing_inventory) / 2, 2)
    cogs = opening_inventory + purchases - closing_inventory
    turnover_ratio = round(cogs / average_inventory, 2)
    turnover_days = round(365 / turnover_ratio, 2)

    question = (
        f"{company_name} had an opening inventory of ${opening_inventory} and made purchases worth ${purchases} during the year. "
        f"The closing inventory at year-end was ${closing_inventory}. Using this information, calculate the **Inventory Turnover Days**?"
    ).replace("$-", "-$")

    solution = (
        f"Step 1: COGS = Opening Inventory + Purchases - Closing Inventory\n"
        f"             = ${opening_inventory} + ${purchases} - ${closing_inventory} = ${cogs}\n\n"

        f"Step 2: Average Inventory = (Opening Inventory + Closing Inventory) / 2\n"
        f"                          = (${opening_inventory} + ${closing_inventory}) / 2 = ${average_inventory}\n\n"

        f"Step 3: Inventory Turnover Ratio = COGS / Average Inventory = ${cogs} / ${average_inventory} = {turnover_ratio}\n"
        f"        Inventory Turnover Days = 365 / Inventory Turnover Ratio = 365 / {turnover_ratio} = {turnover_days} days\n\n"
    ).replace("$-", "-$")

    return question, solution

# Template 7 (intermediate)
def template_current_ratio_with_adjustment():
    """
    4:Intermediate: Adjusted Current Ratio Calculation with Logical Dependency
    
    Scenario:
    A company's liquidity is assessed using the current ratio:
        Current Ratio = Current Assets / Current Liabilities

    However, accounting standards require that any portion of a long-term liability 
    that becomes due within the next 12 months must be reclassified as a current liability. 
    This affects the company's liquidity position.

    This problem tests conceptual understanding of liquidity metrics and the effect of reclassification 
    on financial ratios.

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the change in current ratio after an adjustment.
            - str: A step-by-step solution explaining the calculation.
    """

    company_name = random.choice(company_names)
    
    current_assets = random.randint(80000, 150000)
    current_liabilities = random.randint(30000, 70000)
    long_term_loan = random.randint(20000, 50000)
    reclassified_amount = random.choice([5000, 10000, 15000])  # reclassified to current

    # Step 1
    initial_ratio = round(current_assets / current_liabilities, 2)

    # Step 2
    adjusted_liabilities = current_liabilities + reclassified_amount

    # Step 3
    adjusted_ratio = round(current_assets / adjusted_liabilities, 2)
    ratio_change = round(initial_ratio - adjusted_ratio, 2)

    question = (
        f"{company_name} has current assets of ${current_assets} and current liabilities of ${current_liabilities}. "
        f"It also holds a long-term loan of ${long_term_loan}, out of which ${reclassified_amount} becomes due within the next year "
        f"and must be reclassified as a current liability. \n\n"
        f"Determine the **change** in the current ratio."
    ).replace("$-", "-$")

    solution = (
        f"Step 1: Original Current Ratio:\n"
        f"        = Current Assets / Current Liabilities\n"
        f"        = ${current_assets} / ${current_liabilities} = {initial_ratio}\n\n"

        f"Step 2: Adjusted Current Liabilities = ${current_liabilities} + ${reclassified_amount} = ${adjusted_liabilities}\n\n"

        f"Step 3: Adjusted Ratio = ${current_assets} / ${adjusted_liabilities} = {adjusted_ratio}\n"
        f"        Change in ratio = {initial_ratio:.2f} - {adjusted_ratio:.2f} = {ratio_change}\n\n"
    ).replace("$-", "-$")

    return question, solution



# Template 15 (advanced)
def template_business_combination():
    """
    5:Advanced: Business Combination Goodwill Computation
    
    Scenario: This template models a business combination where Company A acquires Company B. 
    The acquisition involves paying cash and issuing shares as purchase consideration. 
    Company B's identifiable assets and liabilities are valued at their fair values. 
    The task is to calculate the goodwill arising from this acquisition, 
    which represents the excess of the purchase consideration over the net identifiable assets acquired.

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the goodwill arising from an acquisition.
            - str: A step-by-step solution explaining the calculation.
    """

    company_a, company_b = random.sample(company_names, 2)

    # Step 1 inputs
    cash_paid = random.randint(200000, 600000)
    shares_issued = random.randint(1000, 5000)
    share_price = random.randint(100, 200)
    total_consideration = cash_paid + (shares_issued * share_price)

    # Step 2 inputs
    land = random.randint(150000, 300000)
    inventory = random.randint(80000, 150000)
    patents = random.randint(60_000, 120000)
    total_assets = land + inventory + patents

    # Step 3 inputs
    borrowings = random.randint(50000, 120000)
    payables = random.randint(30000, 90000)
    total_liabilities = borrowings + payables

    # Step 4
    net_assets = total_assets - total_liabilities

    # Step 5
    goodwill = total_consideration - net_assets

    question = (
        f"{company_a} has acquired {company_b} in a business combination. To finance the acquisition, "
        f"{company_a} paid ${cash_paid} in cash and issued {shares_issued} shares valued at ${share_price} each. "
        f"The fair values of {company_b}'s identifiable assets include land worth ${land}, inventory worth ${inventory}, "
        f"and patents valued at ${patents}. The assumed liabilities include borrowings of ${borrowings} and trade payables of ${payables}. "
        f"Based on this information, compute the **goodwill** arising on the acquisition."
    ).replace("$-", "-$")

    solution = (
        f"Step 1: Total Consideration = Cash Paid + (Shares Issued × Share Price)\n"
        f"                            = ${cash_paid} + ({shares_issued} × ${share_price}) = ${total_consideration}\n\n"

        f"Step 2: Total Identifiable Assets = Land + Inventory + Patents\n"
        f"                                  = ${land} + ${inventory} + ${patents} = ${total_assets}\n\n"

        f"Step 3: Total Liabilities = Borrowings + Payables\n"
        f"                          = ${borrowings} + ${payables} = ${total_liabilities}\n\n"

        f"Step 4: Net Identifiable Assets = Total Assets - Total Liabilities\n"
        f"                                = ${total_assets} - ${total_liabilities} = ${net_assets}\n\n"

        f"Step 5: Goodwill = Total Consideration - Net Identifiable Assets\n"
        f"                 = ${total_consideration} - ${net_assets} = ${goodwill}\n\n"
    ).replace("$-", "-$")

    return question, solution



def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # List of template functions
    templates = [
        template_cash_accounts_payable,
        template_balance_sheet_equation,
        template_inventory_turnover_days,
        template_current_ratio_with_adjustment,
        template_business_combination
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
    output_file = "../../testset/accounting_and_financial_reporting/balance_sheets.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()