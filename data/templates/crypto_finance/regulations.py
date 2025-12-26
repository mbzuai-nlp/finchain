import random
import json

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_crypto_tax_penalty():
    """1:Basic: Crypto exchange tax penalty calculation."""
    transaction_volume = generate_random_value(10000, 50000)
    penalty_rate = round(random.uniform(2, 5), 2)
    question = f"A crypto exchange processed transactions worth ${transaction_volume:.2f} USD. Due to non-compliance with tax regulations, a penalty of {penalty_rate:.2f}% is imposed. What is the penalty amount in USD?"
    penalty_amount = round(transaction_volume * (penalty_rate / 100), 2)
    solution = f"Step 1: Convert the penalty rate to decimal: {penalty_rate/100:.4f}.\n"
    solution += f"Step 2: Multiply the transaction volume ${transaction_volume:.2f} by the penalty rate in decimal to obtain ${penalty_amount:.2f}.\n"
    solution += f"Step 3: The penalty amount is ${penalty_amount:.2f}."
    return question, solution

def template_compliance_fee_adjustment():
    """2:Basic: Crypto compliance fee adjustment."""
    base_fee = generate_random_value(500, 2000)
    adjustment_factor = round(random.uniform(1.05, 1.20), 2)
    question = f"A crypto firm has a base compliance fee of ${base_fee:.2f} USD. Following new regulations, this fee is adjusted by a factor of {adjustment_factor:.2f}. What is the adjusted fee in USD?"
    adjusted_fee = round(base_fee * adjustment_factor, 2)
    solution = f"Step 1: Multiply the base fee ${base_fee:.2f} by the adjustment factor {adjustment_factor:.2f}.\n"
    solution += f"Step 2: The adjusted fee is ${adjusted_fee:.2f}."
    return question, solution

def template_regulatory_impact():
    """3:Intermediate: Regulatory impact on listing fee."""
    current_fee = generate_random_value(1000, 5000)
    impact_percentage = round(random.uniform(1, 10), 2)
    question = f"A crypto exchange charges a listing fee of ${current_fee:.2f} USD. In response to new regulations, this fee is increased by {impact_percentage:.2f}%. What is the increase in the fee amount in USD?"
    increase_amount = round(current_fee * (impact_percentage / 100), 2)
    solution = f"Step 1: Convert the impact percentage to decimal: {impact_percentage/100:.4f}.\n"
    solution += f"Step 2: Multiply the current fee ${current_fee:.2f} by the decimal impact to obtain an increase of ${increase_amount:.2f}.\n"
    solution += f"Step 3: The increase in fee amount is ${increase_amount:.2f}."
    return question, solution

def template_trade_cost_adjustment():
    """3:Intermediate: Regulatory-imposed trade cost adjustment."""
    original_cost = generate_random_value(50, 300)
    regulation_multiplier = round(random.uniform(1.10, 1.50), 2)
    question = f"Due to enhanced regulatory requirements, a crypto platform adjusts its trade cost of ${original_cost:.2f} USD per transaction by a multiplier of {regulation_multiplier:.2f}. What is the additional cost per trade in USD?"
    additional_cost = round(original_cost * (regulation_multiplier - 1), 2)
    solution = f"Step 1: Determine the multiplier increase by subtracting 1 from {regulation_multiplier:.2f} to get {regulation_multiplier - 1:.2f}.\n"
    solution += f"Step 2: Multiply the original cost ${original_cost:.2f} USD by the increase factor {regulation_multiplier - 1:.2f}.\n"
    solution += f"Step 3: The additional cost per trade is ${additional_cost:.2f}."
    return question, solution

def template_multi_factor_regulatory_risk():
    """4:Advanced: Multi-factor regulatory compliance cost evaluation."""
    baseline_cost = generate_random_value(10000, 50000)
    factor_a = round(random.uniform(0.05, 0.15), 2)
    factor_b = round(random.uniform(0.02, 0.10), 2)
    factor_c = round(random.uniform(0.03, 0.08), 2)
    total_factor = factor_a + factor_b + factor_c
    question = f"A crypto firm has a baseline compliance cost of ${baseline_cost:.2f} USD. New regulatory measures impose additional cost factors from audit frequency ({factor_a*100:.2f}%), regulatory fines ({factor_b*100:.2f}%), and compliance surcharge ({factor_c*100:.2f}%). Assuming these factors add linearly, what is the total additional cost incurred in USD?"
    additional_cost = round(baseline_cost * total_factor, 2)
    solution = f"Step 1: Sum the regulatory cost factors: {factor_a:.2f} + {factor_b:.2f} + {factor_c:.2f} = {total_factor:.2f}.\n"
    solution += f"Step 2: Multiply the baseline cost ${baseline_cost:.2f} by the total factor {total_factor:.2f}.\n"
    solution += f"Step 3: The total additional cost incurred is ${additional_cost:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_crypto_tax_penalty,
        template_compliance_fee_adjustment,
        template_regulatory_impact,
        template_trade_cost_adjustment,
        template_multi_factor_regulatory_risk
    ]
    all_problems = []
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        for i in range(10):
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            question, solution = template_func()
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            all_problems.append(problem_entry)
            random.seed()
    random.shuffle(all_problems)
    output_file = "../../testset/crypto_finance/regulations.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()