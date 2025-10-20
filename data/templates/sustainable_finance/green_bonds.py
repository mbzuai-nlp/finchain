import random
import json

# Named entities for investors and companies
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = [
    "Apple", "Tesla", "Google", "Microsoft", "Amazon",
    "General Electric", "IBM", "Coca-Cola", "Ford", "Walmart"
]

# -----------------------------------------------------------------------------
# Basic Question 1: Green Bond Yield Calculation
# -----------------------------------------------------------------------------
def template_green_bond_basic_yield_calculation():
    """1:Basic: Green Bond Yield Calculation (2 steps)"""
    # Randomly select investor and company
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Define parameters for the green bond
    principal = random.randint(5000, 20000)                   # Investment amount
    yield_rate = round(random.uniform(2, 6), 2)               # Annual yield in %
    time = random.randint(1, 3)                               # Time period in years

    # Construct the question
    question = (
        f"{investor} purchased a green bond issued by {company} for ${principal}. "
        f"The bond offers an annual yield of {yield_rate}% compounded annually over {time} years. "
        f"Calculate the total interest earned from this green bond investment."
    )

    # Step 1: Calculate the compound (future) amount
    future_value = round(principal * (1 + yield_rate / 100) ** time, 2)
    # Step 2: Calculate the interest earned (compound interest)
    interest_earned = round(future_value - principal, 2)

    solution = (
        f"Step 1: Compute the future value of the investment:\n"
        f"  Future Value = Principal × (1 + Yield Rate/100)^Time\n"
        f"               = {principal} × (1 + {yield_rate / 100:.4f})^{time} = {future_value}\n\n"
        f"Step 2: Determine the interest earned:\n"
        f"  Interest Earned = Future Value - Principal\n"
        f"                  = {future_value} - {principal} = {interest_earned}"
    )

    return question, solution

# -----------------------------------------------------------------------------
# Basic Question 2: Green Bond Tax Incentive Calculation
# -----------------------------------------------------------------------------
def template_green_bond_basic_tax_incentive():
    """2:Basic: Green Bond Tax Incentive Calculation (3 steps)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Parameters for the green bond investment
    principal = random.randint(10000, 30000)
    coupon_rate = round(random.uniform(3, 7), 2)              # Annual coupon rate in %
    time = random.randint(1, 3)
    tax_credit_rate = round(random.uniform(5, 15), 2)         # Tax credit in %

    question = (
        f"{investor} invested ${principal} in a green bond issued by {company} with an annual coupon rate of "
        f"{coupon_rate}% compounded annually over {time} years. Due to sustainable finance policies, the investor "
        f"receives a tax credit equal to {tax_credit_rate}% of the interest earned. Calculate the net benefit from "
        f"the tax incentive, which is the sum of the compound interest and the tax credit."
    )

    # Step 1: Compute the compound amount and interest earned.
    future_value = round(principal * (1 + coupon_rate / 100) ** time, 2)
    interest_earned = round(future_value - principal, 2)
    # Step 2: Compute the tax credit on the interest earned.
    tax_credit = round(interest_earned * (tax_credit_rate / 100), 2)
    # Step 3: Compute the net benefit (interest earned plus tax credit).
    net_benefit = round(interest_earned + tax_credit, 2)

    solution = (
        f"Step 1: Compute the compound amount and interest earned:\n"
        f"  Future Value = {principal} × (1 + {coupon_rate / 100:.4f})^{time} = {future_value}\n"
        f"  Interest Earned = Future Value - Principal = {future_value} - {principal} = {interest_earned}\n\n"
        f"Step 2: Calculate the tax credit:\n"
        f"  Tax Credit = Interest Earned × (Tax Credit Rate/100)\n"
        f"             = {interest_earned} × ({tax_credit_rate}/100) = {tax_credit}\n\n"
        f"Step 3: Determine the net benefit:\n"
        f"  Net Benefit = Interest Earned + Tax Credit = {interest_earned} + {tax_credit} = {net_benefit}"
    )

    return question, solution

# -----------------------------------------------------------------------------
# Intermediate Question 1: Green Bond Synergy Benefit Calculation
# -----------------------------------------------------------------------------
def template_green_bond_intermediate_synergy_benefit():
    """3:Intermediate: Green Bond Synergy Benefit Calculation (4 steps)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Parameters for the green bond and synergy effects
    principal = random.randint(10000, 25000)
    coupon_rate = round(random.uniform(3, 8), 2)
    time = random.randint(2, 5)
    annual_savings = random.randint(1000, 5000)               # Annual cost savings due to energy efficiency
    bonus_rate = round(random.uniform(10, 30), 2)             # Bonus dollars per $500 saved

    question = (
        f"{investor} invested in a green bond issued by {company} for ${principal} at an annual coupon rate of {coupon_rate}% "
        f"compounded annually over {time} years. As a result of energy efficiency measures financed by the bond, "
        f"{company} achieves annual cost savings of ${annual_savings}. Additionally, the investor receives a synergy bonus "
        f"of ${bonus_rate} for every $500 saved annually. Calculate the total net benefit to the investor, including "
        f"both the compound interest and the synergy bonus."
    )

    # Step 1: Compute the future value and interest earned from the bond.
    future_value = round(principal * (1 + coupon_rate / 100) ** time, 2)
    interest_earned = round(future_value - principal, 2)
    # Step 2: Calculate the bonus earned per year from cost savings.
    bonus_per_year = round((annual_savings / 500) * bonus_rate, 2)
    # Step 3: Compute the total bonus over the entire period.
    total_bonus = round(bonus_per_year * time, 2)
    # Step 4: Sum the compound interest and the synergy bonus for the total net benefit.
    total_net_benefit = round(interest_earned + total_bonus, 2)

    solution = (
        f"Step 1: Calculate the compound interest earned:\n"
        f"  Future Value = {principal} × (1 + {coupon_rate / 100:.4f})^{time} = {future_value}\n"
        f"  Interest Earned = Future Value - Principal = {future_value} - {principal} = {interest_earned}\n\n"
        f"Step 2: Determine the annual synergy bonus:\n"
        f"  Bonus per Year = (Annual Savings / 500) × Bonus Rate = ({annual_savings} / 500) × {bonus_rate} = {bonus_per_year}\n\n"
        f"Step 3: Compute the total synergy bonus over {time} years:\n"
        f"  Total Bonus = Bonus per Year × Time = {bonus_per_year} × {time} = {total_bonus}\n\n"
        f"Step 4: Calculate the total net benefit:\n"
        f"  Total Net Benefit = Interest Earned + Total Bonus = {interest_earned} + {total_bonus} = {total_net_benefit}"
    )

    return question, solution

