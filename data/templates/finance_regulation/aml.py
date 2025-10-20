import random

investor_names = ["John Doe", "Sarah Nguyen", "Emily White", "Carlos Alvarez", "Ava Patel"]
company_names = [
    "Goldman Sachs", "Wells Fargo", "Bank of America", "JPMorgan Chase", "Morgan Stanley",
    "Citibank", "Charles Schwab", "American Express", "Fidelity Investments", "Robinhood"
]

# BASIC SCENARIOS (1–2 steps)
def template_aml_basic_threshold_violation():
    """1:Basic: Detect whether a cash transaction violates the AML threshold (above or below)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    threshold = 10000

    # Decide whether to generate above or below threshold amount
    if random.random() < 0.5:
        amount = random.randint(threshold + 1, threshold + 5000)  # Above threshold
        should_report = True
    else:
        amount = random.randint(threshold - 5000, threshold - 1)  # Below threshold
        should_report = False

    question = (
        f"{investor} deposited ${amount} in cash into their account at {company}. "
        f"Given the AML threshold for cash reporting is ${threshold}, should this transaction be reported?"
    )

    if should_report:
        solution = (
            f"Step 1: Compare the cash deposit (${amount}) with the AML threshold (${threshold}).\n"
            f"Since ${amount} > ${threshold}, the transaction exceeds the threshold.\n\n"
            f"Step 2: Conclusion: This transaction **should be reported** under AML regulations."
        )
    else:
        solution = (
            f"Step 1: Compare the cash deposit (${amount}) with the AML threshold (${threshold}).\n"
            f"Since ${amount} < ${threshold}, the transaction does not exceed the threshold.\n\n"
            f"Step 2: Conclusion: This transaction does not need to be reported under AML regulations."
        )

    return question, solution



def template_aml_basic_structuring_detection():
    """2:Basic: Detect possible structuring by splitting deposits (above or below threshold)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    threshold = 10000

    # Randomly decide whether the total should exceed or not exceed the threshold
    if random.random() < 0.5:
        # Case: likely structuring (total just over threshold using two deposits)
        while True:
            amounts = [random.randint(4500, 6000), random.randint(4500, 6000)]
            total = sum(amounts)
            if total > threshold:
                likely_structuring = True
                break
    else:
        # Case: not structuring (total well below threshold)
        while True:
            amounts = [random.randint(3000, 4500), random.randint(3000, 4500)]
            total = sum(amounts)
            if total < threshold:
                likely_structuring = False
                break

    question = (
        f"{investor} made two consecutive cash deposits of ${amounts[0]} and ${amounts[1]} into an account at {company}. "
        f"The AML reporting threshold is ${threshold}. Is this an example of structuring?"
    )

    if likely_structuring:
        solution = (
            f"Step 1: Add the two deposits: ${amounts[0]} + ${amounts[1]} = ${total}\n"
            f"Step 2: Since the total ${total} > ${threshold}, and the amounts were split into smaller deposits, "
            f"this may indicate an attempt to avoid triggering reporting requirements.\n\n"
            f"Conclusion: Yes, this is likely structuring under AML regulations."
        )
    else:
        solution = (
            f"Step 1: Add the two deposits: ${amounts[0]} + ${amounts[1]} = ${total}\n"
            f"Step 2: Since the total ${total} < ${threshold}, and the amounts are small, "
            f"this does not indicate an attempt to avoid reporting.\n\n"
            f"Conclusion: No, this is unlikely to be structuring under AML regulations."
        )

    return question, solution



