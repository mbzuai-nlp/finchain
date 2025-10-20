import random, json

# Named entities for investors and US companies (sampled)
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = [
    "Apple Inc.", "Microsoft Corporation", "Amazon.com, Inc.", "Tesla, Inc.", "Alphabet Inc.",
    "Facebook, Inc.", "Boeing", "Johnson & Johnson", "Walmart", "JPMorgan Chase"
]

# -----------------------------------------
# Basic Question 1: Energy Cost Savings
# Two-step basic calculation: a percentage reduction on energy costs.
def template_energy_cost_savings():
    """1:Basic: Energy Cost Savings Calculation"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Annual energy expense in dollars and percentage reduction from sustainability initiatives
    energy_cost = random.randint(50000, 100000)      # e.g., $50,000 - $100,000
    reduction_percent = round(random.uniform(5, 15), 2)  # e.g., 5% - 15%

    question = (
        f"{investor} reviewed {company}'s sustainability report and noted that the company's annual "
        f"energy expenditure of ${energy_cost} was reduced by {reduction_percent}% after implementing "
        "energy efficiency measures. Calculate the annual energy cost savings."
    )
    
    # Step 1: Calculate the reduction amount.
    saving_amount = round(energy_cost * (reduction_percent / 100), 2)
    # (Step 2: The result is the annual savings.)
    solution = (
        f"Step 1: Compute the cost reduction:\n"
        f"  Savings = Energy Cost × (Reduction Percent / 100)\n"
        f"          = {energy_cost} × ({reduction_percent} / 100) = {saving_amount}\n\n"
        f"Step 2: Therefore, the annual energy cost savings is ${saving_amount}."
    )
    return question, solution

# -----------------------------------------
# Basic Question 2: Waste Management Cost Savings
# Two or three steps: a fixed percentage decrease in waste disposal cost.
def template_waste_management_savings():
    """2:Basic: Waste Management Cost Savings Calculation"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    waste_cost = random.randint(20000, 50000)         # Annual waste disposal cost
    reduction_percent = round(random.uniform(10, 20), 2)  # Reduction percentage due to improved practices

    question = (
        f"{investor} examined {company}'s sustainability initiatives and found that waste management costs "
        f"of ${waste_cost} per year were reduced by {reduction_percent}% through improved recycling and waste "
        "management strategies. Calculate the annual savings in waste management costs."
    )
    
    # Step 1: Compute the waste cost saving.
    saving_amount = round(waste_cost * (reduction_percent / 100), 2)
    # Optional Step 2: Reiterate that the saving is the difference.
    solution = (
        f"Step 1: Calculate the savings from waste management:\n"
        f"  Savings = Waste Cost × (Reduction Percent / 100)\n"
        f"          = {waste_cost} × ({reduction_percent} / 100) = {saving_amount}\n\n"
        f"Step 2: Thus, the annual cost savings in waste management is ${saving_amount}."
    )
    return question, solution

# -----------------------------------------
# Intermediate Question 1: Dual-Operational Savings
# Three to four steps: total savings from both energy and waste reductions.
def template_dual_operational_savings():
    """3:Intermediate: Dual Operational Savings from Energy and Waste Management"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Annual costs and respective percentage reductions for two initiatives
    energy_cost = random.randint(60000, 120000)
    waste_cost = random.randint(15000, 40000)
    energy_reduction = round(random.uniform(5, 12), 2)
    waste_reduction = round(random.uniform(8, 18), 2)
    
    question = (
        f"{investor} is analyzing {company}'s sustainability report. The report shows that energy expenses of "
        f"${energy_cost} were reduced by {energy_reduction}% and waste management costs of ${waste_cost} were reduced "
        f"by {waste_reduction}% due to new sustainability initiatives. Calculate the total annual cost savings "
        "from these measures."
    )
    
    # Step 1: Calculate energy savings.
    energy_saving = round(energy_cost * (energy_reduction / 100), 2)
    # Step 2: Calculate waste savings.
    waste_saving = round(waste_cost * (waste_reduction / 100), 2)
    # Step 3: Sum both savings.
    total_saving = round(energy_saving + waste_saving, 2)
    # Step 4 (optional): Show total combined cost.
    solution = (
        f"Step 1: Energy Savings = {energy_cost} × ({energy_reduction} / 100) = {energy_saving}\n"
        f"Step 2: Waste Savings = {waste_cost} × ({waste_reduction} / 100) = {waste_saving}\n"
        f"Step 3: Total Annual Savings = Energy Savings + Waste Savings\n"
        f"          = {energy_saving} + {waste_saving} = {total_saving}\n\n"
        f"Therefore, the combined annual cost savings is ${total_saving}."
    )
    return question, solution

# -----------------------------------------
# Intermediate Question 2: Supply Chain Sustainability Savings
# Four steps: fixed cost saving plus an additional percentage saving on the remaining cost.
def template_supply_chain_savings():
    """4:Intermediate: Supply Chain Cost Savings from Sustainable Logistics"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Assume supply chain cost and two types of savings
    supply_chain_cost = random.randint(80000, 150000)
    fixed_saving = random.randint(5000, 15000)  # Fixed amount saving from process improvement
    extra_saving_percent = round(random.uniform(5, 10), 2)  # Additional percentage saving on remaining cost
    
    question = (
        f"{investor} reviewed {company}'s supply chain operations. The annual operational cost was "
        f"${supply_chain_cost}. By adopting sustainable logistics practices, the company achieved a fixed cost saving "
        f"of ${fixed_saving} and an additional {extra_saving_percent}% saving on the remaining costs. Calculate the total "
        "annual supply chain cost savings."
    )
    
    # Step 1: Compute the remaining cost after fixed savings.
    remaining_cost = supply_chain_cost - fixed_saving
    # Step 2: Compute the additional saving from the remaining cost.
    additional_saving = round(remaining_cost * (extra_saving_percent / 100), 2)
    # Step 3: Total savings is the sum of fixed and additional savings.
    total_saving = round(fixed_saving + additional_saving, 2)
    # Step 4: Present the detailed calculation.
    solution = (
        f"Step 1: Remaining Cost = Supply Chain Cost - Fixed Saving\n"
        f"          = {supply_chain_cost} - {fixed_saving} = {remaining_cost}\n"
        f"Step 2: Additional Saving = Remaining Cost × (Extra Saving Percent / 100)\n"
        f"          = {remaining_cost} × ({extra_saving_percent} / 100) = {additional_saving}\n"
        f"Step 3: Total Savings = Fixed Saving + Additional Saving\n"
        f"          = {fixed_saving} + {additional_saving} = {total_saving}\n\n"
        f"Thus, the total annual supply chain cost savings is ${total_saving}."
    )
    return question, solution

