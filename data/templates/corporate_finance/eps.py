import random
from misc import companies, currencies

# 1) EPS with weighted-average shares
def template_eps_weighted_average():
    """
    1:Basic: Compute EPS with weighted-average shares.
    Scenario: new shares issued during the year.
    Returns (question_str, solution_str)
    """
    company, industry = random.choice(companies)

    net_income  = random.randint(200_000, 12_000_000)       # $
    beg_shares  = random.randint(200_000, 900_000)          # shares on Jan 1
    new_shares  = random.randint(20_000, 250_000)           # shares issued
    issue_month = random.randint(2, 10)                     # Feb–Oct
    months_out  = 12 - issue_month + 1

    # Step 1: weighted-average shares
    wtd_shares = round(beg_shares + new_shares * (months_out / 12), 2)

    # Step 2: EPS
    eps = round(net_income / wtd_shares, 2)

    question = (
        f"{company}, operating in the {industry} industry, reported:\n\n"
        f"Net Income: ${net_income:,.0f}\n"
        f"Common Shares Outstanding on January 1: {beg_shares:,}\n"
        f"{new_shares:,} additional shares were issued on "
        f"{calendar.month_name[issue_month]} 1 and remained outstanding for the rest of the year.\n\n"
        "What is the company’s Earnings Per Share (EPS)?"
    )

    solution = (
        "Step 1  Compute weighted-average shares\n"
        f"Weighted shares = {beg_shares:,} + {new_shares:,} × ({months_out}/12)\n"
        f"               = {wtd_shares:,.2f}\n\n"
        "Step 2  Compute EPS\n"
        f"EPS = ${net_income:,.0f} ÷ {wtd_shares:,.2f} = ${eps:,.2f} per share"
    )

    return question, solution


# 2) EPS with quarterly preferred-dividend rate
def template_eps_quarterly_pref_div():
    """
    2:Basic: Compute EPS with quarterly preferred dividends.
    Scenario: preferred dividends stated per share per quarter.
    Returns (question_str, solution_str)
    """
    company, industry = random.choice(companies)

    net_income     = random.randint(300_000, 15_000_000)    # $
    pref_shares    = random.randint(10_000, 60_000)         # preferred shares
    quarterly_rate = round(random.uniform(0.25, 2.00), 2)   # $/share/quarter
    common_shares  = random.randint(250_000, 1_200_000)     # common shares

    # Step 1: annual preferred dividends
    annual_pref_div = round(pref_shares * quarterly_rate * 4, 2)

    # Step 2: EPS
    eps = round((net_income - annual_pref_div) / common_shares, 2)

    question = (
        f"{company}, operating in the {industry} industry, reported:\n\n"
        f"Net Income: ${net_income:,.0f}\n"
        f"Preferred Stock: {pref_shares:,} shares paying ${quarterly_rate:,.2f} per share each quarter\n"
        f"Common Shares Outstanding: {common_shares:,}\n\n"
        "What is the company’s Earnings Per Share (EPS)?"
    )

    solution = (
        "Step 1  Annualize preferred dividends\n"
        f"Annual preferred dividends = {pref_shares:,} × ${quarterly_rate:,.2f} × 4\n"
        f"                           = ${annual_pref_div:,.2f}\n\n"
        "Step 2  Compute EPS\n"
        f"EPS = (${net_income:,.0f} – ${annual_pref_div:,.2f}) ÷ {common_shares:,}\n"
        f"    = ${eps:,.2f} per share"
    )

    return question, solution

