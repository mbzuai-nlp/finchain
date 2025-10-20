import random
import json

# Named entities for investors and companies (US companies)
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = ["Tesla Inc.", "Apple Inc.", "Amazon Inc.", "Microsoft Corp.", "Google LLC"]

# Basic Scenario 1: Carbon Credit Purchase Calculation
def template_carbon_credit_purchase():
    """1:Basic: Carbon Credit Purchase Calculation (2-step reasoning)"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    investment = random.randint(1000, 5000)  # total investment in dollars
    price_per_credit = round(random.uniform(10, 20), 2)  # cost per carbon credit
    # Step 1: Calculate raw credits (assume exact division and integerize by truncating the decimal part)
    credits = round(investment / price_per_credit, 2)
    int_credits = int(credits)
    question = (
        f"{investor_name} from {company_name} invested ${investment} (Investment) in purchasing carbon credits. "
        f"Each carbon credit costs ${price_per_credit:.2f} (Price per Credit). Calculate the number of carbon credits purchased."
    )
    solution = (
        f"Step 1: Calculate the number of carbon credits:\n"
        f"  Number of Credits = Investment / Price per Credit = {investment} / {price_per_credit:.2f} ≈ {credits}\n\n"
        f"Step 2: Integerize the value to obtain the final answer.\n"
        f"  Final Answer: {int_credits} carbon credits purchased."
    )
    return question, solution

# Basic Scenario 2: Carbon Credit Rebate Calculation
def template_carbon_credit_rebate():
    """2:Basic: Carbon Credit Rebate Calculation (2-step reasoning)"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    investment = random.randint(1000, 5000)
    price_per_credit = round(random.uniform(8, 15), 2)
    rebate_per_credit = round(random.uniform(1, 5), 2)  # fixed rebate per credit < price_per_credit
    threshold = random.randint(20, 40)  # minimum credits to qualify for rebate
    credits = round(investment / price_per_credit, 2)
    if credits > threshold:
        total_rebate = round(credits * rebate_per_credit, 2)
    else:
        total_rebate = 0.0

    question = (
        f"{investor_name} from {company_name} invested ${investment} (Investment) in carbon credits at ${price_per_credit:.2f} per credit (Price per Credit). "
        f"If the company receives a rebate of ${rebate_per_credit:.2f} per credit when more than {threshold} credits are purchased, "
        f"calculate the total rebate received."
    )
    if credits > threshold:
        solution = (
            f"Step 1: Determine the number of carbon credits purchased:\n"
            f"  Number of Credits = Investment / Price per Credit = {investment} / {price_per_credit:.2f} ≈ {credits}\n\n"
            f"Step 2: Since {credits} > {threshold}, the rebate is applied:\n"
            f"  Total Rebate = Number of Credits × Rebate per Credit = {credits} × {rebate_per_credit:.2f} = ${total_rebate:.2f}\n"
            f"Final Answer: ${total_rebate:.2f} total rebate."
        )
    else:
        solution = (
            f"Step 1: Determine the number of carbon credits purchased:\n"
            f"  Number of Credits = Investment / Price per Credit = {investment} / {price_per_credit:.2f} ≈ {credits}\n\n"
            f"Step 2: Since {credits} <= {threshold}, the rebate is not applied:\n"
            f"  Total Rebate = 0.0\n"
            f"Final Answer: ${total_rebate:.2f} total rebate."
        )

    return question, solution

