import random
import json

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_compliance_penalty():
    """Basic: Compliance penalty for over-limit exposure."""
    exposure = generate_random_value(100000, 500000)
    threshold = generate_random_value(80000, exposure - 1000)
    penalty_rate = generate_random_value(1, 10)
    question = (f"A company has a risk exposure of ${exposure:.2f} but the regulatory threshold is "
                f"${threshold:.2f}. If a penalty rate of {penalty_rate:.2f}% is applied on the excess exposure, "
                f"what is the penalty amount?")
    excess = exposure - threshold
    penalty = round(excess * penalty_rate / 100, 2)
    solution = ("Step 1: Determine the excess exposure by subtracting the threshold from the total exposure.\n"
                f"  Excess exposure = ${exposure:.2f} - ${threshold:.2f} = ${excess:.2f}.\n"
                "Step 2: Apply the penalty rate to the excess exposure.\n"
                f"  Penalty = ${excess:.2f} * ({penalty_rate:.2f}% / 100) = ${penalty:.2f}.")
    return question, solution

def template_capital_shortfall():
    """Basic: Capital shortfall for regulatory compliance."""
    current_capital = generate_random_value(50000, 300000)
    min_requirement = generate_random_value(current_capital + 1000, current_capital + 100000)
    question = (f"A firm has current capital of ${current_capital:.2f} but the regulatory minimum requirement is "
                f"${min_requirement:.2f}. What is the capital shortfall?")
    shortfall = round(min_requirement - current_capital, 2)
    solution = ("Step 1: Calculate the difference between the minimum capital requirement and the current capital.\n"
                f"  Shortfall = ${min_requirement:.2f} - ${current_capital:.2f} = ${shortfall:.2f}.")
    return question, solution

def template_capital_requirement():
    """Intermediate: Capital requirement evaluation."""
    current_capital = generate_random_value(50000, 300000)
    min_requirement = generate_random_value(current_capital + 1000, current_capital + 100000)
    question = (f"A bank reports a current capital of ${current_capital:.2f} while the regulator demands a "
                f"minimum capital of ${min_requirement:.2f}. What is the deficiency that needs to be addressed?")
    deficiency = round(min_requirement - current_capital, 2)
    solution = ("Step 1: Compare the current capital with the regulatory minimum.\n"
                f"  Deficiency = ${min_requirement:.2f} - ${current_capital:.2f} = ${deficiency:.2f}.")
    return question, solution

def template_liquidity_gap():
    """Intermediate: Liquidity gap in compliance."""
    liquid_assets = generate_random_value(50000, 200000)
    liquidity_requirement = generate_random_value(liquid_assets + 1000, liquid_assets + 50000)
    question = (f"A financial institution holds liquid assets valued at ${liquid_assets:.2f} while the liquidity "
                f"requirement is ${liquidity_requirement:.2f}. What is the liquidity gap?")
    gap = round(liquidity_requirement - liquid_assets, 2)
    solution = ("Step 1: Subtract the value of liquid assets from the liquidity requirement.\n"
                f"  Liquidity gap = ${liquidity_requirement:.2f} - ${liquid_assets:.2f} = ${gap:.2f}.")
    return question, solution

def template_multi_factor_regulatory_compliance():
    """Advanced: Multi-factor Regulatory Compliance Assessment."""
    exposure = generate_random_value(100000, 500000)
    threshold = generate_random_value(80000, exposure - 1000)
    penalty_rate = generate_random_value(1, 10)
    current_capital = generate_random_value(50000, 300000)
    min_capital = generate_random_value(current_capital + 1000, current_capital + 100000)
    liquid_assets = generate_random_value(50000, 200000)
    liquidity_requirement = generate_random_value(liquid_assets + 1000, liquid_assets + 50000)
    
    question = (f"A financial institution faces multiple regulatory requirements. It has a risk exposure of ${exposure:.2f} "
                f"with a regulatory threshold of ${threshold:.2f} and a penalty rate of {penalty_rate:.2f}%. Its current capital is "
                f"${current_capital:.2f} while the minimum capital requirement is ${min_capital:.2f}. Additionally, it holds "
                f"liquid assets worth ${liquid_assets:.2f} against a liquidity requirement of ${liquidity_requirement:.2f}. "
                f"Calculate the total regulatory penalty, defined as the sum of the compliance penalty, the capital shortfall, "
                f"and the liquidity gap.")
    
    compliance_penalty = round((exposure - threshold) * penalty_rate / 100, 2)
    capital_shortfall = round(min_capital - current_capital, 2)
    liquidity_gap = round(liquidity_requirement - liquid_assets, 2)
    total_penalty = round(compliance_penalty + capital_shortfall + liquidity_gap, 2)
    
    solution = ("Step 1: Compute the compliance penalty: \n"
                f"  Compliance penalty = (${exposure:.2f} - ${threshold:.2f}) * ({penalty_rate:.2f}% / 100) = ${compliance_penalty:.2f}.\n"
                "Step 2: Calculate the capital shortfall:\n"
                f"  Capital shortfall = ${min_capital:.2f} - ${current_capital:.2f} = ${capital_shortfall:.2f}.\n"
                "Step 3: Determine the liquidity gap:\n"
                f"  Liquidity gap = ${liquidity_requirement:.2f} - ${liquid_assets:.2f} = ${liquidity_gap:.2f}.\n"
                "Step 4: Sum the three components to get the total regulatory penalty:\n"
                f"  Total penalty = ${compliance_penalty:.2f} + ${capital_shortfall:.2f} + ${liquidity_gap:.2f} = ${total_penalty:.2f}.")
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_compliance_penalty,
        template_capital_shortfall,
        template_capital_requirement,
        template_liquidity_gap,
        template_multi_factor_regulatory_compliance
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
    output_file = "../../testset/risk_management/regulatory_compliance.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()