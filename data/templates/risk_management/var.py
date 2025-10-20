import random
import json
from scipy.stats import norm

def generate_random_value(min_val, max_val):
    return round(random.uniform(min_val, max_val), 2)

def template_single_asset_var():
    """Basic: Single asset portfolio VaR calculation."""
    portfolio_value = generate_random_value(10000, 50000)
    volatility = round(random.uniform(1.00, 5.00), 2)  # Daily volatility in %
    time_horizon = random.randint(1, 5)  # in days
    confidence = round(random.uniform(90.00, 99.00), 2)  # Confidence level in %
    risk_multiplier = 1 + ((100 - confidence) / 100)
    sqrt_time = round(time_horizon**0.5, 2)
    var_value = round(portfolio_value * (volatility / 100) * sqrt_time * risk_multiplier, 2)
    
    question = (f"A portfolio valued at ${portfolio_value} has a daily volatility of {volatility}% over a time horizon of {time_horizon} days "
                f"at a confidence level of {confidence}%. What is the estimated Value at Risk (VaR) in USD?")
    
    solution = "Step 1: Convert the daily volatility to a factor: volatility factor = " + f"{volatility/100:.4f}.\n"
    solution += f"Step 2: Account for the time horizon using the square root: sqrt({time_horizon}) = {sqrt_time}.\n"
    solution += f"Step 3: Apply the confidence adjustment with a multiplier of {risk_multiplier:.2f}.\n"
    solution += "Step 4: Compute VaR as: portfolio_value * volatility_factor * sqrt_time * risk_multiplier.\n"
    solution += f"Resulting VaR = ${var_value:.2f}."
    
    return question, solution

def template_stock_return_var():
    """Basic: Stock return VaR under market risk."""
    asset_value = generate_random_value(5000, 20000)
    loss_percent = round(random.uniform(0.50, 3.00), 2)  # Expected loss percentage
    confidence = round(random.uniform(90.00, 95.00), 2)
    z = norm.ppf(confidence / 100)
    var_value = round(asset_value * (loss_percent / 100) * z, 2)
    question = (f"A stock valued at ${asset_value} is expected to experience a loss of {loss_percent}% under adverse market conditions "
                f"at a confidence level of {confidence}%. What is the Value at Risk (VaR) in USD?")
    
    solution = "Step 1: Convert the loss percentage to a decimal factor: " + f"{loss_percent/100:.4f}.\n"
    solution += f"Step 2: Retrieve the z-score for {confidence:.2f}% confidence: z = {z:.4f}.\n"
    solution += "Step 3: Compute VaR as: asset value × loss factor × z.\n"
    solution += f"Resulting VaR = ${var_value:.2f}."
    
    return question, solution

def template_multi_asset_var():
    """Intermediate: Multi-asset portfolio VaR with diversification."""
    portfolio_value = generate_random_value(50000, 200000)
    w1 = random.randint(20, 40)
    w2 = random.randint(20, 40)
    w3 = 100 - (w1 + w2)
    asset_weights = [w1, w2, w3]
    volatilities = [round(random.uniform(1.00, 4.00), 2) for _ in range(3)]
    time_horizon = random.randint(1, 5)
    confidence = round(random.uniform(90.00, 99.00), 2)
    risk_multiplier = 1 + ((100 - confidence) / 100)
    sqrt_time = round(time_horizon**0.5, 2)
    weighted_vol = sum((w/100.0)*v for w, v in zip(asset_weights, volatilities))
    var_value = round(portfolio_value * (weighted_vol / 100) * sqrt_time * risk_multiplier, 2)
    
    question = (f"A portfolio valued at ${portfolio_value} is diversified among three assets with weights {asset_weights[0]}%, "
                f"{asset_weights[1]}%, and {asset_weights[2]}%, and corresponding volatilities of {volatilities[0]}%, "
                f"{volatilities[1]}%, and {volatilities[2]}%. With a time horizon of {time_horizon} days and a confidence level of "
                f"{confidence}%, what is the portfolio's VaR in USD?")
    
    solution = "Step 1: Compute the weighted average volatility from the asset volatilities and weights.\n"
    for i in range(3):
        solution += f"  Asset {i+1}: weight = {asset_weights[i]}%, volatility = {volatilities[i]}%.\n"
    solution += "Step 2: Convert the weighted volatility to a decimal factor.\n"
    solution += f"Step 3: Adjust for time horizon (sqrt({time_horizon}) = {sqrt_time}) and apply a confidence multiplier of {risk_multiplier:.2f}.\n"
    solution += "Step 4: Compute VaR as: portfolio_value * (weighted_volatility/100) * sqrt_time * risk_multiplier.\n"
    solution += f"Resulting VaR = ${var_value:.2f}."
    
    return question, solution

