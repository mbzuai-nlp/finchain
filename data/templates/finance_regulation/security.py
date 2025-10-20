import random

# Sample named entities
investor_names = ["Alice Johnson", "Robert Smith", "Maria Garcia", "James Wang", "Linda Davis"]
company_names = [
    "Tesla", "Amazon", "Apple", "Google", "Microsoft",
    "Meta", "Netflix", "JPMorgan Chase", "Goldman Sachs", "Pfizer"
]

def random_entities():
    return random.choice(investor_names), random.choice(company_names)

### BASIC LEVEL (1-2 steps) ###

def template_security_basic_disclosure_threshold():
    """1:Basic: Determine disclosure obligation based on investor type and threshold rules"""
    investor, company = random_entities()

    # Different investor types
    investor_type = random.choice(["individual investor", "institutional investor", "passive investor"])

    # Ownership percentage
    ownership = round(random.uniform(1, 15), 2)

    # Define thresholds based on investor type
    if investor_type == "passive investor":
        threshold = 10.0  # 13G
        form = "Schedule 13G"
    else:
        threshold = 5.0   # 13D
        form = "Schedule 13D"

    question = (
        f"{investor}, a {investor_type}, has acquired {ownership:.2f}% of {company}'s shares.\n"
        f"According to SEC rules, a {form} must be filed if ownership exceeds {threshold:.1f}%.\n"
        f"Is disclosure required in this case?"
    )

    disclosure_required = ownership > threshold

    solution = (
        f"Step 1: Identify investor type: {investor_type} → Threshold = {threshold}% → Required form: {form}\n"
        f"Step 2: Compare ownership: {ownership:.2f}% {'>' if disclosure_required else '<='} {threshold}%\n"
        f"Conclusion: {'Yes' if disclosure_required else 'No'}, disclosure {'is' if disclosure_required else 'is not'} required under SEC rules."
    )

    return question, solution


def template_security_basic_insider_trading_gain():
    """2:Basic: Calculate gain from insider trading"""
    investor, company = random_entities()
    buy_price = round(random.uniform(80, 100), 2)
    sell_price = round(random.uniform(110, 140), 2)
    shares = random.randint(100, 1000)
    
    gain = (sell_price - buy_price) * shares
    question = (
        f"{investor}, an executive at {company}, bought {shares} shares at ${buy_price:.2f} based on non-public information.\n"
        f"They sold them later at ${sell_price:.2f}. What is the total gain made through insider trading?"
    )
    solution = (
        f"Step 1: Calculate the gain per share: ${sell_price:.2f} - ${buy_price:.2f} = ${sell_price - buy_price:.2f}\n"
        f"Step 2: Multiply by number of shares: {shares} × ${sell_price - buy_price:.2f} = ${gain:.2f}"
    )
    return question, solution

### INTERMEDIATE LEVEL (3-4 steps) ###

def template_security_intermediate_reg_a_investment_limit():
    """3:Intermediate: Check if investment exceeds Reg A+ Tier 2 limit (4 reasoning steps)"""

    investor, company = random_entities()
    annual_income = random.randint(50_000, 150_000)
    investment = random.randint(20_000, 70_000)
    is_audited = random.choice([True, False])
    limit_ratio = 0.10
    limit = round(annual_income * limit_ratio, 2)

    question = (
        f"{investor} wants to invest ${investment:,} in a Regulation A+ Tier 2 offering from {company}.\n"
        f"Their reported annual income is ${annual_income:,}. "
        f"The offering is {'audited' if is_audited else 'unaudited'}.\n"
        f"Under SEC rules, unaudited offerings are subject to a 10% income cap. "
        f"Can {investor} legally make this investment?"
    )

    # Determine if limit applies and assess legality
    solution = (
        f"Step 1: Identify audit status → Offering is {'audited' if is_audited else 'unaudited'}.\n"
        f"Step 2: Determine if 10% income cap applies → "
        f"{'No cap for audited offerings.' if is_audited else f'Cap applies → 10% of ${annual_income:,} = ${limit:,.2f}'}\n"
        f"Step 3: {'No comparison needed (✓)' if is_audited else f'Compare investment ${investment:,} to limit ${limit:,.2f} → ' + ('Within limit (✓)' if investment <= limit else 'Exceeds limit (✗)')}\n"
        f"Step 4: Conclusion → " +
        (
            "Yes, the investment is allowed because the offering is audited."
            if is_audited else (
                "Yes, investment is within the permitted cap."
                if investment <= limit else
                "No, investment exceeds the allowable limit for unaudited offerings."
            )
        )
    )

    return question, solution


