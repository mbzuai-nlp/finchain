import random

company_names = ["Microsoft", "Apple", "NVIDIA", "Amazon", "Alphabet", "Meta Platforms", "Berkshire Hathaway", "Eli Lilly", "Broadcom", "Visa", "JPMorgan Chase", "Tesla", "Walmart", "Mastercard", "UnitedHealth"]


bank_names = ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Goldman Sachs", 
              "Morgan Stanley", "PNC Financial Services", "Capital One"]

def validate_inputs(cost, useful_life, months_used=None, salvage_value=None):
    """

    Validates input parameters for depreciation calculations.

    Scenario: Ensuring that the inputs for asset depreciation calculations meet necessary constraints. 
    The cost and useful life must be positive. If provided, months_used should be between 1 and 12, 
    and salvage_value must be non-negative and less than cost.
    
    Raises:
        ValueError: If any input does not meet the specified requirements.
    """
    if cost <= 0:
        raise ValueError("Cost must be positive")
    if useful_life <= 0:
        raise ValueError("Useful life must be positive")
    if months_used is not None and not (0 < months_used <= 12):
        raise ValueError("Months used must be between 1 and 12")
    if salvage_value is not None and (salvage_value < 0 or salvage_value >= cost):
        raise ValueError("Salvage value must be non-negative and less than cost")

# Template 1 (basic)
def template_depreciation_straight_line():
    """
    1:Basic: Straight-Line Depreciation

    Scenario: A company purchases a machine for a certain cost and uses the straight-line depreciation method
    over a defined useful life with a given salvage value. The goal is to determine the annual depreciation expense.
    
    Returns:
        tuple: (question, solution) where:
            - question (str): A formatted problem statement describing the depreciation scenario.
            - solution (str): Step-by-step solution with calculations.
    """
    company_name = random.choice(company_names)
    cost = random.randint(50000, 100000)
    useful_life = random.randint(5, 15)
    salvage_value = random.randint(5000, 20000)
    
    question = f"""{company_name} purchases a new machine for ${cost}. The estimated useful life of the machine is {useful_life} years,
    and it is expected to have a salvage value of ${salvage_value} at the end of its useful life. {company_name} follows the
    straight-line depreciation method. What is the annual depreciation expense for this machine?
    """.replace("$-", "-$")
    
    step1 = cost - salvage_value
    depreciation_expense = round(step1 / useful_life, 2)
    
    solution = f"""
    Step 1: "Depreciable Amount = (Cost - Salvage Value) / Useful Life"
                                = ({cost} - {salvage_value}) / {useful_life} = {depreciation_expense}
    """.replace("$-", "-$")
    
    return question, solution

# Template 2 (basic)
def template_sum_of_years_digits():
    """
    2:Basic: Sum-of-the-Years-Digits Depreciation

    Scenario: A company applies the sum-of-the-years-digits (SYD) method to depreciate an asset.
    The objective is to determine the depreciation expense for a specific year.
    
    Returns:
        tuple: (question, solution) where:
            - question (str): A formatted problem statement describing the depreciation scenario.
            - solution (str): Step-by-step solution with calculations.
    """
    company_name = random.choice(company_names)
    cost = random.randint(60000, 120000)
    useful_life = random.randint(5, 15)
    year = random.randint(1, useful_life)
    
    question = f"""{company_name} purchases an asset for ${cost} and applies the sum-of-the-years-digits (SYD) depreciation method.
    The asset has a useful life of {useful_life} years. What is the depreciation expense for year {year}?
    """.replace("$-", "-$")
    
    sum_of_years = sum(range(1, useful_life + 1))
    depreciation_factor = round((useful_life - year + 1) / sum_of_years, 2)
    depreciable_amount = cost
    depreciation_expense = round(depreciable_amount * depreciation_factor, 2)
    
    solution = f"""
    Step 1: Depreciation Factor = Remaining Life / Sum of Years
                                = ({useful_life} - {year} + 1) / {sum_of_years} 
                                = {depreciation_factor}
    
    Step 2: Depreciation Expense = Depreciable Amount * Depreciation Factor
                                 = ${depreciable_amount} * {depreciation_factor} 
                                 = ${depreciation_expense}
    """.replace("$-", "-$")
      
    return question, solution