# INTERMEDIATE SCENARIOS (3–4 steps)
def template_aml_intermediate_beneficial_ownership_check():
    """3:Intermediate: Verify whether beneficial ownership disclosure is required (above or below threshold)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    threshold = 25

    # Randomly choose whether to exceed or stay below the threshold
    if random.random() < 0.5:
        # Above threshold case: requires disclosure
        while True:
            ownerships = [random.randint(15, 30), random.randint(10, 30)]
            final_ownership = sum(ownerships)
            if final_ownership > threshold:
                requires_disclosure = True
                break
    else:
        # Below threshold case: does not require disclosure
        while True:
            ownerships = [random.randint(5, 15), random.randint(5, 15)]
            final_ownership = sum(ownerships)
            if final_ownership <= threshold:
                requires_disclosure = False
                break

    question = (
        f"{investor} owns {ownerships[0]}% of a shell company and an additional {ownerships[1]}% via a trust. "
        f"The shell company is opening an account at {company}. Must the beneficial ownership be disclosed?"
    )

    if requires_disclosure:
        solution = (
            f"Step 1: Add ownership percentages: {ownerships[0]}% + {ownerships[1]}% = {final_ownership}%\n"
            f"Step 2: Compare with AML disclosure threshold of {threshold}%.\n"
            f"Since {final_ownership}% > {threshold}%, disclosure is required.\n\n"
            f"Conclusion: Yes, the beneficial ownership must be disclosed under AML regulations."
        )
    else:
        solution = (
            f"Step 1: Add ownership percentages: {ownerships[0]}% + {ownerships[1]}% = {final_ownership}%\n"
            f"Step 2: Compare with AML disclosure threshold of {threshold}%.\n"
            f"Since {final_ownership}% ≤ {threshold}%, disclosure is not required.\n\n"
            f"Conclusion: No, beneficial ownership does not need to be disclosed in this case."
        )

    return question, solution



def template_aml_intermediate_multiple_entities_with_ownership():
    """4:Intermediate: Trace indirect beneficial ownership through randomized layered entities (above/below threshold)"""
    investor = random.choice(investor_names)
    company = random.choice(company_names)
    threshold = 25

    def generate_layers(above_threshold=True):
        # Try generating until the effective ownership matches the goal
        for _ in range(100):
            layers = [
                {"layer": 1, "ownership": random.randint(30, 90)},
                {"layer": 2, "ownership": random.randint(30, 90)},
                {"layer": 3, "ownership": random.randint(30, 90)},
            ]
            effective_ownership = 1.0
            for l in layers:
                effective_ownership *= (l["ownership"] / 100)
            effective_percent = round(effective_ownership * 100, 2)
            if (above_threshold and effective_percent > threshold) or (not above_threshold and effective_percent <= threshold):
                return layers, effective_percent
        # fallback in case of bad luck
        return layers, effective_percent

    # Randomly choose to generate an above or below threshold case
    above_threshold = random.random() < 0.5
    layers, effective_ownership_percent = generate_layers(above_threshold)

    question = (
        f"{investor} indirectly owns shares in an entity opening an account at {company} via 3 layered shell companies with "
        f"{layers[0]['ownership']}%, {layers[1]['ownership']}%, and {layers[2]['ownership']}% ownership at each level.\n"
        f"Does this exceed the beneficial ownership threshold of {threshold}%?"
    )

    solution = (
        f"Step 1: Multiply ownership at each layer:\n"
        f"  Effective Ownership = ({layers[0]['ownership']}% × {layers[1]['ownership']}% × {layers[2]['ownership']}%)\n"
        f"                     = {effective_ownership_percent:.2f}%\n\n"
        f"Step 2: Compare with threshold: {effective_ownership_percent:.2f}% "
        f"{'>' if effective_ownership_percent > threshold else '≤'} {threshold}%\n"
        f"Step 3: Conclusion: {'Yes' if effective_ownership_percent > threshold else 'No'}, disclosure "
        f"{'is' if effective_ownership_percent > threshold else 'is not'} required under AML regulations."
    )

    return question, solution



def template_aml_advanced_sar_decision_based_on_risk_score_and_flags():
    """5:Advanced: File SAR based on risk score, number and nature of red flags (multi-step)"""

    investor = random.choice(investor_names)
    company = random.choice(company_names)
    score = random.randint(65, 95)
    all_flags = ["PEP", "Unusual transaction", "Offshore entity", "High cash activity", "Unverified source of funds"]
    k = random.randint(0, len(all_flags))  # choose 0–5 flags
    flags = random.sample(all_flags, k=k)

    threshold_score = 75
    threshold_flags = 2

    question = (
        f"{investor} is being reviewed at {company}.\n"
        f"- Risk Score: {score}\n"
        f"- Flags Raised: {', '.join(flags) if flags else 'None'}\n"
        f"A Suspicious Activity Report (SAR) must be filed if:\n"
        f"(1) Risk Score exceeds {threshold_score}, **and**\n"
        f"(2) More than {threshold_flags - 1} red flags are present, **or** certain flags such as 'PEP' or 'Unverified source of funds' are present.\n"
        f"Should a SAR be filed?"
    )

    # Evaluate conditions
    critical_flags = {"PEP", "Unverified source of funds"}
    has_critical_flag = any(f in critical_flags for f in flags)
    sufficient_flags = len(flags) >= threshold_flags
    high_score = score > threshold_score
    decision = high_score and (sufficient_flags or has_critical_flag)

    solution = (
        f"Step 1: Risk Score = {score} → {'Exceeds' if high_score else 'Does not exceed'} threshold of {threshold_score}.\n"
        f"Step 2: Number of red flags = {len(flags)} → {'Sufficient' if sufficient_flags else 'Insufficient'} (Need ≥ {threshold_flags}).\n"
        f"Step 3: Check for critical flags (PEP, Unverified source of funds) → "
        f"{'Present' if has_critical_flag else 'None present'}.\n"
        f"Step 4: Regulatory logic: SAR is filed if score is high **and** (flags are sufficient **or** critical flag is present).\n"
        f"Step 5: Final evaluation → All conditions {'met' if decision else 'not met'}.\n"
        f"Conclusion: {'File' if decision else 'Do not file'} a Suspicious Activity Report."
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
        template_aml_basic_threshold_violation,
        template_aml_basic_structuring_detection,
        template_aml_intermediate_beneficial_ownership_check,
        template_aml_intermediate_multiple_entities_with_ownership,
        template_aml_advanced_sar_decision_based_on_risk_score_and_flags
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
    output_file = "../../testset/finance_regulation/aml.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")


if __name__ == "__main__":
   main()