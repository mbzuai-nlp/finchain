import random
import json

# Named entities for investors and companies
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = [
    "Tesla Inc", "NextEra Energy", "First Solar", "Apple Inc", 
    "Google LLC", "Microsoft", "Amazon", "Starbucks", "Walmart", "Coca-Cola"
]

# ---------------- Basic Level Questions (2-3 steps) ----------------

def template_energy_efficiency_savings():
    """1:Basic: Calculate Annual Energy Cost Savings from an Energy Efficiency Upgrade"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    # Original annual energy cost in dollars
    original_cost = random.randint(20000, 50000)
    # Expected percentage saving from the upgrade
    saving_percentage = random.randint(5, 15)
    
    question = (
        f"{investor_name} invested in an energy efficiency upgrade at {company_name} to reduce energy costs. "
        f"The project is expected to reduce the annual energy expenditure by {saving_percentage}% from a current cost of ${original_cost}. "
        f"Calculate the new annual cost."
    )
    
    # Step 1: Compute the savings amount.
    savings = round(original_cost * (saving_percentage / 100), 2)
    # Step 2: Compute the new energy cost (optional for verification).
    new_cost = original_cost - savings
    solution = (
        f"Step 1: Compute the cost savings:\n"
        f"  Savings = Original Cost × (Saving Percentage / 100)\n"
        f"          = {original_cost} × ({saving_percentage} / 100) = {savings}\n\n"
        f"Step 2: Compute the new annual cost:\n"
        f"  New Cost = Original Cost - Savings\n"
        f"           = {original_cost} - {savings} = {new_cost}\n\n"
        f"Thus, the new annual energy cost is ${new_cost}."
    )
    return question, solution

def template_financing_cost_reduction():
    """2:Basic: Calculate New Financing Rate after a Reduction in Basis Points"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    # Initial financing cost as an annual rate (in percentage)
    initial_rate = round(random.uniform(4, 10), 2)
    # Reduction in financing cost given in basis points (1 bp = 0.01%)
    reduction_bp = random.randint(20, 80)
    
    question = (
        f"{investor_name} supports a sustainable finance project at {company_name} that improves its social impact profile. "
        f"This success leads to a reduction in the company's financing cost by {reduction_bp} basis points. "
        f"If the initial annual financing rate was {initial_rate}%, calculate the new financing rate."
    )
    
    # Step 1: Convert basis points to percentage.
    reduction_percent = reduction_bp * 0.01
    # Step 2: Compute the new financing rate.
    new_rate = round(initial_rate - reduction_percent, 2)
    solution = (
        f"Step 1: Convert the reduction from basis points to percentage:\n"
        f"  Reduction = {reduction_bp} bp = {reduction_percent:.2f}%\n\n"
        f"Step 2: Compute the new financing rate:\n"
        f"  New Rate = Initial Rate - Reduction\n"
        f"           = {initial_rate}% - {reduction_percent:.2f}% = {new_rate}%\n\n"
        f"Thus, the new financing rate is {new_rate}%."
    )
    return question, solution

# ---------------- Intermediate Level Questions (3-4 steps) ----------------

def template_supply_chain_integration():
    """3:Intermediate: Calculate Annual Savings from Sustainable Supply Chain Integration"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    # Original cost per unit (in dollars)
    original_cost_per_unit = random.randint(50, 200)
    # Percentage reduction in cost from process re-engineering
    reduction_percentage = random.randint(5, 15)
    # Additional fixed savings per unit from synergy benefits
    fixed_savings = random.randint(5, 20)
    # Annual production volume (units)
    annual_units = random.randint(1000, 10000)
    
    question = (
        f"{investor_name} funds a project at {company_name} aimed at integrating sustainable practices into its supply chain. "
        f"By doing so, the company expects to reduce its cost per unit by {reduction_percentage}% and gain an extra saving of ${fixed_savings} per unit due to synergy effects. "
        f"If the original cost per unit is ${original_cost_per_unit} and the annual production is {annual_units} units, "
        f"calculate the total annual cost savings."
    )
    
    # Step 1: Calculate the cost reduction per unit from the percentage change.
    percentage_saving = round(original_cost_per_unit * (reduction_percentage / 100), 2)
    # Step 2: Total savings per unit.
    saving_per_unit = percentage_saving + fixed_savings
    # Step 3: Calculate total annual savings.
    total_annual_savings = round(saving_per_unit * annual_units, 2)
    solution = (
        f"Step 1: Calculate the percentage-based saving per unit:\n"
        f"  Percentage Saving = Original Cost per Unit × (Reduction Percentage / 100)\n"
        f"                    = {original_cost_per_unit} × ({reduction_percentage} / 100) = {percentage_saving}\n\n"
        f"Step 2: Compute total saving per unit by adding the fixed savings:\n"
        f"  Saving per Unit = Percentage Saving + Fixed Savings\n"
        f"                  = {percentage_saving} + {fixed_savings} = {saving_per_unit}\n\n"
        f"Step 3: Calculate the total annual savings:\n"
        f"  Total Savings = Saving per Unit × Annual Units\n"
        f"                = {saving_per_unit} × {annual_units} = {total_annual_savings}\n\n"
        f"Thus, the total annual cost savings are ${total_annual_savings}."
    )
    return question, solution

def template_combined_cost_tax_savings():
    """4:Intermediate: Calculate Net Savings from Operational Cost Reduction and Tax Incentives"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    # Annual operational cost (in dollars)
    annual_op_cost = random.randint(50000, 200000)
    # Percentage reduction in operational cost
    op_reduction_percent = random.randint(5, 15)
    # Total project expenses (in dollars)
    project_expenses = random.randint(100000, 500000)
    # Tax credit percentage on project expenses
    tax_credit_percent = random.randint(2, 10)
    
    question = (
        f"{investor_name} is involved in a sustainable operational improvement project at {company_name}. "
        f"As part of the project, the company expects to reduce its annual operational cost by {op_reduction_percent}% and also receive a government tax credit of {tax_credit_percent}% on total project expenses amounting to ${project_expenses}. "
        f"Given an annual operational cost of ${annual_op_cost}, calculate the overall net annual savings."
    )
    
    # Step 1: Calculate the operational cost savings.
    op_savings = round(annual_op_cost * (op_reduction_percent / 100), 2)
    # Step 2: Calculate the tax credit value.
    tax_credit = round(project_expenses * (tax_credit_percent / 100), 2)
    # Step 3: Compute total net savings.
    net_savings = op_savings + tax_credit
    solution = (
        f"Step 1: Compute operational cost savings:\n"
        f"  Operational Savings = Annual Operational Cost × (Reduction Percentage / 100)\n"
        f"                      = {annual_op_cost} × ({op_reduction_percent} / 100) = {op_savings}\n\n"
        f"Step 2: Compute the tax credit value:\n"
        f"  Tax Credit = Project Expenses × (Tax Credit Percentage / 100)\n"
        f"             = {project_expenses} × ({tax_credit_percent} / 100) = {tax_credit}\n\n"
        f"Step 3: Total net savings are the sum of the two components:\n"
        f"  Net Savings = {op_savings} + {tax_credit} = {net_savings}\n\n"
        f"Thus, the overall net annual savings are ${net_savings}."
    )
    return question, solution

