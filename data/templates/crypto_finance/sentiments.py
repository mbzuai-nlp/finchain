import random

def template_price_sentiment():
    """1:Basic: Price sentiment score determination."""
    # Generate a price change in USD, up to 2 decimals
    price_change = round(random.uniform(0.50, 20.00), 2)
    # Generate a sentiment multiplier factor, up to 2 decimals
    multiplier = round(random.uniform(0.10, 2.00), 2)
    
    question = f"A crypto asset experienced a price increase of ${price_change:.2f}. If a sentiment model computes a sentiment score by multiplying the price change by a factor of {multiplier:.2f}, what is the sentiment score?"
    
    sentiment_score = round(price_change * multiplier, 2)
    solution = f"Step 1: Identify the price increase: ${price_change:.2f}.\n"
    solution += f"Step 2: Multiply by the sentiment factor: {price_change:.2f} * {multiplier:.2f}.\n"
    solution += f"Step 3: The resulting sentiment score is ${sentiment_score:.2f}."
    
    return question, solution

def template_volume_sentiment():
    """2:Basic: Volume sentiment score determination."""
    # Generate a trading volume increase in USD
    volume_increase = round(random.uniform(1000.00, 50000.00), 2)
    # Generate a volume sensitivity factor, up to 2 decimals
    sensitivity = round(random.uniform(0.01, 0.50), 2)
    
    question = f"A crypto asset shows a trading volume increase of ${volume_increase:.2f}. If the sentiment model multiplies the volume increase by a sensitivity factor of {sensitivity:.2f} to compute the sentiment score, what sentiment score does it yield?"
    
    sentiment_score = round(volume_increase * sensitivity, 2)
    solution = f"Step 1: Note the volume increase: ${volume_increase:.2f}.\n"
    solution += f"Step 2: Multiply the volume increase by the sensitivity factor: {volume_increase:.2f} * {sensitivity:.2f}.\n"
    solution += f"Step 3: The sentiment score is ${sentiment_score:.2f}."
    
    return question, solution

def template_tweet_influence_sentiment():
    """3:Intermediate: Tweet influence on sentiment."""
    # Generate a tweet count representing the number of influential tweets
    tweet_count = random.randint(50, 500)
    # Generate an average tweet polarity multiplier between 0.50 and 1.50
    tweet_polarity = round(random.uniform(0.50, 1.50), 2)
    # Generate an engagement factor 
    engagement_factor = round(random.uniform(0.05, 0.20), 2)
    
    question = f"A crypto asset receives {tweet_count} tweets in a day. If each tweet contributes by a polarity score of {tweet_polarity:.2f} and the overall impact is further adjusted by an engagement factor of {engagement_factor:.2f}, what is the overall tweet-based sentiment score?"
    
    sentiment_score = round(tweet_count * tweet_polarity * engagement_factor, 2)
    solution = f"Step 1: Count the tweets: {tweet_count}.\n"
    solution += f"Step 2: Multiply by the average tweet polarity: {tweet_count} * {tweet_polarity:.2f}.\n"
    solution += f"Step 3: Adjust by the engagement factor: ({tweet_count} * {tweet_polarity:.2f}) * {engagement_factor:.2f}.\n"
    solution += f"Step 4: The overall tweet-based sentiment score is {sentiment_score:.2f}."
    
    return question, solution

def template_news_impact_sentiment():
    """4:Intermediate: News impact on sentiment measurement."""
    # Generate a number of news articles
    news_count = random.randint(5, 30)
    # Generate an average news sentiment score multiplier
    news_score = round(random.uniform(0.80, 1.20), 2)
    # Generate a news influence factor
    influence_factor = round(random.uniform(0.10, 0.30), 2)
    
    question = f"A crypto market experiences {news_count} news articles in a day. If each article carries an average sentiment multiplier of {news_score:.2f} and the overall influence is weighted by a factor of {influence_factor:.2f}, what is the news-based sentiment score?"
    
    sentiment_score = round(news_count * news_score * influence_factor, 2)
    solution = f"Step 1: Count the news articles: {news_count}.\n"
    solution += f"Step 2: Multiply by the average news sentiment: {news_count} * {news_score:.2f}.\n"
    solution += f"Step 3: Apply the influence factor: ({news_count} * {news_score:.2f}) * {influence_factor:.2f}.\n"
    solution += f"Step 4: The news-based sentiment score is {sentiment_score:.2f}."
    
    return question, solution

def template_multi_factor_sentiment():
    """5:Advanced: Multi-factor crypto sentiment analysis."""
    # Generate tweet metrics
    tweet_count = random.randint(100, 1000)
    tweet_polarity = round(random.uniform(0.60, 1.40), 2)
    tweet_engagement = round(random.uniform(0.05, 0.25), 2)
    
    # Generate news metrics
    news_count = random.randint(10, 40)
    news_score = round(random.uniform(0.90, 1.30), 2)
    news_influence = round(random.uniform(0.10, 0.35), 2)
    
    # Generate price change component in USD
    price_change = round(random.uniform(1.00, 50.00), 2)
    price_factor = round(random.uniform(0.10, 0.40), 2)
    
    question = (f"For a crypto asset, sentiment is computed from multiple factors. It received {tweet_count} tweets with an average polarity of {tweet_polarity:.2f} and an engagement factor of {tweet_engagement:.2f}. "
                f"Additionally, there were {news_count} news articles with an average sentiment of {news_score:.2f} and a news influence of {news_influence:.2f}. "
                f"Finally, the asset had a price change of ${price_change:.2f} adjusted by a factor of {price_factor:.2f}. "
                f"If the overall sentiment score is the sum of the tweet-based, news-based, and price-based sentiment scores, what is the overall sentiment score?")
    
    tweet_component = tweet_count * tweet_polarity * tweet_engagement
    news_component = news_count * news_score * news_influence
    price_component = price_change * price_factor
    overall_sentiment = round(tweet_component + news_component + price_component, 2)
    
    solution = f"Step 1: Compute tweet-based sentiment: {tweet_count} * {tweet_polarity:.2f} * {tweet_engagement:.2f} = {tweet_component:.2f}.\n"
    solution += f"Step 2: Compute news-based sentiment: {news_count} * {news_score:.2f} * {news_influence:.2f} = {news_component:.2f}.\n"
    solution += f"Step 3: Compute price-based sentiment: {price_change:.2f} * {price_factor:.2f} = {price_component:.2f}.\n"
    solution += f"Step 4: Sum all components: {tweet_component:.2f} + {news_component:.2f} + {price_component:.2f} = {overall_sentiment:.2f}."
    
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    templates = [
        template_price_sentiment,
        template_volume_sentiment,
        template_tweet_influence_sentiment,
        template_news_impact_sentiment,
        template_multi_factor_sentiment
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
    output_file = "../../testset/crypto_finance/sentiments.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()