def template_time_horizon_var():
    """Intermediate: Correct Value at Risk (VaR) calculation using standard normal z-score."""
    
    # Generate portfolio parameters
    portfolio_value = generate_random_value(20000, 100000)
    volatility = round(random.uniform(2.00, 6.00), 2)  # daily volatility in %
    time_horizon = random.randint(3, 10)  # in days
    confidence = round(random.uniform(92.00, 98.00), 2)  # in %

    # Convert daily volatility to decimal
    sigma_daily = volatility / 100

    # Compute z-score for given confidence level
    z_score = norm.ppf(confidence / 100)

    # Adjust for time horizon
    sqrt_time = time_horizon ** 0.5

    # Compute VaR
    var_value = round(portfolio_value * sigma_daily * sqrt_time * z_score, 2)

    # ---------- Question ----------
    question = (f"A portfolio worth ${portfolio_value} exhibits a daily volatility of {volatility}% over a time horizon of {time_horizon} days "
                f"at a confidence level of {confidence}%. What is the Value at Risk (VaR) in USD?")
    
    # ---------- Solution ----------
    solution = (
        f"Step 1: Convert the daily volatility to decimal: {volatility}% → {sigma_daily:.4f}\n"
        f"Step 2: Determine the z-score for the {confidence}% confidence level: z = {z_score:.4f}\n"
        f"Step 3: Adjust volatility for time horizon (sqrt rule): sqrt({time_horizon}) = {sqrt_time:.4f}\n"
        f"Step 4: Compute VaR = Portfolio Value × sigma_daily × sqrt(Time) × z\n"
        f"        = ${portfolio_value} × {sigma_daily:.4f} × {sqrt_time:.4f} × {z_score:.4f} ≈ ${var_value:,.2f}"
    )

    return question, solution

def template_multi_factor_var():
    """Advanced: Multi-factor portfolio VaR with market, credit, and liquidity risks."""
    portfolio_value = generate_random_value(100000, 500000)
    market_vol = round(random.uniform(1.00, 4.00), 2)
    credit_risk = round(random.uniform(0.50, 2.50), 2)
    liquidity_risk = round(random.uniform(0.30, 1.50), 2)
    time_horizon = random.randint(5, 15)
    confidence = round(random.uniform(95.00, 99.00), 2)
    risk_multiplier = 1 + ((100 - confidence) / 100)
    sqrt_time = round(time_horizon**0.5, 2)
    combined_factor = (market_vol + credit_risk + liquidity_risk) / 3.0
    var_value = round(portfolio_value * (combined_factor / 100) * sqrt_time * risk_multiplier, 2)
    
    question = (f"A portfolio valued at ${portfolio_value} is exposed to multiple risk factors: a market volatility of {market_vol}%, "
                f"a credit risk of {credit_risk}%, and a liquidity risk of {liquidity_risk}%. With a time horizon of {time_horizon} days "
                f"and a confidence level of {confidence}%, what is the estimated Value at Risk (VaR) in USD?")
    
    solution = "Step 1: Determine the combined risk factor as the average of the market, credit, and liquidity risks.\n"
    solution += f"  Combined factor = ({market_vol}% + {credit_risk}% + {liquidity_risk}%)/3 = {combined_factor:.2f}%.\n"
    solution += "Step 2: Convert the combined factor to a decimal by dividing by 100.\n"
    solution += f"Step 3: Adjust for the time horizon (sqrt({time_horizon}) = {sqrt_time}) and apply a confidence multiplier of {risk_multiplier:.2f}.\n"
    solution += "Step 4: Compute VaR as: portfolio_value * (combined_factor/100) * sqrt_time * risk_multiplier.\n"
    solution += f"Resulting VaR = ${var_value:.2f}."
    
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_single_asset_var,
        template_stock_return_var,
        template_multi_asset_var,
        template_time_horizon_var,
        template_multi_factor_var
    ]
    
    all_problems = []
    
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip() if ':' in template_func.__doc__ else ""
        
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
    output_file = "../../testset/risk_management/var.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