# 1) EPS with preferred dividends AND weighted-average shares
def template_eps_pref_div_weighted():
    """
    3:Intermediate: Compute EPS with preferred dividends and weighted-average shares.
    3-step reasoning:
      1. Subtract preferred dividends from net income
      2. Compute weighted-average common shares (new shares issued mid-year)
      3. Divide to get EPS
    Returns (question, solution)
    """
    company, industry = random.choice(companies)

    net_income          = random.randint(400_000, 15_000_000)
    preferred_dividends = round(random.uniform(20_000, 150_000), 2)

    beg_shares  = random.randint(300_000, 900_000)        # shares on Jan 1
    new_shares  = random.randint(30_000, 200_000)         # issued later
    issue_month = random.randint(2, 10)                   # Feb–Oct
    months_out  = 12 - issue_month + 1

    # Step 1: earnings available to common
    earnings_common = round(net_income - preferred_dividends, 2)

    # Step 2: weighted-average shares
    wtd_shares = round(beg_shares + new_shares * (months_out / 12), 2)

    # Step 3: EPS
    eps = round(earnings_common / wtd_shares, 2)

    question = (
        f"{company}, operating in the {industry} industry, reported the following:\n\n"
        f"Net Income: ${net_income:,.0f}\n"
        f"Preferred Dividends: ${preferred_dividends:,.2f}\n"
        f"Common Shares Outstanding on January 1: {beg_shares:,}\n"
        f"{new_shares:,} additional shares were issued on {calendar.month_name[issue_month]} 1 and remained outstanding for the rest of the year.\n\n"
        "What is the company’s Earnings Per Share (EPS)?"
    )

    solution = (
        "Step 1  Earnings available to common\n"
        f"Earnings = ${net_income:,.0f} – ${preferred_dividends:,.2f} = ${earnings_common:,.2f}\n\n"
        "Step 2  Weighted-average shares\n"
        f"Weighted shares = {beg_shares:,} + {new_shares:,} × ({months_out}/12) = {wtd_shares:,.2f}\n\n"
        "Step 3  EPS\n"
        f"EPS = ${earnings_common:,.2f} ÷ {wtd_shares:,.2f} = ${eps:,.2f} per share"
    )

    return question, solution


# 2) EPS with quarterly preferred rate AND year-end share buyback
def template_eps_quarterly_pref_buyback():
    """
    4:Intermediate: Compute EPS with quarterly preferred dividends and year-end buyback.
    3-step reasoning:
      1. Annualize preferred dividends from a quarterly rate
      2. Compute weighted-average shares after a buyback using day-weighting (365-day year)
      3. Divide to get EPS
    Returns (question, solution)
    """

    import calendar

    company, industry = random.choice(companies)

    net_income       = random.randint(500_000, 18_000_000)
    pref_shares      = random.randint(15_000, 70_000)
    quarterly_rate   = round(random.uniform(0.30, 2.50), 2)  # $ per share per quarter

    beg_shares  = random.randint(400_000, 1_100_000)
    buyback_shr = random.randint(20_000, 120_000)
    buyback_month = random.randint(1, 12)                    # Jan–Dec
    
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    max_day = days_in_month[buyback_month - 1]
    buyback_day = random.randint(1, max_day)
    day_of_year = sum(days_in_month[:buyback_month - 1]) + buyback_day
    days_in_year = 365
    days_remaining = days_in_year - day_of_year + 1  # inclusive NOT outstanding

    # Step 1: annual preferred dividends
    annual_pref_div = round(pref_shares * quarterly_rate * 4, 2)

    # Step 2: weighted-average shares (buyback reduces count)
    wtd_shares = round(beg_shares - buyback_shr * (days_remaining / 365), 2)

    # Step 3: EPS
    eps = round((net_income - annual_pref_div) / wtd_shares, 2)

    question = (
        f"{company}, operating in the {industry} industry, reported the following:\n\n"
        f"Net Income: ${net_income:,.0f}\n"
        f"Preferred Stock: {pref_shares:,} shares paying ${quarterly_rate:,.2f} per share each quarter\n"
        f"Common Shares Outstanding on January 1: {beg_shares:,}\n"
        f"The company repurchased {buyback_shr:,} shares on {calendar.month_name[buyback_month]} {buyback_day}.\n\n"
        "What is the company’s Earnings Per Share (EPS)?"
    )

    solution = (
        "Step 1  Annualize preferred dividends\n"
        f"Annual preferred dividends = {pref_shares:,} × ${quarterly_rate:,.2f} × 4 = ${annual_pref_div:,.2f}\n\n"
        "Step 2  Weighted-average shares\n"
        f"Weighted shares = {beg_shares:,} – {buyback_shr:,} × ({days_remaining}/365) = {wtd_shares:,.2f}\n\n"
        "Step 3  EPS\n"
        f"EPS = (${net_income:,.0f} – ${annual_pref_div:,.2f}) ÷ {wtd_shares:,.2f} = ${eps:,.2f} per share"
    )

    return question, solution

