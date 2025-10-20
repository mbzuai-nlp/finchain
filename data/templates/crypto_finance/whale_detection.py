import random
import json

def generate_random_value(low, high):
    return round(random.uniform(low, high), 2)

def template_large_transfer_detection():
    """1:Basic: Large Transfer Whale Detection."""
    transfer_amount = generate_random_value(100000, 1000000)
    threshold = generate_random_value(50000, 100000)
    # Ensure transfer_amount > threshold
    if transfer_amount <= threshold:
        transfer_amount = threshold + generate_random_value(1000, 100000)
    question = f"A transaction of ${transfer_amount:.2f} has been recorded. The threshold to flag a whale transfer is ${threshold:.2f}. What is the excess amount over the threshold?"
    excess = transfer_amount - threshold
    solution = "Step 1: Identify the transfer amount and the threshold.\n"
    solution += f"  Transfer Amount = ${transfer_amount:.2f}; Threshold = ${threshold:.2f}.\n"
    solution += "Step 2: Compute the excess by subtracting the threshold from the transfer amount.\n"
    solution += f"  Excess = ${transfer_amount:.2f} - ${threshold:.2f} = ${excess:.2f}."
    return question, solution

def template_wallet_activity_detection():
    """1:Basic: Wallet Activity Whale Detection."""
    transfer_amount = generate_random_value(50000, 500000)
    threshold = generate_random_value(20000, 50000)
    # Ensure transfer_amount > threshold
    if transfer_amount <= threshold:
        transfer_amount = threshold + generate_random_value(1000, 50000)
    ratio = transfer_amount / threshold
    question = f"A wallet executes a transfer of ${transfer_amount:.2f}. Given that the whale detection threshold is ${threshold:.2f}, what is the ratio of the transfer amount to the threshold (rounded to two decimal places)?"
    solution = "Step 1: Note the transfer amount and the threshold.\n"
    solution += f"  Transfer Amount = ${transfer_amount:.2f}; Threshold = ${threshold:.2f}.\n"
    solution += "Step 2: Calculate the ratio as Transfer Amount divided by Threshold.\n"
    solution += f"  Ratio = {transfer_amount:.2f} / {threshold:.2f} = {ratio:.2f}."
    return question, solution

def template_multiple_transaction_analysis():
    """2:Intermediate: Multi-transaction Whale Detection Analysis."""
    trans1 = generate_random_value(30000, 300000)
    trans2 = generate_random_value(30000, 300000)
    trans3 = generate_random_value(30000, 300000)
    threshold = generate_random_value(50000, 150000)
    excess1 = trans1 - threshold if trans1 > threshold else 0
    excess2 = trans2 - threshold if trans2 > threshold else 0
    excess3 = trans3 - threshold if trans3 > threshold else 0
    total_excess = excess1 + excess2 + excess3
    question = (f"Three transactions of ${trans1:.2f}, ${trans2:.2f}, and ${trans3:.2f} are recorded. "
                f"If the whale detection threshold is ${threshold:.2f} for each transaction, what is the total excess amount over the threshold across all transactions?")
    solution = "Step 1: For each transaction, compute the excess amount over the threshold (only if above threshold).\n"
    solution += f"  Transaction 1 excess: max(${trans1:.2f} - ${threshold:.2f}, 0) = ${excess1:.2f}\n"
    solution += f"  Transaction 2 excess: max(${trans2:.2f} - ${threshold:.2f}, 0) = ${excess2:.2f}\n"
    solution += f"  Transaction 3 excess: max(${trans3:.2f} - ${threshold:.2f}, 0) = ${excess3:.2f}\n"
    solution += "Step 2: Sum the excess amounts.\n"
    solution += f"  Total Excess = ${excess1:.2f} + ${excess2:.2f} + ${excess3:.2f} = ${total_excess:.2f}."
    return question, solution

def template_threshold_adjustment_detection():
    """2:Intermediate: Variable Threshold Whale Detection."""
    trans_amount = generate_random_value(80000, 600000)
    orig_threshold = generate_random_value(40000, 100000)
    factor = round(random.uniform(-5, 5), 2)
    new_threshold = orig_threshold * (1 + factor / 100)
    excess = trans_amount - new_threshold if trans_amount > new_threshold else 0
    question = (f"A transfer of ${trans_amount:.2f} is observed. Initially, the whale detection threshold is set at ${orig_threshold:.2f}. "
                f"After an adjustment of {factor:.2f}%, the new threshold becomes ${new_threshold:.2f}. What is the excess amount of the transfer over the new threshold?")
    solution = "Step 1: Compute the new threshold by adjusting the original threshold by the given percentage.\n"
    solution += f"  New Threshold = ${orig_threshold:.2f} * (1 + {factor:.2f}/100) = ${new_threshold:.2f}.\n"
    solution += "Step 2: Calculate the excess of the transfer amount over the new threshold.\n"
    solution += f"  Excess = ${trans_amount:.2f} - ${new_threshold:.2f} = ${excess:.2f}."
    return question, solution

def template_cross_exchange_impact():
    """3:Advanced: Cross-Exchange Whale Transaction."""
    amount = generate_random_value(200000, 1000000)
    fee_percent = round(random.uniform(0.50, 5.00), 2)
    threshold = generate_random_value(150000, 500000)
    effective_amount = amount * (1 - fee_percent / 100)
    net_excess = effective_amount - threshold if effective_amount > threshold else 0
    question = (f"A transfer of ${amount:.2f} is made between two exchanges. Exchange B applies a fee of {fee_percent:.2f}%, "
                f"resulting in an effective transfer value of ${effective_amount:.2f}. Given a whale detection threshold of ${threshold:.2f}, "
                f"what is the net excess amount over the threshold?")
    solution = "Step 1: Determine the effective transfer amount after applying the fee.\n"
    solution += f"  Effective Amount = ${amount:.2f} * (1 - {fee_percent:.2f}/100) = ${effective_amount:.2f}\n"
    solution += "Step 2: Compute the net excess of the effective amount over the threshold.\n"
    solution += f"  Net Excess = ${effective_amount:.2f} - ${threshold:.2f} = ${net_excess:.2f}."
    return question, solution

def main():
    """
    Generate 10 instances of each template with different random seeds 
    and write the results to a JSON file.
    """
    templates = [
        template_large_transfer_detection,
        template_wallet_activity_detection,
        template_multiple_transaction_analysis,
        template_threshold_adjustment_detection,
        template_cross_exchange_impact
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
    output_file = "../../testset/crypto_finance/whale_detection.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == '__main__':
    main()