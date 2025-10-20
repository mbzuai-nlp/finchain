import random
import json

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_defi_staking_return():
    """1:Basic: DeFi staking APY reward calculation."""
    staked_amount = generate_random_value(1000, 10000)
    apy = round(random.uniform(5, 15), 2)
    question = f"A user stakes ${staked_amount:.2f} in a DeFi staking pool with an annual percentage yield (APY) of {apy:.2f}%. What is the annual reward in USD?"
    reward = round(staked_amount * (apy / 100), 2)
    solution = "Step 1: Determine the proportional reward by applying the APY to the staked amount.\n"
    solution += f"  Reward = ${staked_amount:.2f} * ({apy:.2f}/100) = ${reward:.2f}.\n"
    solution += "Step 2: The computed value represents the annual reward in USD."
    return question, solution

def template_defi_swap_fee():
    """2:Basic: Decentralized exchange swap fee calculation."""
    swap_amount = generate_random_value(500, 5000)
    fee_percent = round(random.uniform(0.1, 1.0), 2)
    question = f"In a decentralized exchange, if a user swaps tokens worth ${swap_amount:.2f} and the swap fee is {fee_percent:.2f}%, what is the fee in USD?"
    fee = round(swap_amount * (fee_percent / 100), 2)
    solution = "Step 1: Compute the fee by applying the percentage fee to the swap amount.\n"
    solution += f"  Fee = ${swap_amount:.2f} * ({fee_percent:.2f}/100) = ${fee:.2f}.\n"
    solution += "Step 2: The result is the fee paid in USD."
    return question, solution

def template_liquidity_pool_reward():
    """3:Intermediate: Liquidity pool reward calculation."""
    total_fees = generate_random_value(1000, 10000)
    provider_share = round(random.uniform(0.05, 0.30), 2)
    provider_share_pct = provider_share * 100
    question = (
        f"A liquidity pool generates total fees of ${total_fees:.2f} over a period. "
        f"If a liquidity provider is entitled to {provider_share_pct:.2f}% of the fees, "
        "what is their reward in USD?"
    )
    reward = round(total_fees * provider_share, 2)
    solution = "Step 1: Identify the provider's share of the total fees.\n"
    solution += (
        f"  Reward = ${total_fees:.2f} × ({provider_share_pct:.2f}/100) = ${reward:.2f}.\n"
    )
    solution += "Step 2: The computed value is the liquidity provider's reward in USD."
    return question, solution

def template_yield_farming_roi():
    """4:Intermediate: Yield farming ROI sensitivity analysis with duration adjustment."""
    initial_investment = generate_random_value(2000, 20000)
    roi_annual_pct = round(random.uniform(10, 50), 2)  # Annualized ROI in percent
    duration_months = random.randint(1, 12)

    # Step 1: Convert the annual ROI into the ROI for the actual holding period (linear scaling)
    roi_period_pct = roi_annual_pct * (duration_months / 12.0)

    # Step 2: Calculate the return in USD for the period
    roi_value = round(initial_investment * (roi_period_pct / 100), 2)

    question = (
        f"In a yield farming protocol, a user invests ${initial_investment:.2f} and achieves an annualized ROI "
        f"of {roi_annual_pct:.2f}%. If the investment lasts {duration_months} months, what is the total ROI in USD "
        f"for the period?"
    )

    solution = (
        "Step 1: Adjust the annual ROI to the actual investment period:\n"
        f"  ROI_period% = {roi_annual_pct:.2f}% × ({duration_months}/12) = {roi_period_pct:.2f}%\n\n"
        "Step 2: Apply the ROI% to the initial investment:\n"
        f"  ROI = ${initial_investment:.2f} × ({roi_period_pct:.2f}/100) = ${roi_value:.2f}\n\n"
        f"Answer: The total return over {duration_months} months is ${roi_value:.2f}."
    )

    return question, solution

def template_defi_multi_factor_portfolio():
    """5:Advanced: Multi-factor impact on a DeFi portfolio."""
    portfolio_value = generate_random_value(50000, 200000)
    staking_percentage = round(random.uniform(0.1, 0.5), 2)
    swap_fee_sensitivity = round(random.uniform(-2, 2), 2)
    yield_factor = round(random.uniform(5, 20), 2)
    question = f"A DeFi portfolio valued at ${portfolio_value:.2f} has a staking component constituting {staking_percentage*100:.2f}% of its value. Additionally, changes in swap fee rates affect the portfolio with a sensitivity of {swap_fee_sensitivity:.2f}. If yield farming provides an effective boost of {yield_factor:.2f}%, what is the net impact value in USD on the portfolio?"
    staking_impact = portfolio_value * staking_percentage * (yield_factor / 100)
    fee_impact = portfolio_value * (swap_fee_sensitivity / 100)
    impact = round(staking_impact + fee_impact, 2)
    solution = "Step 1: Calculate the impact from the staking yield component by considering its percentage share and yield boost.\n"
    solution += f"  Staking Impact = ${portfolio_value:.2f} * {staking_percentage:.2f} * ({yield_factor:.2f}/100) = ${staking_impact:.2f}.\n"
    solution += "Step 2: Assess the impact due to swap fee sensitivity as a proportional effect on the entire portfolio.\n"
    solution += f"  Fee Impact = ${portfolio_value:.2f} * ({swap_fee_sensitivity:.2f}/100) = ${fee_impact:.2f}.\n"
    solution += f"Step 3: Sum both impacts to estimate the net effect: ${impact:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_defi_staking_return,
        template_defi_swap_fee,
        template_liquidity_pool_reward,
        template_yield_farming_roi,
        template_defi_multi_factor_portfolio
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
    output_file = "../../testset/crypto_finance/defi.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()