# Template 3 (intermediate)
def template_partial_year_and_disposal_depreciation():
    """
    5:Intermediate: Partial-Year Depreciation and Asset Disposal

    Generates a financial reasoning question and solution related to depreciation when:
    - An asset is acquired during the year (not at beginning)
    - Depreciation for the acquisition year is prorated
    - The asset is sold before the end of its useful life
    - Gain or loss on disposal is calculated

    Returns:
        tuple: (question, solution) where:
            - question (str): The problem statement.
            - solution (str): The step-by-step solution explanation.
    """
    company_name = random.choice(company_names)
    cost = random.randint(50000, 120000)
    useful_life = random.randint(5, 10)
    months_held_in_first_year = random.choice([3, 6, 9])  # Partial year usage
    sale_year = random.randint(2, useful_life - 1)  # Disposed before end of life
    sale_price = round(random.uniform(0.3, 0.8) * cost, 2)

    validate_inputs(cost, useful_life)

    annual_depreciation = round(cost / useful_life, 2)
    partial_year_depreciation = round(annual_depreciation * (months_held_in_first_year / 12), 2)
    full_years = sale_year - 1
    depreciation_full_years = round(full_years * annual_depreciation, 2)
    accumulated_depreciation = round(partial_year_depreciation + depreciation_full_years, 2)
    book_value_at_sale = round(cost - accumulated_depreciation, 2)
    gain_or_loss = round(sale_price - book_value_at_sale, 2)

    question = f"""{company_name} purchases an equipment for ${cost} with an estimated useful life of {useful_life} years.
    The equipment was acquired and placed in service in April, and the company uses straight-line depreciation with full-month convention.
    After {sale_year} years, the asset is sold for ${sale_price}. Compute the gain or loss on disposal, considering partial-year
    depreciation in the year of purchase.
    """.replace("$-", "-$")

    solution = f"""
    Step 1: Compute depreciation for the acquisition year:
            Annual Depreciation = Cost / Useful Life
                                = ${cost} / {useful_life} 
                                = ${annual_depreciation}
            Partial-Year Depreciation = Annual Depreciation × (Months Used / 12)
                                      = ${annual_depreciation} × ({months_held_in_first_year}/12) 
                                      = ${partial_year_depreciation}

    Step 2: Calculate total accumulated depreciation at time of sale:
            Depreciation for {full_years} full years = Annual Depreciation × Number of Full Years
                                                     = ${annual_depreciation} × {full_years} 
                                                     = ${depreciation_full_years}
            Total Accumulated Depreciation = Partial-Year Depreciation + Depreciation for {full_years} full years
                                           = ${partial_year_depreciation} + ${depreciation_full_years} 
                                           = ${accumulated_depreciation}

    Step 3: Compute book value at sale and determine gain/loss:
            Book Value at Sale = ${cost} - ${accumulated_depreciation} 
                               = ${book_value_at_sale}
            Gain/Loss = Sale Price  - Book Value at Sale
                       = ${sale_price} - ${book_value_at_sale}
                       = ${gain_or_loss}
            
    """.replace("$-", "-$")

    if gain_or_loss > 0:
        solution = solution.replace("Gain/Loss", "Gain")
    else:
        solution = solution.replace("Gain/Loss", "Loss")

    return question, solution

def template_impairment_with_value_in_use():
    """
    4:Intermediate: Asset Impairment using Value in Use

    Generates a financial reasoning problem involving asset impairment loss using the 'value-in-use' approach.

    Scenario:
    - A company assesses an asset for impairment.
    - Carrying amount is compared with the *higher* of Net Selling Price and Value in Use.
    - Impairment loss is recorded if Carrying Amount > Recoverable Amount.

    Three Reasoning Steps:
    1. Compute carrying amount of the asset.
    2. Compute recoverable amount as the higher of Net Selling Price and Value in Use.
    3. Compare Carrying Amount and Recoverable Amount and calculate impairment loss.

    Returns:
        tuple: (question, solution)
    """
    company_name = random.choice(company_names)
    cost = random.randint(100000, 180000)
    accumulated_depreciation = random.randint(30000, 80000)
    net_selling_price = random.randint(40000, 90000)
    value_in_use = random.randint(50000, 100000)

    # Ensure valid values
    validate_inputs(cost, 1)
    if accumulated_depreciation >= cost:
        raise ValueError("Invalid: accumulated depreciation exceeds cost.")

    carrying_amount = cost - accumulated_depreciation
    recoverable_amount = max(net_selling_price, value_in_use)
    impairment_loss = max(0, carrying_amount - recoverable_amount)

    question = f"""{company_name} owns an asset originally purchased for ${cost}. The accumulated depreciation so far is ${accumulated_depreciation}, 
    bringing the carrying amount down to ${carrying_amount}. Due to adverse economic conditions, the company assesses the asset for impairment. 
    The Net Selling Price is estimated to be ${net_selling_price}, and the Value in Use is calculated at ${value_in_use}. Determine whether the asset is impaired 
    and, if so, compute the impairment loss.
    """.replace("$-", "-$")

    solution = f"""
    Step 1: Calculate the carrying amount of the asset:
            Carrying Amount = Cost - Accumulated Depreciation
                            = ${cost} - ${accumulated_depreciation} = ${carrying_amount}

    Step 2: Determine the recoverable amount:
            Recoverable Amount = max(Net Selling Price, Value in Use)
                            = max(${net_selling_price}, ${value_in_use}) = ${recoverable_amount}

    Step 3: Compare the carrying amount with the recoverable amount:
            If Carrying Amount > Recoverable Amount → Impairment Loss = Carrying Amount - Recoverable Amount
            Impairment Loss = max(0, ${carrying_amount} - ${recoverable_amount}) = ${impairment_loss}
    """.replace("$-", "-$")

    return question, solution


