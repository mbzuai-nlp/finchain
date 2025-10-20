import random
from misc import companies, currencies

def template_dividend_target_payout_policy():
    """
    1:Basic: Compute total dividend when the firm applies a target payout ratio to EPS.
    """
    company = random.choice(companies)[0]
    currency = "$"

    eps = round(random.uniform(2, 8), 2)                      # earnings per share
    payout_ratio = round(random.uniform(0.3, 0.7), 2)         # 30-70 %
    shares = random.randint(800_000, 4_000_000)

    question = (
        f"{company} follows a target-payout policy.  With forecasted earnings of "
        f"{currency}{eps:,.2f} per share and a payout ratio of {payout_ratio*100:.0f} %, "
        f"the company has {shares:,} shares outstanding.  "
        f"How much total dividend will it pay this year?"
    )

    dps = round(eps * payout_ratio, 2)
    total = round(dps * shares, 2)

    solution = (
        "Step 1  Calculate the dividend per share (DPS):\n"
        f"        DPS = EPS × Payout Ratio = {currency}{eps:,.2f} × {payout_ratio:.2f}\n"
        f"            = {currency}{dps:,.2f}\n\n"
        "Step 2  Calculate the total dividend:\n"
        f"        Total = {currency}{dps:,.2f} × {shares:,}\n"
        f"              = {currency}{total:,.2f}"
    )

    return question, solution


def template_dividend_stable_growth_policy():
    """
    2:Basic: Compute total dividend given a stable growth rate and last year's DPS.
    """
    company = random.choice(companies)[0]
    currency = "$"

    last_dps = round(random.uniform(0.5, 3.0), 2)
    growth_rate = round(random.uniform(0.03, 0.12), 3)        # 3-12 %
    shares = random.randint(1_000_000, 6_000_000)

    question = (
        f"{company} has committed to increasing its dividend per share by "
        f"{growth_rate*100:.1f}% annually.  Last year it paid "
        f"{currency}{last_dps:,.2f} per share and now has {shares:,} shares outstanding.  "
        f"What total dividend will it pay this year?"
    )

    new_dps = round(last_dps * (1 + growth_rate), 2)
    total = round(new_dps * shares, 2)

    solution = (
        "Step 1  Find the new dividend per share:\n"
        f"        New DPS = Last DPS × (1 + g)\n"
        f"                = {currency}{last_dps:,.2f} × (1 + {growth_rate:.3f})\n"
        f"                = {currency}{new_dps:,.2f}\n\n"
        "Step 2  Find the total dividend:\n"
        f"        Total = {currency}{new_dps:,.2f} × {shares:,}\n"
        f"              = {currency}{total:,.2f}"
    )

    return question, solution


# ------------------------------------------------------------------
#  Lintner Smoothing Model  (target-payout with partial adjustment)
#    Steps:
#      1) Target DPS  = EPS × Target Payout Ratio
#      2) New DPS     = Last-year DPS + c · (Target DPS – Last-year DPS)
#      3) Total Cash  = New DPS × Shares Outstanding
# ------------------------------------------------------------------
def template_dividend_lintner_smoothing():
    """
    3:Intermediate: Compute total dividend using Lintner's smoothing model.
    """
    company = random.choice(companies)[0]
    currency = "$"

    eps = round(random.uniform(2, 8), 2)
    payout_ratio = round(random.uniform(0.35, 0.65), 2)    # 35-65 %
    last_dps = round(random.uniform(0.5, 3), 2)
    adj_factor = round(random.uniform(0.3, 0.6), 2)        # 30-60 % speed of adjustment
    shares = random.randint(1_000_000, 6_000_000)

    question = (
        f"{company} follows Lintner’s dividend-smoothing model.  Earnings per share are "
        f"{currency}{eps:,.2f}.  The target payout ratio is {payout_ratio*100:.0f} %, "
        f"and last year’s dividend was {currency}{last_dps:,.2f} per share.  "
        f"The board adjusts dividends toward the target at a speed of {adj_factor*100:.0f} %.  "
        f"With {shares:,} shares outstanding, how much total cash dividend will be paid this year?"
    )

    target_dps = round(eps * payout_ratio, 2)
    new_dps = round(last_dps + adj_factor * (target_dps - last_dps), 2)
    total_div = round(new_dps * shares, 2)

    solution = (
        "Step 1  Target DPS = EPS × Payout Ratio\n"
        f"             = {currency}{eps:,.2f} × {payout_ratio:.2f}\n"
        f"             = {currency}{target_dps:,.2f}\n\n"
        "Step 2  Apply Lintner adjustment:\n"
        f"        New DPS = Last DPS + c·(Target – Last)\n"
        f"                = {currency}{last_dps:,.2f} + {adj_factor:.2f}"
        f"×({currency}{target_dps:,.2f} – {currency}{last_dps:,.2f})\n"
        f"                = {currency}{new_dps:,.2f}\n\n"
        "Step 3  Total cash dividend:\n"
        f"        {currency}{new_dps:,.2f} × {shares:,} = {currency}{total_div:,.2f}"
    )

    return question, solution


