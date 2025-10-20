import random
import json

# Named entities for investors and companies
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
company_names = ["Apple", "Google", "Microsoft", "Amazon", "Tesla", "Facebook", "Netflix", "Walmart"]

# ------------------------------------------------------------------
# Basic Scenario 1: Cash Payment Calculation in a Deal Structure
def template_cash_payment_calculation():
    """1:Basic: Cash Payment Calculation in a Deal Structure"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    total_deal = random.randint(50, 200)            # in million dollars
    cash_percent = random.randint(30, 70)           # %
    
    # Compute cash component (rounded to 2 dp for display)
    cash_payment = round(total_deal * cash_percent / 100, 2)

    question = (
        f"{investor} is acquiring {company} for ${total_deal} million. "
        f"The deal stipulates that {cash_percent}% of the consideration is paid in cash, "
        f"with the remainder in stock. Calculate the cash component of the deal."
    )

    solution = (
        f"Step 1: Identify key figures:\n"
        f"  Total Deal Value = ${total_deal:.2f} million\n"
        f"  Cash Percentage  = {cash_percent}%\n\n"
        f"Step 2: Compute the cash payment:\n"
        f"  Cash Payment = ${total_deal:.2f} × ({cash_percent}/100)\n"
        f"               = ${cash_payment:.2f} million"
    )
    return question, solution

# ------------------------------------------------------------------
# Basic Scenario 2: Stock Swap Calculation in a Deal Structure
def template_stock_swap_calculation():
    """2:Basic: Stock Swap Calculation in a Deal Structure"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    total_deal = round(random.uniform(10, 50), 2)   # in million dollars
    share_price = round(random.uniform(0.5, 5.0), 2)  # in million dollars per share
    
    # Compute number of shares (rounded to 2 dp for display)
    shares = round(total_deal / share_price, 2)

    question = (
        f"{investor} is acquiring {company} in a stock‑swap deal valued at "
        f"${total_deal:.2f} million. If each share is valued at "
        f"${share_price:.2f} million, how many shares will be issued?"
    )

    solution = (
        f"Step 1: Identify key figures:\n"
        f"  Total Deal Value = ${total_deal:.2f} million\n"
        f"  Share Price      = ${share_price:.2f} million per share\n\n"
        f"Step 2: Compute the shares to issue:\n"
        f"  Shares Issued = ${total_deal:.2f} / ${share_price:.2f}\n"
        f"                = {shares:.2f} shares"
    )
    return question, solution



