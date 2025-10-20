import random
import json

def template_market_downturn_revenue():
    """Basic:Market downturn impact on revenue."""
    initial_revenue = round(random.uniform(100000, 500000), 2)
    downturn = round(random.uniform(5, 20), 2)
    new_revenue = round(initial_revenue * (1 - downturn / 100), 2)
    question = f"A company with an initial revenue of ${initial_revenue:.2f} experiences a market downturn causing a {downturn:.2f}% decrease in revenue. What is the new revenue?"
    solution = "Step 1: Recognize that a downturn of {:.2f}% reduces the revenue by that fraction.".format(downturn)
    solution += f"\nStep 2: The new revenue is computed by reducing the original revenue by {downturn:.2f}%."
    solution += f"\nStep 3: Thus, new revenue = ${initial_revenue:.2f} * (1 - {downturn:.2f}/100) = ${new_revenue:.2f}."
    return question, solution

def template_operating_cost_increase():
    """Basic:Operating cost sensitivity."""
    initial_cost = round(random.uniform(50000, 250000), 2)
    increase = round(random.uniform(3, 15), 2)
    new_cost = round(initial_cost * (1 + increase / 100), 2)
    question = f"A firm has operating costs of ${initial_cost:.2f}. If operating costs increase by {increase:.2f}%, what is the new operating cost?"
    solution = "Step 1: An increase of {:.2f}% means the cost rises by that proportion.".format(increase)
    solution += f"\nStep 2: The new cost is obtained by increasing the original cost by {increase:.2f}%."
    solution += f"\nStep 3: Therefore, new operating cost = ${initial_cost:.2f} * (1 + {increase:.2f}/100) = ${new_cost:.2f}."
    return question, solution

def template_revenue_recovery_effect():
    """Intermediate:Revenue recovery effect after downturn."""
    initial_revenue = round(random.uniform(200000, 800000), 2)
    downturn = round(random.uniform(10, 30), 2)
    recovery = round(random.uniform(5, 20), 2)
    new_revenue = round(initial_revenue * (1 - downturn / 100) * (1 + recovery / 100), 2)
    question = f"A company with an initial revenue of ${initial_revenue:.2f} experiences a downturn of {downturn:.2f}% and then recovers by {recovery:.2f}%. What is the new revenue after recovery?"
    solution = "Step 1: The revenue declines by {:.2f}% due to the downturn.".format(downturn)
    solution += f"\nStep 2: Afterwards, the revenue recovers by {recovery:.2f}%, increasing the reduced revenue."
    solution += f"\nStep 3: Hence, new revenue = ${initial_revenue:.2f} * (1 - {downturn:.2f}/100) * (1 + {recovery:.2f}/100) = ${new_revenue:.2f}."
    return question, solution

def template_interest_rate_impact():
    """Intermediate:Interest rate impact on financing cost."""
    loan_amount = round(random.uniform(500000, 2000000), 2)
    rate_change = round(random.uniform(0.5, 3.0), 2)
    sensitivity = round(random.uniform(0.5, 2.0), 2)
    additional_cost = round(loan_amount * (rate_change / 100) * sensitivity, 2)
    question = f"A company has a loan of ${loan_amount:.2f}. If interest rates increase by {rate_change:.2f}% and the financing cost sensitivity is {sensitivity:.2f}, what is the additional financing cost?"
    solution = "Step 1: Recognize that an interest rate increase affects the financing cost proportionally."
    solution += f"\nStep 2: Multiply the loan amount by the rate change ({rate_change:.2f}%) and the sensitivity ({sensitivity:.2f})."
    solution += f"\nStep 3: Thus, additional cost = ${loan_amount:.2f} * ({rate_change:.2f}/100) * {sensitivity:.2f} = ${additional_cost:.2f}."
    return question, solution

def template_investment_scenario_planning():
    """Advanced:Multi-factor scenario on investment value."""
    initial_investment = round(random.uniform(1000000, 5000000), 2)
    market_change = round(random.uniform(-10, 10), 2)
    interest_change = round(random.uniform(-5, 5), 2)
    inflation_change = round(random.uniform(-3, 3), 2)
    market_sens = round(random.uniform(0.5, 2.5), 2)
    interest_sens = round(random.uniform(0.5, 2.5), 2)
    inflation_sens = round(random.uniform(0.5, 2.5), 2)
    delta_value = round(initial_investment * (market_sens * (market_change / 100) + interest_sens * (interest_change / 100) + inflation_sens * (inflation_change / 100)), 2)
    question = f"An investment of ${initial_investment:.2f} is influenced by multiple factors: market change of {market_change:.2f}%, interest rate change of {interest_change:.2f}%, and inflation change of {inflation_change:.2f}% with sensitivities {market_sens:.2f}, {interest_sens:.2f}, and {inflation_sens:.2f}, respectively. What is the overall change in the investment value?"
    solution = "Step 1: Each factor influences the investment value based on its sensitivity."
    solution += f"\nStep 2: Evaluate each impact: market ({market_sens:.2f} * {market_change/100:.4f}), interest ({interest_sens:.2f} * {interest_change/100:.4f}), and inflation ({inflation_sens:.2f} * {inflation_change/100:.4f})."
    solution += f"\nStep 3: Sum these contributions and multiply by the initial investment ${initial_investment:.2f} to obtain ${delta_value:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    # List of template functions
    templates = [
        template_market_downturn_revenue,
        template_operating_cost_increase,
        template_revenue_recovery_effect,
        template_interest_rate_impact,
        template_investment_scenario_planning
    ]
    # List to store all generated problems
    all_problems = []
    # Generate 10 problems for each template
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
    output_file = "../../testset/risk_management/scenario_planning.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()