# ------------------------------------------------------------------
#  Stock-Dividend Effect + DPS Growth
#    Steps:
#      1) New Shares = Old Shares × (1 + Stock-Dividend %)
#      2) New DPS    = Last DPS × (1 + Growth g)
#      3) Total Cash = New DPS × New Shares
# ------------------------------------------------------------------
def template_dividend_stock_plus_growth():
    """
    4:Intermediate: Compute total cash dividend with stock dividend and DPS growth.
    """
    company = random.choice(companies)[0]
    currency = "$"

    shares_old = random.randint(2_000_000, 8_000_000)
    stock_pct = round(random.uniform(0.05, 0.20), 2)       # 5-20 % stock dividend
    last_dps = round(random.uniform(0.4, 2.0), 2)
    growth = round(random.uniform(0.04, 0.12), 3)          # 4-12 % DPS growth

    question = (
        f"{company} declares a {stock_pct*100:.0f}% stock dividend and also commits to raise "
        f"its cash dividend per share by {growth*100:.1f}% over last year’s "
        f"{currency}{last_dps:,.2f}.  Before the stock dividend the firm had {shares_old:,} shares outstanding.  "
        f"How much cash will the firm distribute this year?"
    )

    shares_new = round(shares_old * (1 + stock_pct))
    new_dps = round(last_dps * (1 + growth), 2)
    total_cash = round(new_dps * shares_new, 2)

    solution = (
        "Step 1  New shares after stock dividend:\n"
        f"        {shares_old:,} × (1 + {stock_pct:.2f}) = {shares_new:,}\n\n"
        "Step 2  New DPS after planned growth:\n"
        f"        {currency}{last_dps:,.2f} × (1 + {growth:.3f}) = {currency}{new_dps:,.2f}\n\n"
        "Step 3  Total cash dividend:\n"
        f"        {currency}{new_dps:,.2f} × {shares_new:,} = {currency}{total_cash:,.2f}"
    )

    return question, solution


def template_dividend_lintner_three_year_avg():
    """
    5:Advanced: Compute total cash dividend with stock dividend and DPS growth.
    """
    company = random.choice(companies)[0]
    currency = "$"

    eps = [round(random.uniform(1.5, 4.5), 2) for _ in range(3)]
    payout_ratio = round(random.uniform(0.35, 0.65), 2)      # 35–65 %
    last_dps = round(random.uniform(0.4, 2.0), 2)
    adj_factor = round(random.uniform(0.3, 0.6), 2)          # speed of adjustment 30–60 %
    shares = random.randint(1_000_000, 6_000_000)

    question = (
        f"{company} follows Lintner’s smoothing model based on a three-year average of "
        f"earnings per share (EPS).  EPS over the past three years were "
        f"{currency}{eps[0]:,.2f}, {currency}{eps[1]:,.2f}, and {currency}{eps[2]:,.2f}.  "
        f"The target payout ratio is {payout_ratio*100:.0f} %, and last year’s dividend was "
        f"{currency}{last_dps:,.2f} per share.  The board moves {adj_factor*100:.0f} % of the way "
        f"toward the target each year.  With {shares:,} shares outstanding, how much total cash "
        f"dividend will be paid this year?"
    )

    avg_eps   = round(sum(eps) / 3, 2)                                    # Step 1
    target_dps = round(avg_eps * payout_ratio, 2)                         # Step 2
    new_dps    = round(last_dps + adj_factor * (target_dps - last_dps), 2) # Step 3
    total_div  = round(new_dps * shares, 2)                               # Step 4

    solution = (
        "Step 1  Three-year average EPS:\n"
        f"        ({currency}{eps[0]:,.2f} + {currency}{eps[1]:,.2f} + {currency}{eps[2]:,.2f}) ÷ 3 "
        f"= {currency}{avg_eps:,.2f}\n\n"
        "Step 2  Target dividend per share (DPS):\n"
        f"        {currency}{avg_eps:,.2f} × {payout_ratio:.2f} = {currency}{target_dps:,.2f}\n\n"
        "Step 3  Apply Lintner adjustment:\n"
        f"        New DPS = {currency}{last_dps:,.2f} + {adj_factor:.2f}"
        f"×({currency}{target_dps:,.2f} – {currency}{last_dps:,.2f})\n"
        f"                = {currency}{new_dps:,.2f}\n\n"
        "Step 4  Total cash dividend:\n"
        f"        {currency}{new_dps:,.2f} × {shares:,} = {currency}{total_div:,.2f}"
    )

    return question, solution



def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # List of template functions
    templates = [
        template_dividend_target_payout_policy,
        template_dividend_stable_growth_policy,
        template_dividend_lintner_smoothing,
        template_dividend_stock_plus_growth,
        template_dividend_lintner_three_year_avg
    ]
    
    # List to store all generated problems
    all_problems = []
    
    # Generate 10 problems for each template
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        
        for i in range(10):
            # Generate a unique seed for each problem
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            
            # Generate the problem and solution
            question, solution = template_func()
            
            # Create a JSON entry
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            
            # Add to the list of problems
            all_problems.append(problem_entry)
            
            # Reset the random seed
            random.seed()
    
    random.shuffle(all_problems)
    # Write all problems to a .jsonl file
    output_file = "../../testset/corporate_finance/div_policies.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()