import random
import json

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_capital_allocation_risk_appetite():
    """1:Basic: Capital allocation based on risk appetite."""
    risk_score = generate_random_value(10, 90)  # risk appetite score in percentage
    capital = generate_random_value(50000, 200000)  # total capital in USD
    question = (f"A company with a risk appetite score of {risk_score:.2f}% and total capital of ${capital:.2f} "
                f"allocates high-risk investments equal to its risk appetite percentage of its capital. "
                f"What is the maximum dollar value allocated for high-risk investments?")
    allocated = round(capital * (risk_score / 100), 2)
    solution = ("Step 1: Recognize that the high-risk allocation equals the risk appetite percentage of the total capital.\n"
                f"Step 2: Compute allocation = ${capital:.2f} * ({risk_score:.2f} / 100) = ${allocated:.2f}.\n"
                "This is the maximum dollar value allocated for high-risk investments.")
    return question, solution

def template_risk_threshold_measurement():
    """2:Basic: Determine risk threshold in risk management."""
    risk_appetite = generate_random_value(5, 50)  # risk appetite in percentage
    baseline_capital = generate_random_value(100000, 300000)  # baseline capital in USD
    question = (f"A firm sets its risk threshold based on a risk appetite of {risk_appetite:.2f}% applied to a baseline capital of ${baseline_capital:.2f}. "
                f"What is the risk threshold in USD?")
    threshold = round(baseline_capital * (risk_appetite / 100), 2)
    solution = ("Step 1: Understand that the risk threshold is computed as the baseline capital multiplied by the risk appetite percentage.\n"
                f"Step 2: Calculate threshold = ${baseline_capital:.2f} * ({risk_appetite:.2f} / 100) = ${threshold:.2f}.\n"
                "This is the risk threshold in USD.")
    return question, solution

def template_risk_adjusted_return():
    """3:Intermediate: Risk adjusted capital allocation."""
    capital = generate_random_value(100000, 500000)  # total capital in USD
    risk_factor = generate_random_value(5, 25)  # risk factor in percentage
    risk_premium = generate_random_value(1, 10)  # additional risk premium in percentage
    question = (f"A portfolio with a capital of ${capital:.2f} uses a risk factor of {risk_factor:.2f}% and "
                f"an additional risk premium of {risk_premium:.2f}% to determine extra capital allocation for high-risk opportunities. "
                f"Calculate the additional capital allocated.")
    allocation = round(capital * (risk_factor / 100) * (risk_premium / 100), 2)
    solution = ("Step 1: Recognize that extra capital allocation is determined by multiplying the capital with the risk factor and then by the risk premium ratio.\n"
                f"Step 2: Compute allocation = ${capital:.2f} * ({risk_factor:.2f} / 100) * ({risk_premium:.2f} / 100) = ${allocation:.2f}.\n"
                "This is the additional capital allocated for high-risk opportunities.")
    return question, solution

def template_risk_exposure_limit():
    """4:Intermediate: Maximum risk exposure based on risk appetite."""
    assets = generate_random_value(200000, 800000)  # total assets in USD
    risk_appetite = generate_random_value(10, 40)  # risk appetite in percentage
    question = (f"A bank with total assets of ${assets:.2f} determines its maximum risk exposure by applying its risk appetite of {risk_appetite:.2f}%. "
                f"What is the maximum risk exposure in USD?")
    exposure = round(assets * (risk_appetite / 100), 2)
    solution = ("Step 1: Understand that maximum risk exposure is derived by applying the risk appetite percentage to total assets.\n"
                f"Step 2: Calculate exposure = ${assets:.2f} * ({risk_appetite:.2f} / 100) = ${exposure:.2f}.\n"
                "This is the maximum risk exposure in USD.")
    return question, solution

def template_multi_factor_risk_appetite_assessment():
    """5:Advanced: Multi-factor risk appetite assessment."""
    capital = generate_random_value(500000, 2000000)  # base capital in USD
    risk_score = generate_random_value(20, 70)  # risk appetite score in percentage
    volatility = generate_random_value(0.50, 10)  # market volatility in percentage
    question = (f"A financial institution with a base capital of ${capital:.2f} has a risk appetite score of {risk_score:.2f}%. "
                f"In a high volatility environment with a volatility measure of {volatility:.2f}%, the risk appetite is adjusted "
                f"by a factor of (1 + volatility/100). What is the adjusted risk threshold in USD?")
    adjusted_threshold = round(capital * (risk_score / 100) * (1 + volatility / 100), 2)
    solution = ("Step 1: Recognize that the base risk threshold is calculated as capital multiplied by the risk appetite percentage.\n"
                "Step 2: Adjust the risk threshold by the market volatility factor, computed as (1 + volatility/100).\n"
                f"Step 3: Therefore, adjusted threshold = ${capital:.2f} * ({risk_score:.2f} / 100) * (1 + {volatility:.2f} / 100) = ${adjusted_threshold:.2f}.\n"
                "This is the adjusted risk threshold in USD.")
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_capital_allocation_risk_appetite,
        template_risk_threshold_measurement,
        template_risk_adjusted_return,
        template_risk_exposure_limit,
        template_multi_factor_risk_appetite_assessment
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
    output_file = "../../testset/risk_management/risk_appetite.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()