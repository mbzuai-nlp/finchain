import random

company_names = ["Microsoft", "Apple", "NVIDIA", "Amazon", "Alphabet", "Meta Platforms", "Berkshire Hathaway", "Eli Lilly", "Broadcom", "Visa", "JPMorgan Chase", "Tesla", "Walmart", "Mastercard", "UnitedHealth"]


bank_names = ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Goldman Sachs", 
              "Morgan Stanley", "PNC Financial Services", "Capital One"]


# Template 1 (basic)
def template_calculate_closing_cash_balance():
    """
    1:Basic: Closing Cash Balance

    Scenario:
        A company evaluates its closing cash balance at the end of a month based on different 
        sources of cash inflows and outflows. The calculation follows:

            Closing Cash Balance = Opening Balance + (Net Operating Cash - Net Investing Cash + Net Financing Cash)

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the closing cash balance.
            - str: A step-by-step solution explaining the calculation.
    """

    # Inputs
    company_name = random.choice(company_names)
    opening_balance = random.randint(20000, 40000)
    net_operating_cash = random.randint(30000, 60000)
    net_investing_cash = random.randint(-10000, 15000)
    net_financing_cash = random.randint(-5000, 10000)

    # Calculations
    total_net_cash_flow = net_operating_cash + net_investing_cash + net_financing_cash
    closing_balance = opening_balance + total_net_cash_flow

    question = (
        f"{company_name} starts the month with a cash balance of ${opening_balance}. It has a net cash inflow of ${net_operating_cash} from "
        f"operating activities, a net cash outflow of ${net_investing_cash} from investing activities, and a net cash inflow of ${net_financing_cash} "
        f"from financing activities. Calculate the closing cash balance for the company."
    ).replace("$-", "-$")

    solution = f"""
    Step 1. Total Net Cash Flow = Net Operating Cash + Net Investing Cash + Net Financing Cash
                                = ${net_operating_cash} + ${net_investing_cash} + ${net_financing_cash} = ${total_net_cash_flow}
    Step 2. Closing Cash Balance = Opening Balance + Total Net Cash Flow
                                 = ${opening_balance} + ${total_net_cash_flow} = ${closing_balance}
    """.replace("$-", "-$")

    return question, solution

def template_calculate_tax_cash_outflow():
    """
    2:Basic: Tax Cash Outflow

    Scenario:
        A company calculates the actual cash outflow for taxes based on its income tax expense 
        and the changes in taxes payable throughout the year. The calculation follows:

            Tax Cash Outflow = Tax Expense - (Closing Taxes Payable - Opening Taxes Payable)

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the tax cash outflow.
            - str: A step-by-step solution explaining the calculation.
    """

    # Inputs
    company_name = random.choice(company_names)
    tax_expense = 25000
    opening_taxes_payable = random.randint(5000, 10000)
    closing_taxes_payable = random.randint(8000, min(16000, opening_taxes_payable + tax_expense))

    # Calculations
    change_in_taxes_payable = closing_taxes_payable - opening_taxes_payable
    tax_cash_outflow = tax_expense - change_in_taxes_payable

    question = (
        f"{company_name} reports an income tax expense of ${tax_expense}. At the beginning of the year, the company "
        f"had ${opening_taxes_payable} in taxes payable, and at the end of the year, taxes payable increased to ${closing_taxes_payable}. Calculate the cash "
        f"outflow for taxes."
    ).replace("$-", "-$")

    solution = f"""
    Step 1. Change in Taxes Payable = Closing Taxes Payable - Opening Taxes Payable
                                    = ${closing_taxes_payable} - ${opening_taxes_payable} 
                                    = ${change_in_taxes_payable}
    Step 2. Tax Cash Outflow = Tax Expense - Change in Taxes Payable
                             = ${tax_expense} - ${change_in_taxes_payable} 
                             = ${tax_cash_outflow}
    """.replace("$-", "-$")

    return question, solution

def template_indirect_cash_flow_operations_advanced():
    """
    3:Intermediate: Indirect Method – Cash Flow from Operating Activities with Amortization

    Scenario:
        A company prepares its cash flow statement using the indirect method.
        It reports net income, depreciation, amortization, and changes in working capital components:
        - increase in accounts receivable,
        - increase in inventory,
        - decrease in accounts payable,
        - and increase in accrued expenses.

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the cash flow from operating activities using the indirect method.
            - str: A step-by-step solution with three logically independent steps.
    """
    # Inputs
    company_name = random.choice(company_names)
    net_income = random.randint(80000, 150000)
    depreciation = random.randint(10000, 25000)
    amortization = random.randint(5000, 20000)
    increase_receivable = random.randint(10000, 30000)
    increase_inventory = random.randint(10000, 25000)
    decrease_payable = random.randint(5000, 15000)
    increase_accrued_expenses = random.randint(5000, 12000)

    # Calculations
    adjusted_net_income = net_income + depreciation + amortization
    net_wc_change = (
        -increase_receivable
        - increase_inventory
        - decrease_payable
        + increase_accrued_expenses
    )
    cash_flow_operations = adjusted_net_income + net_wc_change

    # Question
    question = (
        f"{company_name} reported a net income of ${net_income}. During the same period, it incurred depreciation of ${depreciation}, "
        f"amortization of ${amortization}, an increase in accounts receivable of ${increase_receivable}, "
        f"an increase in inventory of ${increase_inventory}, a decrease in accounts payable of ${decrease_payable}, "
        f"and an increase in accrued expenses of ${increase_accrued_expenses}. "
        f"Compute the cash flow from operating activities using the indirect method."
    ).replace("$-", "-$")

    # Solution
    solution = f"""
    Step 1. Adjusted Net Income = Net Income + Depreciation + Amortization
                                = ${net_income} + ${depreciation} + ${amortization}
                                = ${adjusted_net_income}

    Step 2. Net Working Capital Change = -Increase in Accounts Receivable - Increase in Inventory
                                        - Decrease in Accounts Payable + Increase in Accrued Expenses
                                    = -${increase_receivable} - ${increase_inventory} - ${decrease_payable} + ${increase_accrued_expenses}
                                    = ${net_wc_change}

    Step 3. Cash Flow from Operating Activities = Adjusted Net Income + Net Working Capital Change
                                                = ${adjusted_net_income} + ${net_wc_change}
                                                = ${cash_flow_operations}
    """.replace("$-", "-$")

    return question, solution


