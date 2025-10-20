import random


company_names = ["Microsoft", "Apple", "NVIDIA", "Amazon", "Alphabet", "Meta Platforms", "Berkshire Hathaway", "Eli Lilly", "Broadcom", "Visa", "JPMorgan Chase", "Tesla", "Walmart", "Mastercard", "UnitedHealth"]

bank_names = ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Goldman Sachs", 
              "Morgan Stanley", "PNC Financial Services", "Capital One"]

def generate_random_value(low, high):
    return random.randint(low, high)


def validate_financials(revenue, cogs, operating_expenses=0, depreciation=0):
    """
    Validates basic financial metrics to ensure they make business sense.
    
    Parameters:
        revenue (float): Total revenue, must be positive.
        cogs (float): Cost of Goods Sold (COGS), cannot be negative and must not exceed revenue.
        operating_expenses (float, optional): Operating expenses, default is 0, cannot be negative.
        depreciation (float, optional): Depreciation expense, default is 0, cannot be negative.
    
    Raises:
        ValueError: If any of the financial constraints are violated.
    """

    if revenue <= 0:
        raise ValueError("Revenue must be positive")
    if cogs < 0:
        raise ValueError("COGS cannot be negative")
    if operating_expenses < 0:
        raise ValueError("Operating expenses cannot be negative")
    if depreciation < 0:
        raise ValueError("Depreciation cannot be negative")
    if cogs > revenue:
        raise ValueError("COGS cannot exceed revenue")
    if (cogs + operating_expenses + depreciation) > revenue:
        raise ValueError("Total costs cannot exceed revenue")
    
# Template 1 (basic)
def template_revenue_vs_cogs():
    """
    1:Basic: Revenue and Cost of Goods Sold (COGS)
    
    Scenario:
        A company wants to determine its Gross Profit by subtracting its Cost of Goods Sold (COGS) from its total revenue.
    
    Returns:
        tuple: (question, solution)
            - question is a formatted financial scenario,
            - solution provides a step-by-step breakdown of the answer.
    """
    company_name = random.choice(company_names)
    revenue = random.randint(50000, 100000)
    cogs = random.randint(10000, 50000)
    gross_profit = revenue - cogs
    question = f"{company_name} has a total revenue of ${revenue} and its Cost of Goods Sold (COGS) is ${cogs}. What is its Gross Profit?".replace("$-", "-$")
    solution = (
        f"Step-1: Use the formula for Gross Profit:\n"
        f"  Gross Profit = Revenue - COGS\n"
        f"               = ${revenue} - ${cogs} = ${gross_profit}"
    ).replace("$-", "-$")
    
    return question, solution

# Template 2 (basic)
def template_operating_expenses_effect():
    """
    2:Basic: Operating Expenses Effect
    
    Scenario:
        A company wants to determine its Operating Profit by deducting Operating Expenses from its Gross Profit.
    
    Returns:
        tuple: (question, solution)
            - question is a formatted financial scenario,
            - solution provides a step-by-step breakdown of the answer.
    """
    company_name = random.choice(company_names)
    gross_profit = random.randint(40000, 80000)
    operating_expenses = random.randint(10000, 30000)
    operating_profit = gross_profit - operating_expenses
    question = (f"{company_name}'s Gross Profit is ${gross_profit}, and its Operating Expenses amount to "
                f"${operating_expenses}. What is its Operating Profit?").replace("$-", "-$")
    solution = (
        f"Step-1: Use the formula for Operating Profit:\n"
        f"  Operating Profit = Gross Profit - Operating Expenses\n"
        f"                   = ${gross_profit} - ${operating_expenses} = ${operating_profit}"
    ).replace("$-", "-$")

    return question, solution

# Template 3 (intermediate)
def template_depreciation_ddb():
    """
    3:Intermediate: Depreciation - Double Declining Balance Method

    Scenario:
        A company purchases an asset and depreciates it using the DDB method over its useful life.
        The question asks for the book value at the end of the second year.

    Returns:
        tuple: (question, solution)
            - question (str): The problem statement
            - solution (str): Step-by-step explanation of the answer
    """
    try:
        company_name = random.choice(company_names)
        asset_cost = generate_random_value(50000, 150000)
        useful_life = random.choice([5, 6, 7, 8])
        depreciation_rate = round((2 / useful_life), 2)

        # First year depreciation
        year1_depreciation = round(asset_cost * depreciation_rate, 2)
        year1_book_value = round(asset_cost - year1_depreciation, 2)

        # Second year depreciation
        year2_depreciation = round(year1_book_value * depreciation_rate, 2)
        year2_book_value = round(year1_book_value - year2_depreciation, 2)

        question = (
            f"{company_name} purchased a machine for ${asset_cost}. The machine has an estimated useful life of {useful_life} years. "
            f"The company applies the Double Declining Balance method for depreciation. Calculate the book value at the end of the second year."
        ).replace("$-", "-$")

        solution = (
            f"Step 1: Determine the annual depreciation rate using DDB:\n"
            f"        Depreciation Rate = 2 / Useful Life\n"
            f"                          = 2 / {useful_life}\n" 
            f"                          = {depreciation_rate}\n\n"
            f"Step 2: Compute depreciation and book value for Year 1:\n"
            f"        Year 1 Depreciation = ${asset_cost} × {depreciation_rate} = ${year1_depreciation}\n"
            f"        Year 1 Book Value = ${asset_cost} - ${year1_depreciation} = ${year1_book_value}\n\n"
            f"Step 3: Compute depreciation and book value for Year 2:\n"
            f"        Year 2 Depreciation = ${year1_book_value} × {depreciation_rate} = ${year2_depreciation}\n"
            f"        Year 2 Book Value = ${year1_book_value} - ${year2_depreciation} = ${year2_book_value}"
        ).replace("$-", "-$")

        return question, solution

    except ValueError as e:
        return f"Error generating question: {str(e)}", None

