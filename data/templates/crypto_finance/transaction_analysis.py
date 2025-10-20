import random

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_transaction_fee_calculation():
    """Basic: Transaction with percentage fee."""
    transaction_value = generate_random_value(1000, 5000)
    fee_percent = round(random.uniform(0.5, 5.0), 2)
    question = f"A crypto transaction of ${transaction_value:.2f} is processed with a fee of {fee_percent:.2f}%. What is the net amount received?"
    net_amount = round(transaction_value * (1 - fee_percent/100), 2)
    solution = "Step 1: Compute the fee percentage of the transaction value.\n"
    solution += f"  {transaction_value:.2f} * ({fee_percent:.2f}/100) = ${transaction_value * (fee_percent/100):.2f} fee.\n"
    solution += "Step 2: Subtract the fee from the original amount.\n"
    solution += f"  Net amount = {transaction_value:.2f} - {transaction_value * (fee_percent/100):.2f} = ${net_amount:.2f}."
    return question, solution

def template_fixed_fee_transaction():
    """Basic: Transaction with fixed fee."""
    transaction_value = generate_random_value(500, 3000)
    fixed_fee = generate_random_value(1, 50)
    question = f"A crypto transaction worth ${transaction_value:.2f} has a fixed fee of ${fixed_fee:.2f}. What is the net amount received?"
    net_amount = round(transaction_value - fixed_fee, 2)
    solution = "Step 1: Identify the fixed fee to be subtracted.\n"
    solution += f"  Fixed fee = ${fixed_fee:.2f}.\n"
    solution += "Step 2: Subtract the fee from the transaction value.\n"
    solution += f"  Net amount = {transaction_value:.2f} - {fixed_fee:.2f} = ${net_amount:.2f}."
    return question, solution

def template_bulk_transaction_fees():
    """Intermediate: Batch of transactions with varying fees."""
    t1 = generate_random_value(1000, 5000)
    t2 = generate_random_value(1000, 5000)
    t3 = generate_random_value(1000, 5000)
    fee1 = round(random.uniform(0.5, 5.0), 2)
    fee2 = round(random.uniform(0.5, 5.0), 2)
    fee3 = round(random.uniform(0.5, 5.0), 2)
    question = (f"A batch of crypto transactions includes amounts of ${t1:.2f}, ${t2:.2f}, and ${t3:.2f} "
                f"with respective fee rates of {fee1:.2f}%, {fee2:.2f}%, and {fee3:.2f}%. "
                f"What is the total net amount received from all transactions?")
    net1 = t1 * (1 - fee1/100)
    net2 = t2 * (1 - fee2/100)
    net3 = t3 * (1 - fee3/100)
    total_net = round(net1 + net2 + net3, 2)
    solution = "Step 1: Compute the net amount for each transaction:\n"
    solution += f"  Transaction 1: {t1:.2f} * (1 - {fee1:.2f}/100) = ${net1:.2f}.\n"
    solution += f"  Transaction 2: {t2:.2f} * (1 - {fee2:.2f}/100) = ${net2:.2f}.\n"
    solution += f"  Transaction 3: {t3:.2f} * (1 - {fee3:.2f}/100) = ${net3:.2f}.\n"
    solution += "Step 2: Sum up the net amounts:\n"
    solution += f"  Total net amount = ${total_net:.2f}."
    return question, solution

def template_cross_chain_transfer():
    """Intermediate: Cross-chain transfer with fee and bonus."""
    initial_value = generate_random_value(1000, 10000)
    fee_percent = round(random.uniform(1.0, 3.0), 2)
    bonus = generate_random_value(10, 100)
    question = (f"A cross-chain crypto transaction of ${initial_value:.2f} is subject to a fee of {fee_percent:.2f}%. "
                f"After fee deduction, a bonus of ${bonus:.2f} is credited. What is the net amount received?")
    net_after_fee = initial_value * (1 - fee_percent/100)
    net_final = round(net_after_fee + bonus, 2)
    solution = "Step 1: Deduct the fee from the initial transaction value.\n"
    solution += f"  {initial_value:.2f} * (1 - {fee_percent:.2f}/100) = ${net_after_fee:.2f} after fee.\n"
    solution += "Step 2: Add the bonus credit to the amount after fee deduction.\n"
    solution += f"  Net amount = {net_after_fee:.2f} + {bonus:.2f} = ${net_final:.2f}."
    return question, solution

def template_multi_factor_transaction():
    """Advanced: Multi-factor transaction with split and bonus."""
    transaction_value = generate_random_value(5000, 20000)
    split_ratio = 0.60  # 60% to network 1, 40% to network 2
    fee_percent_net1 = round(random.uniform(1.0, 4.0), 2)
    fixed_fee_net2 = generate_random_value(20, 100)
    bonus_percent_net2 = round(random.uniform(2.0, 6.0), 2)
    
    part1 = transaction_value * split_ratio
    part2 = transaction_value * (1 - split_ratio)
    net1 = part1 * (1 - fee_percent_net1/100)
    net2 = (part2 - fixed_fee_net2) * (1 + bonus_percent_net2/100)
    total_net = round(net1 + net2, 2)
    
    question = (f"A crypto transaction of ${transaction_value:.2f} is split into two parts: 60% goes to Network 1 and "
                f"40% goes to Network 2. Network 1 charges a fee of {fee_percent_net1:.2f}% on its part. "
                f"Network 2 applies a fixed fee of ${fixed_fee_net2:.2f} and then adds a bonus of {bonus_percent_net2:.2f}% on the remaining amount. "
                f"What is the total net amount received?")
                
    solution = "Step 1: Split the transaction:\n"
    solution += f"  Part1 (Network 1): {transaction_value:.2f} * 60% = ${part1:.2f}.\n"
    solution += f"  Part2 (Network 2): {transaction_value:.2f} * 40% = ${part2:.2f}.\n"
    solution += "Step 2: Process each network separately:\n"
    solution += f"  Network 1: {part1:.2f} * (1 - {fee_percent_net1:.2f}/100) = ${net1:.2f}.\n"
    solution += f"  Network 2: ({part2:.2f} - {fixed_fee_net2:.2f}) * (1 + {bonus_percent_net2:.2f}/100) = ${net2:.2f}.\n"
    solution += "Step 3: Sum the net amounts from both networks:\n"
    solution += f"  Total net amount = ${net1:.2f} + ${net2:.2f} = ${total_net:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    import json
    templates = [
        template_transaction_fee_calculation,
        template_fixed_fee_transaction,
        template_bulk_transaction_fees,
        template_cross_chain_transfer,
        template_multi_factor_transaction
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
    output_file = "../../testset/crypto_finance/transaction_analysis.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()