def template_security_intermediate_multiple_reporting_thresholds():
    """4:Intermediate: Calculate combined ownership across entities for SEC 5% reporting rule (fixed 4-step reasoning)"""
    
    investor, company = random_entities()
    direct = round(random.uniform(2, 4), 2)
    trust = round(random.uniform(1, 3), 2)
    spouse = round(random.uniform(1, 4), 2)
    total = round(direct + trust + spouse, 2)
    threshold = 5.0

    question = (
        f"{investor} holds ownership in {company} through three sources:\n"
        f"- Direct: {direct:.2f}%\n"
        f"- Family trust: {trust:.2f}%\n"
        f"- Spouse: {spouse:.2f}%\n"
        f"Under SEC rules, beneficial ownership exceeding {threshold}% requires a public disclosure filing.\n"
        f"Does {investor} need to report their ownership?"
    )

    solution = (
        f"Step 1: Identify all forms of indirect and direct ownership.\n"
        f"         → Direct = {direct:.2f}%, Trust = {trust:.2f}%, Spouse = {spouse:.2f}%\n"
        f"Step 2: Aggregate total beneficial ownership = {direct:.2f}% + {trust:.2f}% + {spouse:.2f}% = {total:.2f}%\n"
        f"Step 3: Compare total ownership with the SEC threshold (5.00%) → {total:.2f}% {'>' if total > threshold else '<='} 5.00%\n"
        f"Step 4: Conclusion → "
        f"{'Yes, disclosure is required because total ownership exceeds 5%.' if total > threshold else 'No, disclosure is not required.'}"
    )

    return question, solution



### ADVANCED LEVEL (>4 steps) ###
def template_security_advanced_merger_announcement_timing():
    """5:Advanced: Evaluate insider trading gains and determine SEC penalty under variable enforcement rules"""
    investor, company = random_entities()

    # Price movement before and after announcement
    pre_price = round(random.uniform(50, 70), 2)
    multiplier = random.uniform(0.8, 1.5)  # price may rise or fall
    post_price = round(pre_price * multiplier, 2)
    shares = random.randint(500, 2000)

    # Calculate gain or loss
    gain_per_share = round(post_price - pre_price, 2)
    total_gain = round(gain_per_share * shares, 2)

    # Penalty logic — maximum of 3× gain or fixed statutory fine
    statutory_penalty = 200_000
    penalty = max(3 * abs(total_gain), statutory_penalty)

    # Determine whether it's a profit or a loss
    gain_label = "gain" if total_gain > 0 else "loss"
    penalty_comment = (
        f"Although the investor incurred a {gain_label}, SEC may still impose penalties if the trade was illegal."
        if total_gain < 0 else
        "Since the investor profited from the trade, SEC may impose penalties based on the gain."
    )

    question = (
        f"{investor} traded {shares} shares of {company} one day before a confidential merger announcement.\n"
        f"The stock price moved from ${pre_price:.2f} to ${post_price:.2f} after the announcement.\n"
        f"The SEC is investigating potential insider trading. What is the {gain_label}, and what penalty may apply under SEC rules?"
    )

    solution = (
        f"Step 1: Gain/Loss per share = ${post_price:.2f} - ${pre_price:.2f} = ${gain_per_share:.2f}\n"
        f"Step 2: Total {gain_label} = {shares} × ${gain_per_share:.2f} = ${total_gain:.2f}\n"
        f"Step 3: SEC penalty is the greater of 3× gain/loss or a statutory fine of ${statutory_penalty:,.2f}\n"
        f"         → 3× gain/loss = ${3 * abs(total_gain):,.2f}\n"
        f"         → Statutory fine = ${statutory_penalty:,.2f}\n"
        f"Step 4: Penalty = max(3× gain/loss, statutory fine) = ${penalty:,.2f}\n"
        f"Step 5: {penalty_comment}"
    )

    return question, solution



def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    # ----------- Export All to JSONL -----------

    # List of template functions
    templates = [
        template_security_basic_disclosure_threshold,
        template_security_basic_insider_trading_gain,
        template_security_intermediate_reg_a_investment_limit,
        template_security_intermediate_multiple_reporting_thresholds,
        template_security_advanced_merger_announcement_timing
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
    output_file = "../../testset/finance_regulation/security.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")


if __name__ == "__main__":
   main()