# ---------------- Advanced Level Question (5+ steps) ----------------

def template_multiphase_social_impact_investment():
    """5:Advanced: Calculate Overall Net Impact from a Multi-Phase Social Impact Investment"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    # Phase 1: Cost reduction on operating expenses
    initial_op_cost = random.randint(100000, 300000)
    phase1_reduction_percent = random.randint(5, 15)
    # Phase 2: Additional fixed saving per unit due to improved efficiency
    fixed_saving_per_unit = random.randint(5, 20)
    annual_production = random.randint(5000, 20000)
    # Phase 3: Government subsidy as a percentage of total project cost
    total_project_cost = random.randint(200000, 1000000)
    subsidy_percent = random.randint(3, 10)
    
    question = (
        f"{investor_name} has invested in a multi-phase sustainable project at {company_name} aimed at generating social impact. "
        f"In Phase 1, the project is expected to reduce the company's initial operating cost of ${initial_op_cost} by {phase1_reduction_percent}%. "
        f"In Phase 2, further improvements are expected to save an additional ${fixed_saving_per_unit} per unit over an annual production volume of {annual_production} units. "
        f"Finally, in Phase 3, the project qualifies for a government subsidy of {subsidy_percent}% of the total project cost of ${total_project_cost}. "
        f"Calculate the overall net financial impact of the project."
    )
    
    # Step 1: Calculate the savings from Phase 1.
    phase1_savings = round(initial_op_cost * (phase1_reduction_percent / 100), 2)
    # Step 2: Calculate the total additional savings from Phase 2.
    phase2_savings = round(fixed_saving_per_unit * annual_production, 2)
    # Step 3: Compute the government subsidy (Phase 3).
    phase3_subsidy = round(total_project_cost * (subsidy_percent / 100), 2)
    # Step 4: Sum all savings to get the overall net impact.
    overall_net_impact = phase1_savings + phase2_savings + phase3_subsidy
    # Step 5: (Optional) Present each component clearly.
    solution = (
        f"Step 1: Calculate Phase 1 savings (cost reduction):\n"
        f"  Phase 1 Savings = Initial Operating Cost × (Reduction Percentage / 100)\n"
        f"                  = {initial_op_cost} × ({phase1_reduction_percent} / 100) = {phase1_savings}\n\n"
        f"Step 2: Calculate Phase 2 savings from efficiency improvements:\n"
        f"  Phase 2 Savings = Fixed Saving per Unit × Annual Production\n"
        f"                  = {fixed_saving_per_unit} × {annual_production} = {phase2_savings}\n\n"
        f"Step 3: Compute Phase 3 subsidy:\n"
        f"  Phase 3 Subsidy = Total Project Cost × (Subsidy Percentage / 100)\n"
        f"                  = {total_project_cost} × ({subsidy_percent} / 100) = {phase3_subsidy}\n\n"
        f"Step 4: Sum all three components to find the overall net impact:\n"
        f"  Overall Net Impact = Phase 1 Savings + Phase 2 Savings + Phase 3 Subsidy\n"
        f"                     = {phase1_savings} + {phase2_savings} + {phase3_subsidy} = {overall_net_impact}\n\n"
        f"Step 6: Thus, the overall net financial impact of the project is ${overall_net_impact}."
    )
    return question, solution

# ---------------- Main Method to Generate and Save Problems ----------------

def main():
    """
    Generate one problem from each template function and save the results to a JSONL file.
    """
    # List of template functions (2 basic, 2 intermediate, 1 advanced)
    templates = [
        template_energy_efficiency_savings,
        template_financing_cost_reduction,
        template_supply_chain_integration,
        template_combined_cost_tax_savings,
        template_multiphase_social_impact_investment
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
    output_file = "../../testset/sustainable_finance/social_impact_investing.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
