import random
import json

def generate_random_value(min_val, max_val):
    return round(random.uniform(min_val, max_val), 2)

def template_portfolio_var():
    """1:Basic: Portfolio Value at Risk (VaR) calculation."""
    portfolio_value = generate_random_value(100000, 500000)
    volatility = round(random.uniform(5, 20), 2)  # percent daily volatility
    z_score = 1.65  # approximate z-score for 95% confidence
    var = round(portfolio_value * (volatility / 100) * z_score, 2)
    question = f"A portfolio valued at ${portfolio_value} has a daily volatility of {volatility:.2f}%. Using a 95% confidence level (z-score = {z_score}), what is its Value at Risk (VaR) in USD?"
    solution = ("Step 1: Recognize that VaR is determined by multiplying the portfolio value, "
                "the volatility (as a decimal), and the z-score for the 95% confidence level.\n"
                "Step 2: Convert the volatility percentage to a decimal and multiply:\n"
                f"  VaR = ${portfolio_value} * ({volatility}/100) * {z_score} = ${var:.2f}.\n"
                "Step 3: The final VaR represents the expected maximum loss at 95% confidence.")
    return question, solution

def template_stock_sensitivity():
    """1:Basic: Stock Downside Sensitivity."""
    stock_price = generate_random_value(50, 200)
    drop_percentage = round(random.uniform(5, 15), 2)
    loss = round(stock_price * (drop_percentage / 100), 2)
    question = f"A stock priced at ${stock_price} experiences a decline of {drop_percentage:.2f}%. What is the absolute loss in USD?"
    solution = ("Step 1: Understand that the loss is calculated by taking the percentage decline of the stock price.\n"
                "Step 2: Convert the decline percentage to a decimal and multiply with the stock price:\n"
                f"  Loss = ${stock_price} * ({drop_percentage}/100) = ${loss:.2f}.\n"
                "Step 3: The resulting value is the absolute loss in USD.")
    return question, solution

def template_liquidity_risk():
    """2:Intermediate: Liquidity Risk Impact via Bid-Ask Spread."""
    portfolio_value = generate_random_value(50000, 300000)
    bid_ask_spread = round(random.uniform(0.1, 1.0), 2)  # percent
    additional_cost = round(portfolio_value * (bid_ask_spread / 100), 2)
    question = f"A portfolio valued at ${portfolio_value} faces a bid-ask spread of {bid_ask_spread:.2f}% due to liquidity risk. What is the additional cost in USD due to this spread?"
    solution = ("Step 1: The additional cost from liquidity risk is determined by the bid-ask spread applied to the portfolio value.\n"
                "Step 2: Convert the bid-ask spread percentage to a decimal and multiply with the portfolio value:\n"
                f"  Additional Cost = ${portfolio_value} * ({bid_ask_spread}/100) = ${additional_cost:.2f}.\n"
                "Step 3: The final value represents the extra cost incurred due to the spread.")
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
    """3:Advanced: Multi-Factor Portfolio Risk Impact."""
    portfolio_value = generate_random_value(100000, 1000000)
    # Generate three random weights that sum approximately to 100%
    w1 = random.randint(20, 50)
    w2 = random.randint(20, 50)
    w3 = 100 - w1 - w2
    if w3 < 0:
        w3 = random.randint(10, 30)
        total = w1 + w2 + w3
        w1 = int(w1 / total * 100)
        w2 = int(w2 / total * 100)
        w3 = 100 - w1 - w2
    sensitivities = [round(random.uniform(-2, 2), 2) for _ in range(3)]
    factor_changes = [round(random.uniform(-3, 3), 2) for _ in range(3)]
    impact = sum(portfolio_value * (w/100) * (fc/100) * s for w, fc, s in zip([w1, w2, w3], factor_changes, sensitivities))
    impact = round(impact, 2)
    question = (f"A portfolio valued at ${portfolio_value} is exposed to three risk factors: market volatility, liquidity spread, and credit spread. "
                f"Their respective weights are {w1}%, {w2}%, and {w3}%. Their sensitivities are {sensitivities[0]:.2f}, {sensitivities[1]:.2f}, and {sensitivities[2]:.2f}, "
                f"and the corresponding changes in these factors are {factor_changes[0]:.2f}%, {factor_changes[1]:.2f}%, and {factor_changes[2]:.2f}%. "
                "What is the overall portfolio risk impact in USD?")
    solution = ("Step 1: For each risk factor, compute its impact by multiplying the portfolio value, the factor's weight (as a decimal), "
                "the change in the factor (as a decimal), and its sensitivity.\n"
                "Step 2: Sum the impacts of all risk factors to get the overall effect:\n"
                f"  Overall Impact = ${impact:.2f}.\n"
                "Step 3: The resulting value represents the portfolio's risk impact in USD.")
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_portfolio_var,
        template_stock_sensitivity,
        template_liquidity_risk,
        template_volatility_sensitivity,
        template_multi_factor_portfolio
    ]

    all_problems = []

    for template_func in templates:
        id_val = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()

        for i in range(10):
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            question, solution = template_func()
            problem_entry = {
                "seed": seed,
                "id": id_val,
                "level": level,
                "question": question,
                "solution": solution
            }
            all_problems.append(problem_entry)
            random.seed()

    random.shuffle(all_problems)
    output_file = "../../testset/risk_management/risk_metrics.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()