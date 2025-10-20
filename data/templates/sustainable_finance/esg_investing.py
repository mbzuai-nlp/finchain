import random
import json

# Named entities for investors and companies
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = [
    "Apple Inc.", "Microsoft Corporation", "Tesla Inc.", "Amazon.com Inc.", 
    "Alphabet Inc.", "Facebook Inc.", "JPMorgan Chase & Co.", "Walmart Inc.",
    "Berkshire Hathaway Inc.", "Johnson & Johnson"
]

# Template 1: Basic – Simple ESG Cost Savings Calculation
def template_esg_simple_cost_savings():
    """1:Basic: Simple ESG Cost Savings Calculation"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    monthly_savings = random.randint(500, 2000)  # Monthly cost savings in dollars
    months = random.randint(6, 24)              # Duration in months
    question = (f"{investor} backed an energy-efficient upgrade at {company}, "
                f"which reduces operating costs by ${monthly_savings} per month. "
                f"Over a period of {months} months, what is the total cost savings?")
    # Step 1: Calculate the total savings over the period
    total_savings = monthly_savings * months
    solution = (f"Step 1: Multiply the monthly savings by the number of months:\n"
                f"  Total Savings = {monthly_savings} × {months} = {total_savings}\n"
                f"Thus, the project yields ${total_savings} in total cost savings.")
    return question, solution

# Template 2: Basic – Green Bond Yield Calculation with Simple Interest
def template_esg_green_bond_yield():
    """2:Basic: Green Bond Yield Calculation with Simple Interest"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    principal = random.randint(10000, 50000)  # Investment amount in dollars
    rate = round(random.uniform(3, 7), 2)     # Annual yield in percent
    years = random.randint(1, 5)

    # Question focuses on total interest (NOT including principal)
    question = (f"{investor} invested ${principal} in green bonds issued by {company}. "
                f"The bonds offer a simple annual yield of {rate}% for {years} years. "
                f"Calculate the total interest earned after {years} years (ignore compounding).")

    # Step 1: Calculate the annual interest
    annual_interest = round(principal * rate / 100, 2)

    # Step 2: Compute the total interest earned over the years
    total_interest = round(annual_interest * years, 2)

    # Solution matches the question (only total interest)
    solution = (f"Step 1: Compute the annual interest:\n"
                f"  Annual Interest = Principal × (Rate/100)\n"
                f"                  = {principal} × ({rate}/100) = {annual_interest}\n"
                f"Step 2: Compute the total interest over {years} years:\n"
                f"  Total Interest = Annual Interest × Years\n"
                f"                 = {annual_interest} × {years} = {total_interest}\n"
                f"Therefore, the total interest earned after {years} years is ${total_interest}.")

    return question, solution

def template_esg_dual_savings():
    """3:Intermediate: Dual ESG Savings with Energy and Water Initiatives (4 steps)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    
    # Randomly determine monthly savings and cost parameters
    monthly_energy_savings = random.randint(2000, 8000)   # Savings from energy efficiency per month
    monthly_water_savings = random.randint(500, 3000)     # Savings from water conservation per month
    annual_maintenance_cost = random.randint(10000, 40000)  # Annual cost for system maintenance
    government_incentive = random.randint(5000, 20000)      # One-time annual government incentive
    
    question = (
        f"{investor} implemented dual ESG initiatives at {company} to improve sustainability. "
        f"The project reduced energy costs by ${monthly_energy_savings} per month and reduced water consumption costs by "
        f"${monthly_water_savings} per month. However, the project incurs an annual maintenance cost of "
        f"${annual_maintenance_cost} and qualifies for a government incentive of ${government_incentive} each year. "
        f"Calculate the net annual savings from the project."
    )
    
    # Step 1: Calculate annual energy savings.
    annual_energy_savings = monthly_energy_savings * 12
    # Step 2: Calculate annual water savings.
    annual_water_savings = monthly_water_savings * 12
    # Step 3: Compute interim savings by summing both annual savings and then subtracting maintenance costs.
    interim_savings = annual_energy_savings + annual_water_savings - annual_maintenance_cost
    # Step 4: Compute net annual savings by adding the government incentive.
    net_annual_savings = interim_savings + government_incentive
    
    solution = (
        f"Step 1: Calculate annual energy savings:\n"
        f"  Annual Energy Savings = Monthly Energy Savings × 12 = {monthly_energy_savings} × 12 = {annual_energy_savings}\n\n"
        f"Step 2: Calculate annual water savings:\n"
        f"  Annual Water Savings = Monthly Water Savings × 12 = {monthly_water_savings} × 12 = {annual_water_savings}\n\n"
        f"Step 3: Compute interim savings by subtracting annual maintenance cost:\n"
        f"  Interim Savings = (Annual Energy Savings + Annual Water Savings) - Annual Maintenance Cost\n"
        f"                  = ({annual_energy_savings} + {annual_water_savings}) - {annual_maintenance_cost} = {interim_savings}\n\n"
        f"Step 4: Add the government incentive to obtain net annual savings:\n"
        f"  Net Annual Savings = Interim Savings + Government Incentive\n"
        f"                     = {interim_savings} + {government_incentive} = {net_annual_savings}"
    )
    return question, solution

# Intermediate Template 2:
# ESG Project ROI Calculation with Net Savings and Investment (4 steps)
def template_esg_project_roi():
    """4:Intermediate: ESG Project ROI Calculation with Net Savings and Investment (4 steps)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    
    # Define parameters for the investment scenario
    initial_investment = random.randint(50000, 200000)      # Initial investment cost
    monthly_energy_savings = random.randint(3000, 12000)      # Monthly energy cost savings
    annual_operating_cost = random.randint(15000, 50000)      # Annual operating cost for the project
    annual_tax_incentive = random.randint(5000, 25000)        # Annual tax incentive received
    years = random.randint(3, 7)                              # Duration of the project in years
    
    question = (
        f"{investor} invested ${initial_investment} in an ESG project at {company}. The project generates monthly energy "
        f"savings of ${monthly_energy_savings}, but incurs an annual operating cost of ${annual_operating_cost}. "
        f"In addition, there is an annual tax incentive of ${annual_tax_incentive}. Over {years} years, calculate the ROI "
        f"(as a percentage) of the project, where ROI = (Total Net Savings / Initial Investment) × 100."
    )
    
    # Step 1: Calculate annual energy savings.
    annual_energy_savings = monthly_energy_savings * 12
    # Step 2: Compute the annual net savings by subtracting operating cost and adding tax incentive.
    annual_net_savings = annual_energy_savings - annual_operating_cost + annual_tax_incentive
    # Step 3: Compute total net savings over the project duration.
    total_net_savings = annual_net_savings * years
    # Step 4: Calculate the ROI percentage.
    roi_percentage = round((total_net_savings / initial_investment) * 100, 2)
    
    solution = (
        f"Step 1: Calculate annual energy savings:\n"
        f"  Annual Energy Savings = Monthly Energy Savings × 12 = {monthly_energy_savings} × 12 = {annual_energy_savings}\n\n"
        f"Step 2: Compute annual net savings:\n"
        f"  Annual Net Savings = Annual Energy Savings - Annual Operating Cost + Annual Tax Incentive\n"
        f"                    = {annual_energy_savings} - {annual_operating_cost} + {annual_tax_incentive} = {annual_net_savings}\n\n"
        f"Step 3: Compute total net savings over {years} years:\n"
        f"  Total Net Savings = Annual Net Savings × Years = {annual_net_savings} × {years} = {total_net_savings}\n\n"
        f"Step 4: Calculate ROI percentage:\n"
        f"  ROI (%) = (Total Net Savings / Initial Investment) × 100\n"
        f"          = ({total_net_savings} / {initial_investment}) × 100 = {roi_percentage}%"
    )
    return question, solution