# Template 4 (intermediate)
def template_calculate_cash_flow_from_financing_activities():
    """
    4:Intermediate: Cash Flow from Financing Activities

    Scenario:
        A company calculates its net cash flow from financing activities by summing up the inflows from 
        issuing equity and debt and subtracting the outflows from debt repayments and dividend payments. 
        The calculation follows:

            Net Cash Flow from Financing Activities = (Equity Issuance + Debt Issuance) - (Debt Repayment + Dividends Paid)

    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the net cash flow from financing activities.
            - str: A step-by-step solution explaining the calculation.
    """

    # Inputs
    company_name = random.choice(company_names)
    equity_issuance = random.randint(50000, 500000)
    debt_issuance = random.randint(100000, 700000)
    debt_repayment = random.randint(50000, 400000)
    dividends_paid = random.randint(20000, 150000)

    # Calculations
    net_cash_flow_financing = (equity_issuance + debt_issuance) - (debt_repayment + dividends_paid)

    question = (
        f"{company_name} issued new equity worth ${equity_issuance}, raised ${debt_issuance} from long-term debt, "
        f"repaid ${debt_repayment} in existing loans, and paid ${dividends_paid} in dividends. Compute the net "
        f"cash flow from financing activities."
    ).replace("$-", "-$")

    solution = f"""
    Step 1. Compute total cash inflows from financing activities:
            Total Inflows = Equity Issuance + Debt Issuance
                          = {equity_issuance} + {debt_issuance} = {equity_issuance + debt_issuance}
    Step 2. Compute total cash outflows from financing activities:
            Total Outflows = Debt Repayment + Dividends Paid
                           = {debt_repayment} + {dividends_paid} = {debt_repayment + dividends_paid}
    Step 3. Compute net cash flow from financing activities:
            Net Cash Flow = Total Inflows - Total Outflows
                          = ({equity_issuance + debt_issuance}) - ({debt_repayment + dividends_paid}) = {net_cash_flow_financing}
    """.replace("$-", "-$")

    return question, solution


# Template 5 (advanced)
def template_calculate_cash_flow_impact_of_acquisition():
    """
    5:Advanced: Cash Flow Impact of Acquisition

    Scenario:
        A company is acquiring another firm and needs to evaluate the impact on its cash flow over a four-year period.
        The calculation considers the acquisition cost, expected annual synergies, and integration costs.
        
        Formula:
            Total Synergies = Synergy1 + Synergy2 + Synergy3 + Synergy4
            Total Integration Costs = Integration Cost1 + Integration Cost2
            Net Cash Flow Impact = Total Synergies - Acquisition Cost - Total Integration Costs
        
    Returns:
        tuple: A tuple containing:
            - str: A question asking to compute the net cash flow impact of the acquisition.
            - str: A step-by-step solution explaining the calculation.
    """

    # Inputs
    company_name = random.choice(company_names)
    acquisition_cost = random.randint(500000, 2000000)
    synergies1, synergies2, synergies3, synergies4 = [random.randint(50000, 200000) for _ in range(4)]
    integration_cost1, integration_cost2 = [random.randint(20000, 100000) for _ in range(2)]

    # Calculations
    total_synergies = synergies1 + synergies2 + synergies3 + synergies4
    total_integration_costs = integration_cost1 + integration_cost2
    net_cash_flow_impact = total_synergies - acquisition_cost - total_integration_costs

    question = (
        f"{company_name} is acquiring another firm for ${acquisition_cost}. It expects annual synergies of ${synergies1}, ${synergies2}, "
        f"${synergies3}, and ${synergies4} over the next four years. The integration costs in the first two years will be "
        f"${integration_cost1} and ${integration_cost2}. Compute the total net cash flow impact of the acquisition."
    ).replace("$-", "-$")

    solution = f"""
    Step 1. Compute total synergy benefits:
            Total Synergies = Synergy1 + Synergy2 + Synergy3 + Synergy4
                            = {synergies1} + {synergies2} + {synergies3} + {synergies4} = {total_synergies}
    Step 2. Compute total integration costs:
            Total Integration Costs = Integration Cost1 + Integration Cost2
                                    = {integration_cost1} + {integration_cost2} = {total_integration_costs}
    Step 3. Compute net cash flow impact:
            Net Cash Flow Impact = Total Synergies - Acquisition Cost - Total Integration Costs
                                 = {total_synergies} - {acquisition_cost} - {total_integration_costs} = {net_cash_flow_impact}
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
        template_calculate_closing_cash_balance,
        template_calculate_tax_cash_outflow,
        template_indirect_cash_flow_operations_advanced,
        template_calculate_cash_flow_from_financing_activities,
        template_calculate_cash_flow_impact_of_acquisition
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
    output_file = "../../testset/accounting_and_financial_reporting/cash_flow_statements.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()
