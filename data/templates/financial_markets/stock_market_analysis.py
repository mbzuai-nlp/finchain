import random
import json

# Named entities for investors and stocks
investor_names = ["Alice Wu", "Brad Johnson", "Carla Simmons", "Daniel Craig", "Eva Gonzalez"]
stock_names = [
    "Apple Inc.", "Tesla Inc.", "Amazon.com Inc.", "Microsoft Corp.", "Netflix Inc.",
    "Google LLC", "Meta Platforms", "Nvidia Corp.", "Disney Co.", "Coca-Cola Co."
]

###############################################################################
# BASIC TEMPLATES (2 Steps)
###############################################################################

def template_sma_easy1():
    """
    1:Basic: Simple Capital Gain Calculation
    This template calculates the capital gain from buying shares at one price 
    and selling them at a higher price.
    2 steps:
      1) Calculate total cost vs. total selling amount
      2) Subtract to find capital gain
    """
    investor_name = random.choice(investor_names)
    company_name = random.choice(stock_names)
    num_shares = random.randint(10, 100)           
    purchase_price = round(random.uniform(50, 150), 2)
    selling_price = round(purchase_price + random.uniform(5, 30), 2)

    question = (
        f"{investor_name} bought {num_shares} shares of {company_name} at ${purchase_price:.2f} per share "
        f"and later sold them at ${selling_price:.2f} per share. Calculate the total capital gain."
    )

    # Step 1: Calculate total cost and total selling
    total_cost = round(num_shares * purchase_price, 2)
    total_selling = round(num_shares * selling_price, 2)

    # Step 2: Calculate capital gain
    capital_gain = total_selling - total_cost

    solution = (
        f"Step 1: Calculate the total purchase and selling amounts:\n"
        f"  Total Cost = {num_shares} × ${purchase_price:.2f} = ${total_cost:.2f}\n"
        f"  Total Selling = {num_shares} × ${selling_price:.2f} = ${total_selling:.2f}\n\n"
        f"Step 2: Calculate the capital gain:\n"
        f"  Capital Gain = ${total_selling:.2f} - ${total_cost:.2f} = ${capital_gain:.2f}"
    )

    return question, solution


def template_sma_easy2():
    """
    2:Basic: Dividend Yield Calculation  (2 steps)
      1) Dividend yield (decimal) = Annual Dividend ÷ Share Price
      2) Convert decimal to percentage   (answer)
    """
    investor_name  = random.choice(investor_names)
    company_name   = random.choice(stock_names)
    annual_div     = round(random.uniform(1.0, 5.0), 2)
    share_price    = round(random.uniform(50, 200), 2)

    # Step 1: decimal yield
    yield_decimal = annual_div / share_price
    # Step 2: percentage
    yield_pct     = yield_decimal * 100

    question = (
        f"{investor_name} is looking at {company_name}, which pays an annual dividend of "
        f"${annual_div:.2f} per share.  With the stock at ${share_price:.2f}, what is the dividend yield?"
    )

    solution = (
        f"Step 1: Decimal yield = ${annual_div:.2f} ÷ ${share_price:.2f} = {yield_decimal:.4f}\n\n"
        f"Step 2 (answer): Percentage yield = {yield_decimal:.4f} × 100 = {yield_pct:.2f}%"
    )

    return question, solution


###############################################################################
# INTERMEDIATE TEMPLATES (3 Steps)
###############################################################################

def template_sma_medium1():
    """
    3:Intermediate: Total Return on Stock (Purchase, Dividend, Sale)
    This template calculates the total dollar return from 
    buying shares, receiving a dividend, and then selling the shares.
    3 steps:
      1) Calculate total cost
      2) Calculate total dividend
      3) Calculate total return = (selling proceeds + dividend) - cost
    """
    investor_name = random.choice(investor_names)
    company_name = random.choice(stock_names)
    num_shares = random.randint(20, 200)
    purchase_price = round(random.uniform(30, 80), 2)
    selling_price = round(purchase_price + random.uniform(10, 40), 2)
    dividend_per_share = round(random.uniform(1.0, 3.0), 2)

    question = (
        f"{investor_name} bought {num_shares} shares of {company_name} at ${purchase_price:.2f} each. "
        f"They received a dividend of ${dividend_per_share:.2f} per share during the holding period. "
        f"Then they sold all shares at ${selling_price:.2f}. "
        f"Calculate the total return (in dollars) from this investment."
    )

    # Step 1: Total cost
    total_cost = round(num_shares * purchase_price, 2)

    # Step 2: Total dividend
    total_dividend = round(num_shares * dividend_per_share, 2)

    # Step 3: Selling amount and total return
    total_selling = round(num_shares * selling_price, 2)
    total_return = total_selling + total_dividend - total_cost

    solution = (
        f"Step 1: Calculate the total cost:\n"
        f"  Total Cost = {num_shares} × ${purchase_price:.2f} = ${total_cost:.2f}\n\n"
        f"Step 2: Calculate the total dividend:\n"
        f"  Total Dividend = {num_shares} × ${dividend_per_share:.2f} = ${total_dividend:.2f}\n\n"
        f"Step 3: Calculate the total selling amount and net return:\n"
        f"  Total Selling = {num_shares} × ${selling_price:.2f} = ${total_selling:.2f}\n"
        f"  Total Return = ${total_selling:.2f} + ${total_dividend:.2f} - ${total_cost:.2f} = ${total_return:.2f}"
    )

    return question, solution