# -----------------------------------------------------------------------------
# Intermediate Question 2: Green Bond Financing Cost Reduction Calculation
# -----------------------------------------------------------------------------
def template_green_bond_intermediate_financing_cost_reduction():
    """4:Intermediate: Green Bond Financing Cost Reduction Calculation (4 steps)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Parameters for the financing scenario
    principal = random.randint(15000, 30000)
    coupon_rate = round(random.uniform(4, 8), 2)
    time = random.randint(2, 4)
    discount = round(random.uniform(0.5, 2), 2)  # Reduction in effective interest rate (in percentage points)

    question = (
        f"{investor} is evaluating a green bond issued by {company} with a principal of ${principal} and an annual coupon rate "
        f"of {coupon_rate}% compounded annually over {time} years. Due to sustainable finance incentives, the effective interest rate "
        f"is reduced by {discount} percentage points. Calculate the financing cost reduction in terms of the difference in compound "
        f"interest between the original and the discounted rates."
    )

    # Step 1: Calculate the original future value and interest cost.
    original_FV = round(principal * (1 + coupon_rate / 100) ** time, 2)
    original_interest = round(original_FV - principal, 2)
    # Step 2: Determine the adjusted (discounted) interest rate.
    adjusted_rate = coupon_rate - discount
    # Step 3: Calculate the adjusted future value and interest cost.
    adjusted_FV = round(principal * (1 + adjusted_rate / 100) ** time, 2)
    adjusted_interest = round(adjusted_FV - principal, 2)
    # Step 4: Compute the financing cost reduction as the difference between the interest costs.
    cost_reduction = round(original_interest - adjusted_interest, 2)

    solution = (
        f"Step 1: Original calculation:\n"
        f"  Original Future Value = {principal} × (1 + {coupon_rate / 100:.4f})^{time} = {original_FV}\n"
        f"  Original Interest = {original_FV} - {principal} = {original_interest}\n\n"
        f"Step 2: Adjust the interest rate:\n"
        f"  Adjusted Rate = {coupon_rate} - {discount} = {adjusted_rate}%\n\n"
        f"Step 3: Adjusted calculation:\n"
        f"  Adjusted Future Value = {principal} × (1 + {adjusted_rate / 100:.4f})^{time} = {adjusted_FV}\n"
        f"  Adjusted Interest = {adjusted_FV} - {principal} = {adjusted_interest}\n\n"
        f"Step 4: Financing cost reduction:\n"
        f"  Cost Reduction = Original Interest - Adjusted Interest = {original_interest} - {adjusted_interest} = {cost_reduction}"
    )

    return question, solution

# -----------------------------------------------------------------------------
# Advanced Question: Comprehensive Benefit Analysis of a Green Bond Investment
# -----------------------------------------------------------------------------
def template_green_bond_advanced_comprehensive_analysis():
    """5:Advanced: Comprehensive Benefit Analysis of a Green Bond Investment (5+ steps)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    # Advanced parameters
    principal = random.randint(20000, 50000)
    coupon_rate = round(random.uniform(3, 8), 2)
    time = random.randint(3, 7)
    tax_credit_rate = round(random.uniform(5, 15), 2)         # Tax credit percentage on interest earned
    annual_savings = random.randint(1000, 5000)               # Annual energy cost savings in dollars
    synergy_bonus_rate = round(random.uniform(20, 50), 2)       # Bonus dollars per $500 saved per year
    reinvestment_percentage = round(random.uniform(10, 50), 2)  # Percentage of interest that is reinvested
    reinvestment_rate = round(random.uniform(2, 6), 2)          # Additional growth rate (%) on reinvested amount

    question = (
        f"{investor} invested in a green bond issued by {company} for ${principal} at an annual coupon rate of {coupon_rate}% "
        f"compounded annually over {time} years. In addition, due to sustainable finance benefits, the investor receives a "
        f"tax credit of {tax_credit_rate}% on the interest earned. Furthermore, {company} achieves annual energy cost savings "
        f"of ${annual_savings}, for which the investor gets a synergy bonus of ${synergy_bonus_rate} per $500 saved each year. "
        f"Moreover, the investor reinvests {reinvestment_percentage}% of the annual interest at an additional rate of {reinvestment_rate}% "
        f"compounded annually. Calculate the total net benefit to the investor by summing the compound interest, tax credit, synergy bonus, "
        f"and reinvestment gains."
    )

    # Step 1: Compute the bond compound interest
    future_value = principal * (1 + coupon_rate / 100) ** time
    interest_earned = future_value - principal
    # Step 2: Calculate the tax credit on the interest earned
    tax_credit = interest_earned * (tax_credit_rate / 100)
    # Step 3: Determine the synergy bonus from energy cost savings
    bonus_per_year = (annual_savings / 500) * synergy_bonus_rate
    total_bonus = bonus_per_year * time
    # Step 4: Compute the reinvestment benefit over the period
    # Assume the interest earned is evenly distributed over the years.
    annual_interest = interest_earned / time
    reinvest_amount = (reinvestment_percentage / 100) * annual_interest
    reinvestment_benefit = 0
    # For each year, the reinvested amount compounds for the remaining years.
    for i in range(1, time + 1):
        # Compounding for (time - i) full years after reinvestment at the end of year i
        reinvestment_benefit += reinvest_amount * (1 + reinvestment_rate / 100) ** (time - i)
    # Step 5: Sum all the benefits to get the total net benefit
    total_net_benefit = interest_earned + tax_credit + total_bonus + reinvestment_benefit

    # Round values for clarity
    future_value = round(future_value, 2)
    interest_earned = round(interest_earned, 2)
    tax_credit = round(tax_credit, 2)
    bonus_per_year = round(bonus_per_year, 2)
    total_bonus = round(total_bonus, 2)
    reinvestment_benefit = round(reinvestment_benefit, 2)
    total_net_benefit = round(total_net_benefit, 2)

    solution = (
        f"Step 1: Compute the compound interest from the green bond:\n"
        f"  Future Value = {principal} × (1 + {coupon_rate / 100:.4f})^{time} = {future_value}\n"
        f"  Interest Earned = Future Value - Principal = {future_value} - {principal} = {interest_earned}\n\n"
        f"Step 2: Calculate the tax credit on the interest earned:\n"
        f"  Tax Credit = Interest Earned × (Tax Credit Rate/100) = {interest_earned} × ({tax_credit_rate}/100) = {tax_credit}\n\n"
        f"Step 3: Determine the synergy bonus from energy cost savings:\n"
        f"  Bonus per Year = (Annual Savings / 500) × Synergy Bonus Rate = ({annual_savings} / 500) × {synergy_bonus_rate} = {bonus_per_year}\n"
        f"  Total Bonus over {time} years = {bonus_per_year} × {time} = {total_bonus}\n\n"
        f"Step 4: Compute the reinvestment benefit:\n"
        f"  Annual Interest = Interest Earned / Time = {interest_earned} / {time} = {annual_interest:.2f}\n"
        f"  Reinvestment Amount per Year = (Reinvestment Percentage/100) × Annual Interest = ({reinvestment_percentage}/100) × {annual_interest:.2f} = {reinvest_amount:.2f}\n"
        f"  Reinvestment Benefit = Sum (for each year i from 1 to {time}) of [Reinvested Amount × (1 + {reinvestment_rate / 100:.4f})^(Time - i)] = {reinvestment_benefit}\n\n"
        f"Step 5: Calculate the Total Net Benefit:\n"
        f"  Total Net Benefit = Interest Earned + Tax Credit + Total Bonus + Reinvestment Benefit\n"
        f"                    = {interest_earned} + {tax_credit} + {total_bonus} + {reinvestment_benefit} = {total_net_benefit}"
    )

    return question, solution

# -----------------------------------------------------------------------------
# Main: Generate and Print the Questions and Solutions
# -----------------------------------------------------------------------------
def main():
    """
    Generate one instance for each ESG QA pair template and write the results to a JSON file.
    """
    # List of template functions
    templates = [
        template_green_bond_basic_yield_calculation,
        template_green_bond_basic_tax_incentive,
        template_green_bond_intermediate_synergy_benefit,
        template_green_bond_intermediate_financing_cost_reduction,
        template_green_bond_advanced_comprehensive_analysis
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
    output_file = "../../testset/sustainable_finance/green_bonds.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