# -----------------------------------------
# Advanced Question: Sustainability ROI Analysis
# Advanced with 6 reasoning steps: multiple savings, tax credit, and operational cost reduction lead to ROI calculation.
def template_sustainability_roi_analysis():
    """5:Advanced: ROI Analysis for a Sustainability Reporting Initiative"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Investment and various saving parameters
    initial_investment = random.randint(200000, 500000)   # Initial cost of implementing the system
    annual_energy_saving = random.randint(40000, 80000)     # Annual energy cost saving
    annual_waste_saving = random.randint(15000, 35000)      # Annual waste management saving
    tax_credit_percent = round(random.uniform(5, 15), 2)    # Tax credit percentage on total savings
    extra_operational_reduction_percent = round(random.uniform(2, 8), 2)  # Extra reduction percentage on base savings
    time_years = random.randint(3, 7)                       # Analysis period in years

    question = (
        f"{investor} invested in a sustainability reporting system at {company} with an initial cost of "
        f"${initial_investment}. Over {time_years} years, the initiative delivered annual energy savings of "
        f"${annual_energy_saving} and waste management savings of ${annual_waste_saving}. Additionally, the program "
        f"earned a tax credit of {tax_credit_percent}% on the combined annual savings and achieved an extra operational cost "
        f"reduction of {extra_operational_reduction_percent}% on the base savings. Calculate the ROI (return on investment) "
        "as a percentage over the entire period."
    )
    
    # Step 1: Compute base annual savings.
    base_savings = annual_energy_saving + annual_waste_saving
    # Step 2: Compute tax credit on base savings.
    tax_credit = round(base_savings * (tax_credit_percent / 100), 2)
    # Step 3: Compute extra operational cost reduction savings.
    extra_savings = round(base_savings * (extra_operational_reduction_percent / 100), 2)
    # Step 4: Total annual saving = base savings + tax credit + extra savings.
    total_annual_saving = round(base_savings + tax_credit + extra_savings, 2)
    # Step 5: Total savings over the period = annual saving * time.
    total_savings_over_time = round(total_annual_saving * time_years, 2)
    # Step 6: ROI percentage = ((total savings over period - initial investment) / initial investment) * 100.
    roi_percentage = round(((total_savings_over_time - initial_investment) / initial_investment) * 100, 2)
    solution = (
        f"Step 1: Base Annual Savings = Energy Saving + Waste Saving\n"
        f"          = {annual_energy_saving} + {annual_waste_saving} = {base_savings}\n\n"
        f"Step 2: Tax Credit = Base Savings × (Tax Credit Percent / 100)\n"
        f"          = {base_savings} × ({tax_credit_percent} / 100) = {tax_credit}\n\n"
        f"Step 3: Extra Operational Reduction = Base Savings × (Extra Reduction Percent / 100)\n"
        f"          = {base_savings} × ({extra_operational_reduction_percent} / 100) = {extra_savings}\n\n"
        f"Step 4: Total Annual Savings = Base Savings + Tax Credit + Extra Savings\n"
        f"          = {base_savings} + {tax_credit} + {extra_savings} = {total_annual_saving}\n\n"
        f"Step 5: Total Savings Over {time_years} Years = Total Annual Savings × Time\n"
        f"          = {total_annual_saving} × {time_years} = {total_savings_over_time}\n\n"
        f"Step 6: ROI (%) = ((Total Savings Over Period - Initial Investment) / Initial Investment) × 100\n"
        f"          = (({total_savings_over_time} - {initial_investment}) / {initial_investment}) × 100 = {roi_percentage}%\n\n"
        f"Thus, the ROI for the sustainability initiative over {time_years} years is {roi_percentage}%."
    )
    return question, solution

# -----------------------------------------
# Main function to generate and display all questions
def main():
    """
    Generate one problem from each template function and save the results to a JSONL file.
    """
    # List of template functions (2 basic, 2 intermediate, 1 advanced)
    templates = [
        template_energy_cost_savings,               # Basic
        template_waste_management_savings,          # Basic
        template_dual_operational_savings,   # Intermediate
        template_supply_chain_savings,       # Intermediate
        template_sustainability_roi_analysis     # Advanced
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
    output_file = "../../testset/sustainable_finance/sustainability_reporting.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