def template_asset_impairment_reversal():
    """
    5:Advanced: Asset Impairment Loss Reversal

    Generates a financial reasoning question and step-by-step solution related to the reversal of an asset impairment loss.

    Scenario:
    - A company had previously recorded an impairment loss on an asset.
    - Due to improved market conditions, a partial reversal is now recognized.
    - Reversal is limited such that the asset's carrying amount after reversal does not exceed the carrying amount net of depreciation had no impairment occurred (per IFRS).
    
    Returns:
        tuple: (question, solution) where:
            - question (str): The problem scenario.
            - solution (str): A four-step reasoning-based answer.
    """
    company_name = random.choice(company_names)
    original_cost = random.randint(120000, 200000)
    useful_life = random.randint(8, 12)
    years_used = random.randint(3, 6)
    annual_depreciation = round(original_cost / useful_life, 2)
    accumulated_depreciation = round(annual_depreciation * years_used, 2)
    carrying_before_impairment = round(original_cost - accumulated_depreciation, 2)

    # Impairment previously recorded
    impairment_loss = round(carrying_before_impairment * random.uniform(0.2, 0.35), 2)
    impaired_carrying_amount = round(carrying_before_impairment - impairment_loss, 2)

    # Now market recovers
    reversal_amount = round(impairment_loss * random.uniform(0.3, 0.7), 2)
    adjusted_carrying_amount = round(impaired_carrying_amount + reversal_amount, 2)

    # Max allowed post-reversal amount under IFRS
    max_post_reversal = carrying_before_impairment  # can't exceed this

    question = f"""{company_name} purchased an asset for ${original_cost} with a useful life of {useful_life} years. 
    After {years_used} years, the accumulated depreciation amounted to ${accumulated_depreciation}. 
    Due to a market downturn, an impairment loss of ${impairment_loss} was recognized.
    One year later, market conditions improved, and {company_name} determined a reversal of impairment loss amounting to ${reversal_amount}.
    As per IFRS, the carrying amount after reversal should not exceed what it would have been if no impairment had occurred.
    
    Calculate:
    1. The carrying amount before impairment.
    2. The carrying amount after impairment loss.
    3. The adjusted carrying amount after reversal.
    4. Verify whether the reversal complies with IFRS.
    """.replace("$-", "-$")

    solution = f"""
    Step 1: Calculate carrying amount before impairment:
            = Original Cost - Accumulated Depreciation
            = {original_cost} - {accumulated_depreciation} = {carrying_before_impairment}
    
    Step 2: Calculate carrying amount after impairment:
            = Carrying Before Impairment - Impairment Loss
            = {carrying_before_impairment} - {impairment_loss} = {impaired_carrying_amount}

    Step 3: Calculate adjusted carrying amount after reversal:
            = Impaired Carrying Amount + Reversal Amount
            = {impaired_carrying_amount} + {reversal_amount} = {adjusted_carrying_amount}

    Step 4: Verify IFRS condition:
            Adjusted Carrying Amount ≤ Max Allowed (Carrying before impairment)
            {adjusted_carrying_amount} ≤ {max_post_reversal} → Valid: {adjusted_carrying_amount <= max_post_reversal}
    """.replace("$-", "-$")

    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # List of template functions
    templates = [
        template_depreciation_straight_line,
        template_sum_of_years_digits,
        template_partial_year_and_disposal_depreciation,
        template_impairment_with_value_in_use,
        template_asset_impairment_reversal
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
    output_file = "../../testset/accounting_and_financial_reporting/depreciation_and_amortization.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()