# Template 5: Advanced – Multi-Factor ESG Synergy with Tax Credits and Efficiency Gains
def template_esg_multi_factor_synergy():
    """5:Advanced: Multi-Factor ESG Synergy Calculation with Tax Credits and Efficiency Gains"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    initial_cost = random.randint(50000, 200000)            # Initial investment cost
    monthly_energy_savings = random.randint(3000, 10000)    # Savings from energy efficiency per month
    annual_tax_credit = random.randint(10000, 30000)        # Annual tax credit in dollars
    operating_costs = random.randint(50000, 150000)         # Annual operating costs in dollars
    efficiency_improvement_rate = round(random.uniform(2, 8), 2)  # Percentage savings on operating costs
    years = random.randint(3, 7)
    
    question = (f"{investor} is evaluating a comprehensive sustainability project at {company} that involves installing "
                f"energy-efficient systems and renewable energy sources. The project requires an initial investment of ${initial_cost}. "
                f"It is expected to reduce energy costs by ${monthly_energy_savings} per month and lower operating costs by "
                f"{efficiency_improvement_rate}% (given operating costs of ${operating_costs} annually). Additionally, the project "
                f"qualifies for an annual tax credit of ${annual_tax_credit}. Calculate the net benefit over {years} years, "
                f"taking into account the initial cost and annual combined savings.")
    
    # Step 1: Calculate annual energy savings
    annual_energy_savings = monthly_energy_savings * 12
    # Step 2: Compute annual efficiency savings from reduced operating costs
    annual_efficiency_savings = round((efficiency_improvement_rate / 100) * operating_costs, 2)
    # Step 3: Total annual savings = energy savings + efficiency savings + tax credit
    annual_total_savings = annual_energy_savings + annual_efficiency_savings + annual_tax_credit
    # Step 4: Total savings over the period
    total_savings_over_years = annual_total_savings * years
    # Step 5: Net benefit after subtracting the initial investment cost
    net_benefit = total_savings_over_years - initial_cost
    
    solution = (f"Step 1: Compute annual energy savings:\n"
                f"  Annual Energy Savings = {monthly_energy_savings} × 12 = {annual_energy_savings}\n\n"
                f"Step 2: Calculate annual efficiency savings:\n"
                f"  Efficiency Savings = (Efficiency Improvement Rate/100) × Operating Costs\n"
                f"                    = ({efficiency_improvement_rate}/100) × {operating_costs} = {annual_efficiency_savings}\n\n"
                f"Step 3: Sum all annual savings:\n"
                f"  Total Annual Savings = Annual Energy Savings + Efficiency Savings + Tax Credit\n"
                f"                     = {annual_energy_savings} + {annual_efficiency_savings} + {annual_tax_credit} = {annual_total_savings}\n\n"
                f"Step 4: Compute total savings over {years} years:\n"
                f"  Total Savings = Total Annual Savings × Years = {annual_total_savings} × {years} = {total_savings_over_years}\n\n"
                f"Step 5: Calculate net benefit by subtracting the initial cost:\n"
                f"  Net Benefit = Total Savings - Initial Cost = {total_savings_over_years} - {initial_cost} = {net_benefit}")
    return question, solution

def main():
    """
    Generate one instance for each ESG QA pair template and write the results to a JSON file.
    """
    # List of template functions
    templates = [
        template_esg_simple_cost_savings,
        template_esg_green_bond_yield,
        template_esg_dual_savings,
        template_esg_project_roi,
        template_esg_multi_factor_synergy
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
    output_file = "../../testset/sustainable_finance/esg_investing.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