def template_eps_pref_div_split_weighted():
    """
    5:Advanced: Compute EPS with preferred dividends, stock split, and weighted-average shares.
    Four reasoning steps:
      1. Annualize preferred dividends from a quarterly rate.
      2. Compute earnings available to common shareholders.
      3. Derive weighted-average common shares after a 2-for-1 split in mid-year.
      4. Divide to obtain EPS.
    Returns (question, solution)
    """
    company, industry = random.choice(companies)

    net_income       = random.randint(600_000, 20_000_000)
    pref_shares      = random.randint(12_000, 60_000)
    quarterly_rate   = round(random.uniform(0.30, 2.50), 2)     # $ per share per quarter

    beg_shares       = random.randint(300_000, 800_000)
    split_month      = 6                                         # June 30 split, 2-for-1
    months_pre_split = split_month
    months_post_split = 12 - months_pre_split

    # Step 1  annual preferred dividends
    annual_pref_div = round(pref_shares * quarterly_rate * 4, 2)

    # Step 2  earnings available to common
    earnings_common = round(net_income - annual_pref_div, 2)

    # Step 3  weighted-average shares (pre-split shares count once, post-split count double)
    #   Pre-split equivalent shares
    pre_eq = beg_shares * (months_pre_split / 12)
    #   Post-split shares (2 × beg_shares) for remaining months
    post_eq = (beg_shares * 2) * (months_post_split / 12)
    wtd_shares = round(pre_eq + post_eq, 2)

    # Step 4  EPS
    eps = round(earnings_common / wtd_shares, 2)

    question = (
        f"{company}, operating in the {industry} industry, reported the following financial data.\n\n"
        f"Net Income $ {net_income:,.0f}\n"
        f"Preferred Stock {pref_shares:,} shares paying $ {quarterly_rate:,.2f} per share each quarter\n"
        f"Common Shares Outstanding on January 1 {beg_shares:,}\n"
        f"A 2-for-1 stock split occurred on June 30 and the split shares remained outstanding through year-end.\n\n"
        "Calculate the company’s Earnings Per Share (EPS)."
    )

    solution = (
        "Step 1  Annualize preferred dividends\n"
        f"Annual preferred dividends = {pref_shares:,} × $ {quarterly_rate:,.2f} × 4 = $ {annual_pref_div:,.2f}\n\n"
        "Step 2  Earnings available to common\n"
        f"Earnings = $ {net_income:,.0f} − $ {annual_pref_div:,.2f} = $ {earnings_common:,.2f}\n\n"
        "Step 3  Weighted-average shares\n"
        f"Pre-split equivalent = {beg_shares:,} × ({months_pre_split}/12) = {pre_eq:,.2f}\n"
        f"Post-split equivalent = {beg_shares*2:,} × ({months_post_split}/12) = {post_eq:,.2f}\n"
        f"Weighted-average shares = {wtd_shares:,.2f}\n\n"
        "Step 4  EPS\n"
        f"EPS = $ {earnings_common:,.2f} ÷ {wtd_shares:,.2f} = $ {eps:,.2f} per share"
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
        template_eps_weighted_average,
        template_eps_quarterly_pref_div,
        template_eps_pref_div_weighted,
        template_eps_quarterly_pref_buyback,
        template_eps_pref_div_split_weighted
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
    output_file = "../../testset/corporate_finance/eps.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()