def template_sma_medium2():
    """
    4:Intermediate: Calculating Share Price from P/E Ratio
    This template estimates the share price using the P/E ratio and 
    the company's total earnings.
    3 steps:
      1) Compute Earnings per Share (EPS)
      2) Multiply EPS by P/E to get share price
      3) Summarize
    """
    investor_name = random.choice(investor_names)
    company_name = random.choice(stock_names)
    pe_ratio = round(random.uniform(10, 40), 2)
    total_earnings = round(random.uniform(1e6, 5e6), 2)
    shares_outstanding = random.randint(100000, 1000000)

    question = (
        f"{investor_name} is analyzing {company_name}, which has a P/E ratio of {pe_ratio:.2f}. "
        f"The company reported total earnings of ${total_earnings:,.2f}, with {shares_outstanding} shares outstanding. "
        f"Using the P/E ratio, estimate {company_name}'s share price."
    )

    # Step 1: EPS
    eps = round(total_earnings / shares_outstanding, 2)

    # Step 2: Share Price
    share_price = round(pe_ratio * eps, 2)

    solution = (
        f"Step 1: Earnings per Share (EPS) = Total Earnings / Shares Outstanding\n"
        f"                                  = ${total_earnings:,.2f} / {shares_outstanding} = ${eps:.2f}\n\n"
        f"Step 2: Share Price = P/E Ratio × EPS\n"
        f"                    = {pe_ratio:.2f} × ${eps:.2f} = ${share_price:.2f}\n\n"
        f"Step 3: Thus, the estimated share price = ${share_price:.2f}."
    )
    return question, solution

###############################################################################
# ADVANCED TEMPLATE (4 Steps)
###############################################################################

def template_sma_hard1():
    """
    5:Advanced: Multiple Purchases + Sale (Cost Basis and Net Profit)
    This template calculates the average cost basis and net profit when 
    an investor buys shares on two different occasions, then sells them all.
    4 steps:
      1) Calculate total shares and total cost
      2) Average cost basis per share
      3) Total proceeds from sale
      4) Net profit = proceeds - cost
    """
    investor_name = random.choice(investor_names)
    company_name = random.choice(stock_names)

    # First purchase
    shares_p1 = random.randint(10, 50)
    price_p1 = round(random.uniform(20, 60), 2)

    # Second purchase
    shares_p2 = random.randint(10, 50)
    price_p2 = round(price_p1 + random.uniform(-10, 20), 2)  # could be lower or higher

    # Final selling price
    selling_price = round(max(price_p1, price_p2) + random.uniform(10, 30), 2)

    question = (
        f"{investor_name} made multiple purchases of {company_name}:\n"
        f"  1) {shares_p1} shares at ${price_p1:.2f} each\n"
        f"  2) {shares_p2} shares at ${price_p2:.2f} each\n"
        f"They later sold all {shares_p1 + shares_p2} shares at ${selling_price:.2f}.\n"
        f"Calculate the average cost basis per share, the total cost basis, and the net profit from the sale."
    )

    # Step 1: total shares and total cost
    total_shares = shares_p1 + shares_p2
    total_cost = round((shares_p1 * price_p1) + (shares_p2 * price_p2), 2)

    # Step 2: average cost
    avg_cost_basis = round(total_cost / total_shares, 2)

    # Step 3: total proceeds
    total_proceeds = round(total_shares * selling_price, 2)

    # Step 4: net profit
    net_profit = total_proceeds - total_cost

    solution = (
        f"Step 1: Total shares = {shares_p1} + {shares_p2} = {total_shares}\n"
        f"        Total cost   = ({shares_p1} × ${price_p1:.2f}) + ({shares_p2} × ${price_p2:.2f}) "
        f"= ${total_cost:.2f}\n\n"
        f"Step 2: Average cost basis per share = Total Cost / Total Shares\n"
        f"                                     = ${total_cost:.2f} / {total_shares} = ${avg_cost_basis:.2f}\n\n"
        f"Step 3: Total proceeds from sale = {total_shares} × ${selling_price:.2f} = ${total_proceeds:.2f}\n\n"
        f"Step 4: Net profit = Total Proceeds - Total Cost\n"
        f"                   = ${total_proceeds:.2f} - ${total_cost:.2f} = ${net_profit:.2f}"
    )
    return question, solution


###############################################################################
# MAIN FUNCTION
###############################################################################

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON Lines file.
    """
    # 1) Gather all stock market arithmetic templates in a list
    templates = [
        template_sma_easy1,
        template_sma_easy2,
        template_sma_medium1,
        template_sma_medium2,
        template_sma_hard1
    ]

    all_problems = []

    # 2) For each template, generate 10 question/solution pairs
    for template_func in templates:
        # Extract the first line of the docstring up to the colon
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()

        for _ in range(10):
            # Create a unique seed
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)

            # Generate question & solution
            question, solution = template_func()

            # Store the problem
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,  # e.g. "Basic", "Intermediate", "Advanced"
                "question": question,
                "solution": solution
            }
            all_problems.append(problem_entry)

            # Reset random to system-based seeding
            random.seed()

    # 3) Shuffle all generated problems
    random.shuffle(all_problems)

    # 4) Write everything to a JSONL file
    output_file = "../../testset/financial_markets/stock_market_analysis.jsonl"
    with open(output_file, "w") as f:
        for problem in all_problems:
            f.write(json.dumps(problem))
            f.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")


# If you want to run this file directly
if __name__ == "__main__":
    main()