# Template 4 (intermediate)
def template_inventory_turnover():
    """
    4:Intermediate: Inventory Turnover Analysis

    Scenario:
        A company is evaluating how efficiently it manages its inventory by analyzing turnover and sales cycle speed.

    Returns:
        tuple: (question, solution)
            - question is a formatted inventory efficiency scenario,
            - solution includes a clear 3-step reasoning.
    """
    try:
        # Sample data generation
        company_name = random.choice(company_names)
        cogs = generate_random_value(250000, 900000)
        opening_inventory = generate_random_value(40000, 100000)
        closing_inventory = generate_random_value(40000, 100000)
        days_in_year = 365

        # Ensure average inventory is valid
        average_inventory = round((opening_inventory + closing_inventory) / 2, 2)
        if average_inventory <= 0:
            raise ValueError("Average inventory must be greater than zero")

        # Inventory turnover and days to sell
        inventory_turnover_ratio = round(cogs / average_inventory, 2)
        days_to_sell = round(days_in_year / inventory_turnover_ratio, 2)

        question = (
            f"{company_name} reported a Cost of Goods Sold (COGS) of ${cogs}. "
            f"The inventory at the beginning of the year was ${opening_inventory} and at the end of the year was ${closing_inventory}. "
            f"Determine how many days, on average, it takes to sell the inventory."
        ).replace("$-", "-$")

        solution = (
            f"Step 1: Compute the Average Inventory.\n"
            f"        Average Inventory = (Opening Inventory + Closing Inventory) / 2\n"
            f"                          = (${opening_inventory} + ${closing_inventory}) / 2 = ${average_inventory}\n\n"
            f"Step 2: Compute the Inventory Turnover Ratio.\n"
            f"        Inventory Turnover Ratio = COGS / Average Inventory\n"
            f"                                 = ${cogs} / ${average_inventory} = {inventory_turnover_ratio}\n\n"
            f"Step 3: Compute Average Days to Sell Inventory.\n"
            f"        Days to Sell = 365 / Inventory Turnover Ratio\n"
            f"                     = {days_in_year} / {inventory_turnover_ratio} = {days_to_sell} days"
        ).replace("$-", "-$")

        return question, solution

    except ValueError as e:
        return f"Error: {str(e)}", None

# Template 3 (advanced)
def template_advanced_dta_warranty_expense():
    """
    6:Advanced: Deferred Tax Asset from Temporary Difference in Warranty Expense (with 4 meaningful reasoning steps)

    Scenario:
        A company accrues warranty expenses under financial reporting rules, but tax rules only allow deduction when actually paid.
        This creates a deductible temporary difference that results in a Deferred Tax Asset (DTA).

    Returns:
        tuple: (question, solution) where:
            - question poses a single advanced financial accounting question (DTA),
            - solution includes 4 reasoning steps, each with substantive financial calculations.
    """
    try:
        company_name = random.choice(company_names)
        reported_expense = generate_random_value(90000, 140000)  # For financial books
        tax_deductible_now = generate_random_value(30000, reported_expense - 10000)
        tax_rate = random.randint(25, 35)

        # Step 1: Identify temporary difference
        temp_difference = reported_expense - tax_deductible_now
        # Step 2: Compute Deferred Tax Asset (DTA)
        dta = round(temp_difference * (tax_rate / 100), 2)

        question = (
            f"{company_name} reported a warranty expense of ${reported_expense} in its financial statements "
            f"under accrual accounting. However, only ${tax_deductible_now} of that is deductible for tax purposes in the current year. "
            f"The applicable tax rate is {tax_rate}%. What is the resulting Deferred Tax Asset (DTA) from this temporary difference?"
        ).replace("$-", "-$")

        solution = (
            f"Step 1: Determine the portion of warranty expense not deductible in the current tax year.\n"
            f"        Temporary Difference = Reported Expense - Tax Deductible Now\n"
            f"                            = ${reported_expense} - ${tax_deductible_now} = ${temp_difference}\n\n"

            f"Step 2: Apply the tax rate to the temporary difference to compute the Deferred Tax Asset.\n"
            f"        DTA = Temporary Difference × Tax Rate\n"
            f"            = ${temp_difference} × ({tax_rate}/100)\n\n"

            f"Step 3: Perform the calculation.\n"
            f"        DTA = ${dta}\n\n"

            f"Step 4: Conclusion\n"
            f"        The Deferred Tax Asset arising from the temporary difference in warranty expense is ${dta}."
        ).replace("$-", "-$")

        return question, solution

    except ValueError as e:
        return f"Error generating question: {str(e)}", None

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # List of template functions
    templates = [
        template_revenue_vs_cogs,
        template_operating_expenses_effect,
        template_depreciation_ddb,
        template_inventory_turnover,
        template_advanced_dta_warranty_expense
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
    output_file = "../../testset/accounting_and_financial_reporting/income_statements.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()