def template_offset_cost_savings():
    """3:Intermediate: Emissions Offset Cost Savings Calculation (4-step reasoning)"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    emissions_offset = random.randint(100, 1000)  # CO2 offset required in metric tons (1 credit offsets 1 ton)
    base_price = round(random.uniform(12, 25), 2)
    discount_percentage = round(random.uniform(5, 15), 2)
    
    # Solution 1
    # Step 1: Credits required equals the emission offset
    credits_required = emissions_offset
    # Step 2: Calculate the gross cost (without discount)
    gross_cost = round(credits_required * base_price, 2)
    # Step 3: Determine the discount amount on the gross cost
    discount_amount = round(gross_cost * discount_percentage / 100, 2)
    # Step 4: Compute the net cost after discount
    net_cost = round(gross_cost - discount_amount, 2)

    # Solution 2
    discounted_price = round(base_price * (1 - discount_percentage / 100), 2)
    net_cost_ = round(credits_required * discounted_price, 2) 
    # due to round operation in last step, net_cost_ might be different from net_cost in solution 1
    
    question = (
        f"{investor_name} from {company_name} needs to offset {emissions_offset} metric tons of CO2. "
        f"1 carbon credit can offset 1 ton CO2. Each carbon credit costs ${base_price:.2f} but the company receives a {discount_percentage:.2f}% discount through a synergy program. "
        f"Calculate the net cost to purchase the required credits."
    )
    solution1 = (
        f"Step 1: Determine the number of credits needed (1 credit offsets 1 ton):\n"
        f"  Credits Required = {emissions_offset}\n\n"
        f"Step 2: Calculate the gross cost without discount:\n"
        f"  Gross Cost = Credits Required × Base Price = {emissions_offset} × {base_price:.2f} = ${gross_cost:.2f}\n\n"
        f"Step 3: Compute the discount amount:\n"
        f"  Discount = Gross Cost × (Discount Percentage / 100) = ${gross_cost:.2f} × {discount_percentage:.2f}% = ${discount_amount:.2f}\n\n"
        f"Step 4: Calculate the net cost after discount:\n"
        f"  Net Cost = Gross Cost - Discount = ${gross_cost:.2f} - ${discount_amount:.2f} = ${net_cost:.2f}\n"
        f"Final Answer: ${net_cost:.2f} is the net cost to offset the emissions."
    )
    solution2 = (
        f"Step 1: Determine the number of credits needed (1 credit offsets 1 ton):\n"
        f"  Credits Required = {emissions_offset}\n\n"
        f"Step 2: Calculate the base price after discount:\n"
        f"  Discounted Price = Base Price × (1 - Discount Percentage / 100) = {base_price:.2f} × (1 - {discount_percentage:.2f}%)) = ${discounted_price:.2f}\n\n"
        f"Step 3: Calculate the net cost after discount:\n"
        f"  Net Cost = Discounted Price × Credits Required = ${discounted_price:.2f} × {emissions_offset} = ${net_cost_:.2f}\n"
        f"Final Answer: ${net_cost_:.2f} is the net cost to offset the emissions."
    )

    return question, solution1, solution2

# Intermediate Scenario 2: Multi-Company Synergy Savings
def template_multi_company_synergy():
    """4:Intermediate: Multi-Company Synergy Savings (4-step reasoning)"""
    investor_name = random.choice(investor_names)
    company1 = random.choice(company_names)
    company2 = random.choice(company_names)
    emissions_company1 = random.randint(50, 300)
    emissions_company2 = random.randint(50, 300)
    base_price = round(random.uniform(10, 20), 2)
    synergy_discount = round(random.uniform(5, 10), 2)  # discount if total credits exceed threshold
    threshold_total_credits = random.randint(200, 400)
    
    # Step 1: Calculate credits required for each company (1 credit offsets 1 ton)
    credits_company1 = emissions_company1
    credits_company2 = emissions_company2
    # Step 2: Total credits required
    total_credits = credits_company1 + credits_company2
    # Step 3: Compute the gross cost for the total credits
    gross_cost = round(total_credits * base_price, 2)
    # Step 4: Apply the synergy discount if the threshold is exceeded
    if total_credits > threshold_total_credits:
        net_cost = round(gross_cost * (1 - synergy_discount / 100), 2)
    else:
        net_cost = gross_cost
    
    question = (
        f"{investor_name} has formed a consortium with {company1} and {company2} to purchase carbon credits. "
        f"{company1} needs to offset {emissions_company1} metric tons and {company2} needs to offset {emissions_company2} metric tons of CO2. "
        f"Each carbon credit costs ${base_price:.2f}. If a synergy discount of {synergy_discount:.2f}% is applied when total credits exceed "
        f"{threshold_total_credits}, calculate the combined net cost for the consortium."
    )
    solution = (
        f"Step 1: Calculate individual credits needed:\n"
        f"  {company1} requires {credits_company1} credits.\n"
        f"  {company2} requires {credits_company2} credits.\n\n"
        f"Step 2: Total credits = {credits_company1} + {credits_company2} = {total_credits}\n\n"
        f"Step 3: Gross cost = Total Credits × Base Price = {total_credits} × ${base_price:.2f} = ${gross_cost:.2f}\n\n"
        f"Step 4: Since {total_credits} "
    )
    if total_credits > threshold_total_credits:
        solution += (
            f"> {threshold_total_credits}, apply a {synergy_discount:.2f}% discount:\n"
            f"  Net Cost = Gross Cost × (1 - Discount/100) = ${gross_cost:.2f} × (1 - {synergy_discount:.2f}/100) = ${net_cost:.2f}\n"
        )
    else:
        solution += (
            f"≤ {threshold_total_credits}, so no discount is applied.\n"
            f"  Net Cost = Gross Cost = ${net_cost:.2f}\n"
        )
    solution += f"Final Answer: The consortium’s combined net cost is ${net_cost:.2f}."
    return question, solution

# Advanced Scenario: Comprehensive Carbon Credit Strategy (function below is wrong)
# def advanced_comprehensive_carbon_credit_strategy():
#     """5:Advanced: Comprehensive Carbon Credit Strategy (6-step reasoning)"""
#     investor_name = random.choice(investor_names)
#     company_name = random.choice(company_names)
#     # Use a larger investment to ensure surplus credits
#     initial_investment = random.randint(20000, 50000)  # dollars available for purchase
#     base_price = round(random.uniform(10, 20), 2)
#     volume_discount = round(random.uniform(5, 10), 2)  # discount percentage on purchase
#     credits_required_for_offset = random.randint(200, 500)  # credits needed for emission offset
#     selling_premium = round(random.uniform(10, 20), 2)   # premium percentage for selling surplus credits
#     rebate_amount = random.randint(500, 2000)  # additional fixed rebate in dollars
    
#     # Step 1: Calculate number of credits purchased (without discount)
#     credits_purchased = round(initial_investment / base_price)
#     # Step 2: Compute the discounted price per credit
#     discounted_price = round(base_price * (1 - volume_discount / 100), 2)
#     # Step 3: Determine total cost at the discounted price
#     total_cost = round(credits_purchased * discounted_price, 2)
#     # Step 4: Determine surplus credits (if any) beyond the required offset
#     surplus_credits = max(0, credits_purchased - credits_required_for_offset)
#     # Step 5: Calculate the selling price per credit with the premium applied
#     selling_price = round(discounted_price * (1 + selling_premium / 100), 2)
#     # Step 6: Compute revenue from selling the surplus credits
#     revenue = round(surplus_credits * selling_price, 2)
#     # Step 7: Calculate net financial impact: revenue plus rebate, minus the total cost
#     net_impact = round((revenue + rebate_amount) - total_cost, 2)
    
#     question = (
#         f"{investor_name} from {company_name} is executing a comprehensive carbon credit strategy. They invest ${initial_investment} "
#         f"to purchase credits at a base price of ${base_price:.2f} per credit. Due to volume, they get a {volume_discount:.2f}% discount. "
#         f"Their emissions offset target is {credits_required_for_offset} credits. Any surplus credits are sold at a premium of {selling_premium:.2f}% "
#         f"over the discounted price, and they also receive a rebate of ${rebate_amount}. Calculate the net financial impact of this strategy."
#     )
#     solution = (
#         f"Step 1: Calculate the total number of credits purchased:\n"
#         f"  Credits Purchased = Investment / Base Price = {initial_investment} / {base_price:.2f} ≈ {credits_purchased}\n\n"
#         f"Step 2: Apply the volume discount to get the discounted price:\n"
#         f"  Discounted Price = Base Price × (1 - Volume Discount/100) = {base_price:.2f} × (1 - {volume_discount:.2f}/100) = ${discounted_price:.2f}\n\n"
#         f"Step 3: Compute the total cost using the discounted price:\n"
#         f"  Total Cost = Credits Purchased × Discounted Price = {credits_purchased} × ${discounted_price:.2f} = ${total_cost:.2f}\n\n"
#         f"Step 4: Determine surplus credits available for sale:\n"
#         f"  Surplus Credits = Credits Purchased - Credits Required = {credits_purchased} - {credits_required_for_offset} = {surplus_credits}\n\n"
#         f"Step 5: Calculate the selling price per credit with the premium:\n"
#         f"  Selling Price = Discounted Price × (1 + Selling Premium/100) = ${discounted_price:.2f} × (1 + {selling_premium:.2f}/100) = ${selling_price:.2f}\n\n"
#         f"Step 6: Calculate revenue from selling surplus credits:\n"
#         f"  Revenue = Surplus Credits × Selling Price = {surplus_credits} × ${selling_price:.2f} = ${revenue:.2f}\n\n"
#         f"Step 7: Determine the net financial impact:\n"
#         f"  Net Impact = (Revenue + Rebate) - Total Cost = (${revenue:.2f} + ${rebate_amount}) - ${total_cost:.2f} = ${net_impact:.2f}\n"
#         f"Final Answer: The net financial impact is ${net_impact:.2f}."
#     )
#     return question, solution

def template_comprehensive_carbon_credit_strategy():
    """5:Advanced: Comprehensive Carbon Credit Strategy (7-step reasoning using discounted price in credit calculation)"""
    investor_name = random.choice(investor_names)
    company_name = random.choice(company_names)
    # Use a larger investment to ensure surplus credits
    initial_investment = random.randint(20000, 50000)  # dollars available for purchase
    base_price = round(random.uniform(10, 20), 2)
    volume_discount = round(random.uniform(5, 10), 2)  # discount percentage on purchase
    credits_required_for_offset = random.randint(200, 500)  # credits needed for emission offset
    selling_premium = round(random.uniform(10, 20), 2)   # premium percentage for selling surplus credits
    rebate_amount = random.randint(500, 2000)  # additional fixed rebate in dollars

    # Step 1: Calculate discounted price per credit
    discounted_price = base_price * (1 - volume_discount / 100)
    # Step 2: Calculate number of credits purchased using discounted price
    credits_purchased = initial_investment / discounted_price
    # Step 3: Determine surplus credits
    surplus_credits = max(0, credits_purchased - credits_required_for_offset)
    # Step 4: Selling price of surplus credits with premium
    selling_price = discounted_price * (1 + selling_premium / 100)
    # Step 5: Revenue from surplus credits
    revenue = surplus_credits * selling_price
    # Step 6: Total gain = revenue + rebate
    total_gain = revenue + rebate_amount
    # Step 7: Net financial impact
    net_impact = total_gain - initial_investment

    # Round only in final presentation
    question = (
        f"{investor_name} from {company_name} is executing a comprehensive carbon credit strategy. "
        f"They invest ${initial_investment} to purchase credits at a base price of ${base_price:.2f} per credit. "
        f"Due to volume, they get a {volume_discount:.2f}% discount. Their emissions offset target is {credits_required_for_offset} credits. "
        f"Any surplus credits are sold at a premium of {selling_premium:.2f}% over the discounted price, "
        f"and they also receive a rebate of ${rebate_amount}. Calculate the net financial impact of this strategy."
    )

    solution = (
        f"Step 1: Calculate the discounted price per credit:\n"
        f"  Discounted Price = Base Price × (1 - Volume Discount/100) = "
        f"${base_price:.2f} × (1 - {volume_discount:.2f}/100) = ${discounted_price:.6f}\n\n"
        
        f"Step 2: Calculate how many credits can be purchased using the discounted price:\n"
        f"  Credits Purchased = Investment / Discounted Price = "
        f"${initial_investment} / ${discounted_price:.6f} ≈ {credits_purchased:.2f} credits\n\n"
        
        f"Step 3: Determine surplus credits beyond the offset target:\n"
        f"  Surplus Credits = Credits Purchased - Emissions Offset Target = "
        f"{credits_purchased:.2f} - {credits_required_for_offset} = {surplus_credits:.2f} credits\n\n"
        
        f"Step 4: Calculate the selling price per surplus credit with premium:\n"
        f"  Selling Price = Discounted Price × (1 + Selling Premium/100) = "
        f"${discounted_price:.6f} × (1 + {selling_premium:.2f}/100) = ${selling_price:.6f}\n\n"
        
        f"Step 5: Compute revenue from selling surplus credits:\n"
        f"  Revenue = Surplus Credits × Selling Price = "
        f"{surplus_credits:.2f} × ${selling_price:.6f} = ${revenue:.2f}\n\n"
        
        f"Step 6: Add the rebate to calculate total financial gain:\n"
        f"  Total Gain = Revenue + Rebate = ${revenue:.2f} + ${rebate_amount} = ${total_gain:.2f}\n\n"
        
        f"Step 7: Determine the net financial impact:\n"
        f"  Net Impact = Total Gain - Initial Investment = ${total_gain:.2f} - ${initial_investment} = ${net_impact:.2f}\n"
        
        f"Final Answer: The net financial impact is ${net_impact:.2f}."
    )
    return question, solution


# Main method to generate and save the QA pairs
def main():
    """
    Generate one instance from each of the five templates and write the results to a JSONL file.
    """
    templates = [
        template_carbon_credit_purchase,
        template_carbon_credit_rebate,
        template_offset_cost_savings,
        template_multi_company_synergy,
        template_comprehensive_carbon_credit_strategy
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
    output_file = "../../testset/sustainable_finance/carbon_credits.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