# ------------------------------------------------------------------
# Intermediate Scenario 1: Earnout Payment with Revenue Bonus Calculation
def template_earnout_with_bonus_calculation():
    """3:Intermediate: Earnout Payment Calculation with Revenue Bonus in a Deal Structure (money shown with $ and 2‑dp)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)

    base_price    = random.randint(20, 100)                      # $ million
    earnout_max   = random.randint(5, 20)                        # $ million
    target_rev    = random.randint(50, 150)                      # $ million
    actual_rev    = random.randint(target_rev, int(target_rev*1.30))
    bonus_rate    = round(random.uniform(0.05, 0.20), 2)         # decimal
    max_bonus     = random.randint(2, 10)                        # $ million

    question = (
        f"{investor} acquired {company} for a base price of ${base_price:.2f} million. "
        f"The deal includes an earn‑out of up to ${earnout_max:.2f} million if "
        f"{company} meets a revenue target of ${target_rev:.2f} million. "
        f"With actual revenue of ${actual_rev:.2f} million, the earn‑out is prorated. "
        f"If actual revenue exceeds 110 % of target, an extra bonus equal to "
        f"{bonus_rate*100:.0f}% of the excess revenue is paid, capped at "
        f"${max_bonus:.2f} million. Calculate the total deal value (base price plus total earn‑out)."
    )

    # calculations (rounded once, at 2 dp)
    earnout_basic   = round(earnout_max * actual_rev / target_rev, 2)
    bonus_threshold = round(1.10 * target_rev, 2)
    bonus_unclipped = round(max(0, actual_rev - bonus_threshold) * bonus_rate, 2)
    bonus           = min(bonus_unclipped, max_bonus)
    total_earnout   = round(earnout_basic + bonus, 2)
    total_value     = round(base_price + total_earnout, 2)

    solution = (
        f"Step 1  Basic earn‑out:\n"
        f"  ${earnout_max:.2f} m × (${actual_rev:.2f} m / ${target_rev:.2f} m) "
        f"= ${earnout_basic:.2f} m\n\n"
        f"Step 2  Bonus threshold:\n"
        f"  110 % × ${target_rev:.2f} m = ${bonus_threshold:.2f} m\n\n"
        f"Step 3  Bonus:\n"
        f"  Excess = max(0, ${actual_rev:.2f} m − ${bonus_threshold:.2f} m) = "
        f"${max(0, actual_rev - bonus_threshold):.2f} m\n"
        f"  Unclipped bonus = Excess × {bonus_rate:.2f} = ${bonus_unclipped:.2f} m\n"
        f"  Bonus = min(Unclipped, cap ${max_bonus:.2f}) = ${bonus:.2f} m\n\n"
        f"Step 4  Total earn‑out = ${earnout_basic:.2f} m + ${bonus:.2f} m = ${total_earnout:.2f} m\n\n"
        f"Step 5  Total deal value = ${base_price:.2f} m + ${total_earnout:.2f} m = ${total_value:.2f} m"
    )
    return question, solution


# ------------------------------------------------------------------
# Intermediate Scenario 2: Adjusted Equity Shares Calculation in a Leveraged Buyout with Bonus Shares
def template_leveraged_buyout_adjusted_shares_calculation():
    """4:Intermediate: Adjusted Equity Shares in an LBO (money shown with $ and 2‑dp; conditional bonus text)"""
    investor = random.choice(investor_names)
    company  = random.choice(company_names)

    total_deal     = random.randint(50, 200)             # $ million
    debt_pct       = random.randint(20, 60)
    equity_pct     = 100 - debt_pct
    share_price    = round(random.uniform(0.5, 5.0), 2)  # $ million per share
    threshold_val  = 2.00                                # $ million
    bonus_factor   = 0.05

    question = (
        f"In a leveraged buyout, {investor} acquires {company} for ${total_deal:.2f} million. "
        f"The deal uses {debt_pct}% debt and {equity_pct}% equity financing. "
        f"Equity is raised by issuing shares at ${share_price:.2f} million per share. "
        f"If the share price is below ${threshold_val:.2f} million, investors receive an additional "
        f"5 % bonus in shares. Calculate the adjusted number of shares issued."
    )

    equity_value  = round(total_deal * equity_pct / 100, 2)              # $ million
    basic_shares  = round(equity_value / share_price, 2)
    bonus_shares  = round(basic_shares * bonus_factor, 2) if share_price < threshold_val else 0.00
    adj_shares    = round(basic_shares + bonus_shares, 2)

    bonus_line = (
        f"Since ${share_price:.2f} m < ${threshold_val:.2f} m, "
        f"bonus shares = 5 % × {basic_shares:.2f} = {bonus_shares:.2f} shares"
        if share_price < threshold_val
        else f"Share price ≥ threshold, so bonus shares = 0"
    )

    solution = (
        f"Step 1  Equity raised:\n"
        f"  ${total_deal:.2f} m × {equity_pct}% = ${equity_value:.2f} m\n\n"
        f"Step 2  Basic shares:\n"
        f"  ${equity_value:.2f} m / ${share_price:.2f} m per share = {basic_shares:.2f} shares\n\n"
        f"Step 3  Bonus shares:\n"
        f"  {bonus_line}\n\n"
        f"Step 4  Adjusted shares issued = {basic_shares:.2f} + {bonus_shares:.2f} = {adj_shares:.2f} shares"
    )
    return question, solution


# ------------------------------------------------------------------
# Advanced Scenario: Multi-step Calculation Involving Control Premium, Debt, and Earnout
def template_control_premium_debt_earnout_calculation():
    """5 : Advanced – Control premium, earn‑out, debt financing (asks for equity value only)."""
    investor = random.choice(investor_names)
    company  = random.choice(company_names)

    base_price              = round(random.uniform(50, 150), 2)   # $ million
    control_premium_percent = random.randint(10, 30)              # %
    earnout_max             = round(random.uniform(5, 20), 2)     # $ million
    achievement_percent     = random.randint(50, 100)             # %
    debt_percent            = random.randint(20, 50)              # %

    # ---------- Question ----------
    question = (
        f"{investor} is acquiring {company}. The base purchase price is "
        f"${base_price:.2f} million. A control premium of {control_premium_percent}% applies. "
        f"The deal also includes an earn‑out of up to ${earnout_max:.2f} million, "
        f"prorated to actual performance (currently {achievement_percent}%). "
        f"The total consideration will be funded with {debt_percent}% debt, the rest equity. "
        f"What is the **equity value** (in $ million) that {investor} must contribute?"
    )

    # ---------- Calculations ----------
    control_premium  = round(base_price * control_premium_percent / 100, 2)
    prorated_earnout = round(earnout_max * achievement_percent   / 100, 2)
    total_deal_value = round(base_price + control_premium + prorated_earnout, 2)
    debt_amount      = round(total_deal_value * debt_percent / 100, 2)
    equity_value     = round(total_deal_value - debt_amount, 2)

    # ---------- Solution ----------
    solution = (
        f"Step 1 – Control premium:\n"
        f"  ${base_price:.2f} × {control_premium_percent}% = ${control_premium:.2f} million\n\n"
        f"Step 2 – Prorated earn‑out:\n"
        f"  ${earnout_max:.2f} × {achievement_percent}% = ${prorated_earnout:.2f} million\n\n"
        f"Step 3 – Total deal value:\n"
        f"  ${base_price:.2f} + ${control_premium:.2f} + ${prorated_earnout:.2f}"
        f" = ${total_deal_value:.2f} million\n\n"
        f"Step 4 – Debt amount:\n"
        f"  ${total_deal_value:.2f} × {debt_percent}% = ${debt_amount:.2f} million\n\n"
        f"Step 5 – Equity value:\n"
        f"  ${total_deal_value:.2f} − ${debt_amount:.2f} = **${equity_value:.2f} million**"
    )

    return question, solution


# ------------------------------------------------------------------
# Main method to generate problems and write to a JSONL file
def main():
    """
    Generate financial reasoning QA pairs on Deal Structure scenarios and save the results to a JSONL file.
    """
    # List of template functions
    templates = [
        template_cash_payment_calculation,             # Basic
        template_stock_swap_calculation,               # Basic
        template_earnout_with_bonus_calculation,  # Intermediate 
        template_leveraged_buyout_adjusted_shares_calculation,  # Intermediate 
        template_control_premium_debt_earnout_calculation  # Advanced
    ]
    
    # List to store all generated problems
    all_problems = []
    
    # Generate one instance per template
    for template_func in templates:
        id = template_func.__doc__.split(':')[0].strip()
        level = template_func.__doc__.split(':')[1].strip()
        
        # Set a unique random seed for reproducibility
        for i in range(10):
        # Generate a unique seed for each problem
            seed = random.randint(1000000000, 4000000000)
            random.seed(seed)
            
            # Generate the question and solution
            question, solution = template_func()
            
            # Create a JSON entry for the problem
            problem_entry = {
                "seed": seed,
                "id": id,
                "level": level,
                "question": question,
                "solution": solution
            }
            
            all_problems.append(problem_entry)
            
            # Reset random seed after each instance
            random.seed()
    
    random.shuffle(all_problems)
    # Write all problems to a JSONL file
    output_file = "../../testset/mergers_and_acquisitions/deal_structure.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
    main()
