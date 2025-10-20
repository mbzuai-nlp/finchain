import random
import json

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_portfolio_single_factor():
    """1:Basic: Single factor stress on portfolio."""
    portfolio_value = generate_random_value(100000, 500000)
    factor_change = round(random.uniform(-5, 5), 2)
    sensitivity = round(random.uniform(-1, 1), 2)
    question = f"A portfolio valued at ${portfolio_value} experiences a stress test with a factor change of {factor_change:.2f}%. Given a sensitivity of {sensitivity:.2f}, what is the expected impact on the portfolio value?"
    impact = portfolio_value * (factor_change / 100) * sensitivity
    solution = "Step 1: Interpret the stress factor as a percentage effect on the portfolio.\n"
    solution += "Step 2: Assess the impact by combining the percentage change with the asset sensitivity.\n"
    solution += f"Overall, the expected impact is ${impact:.2f}."
    return question, solution

def template_sensitivity_of_stock():
    """2:Basic: Stock sensitivity to external shock."""
    stock_value = generate_random_value(50, 500)
    shock = round(random.uniform(-10, 10), 2)
    sensitivity = round(random.uniform(-2, 2), 2)
    question = f"A stock valued at ${stock_value} faces an external shock of {shock:.2f}%. With a sensitivity of {sensitivity:.2f}, what is the impact on the stock price?"
    impact = stock_value * (shock / 100) * sensitivity
    solution = "Step 1: Understand that the shock changes the stock value proportionally based on sensitivity.\n"
    solution += "Step 2: Combine the shock magnitude and sensitivity to estimate the effect.\n"
    solution += f"The computed impact on the stock price is ${impact:.2f}."
    return question, solution

def template_multi_asset_portfolio():
    """3:Intermediate: Multi-asset portfolio with interest rate sensitivity."""
    portfolio_value = round(random.uniform(50000, 200000), 2)
    raw_weights = [random.randint(10, 50) for _ in range(3)]
    total_raw = sum(raw_weights)
    asset_weights = [round(w / total_raw * 100, 2) for w in raw_weights]
    factor_change = round(random.uniform(-4, 4), 2)
    sensitivities = [round(random.uniform(-1.5, 1.5), 2) for _ in range(3)]
    question = (f"A portfolio worth ${portfolio_value:.2f} has 3 asset classes with weights "
                f"{asset_weights[0]}%, {asset_weights[1]}%, and {asset_weights[2]}%, respectively. "
                f"Their sensitivities to interest rate changes are {sensitivities[0]:.2f}, {sensitivities[1]:.2f}, "
                f"and {sensitivities[2]:.2f}. If interest rates change by {factor_change:.2f}%, how does the portfolio value change?")
    total_change = round(
        sum(
            portfolio_value * (weight / 100) * (factor_change / 100) * sensitivity
            for weight, sensitivity in zip(asset_weights, sensitivities)
        ),
        2,
    )
    solution = "Step 1: Calculate contribution for each asset:\n"
    for i in range(3):
        impact = round(portfolio_value * (asset_weights[i] / 100) * (factor_change / 100) * sensitivities[i], 2)
        solution += f"  Asset {i+1}: ${portfolio_value:.2f} * {asset_weights[i] / 100:.2f} * {factor_change/100:.4f} * {sensitivities[i]:.2f} = ${impact:.2f}\n"
    solution += f"Step 2: Sum the contributions to get the total change: ${total_change:.2f}."
    return question, solution

def template_volatility_sensitivity():
    """2:Intermediate: Option Vega Sensitivity to Volatility Change."""
    option_value = generate_random_value(1000, 10000)
    vega = round(random.uniform(1, 50), 2)
    vol_change = round(random.uniform(-5, 5), 2)
    impact = round(vega * vol_change, 2)
    question = (f"An option valued at ${option_value} has a vega of ${vega:.2f} per 1% vol. "
                f"If the underlying asset's volatility changes by {vol_change:.2f}%, "
                "what is the expected change in the option's value in USD?")
    solution = (
        "Step 1: Vega measures sensitivity of option value to volatility (USD per 1% vol).\n"
        "Step 2: Compute change = Vega × ΔVol (in percentage points):\n"
        f"  Change = ${vega:.2f} × ({vol_change:.2f}) = ${impact:.2f}.\n"
        "Step 3: The final outcome represents the expected change in the option's value due to the volatility shift."
    )
    return question, solution

def template_multi_factor_portfolio():
    """5:Advanced: Multi-factor stress testing on diversified portfolio."""
    portfolio_value = generate_random_value(200000, 1000000)
    credit_shock = round(random.uniform(-6, 6), 2)
    market_shock = round(random.uniform(-4, 4), 2)
    credit_sensitivity = round(random.uniform(-1.5, 1.5), 2)
    market_sensitivity = round(random.uniform(-1.5, 1.5), 2)
    question = f"A diversified portfolio worth ${portfolio_value} undergoes two simultaneous stress tests: a credit shock of {credit_shock:.2f}% and a market shock of {market_shock:.2f}%. With credit sensitivity of {credit_sensitivity:.2f} and market sensitivity of {market_sensitivity:.2f}, what is the combined impact on the portfolio value?"
    credit_impact = portfolio_value * (credit_shock / 100) * credit_sensitivity
    market_impact = portfolio_value * (market_shock / 100) * market_sensitivity
    total_impact = credit_impact + market_impact
    solution = "Step 1: Assess the impact of the credit shock based on its sensitivity.\n"
    solution += "Step 2: Assess the impact of the market shock similarly.\n"
    solution += "Step 3: Sum both impacts to obtain the overall effect.\n"
    solution += f"The combined impact on the portfolio is ${total_impact:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_portfolio_single_factor,
        template_sensitivity_of_stock,
        template_multi_asset_portfolio,
        template_volatility_sensitivity,
        template_multi_factor_portfolio
    ]
    all_problems = []
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        for i in range(10):
            seed_val = random.randint(1000000000, 4000000000)
            random.seed(seed_val)
            question, solution = template_func()
            problem_entry = {
                "seed": seed_val,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            all_problems.append(problem_entry)
            random.seed()
    random.shuffle(all_problems)
    output_file = "../../testset/risk_management/stress_testing.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
