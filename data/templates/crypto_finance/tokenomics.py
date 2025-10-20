import random
import json

def template_market_cap_calculation():
    """1:Basic: Market Cap Calculation."""
    supply = random.randint(1000000, 10000000)
    price = round(random.uniform(0.10, 300.00), 2)
    market_cap = round(supply * price, 2)
    question = f"A crypto token has a circulating supply of {supply} tokens and is trading at ${price:.2f} each. What is its market cap in USD?"
    solution = "Step 1: Identify the circulating supply and token price.\n"
    solution += f"  Supply = {supply} and Price = ${price:.2f}.\n"
    solution += "Step 2: Multiply the supply by the price to get market cap.\n"
    solution += f"  Market Cap = {supply} × {price:.2f} = ${market_cap:.2f}."
    return question, solution

def template_token_price_calculation():
    """1:Basic: Token Price Calculation."""
    supply = random.randint(1000000, 10000000)
    price = round(random.uniform(0.10, 300.00), 2)
    market_cap = round(supply * price, 2)
    question = f"If a crypto token has a market cap of ${market_cap:.2f} and a circulating supply of {supply} tokens, what is its price per token in USD?"
    solution = "Step 1: Identify the market cap and circulating supply.\n"
    solution += f"  Market Cap = ${market_cap:.2f} and Supply = {supply}.\n"
    solution += "Step 2: Divide the market cap by the circulating supply to get the token price.\n"
    solution += f"  Price = {market_cap:.2f} ÷ {supply} = ${round(market_cap/supply, 2):.2f}."
    return question, solution

def template_staking_reward_effect():
    """2:Intermediate: Staking Reward Effect."""
    supply = random.randint(1000000, 10000000)
    price = round(random.uniform(0.10, 300.00), 2)
    lock_percent = round(random.uniform(10.00, 30.00), 2)
    price_increase = round(random.uniform(2.00, 10.00), 2)
    effective_supply = supply * (1 - lock_percent/100)
    new_price = round(price * (1 + price_increase/100), 2)
    new_market_cap = round(effective_supply * new_price, 2)
    question = f"A crypto token has a circulating supply of {supply} tokens and is trading at ${price:.2f}. If {lock_percent:.2f}% of tokens are locked through staking, causing the token price to increase by {price_increase:.2f}%, what is the new market cap in USD?"
    solution = "Step 1: Calculate the effective circulating supply after locking tokens.\n"
    solution += f"  Effective Supply = {supply} × (1 - {lock_percent:.2f}/100).\n"
    solution += "Step 2: Calculate the new token price after the increase.\n"
    solution += f"  New Price = ${price:.2f} × (1 + {price_increase:.2f}/100).\n"
    solution += "Step 3: Multiply the effective supply by the new price to get the new market cap.\n"
    solution += f"  New Market Cap = {round(effective_supply, 2)} × ${new_price:.2f} = ${new_market_cap:.2f}."
    return question, solution

def template_emission_schedule_impact():
    """2:Intermediate: Emission Schedule Impact."""
    supply = random.randint(1000000, 10000000)
    price = round(random.uniform(0.10, 300.00), 2)
    emission_percent = round(random.uniform(5.00, 20.00), 2)
    new_supply = supply * (1 + emission_percent/100)
    new_market_cap = round(new_supply * price, 2)
    question = f"A crypto token has a circulating supply of {supply} tokens and is trading at ${price:.2f}. If the protocol issues additional tokens equal to {emission_percent:.2f}% of the current supply, what is the new market cap in USD assuming the price remains unchanged?"
    solution = "Step 1: Calculate the new circulating supply after token emission.\n"
    solution += f"  New Supply = {supply} × (1 + {emission_percent:.2f}/100).\n"
    solution += "Step 2: Multiply the new supply by the unchanged token price to get the new market cap.\n"
    solution += f"  New Market Cap = {round(new_supply, 2)} × ${price:.2f} = ${new_market_cap:.2f}."
    return question, solution

def template_multi_factor_tokenomics():
    """3:Advanced: Multifactor Tokenomics Analysis."""
    supply = random.randint(1000000, 10000000)
    price = round(random.uniform(0.10, 300.00), 2)
    burn_percent = round(random.uniform(2.00, 10.00), 2)
    emission_percent = round(random.uniform(5.00, 15.00), 2)
    market_reaction = round(random.uniform(-5.00, 10.00), 2)
    adjusted_supply = supply * (1 - burn_percent/100) * (1 + emission_percent/100)
    adjusted_price = round(price * (1 + market_reaction/100), 2)
    final_market_cap = round(adjusted_supply * adjusted_price, 2)
    question = (f"A crypto token has a circulating supply of {supply} tokens and is trading at ${price:.2f}. "
                f"The protocol burns {burn_percent:.2f}% of tokens and then issues new tokens equal to {emission_percent:.2f}% "
                f"of the supply. Additionally, due to market reaction, the token price adjusts by {market_reaction:.2f}%. "
                f"What is the final market cap in USD?")
    solution = "Step 1: Calculate the adjusted supply after token burn and emission.\n"
    solution += f"  Adjusted Supply = {supply} × (1 - {burn_percent:.2f}/100) × (1 + {emission_percent:.2f}/100).\n"
    solution += "Step 2: Calculate the adjusted token price after market reaction.\n"
    solution += f"  Adjusted Price = ${price:.2f} × (1 + {market_reaction:.2f}/100).\n"
    solution += "Step 3: Multiply the adjusted supply by the adjusted price to determine the final market cap.\n"
    solution += f"  Final Market Cap = {round(adjusted_supply, 2)} × ${adjusted_price:.2f} = ${final_market_cap:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_market_cap_calculation,
        template_token_price_calculation,
        template_staking_reward_effect,
        template_emission_schedule_impact,
        template_multi_factor_tokenomics
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
    output_file = "../../testset/crypto_finance/tokenomics.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()