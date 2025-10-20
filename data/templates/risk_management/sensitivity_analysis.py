import random
import json

def template_portfolio_single_factor():
    """1:Basic: Single-asset sensitivity to interest rate."""
    portfolio_value = round(random.uniform(10000, 50000), 2)
    factor_change = round(random.uniform(-5, 5), 2)
    sensitivity = round(random.uniform(-1.5, 1.5), 2)
    question = f"A single asset valued at ${portfolio_value:.2f} has a sensitivity of {sensitivity:.2f} to changes in interest rates. If interest rates change by {factor_change:.2f}%, what is the change in the asset's value?"
    solv = round(portfolio_value * (factor_change/100) * sensitivity, 2)
    solution = f"Step 1: Multiply asset value (${portfolio_value:.2f}) by the interest rate change factor ({factor_change/100:.4f}) and sensitivity ({sensitivity:.2f}) to obtain ${solv:.2f}."
    return question, solution

def template_stock_sensitivity():
    """2:Basic: Stock price sensitivity to market index change."""
    stock_price = round(random.uniform(50, 500), 2)
    market_change = round(random.uniform(-3, 3), 2)
    sensitivity = round(random.uniform(-1.0, 1.0), 2)
    question = f"A stock priced at ${stock_price:.2f} exhibits a sensitivity of {sensitivity:.2f} when the market index changes. If the market index shifts by {market_change:.2f}%, what is the expected change in the stock price?"
    solv = round(stock_price * (market_change/100) * sensitivity, 2)
    solution = f"Step 1: Multiply stock price (${stock_price:.2f}) by market change factor ({market_change/100:.4f}) and sensitivity ({sensitivity:.2f}) to get ${solv:.2f}."
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
    solv = sum((portfolio_value * (weight / 100) * (factor_change / 100) * sensitivity) for weight, sensitivity in zip(asset_weights, sensitivities))
    solution = "Step 1: Calculate contribution for each asset:\n"
    for i in range(3):
        impact = round(portfolio_value * (asset_weights[i] / 100) * (factor_change / 100) * sensitivities[i], 2)
        solution += f"  Asset {i+1}: ${portfolio_value:.2f} * {asset_weights[i] / 100:.2f} * {factor_change/100:.4f} * {sensitivities[i]:.2f} = ${impact:.2f}\n"
    solution += f"Step 2: Sum the contributions to get the total change: ${solv:.2f}."
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
    solution = ("Step 1: Vega measures sensitivity of option value to volatility (USD per 1% vol).\n"
        "Step 2: Compute change = Vega × ΔVol (in percentage points):\n"
        f"  Change = ${vega:.2f} × ({vol_change:.2f}) = ${impact:.2f}.\n"
        "Step 3: The final outcome represents the expected change in the option's value due to the volatility shift.")
    return question, solution

def template_multi_factor_portfolio():
    """5:Advanced: Multi-factor sensitivity in portfolio."""
    portfolio_value = round(random.uniform(100000, 500000), 2)
    interest_rate_change = round(random.uniform(-3, 3), 2)
    market_change = round(random.uniform(-4, 4), 2)
    credit_spread_change = round(random.uniform(-2, 2), 2)
    sensitivity_interest = round(random.uniform(-2, 2), 2)
    sensitivity_market = round(random.uniform(-2, 2), 2)
    sensitivity_credit = round(random.uniform(-2, 2), 2)
    question = (f"A portfolio valued at ${portfolio_value:.2f} has sensitivities of {sensitivity_interest:.2f}, "
                f"{sensitivity_market:.2f}, and {sensitivity_credit:.2f} to changes in interest rates, market index, and credit spreads, respectively. "
                f"If interest rates, market index, and credit spreads change by {interest_rate_change:.2f}%, {market_change:.2f}%, and {credit_spread_change:.2f}%, "
                f"what is the overall change in the portfolio value?")
    contrib_interest = portfolio_value * (interest_rate_change/100) * sensitivity_interest
    contrib_market = portfolio_value * (market_change/100) * sensitivity_market
    contrib_credit = portfolio_value * (credit_spread_change/100) * sensitivity_credit
    solv = round(contrib_interest + contrib_market + contrib_credit, 2)
    solution = "Step 1: Calculate individual contributions:\n"
    solution += f"  Interest rate impact: ${portfolio_value:.2f} * {interest_rate_change/100:.4f} * {sensitivity_interest:.2f} = ${round(contrib_interest,2):.2f}\n"
    solution += f"  Market index impact: ${portfolio_value:.2f} * {market_change/100:.4f} * {sensitivity_market:.2f} = ${round(contrib_market,2):.2f}\n"
    solution += f"  Credit spread impact: ${portfolio_value:.2f} * {credit_spread_change/100:.4f} * {sensitivity_credit:.2f} = ${round(contrib_credit,2):.2f}\n"
    solution += f"Step 2: Sum the impacts to obtain the total change: ${solv:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_portfolio_single_factor,
        template_stock_sensitivity,
        template_multi_asset_portfolio,
        template_volatility_sensitivity,
        template_multi_factor_portfolio
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
    output_file = "../../testset/risk_management/sensitivity_analysis.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()