import random
import json

def template_crypto_price_drop():
    """Basic: Basic Crypto Price Impact from Global Event."""
    initial_price = round(random.uniform(100, 1000), 2)
    drop_percentage = round(random.uniform(1, 10), 2)
    final_price = round(initial_price * (1 - drop_percentage / 100), 2)
    question = f"A global event causes a crypto asset's price to drop by {drop_percentage:.2f}%. If the asset was originally priced at ${initial_price:.2f}, what is its new price in USD?"
    solution = ("Step 1: Identify the initial price and the drop percentage.\n" +
                f"Step 2: Calculate the reduction: {drop_percentage:.2f}% of ${initial_price:.2f}.\n" +
                f"Step 3: Subtract the reduction from the initial price to get the new price: ${final_price:.2f}.\n" +
                "Thus, the final price is the computed single value.")
    return question, solution

def template_crypto_volume_increase():
    """Basic: Basic Crypto Volume Change Due to Global Event."""
    initial_volume = round(random.uniform(50000, 200000), 2)
    increase_percentage = round(random.uniform(1, 15), 2)
    final_volume = round(initial_volume * (1 + increase_percentage / 100), 2)
    question = f"A major global event increases the trading volume of a crypto asset by {increase_percentage:.2f}%. If the original trading volume was ${initial_volume:.2f}, what is the new trading volume in USD?"
    solution = ("Step 1: Note the original trading volume and the increase percentage.\n" +
                f"Step 2: Calculate the increased amount: {increase_percentage:.2f}% of ${initial_volume:.2f}.\n" +
                f"Step 3: Add the increase to the original volume to obtain the new volume: ${final_volume:.2f}.\n" +
                "Thus, the answer is the computed value.")
    return question, solution

def template_regulatory_event():
    """Intermediate: Regulatory Change Impact on Crypto Price."""
    initial_price = round(random.uniform(150, 1500), 2)
    impact_percentage = round(random.uniform(-5, 5), 2)
    final_price = round(initial_price * (1 + impact_percentage / 100), 2)
    question = f"Following a regulatory announcement, a crypto asset experiences a price change of {impact_percentage:.2f}%. If its original price was ${initial_price:.2f}, what is the resulting price in USD?"
    solution = ("Step 1: Take note of the initial price and the regulatory impact percentage.\n" +
                f"Step 2: Determine the impact by calculating {impact_percentage:.2f}% of ${initial_price:.2f}.\n" +
                f"Step 3: Adjust the initial price by this impact to derive the new price: ${final_price:.2f}.\n" +
                "Thus, the final crypto price is the computed single value.")
    return question, solution

def template_market_sentiment_shift():
    """Intermediate: Market Sentiment Shift Impact on Crypto Market Cap."""
    initial_market_cap = round(random.uniform(1000000, 5000000), 2)
    sentiment_change = round(random.uniform(-8, 8), 2)
    final_market_cap = round(initial_market_cap * (1 + sentiment_change / 100), 2)
    question = f"A shift in market sentiment changes a crypto asset's market cap by {sentiment_change:.2f}%. If its market cap was initially ${initial_market_cap:.2f}, what is its new market cap in USD?"
    solution = ("Step 1: Identify the initial market cap and the sentiment change percentage.\n" +
                f"Step 2: Evaluate the effect: {sentiment_change:.2f}% of ${initial_market_cap:.2f}.\n" +
                f"Step 3: Alter the initial market cap by the computed effect to obtain ${final_market_cap:.2f}.\n" +
                "Thus, the resulting market cap is the single computed value.")
    return question, solution

def template_global_macro_crypto_strategy():
    """Advanced: Multi-factor Impact on Crypto Price from Global Events."""
    initial_price = round(random.uniform(200, 2000), 2)
    liquidity_impact = round(random.uniform(-3, 3), 2)
    geopolitical_impact = round(random.uniform(-4, 4), 2)
    regulatory_impact = round(random.uniform(-5, 5), 2)
    total_impact = round(liquidity_impact + geopolitical_impact + regulatory_impact, 2)
    final_price = round(initial_price * (1 + total_impact / 100), 2)
    question = (f"A crypto asset with an initial price of ${initial_price:.2f} is affected by three global factors: "
                f"a liquidity change of {liquidity_impact:.2f}%, a geopolitical event causing a {geopolitical_impact:.2f}% change, "
                f"and a regulatory decision leading to a {regulatory_impact:.2f}% impact. Considering the combined effect, what is the new price in USD?")
    solution = ("Step 1: Sum the individual percentage impacts: liquidity, geopolitical, and regulatory.\n" +
                f"Step 2: Total impact is computed as {total_impact:.2f}%.\n" +
                f"Step 3: Adjust the initial price of ${initial_price:.2f} by this total percentage to obtain ${final_price:.2f}.\n" +
                "Thus, the final crypto price is the single calculated value.")
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_crypto_price_drop,
        template_crypto_volume_increase,
        template_regulatory_event,
        template_market_sentiment_shift,
        template_global_macro_crypto_strategy
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
    output_file = "../../testset/crypto_finance/global_events_impact.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()