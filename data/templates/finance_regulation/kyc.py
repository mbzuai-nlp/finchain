import random

# Sample named entities
investor_names = ["Alice Johnson", "Brian Thompson", "Catherine Lee", "Daniel Wright", "Evelyn Clark"]
company_names = ["Wells Fargo", "JPMorgan Chase", "Goldman Sachs", "Citibank", "Bank of America"]

# Helper to choose random entities
def get_random_entities():
    return random.choice(investor_names), random.choice(company_names)

### ========== BASIC QUESTIONS (1-2 step) ==========
def template_kyc_basic_customer_type():
    """1:Intermediate: Classify customer type for KYC based on account nature"""
    investor, company = get_random_entities()

    # Expanded account types for KYC realism
    account_type = random.choice([
        "personal savings",         # individual
        "joint",                    # individual
        "business",                 # corporate
        "non-profit organization",  # NGO
        "trust",                    # trust
        "minor account",            # special individual
        "partnership",             # partnership
        "offshore company"         # corporate/offshore
    ])

    # KYC classification logic
    if account_type in ["personal savings", "joint", "minor account"]:
        classification = "individual customer"
    elif account_type == "trust":
        classification = "trust account"
    elif account_type == "non-profit organization":
        classification = "NGO / non-corporate entity"
    elif account_type == "partnership":
        classification = "partnership entity"
    else:  # business, offshore company
        classification = "corporate customer"

    question = (
        f"{investor} is opening a {account_type} account at {company}. "
        f"According to KYC regulations, how should this customer be classified?"
    )

    solution = (
        f"Step 1: Identify the type of account: {account_type}\n"
        f"Step 2: Apply KYC classification logic:\n"
        f"  - Individual accounts: personal, joint, minor → individual customer\n"
        f"  - Trust → trust account\n"
        f"  - Non-profit → NGO / non-corporate entity\n"
        f"  - Partnership → partnership entity\n"
        f"  - Business/offshore → corporate customer\n"
        f"Answer: {classification}"
    )

    return question, solution


def template_kyc_basic_id_required():
    """2:Intermediate: Evaluate whether a KYC document is valid for identity or address verification"""
    investor, company = get_random_entities()

    # Expanded document set
    documents = [
        "passport",                 # identity
        "driver’s license",         # identity & address (sometimes)
        "national ID card",         # identity
        "utility bill",             # address
        "bank statement",           # address
        "employee ID",              # not valid
        "student ID",               # not valid
        "rental agreement"          # address
    ]

    document = random.choice(documents)
    purpose = random.choice(["identity verification", "address verification"])

    # Classification logic
    identity_docs = ["passport", "driver’s license", "national ID card"]
    address_docs = ["utility bill", "bank statement", "rental agreement", "driver’s license"]

    if purpose == "identity verification":
        is_valid = document in identity_docs
    else:  # address verification
        is_valid = document in address_docs

    question = (
        f"{investor} submitted a {document} to {company} for KYC purposes.\n"
        f"Is this document valid for {purpose} under standard KYC regulations?"
    )

    solution = (
        f"Step 1: Identify the purpose: {purpose}\n"
        f"Step 2: Check if {document} is acceptable for this purpose:\n"
        f"  - Valid identity documents: {', '.join(identity_docs)}\n"
        f"  - Valid address documents: {', '.join(address_docs)}\n"
        f"Step 3: {document} {'is' if is_valid else 'is not'} valid for {purpose}.\n"
        f"Answer: {'Yes' if is_valid else 'No'}"
    )

    return question, solution


### ========== INTERMEDIATE QUESTIONS (3-4 steps) ==========

def template_kyc_intermediate_risk_level_by_country():
    """3:Intermediate: Multi-step reasoning to assess KYC risk level using country, sector, and customer profile"""
    investor, company = get_random_entities()

    # Base country risk levels (based on FATF + sanctions context)
    country_risks = {
        "Germany": {"score": 2.0, "sanctioned": False},
        "USA": {"score": 3.0, "sanctioned": False},
        "France": {"score": 2.5, "sanctioned": False},
        "Iran": {"score": 9.0, "sanctioned": True},
        "North Korea": {"score": 10.0, "sanctioned": True},
        "Russia": {"score": 8.0, "sanctioned": True},
        "China": {"score": 6.0, "sanctioned": False},
        "Turkey": {"score": 5.5, "sanctioned": False}
    }

    sectors = {
        "Retail": {"multiplier": 1.0, "requires_edd": False},
        "Crypto": {"multiplier": 2.0, "requires_edd": True},
        "Defense": {"multiplier": 2.2, "requires_edd": True},
        "Mining": {"multiplier": 1.5, "requires_edd": False},
        "NGO": {"multiplier": 1.8, "requires_edd": True}
    }

    country = random.choice(list(country_risks.keys()))
    sector = random.choice(list(sectors.keys()))
    base_score = country_risks[country]["score"]
    is_sanctioned = country_risks[country]["sanctioned"]
    sector_info = sectors[sector]
    multiplier = sector_info["multiplier"]
    requires_edd = sector_info["requires_edd"]

    composite_score = round(base_score * multiplier, 2)

    # KYC classification
    if composite_score >= 8 or is_sanctioned:
        risk_level = "High Risk"
    elif composite_score >= 5 or requires_edd:
        risk_level = "Medium Risk"
    else:
        risk_level = "Standard Risk"

    question = (
        f"{investor} is opening an account at {company}.\n"
        f"The customer is a national of {country} (base risk: {base_score}, "
        f"{'on' if is_sanctioned else 'not on'} sanctions list).\n"
        f"The business operates in the {sector} sector (risk multiplier: {multiplier}, "
        f"{'EDD required' if requires_edd else 'EDD not required'}).\n"
        f"What is the composite KYC risk level for this customer?"
    )

    solution = (
        f"Step 1: Identify country risk:\n"
        f"  {country} has a base score of {base_score} and "
        f"{'is' if is_sanctioned else 'is not'} on the sanctions list.\n\n"
        f"Step 2: Identify sector impact:\n"
        f"  {sector} sector has a multiplier of {multiplier} and "
        f"{'requires' if requires_edd else 'does not require'} enhanced due diligence (EDD).\n\n"
        f"Step 3: Compute composite risk score:\n"
        f"  {base_score} × {multiplier} = {composite_score}\n\n"
        f"Step 4: Apply classification rules:\n"
        f"  - High Risk if score ≥ 8 or sanctioned country\n"
        f"  - Medium Risk if score ≥ 5 or sector requires EDD\n"
        f"  - Standard Risk otherwise\n\n"
        f"Final classification: {risk_level}"
    )

    return question, solution


def template_kyc_intermediate_source_of_funds_analysis():
    """4:Intermediate: Multi-step source of funds risk evaluation using source type, amount, and context"""
    investor, company = get_random_entities()

    sources = {
        "inheritance": {"base_risk": 2, "traceability": "medium"},
        "cryptocurrency mining": {"base_risk": 7, "traceability": "low"},
        "salary": {"base_risk": 1, "traceability": "high"},
        "lottery winnings": {"base_risk": 8, "traceability": "low"},
        "gift from relative": {"base_risk": 5, "traceability": "low"},
        "real estate sale": {"base_risk": 4, "traceability": "medium"}
    }

    countries = {
        "Germany": {"jurisdiction_risk": 1},
        "Iran": {"jurisdiction_risk": 8},
        "USA": {"jurisdiction_risk": 2},
        "Russia": {"jurisdiction_risk": 7},
        "France": {"jurisdiction_risk": 2}
    }

    source = random.choice(list(sources.keys()))
    country = random.choice(list(countries.keys()))
    amount = random.choice([10000, 50000, 100000, 250000])

    base_risk = sources[source]["base_risk"]
    traceability = sources[source]["traceability"]
    jurisdiction_risk = countries[country]["jurisdiction_risk"]

    total_risk_score = base_risk + jurisdiction_risk
    risk_level = (
        "High Risk" if total_risk_score >= 12 or (amount >= 100000 and traceability == "low")
        else "Medium Risk" if total_risk_score >= 8
        else "Low Risk"
    )

    question = (
        f"{investor} is depositing ${amount:,} into a new account at {company}.\n"
        f"The declared source of funds is '{source}', and the customer resides in {country}.\n"
        f"How should this deposit be classified under KYC source-of-funds risk evaluation?"
    )

    solution = (
        f"Step 1: Evaluate source of funds:\n"
        f"  - Source: {source} → Base risk score = {base_risk}, Traceability = {traceability}\n"
        f"Step 2: Evaluate jurisdictional risk:\n"
        f"  - Country = {country} → Jurisdiction risk score = {jurisdiction_risk}\n"
        f"Step 3: Compute total risk score = {base_risk} (source) + {jurisdiction_risk} (country) = {total_risk_score}\n"
        f"Step 4: Consider high-value red flag:\n"
        f"  - Amount = ${amount:,} → "
        f"{'High' if amount >= 100000 else 'Low'} transaction amount\n"
        f"  - Traceability = {traceability}\n"
        f"  - Flag if high amount + low traceability: {'Yes' if amount >= 100000 and traceability == 'low' else 'No'}\n"
        f"Step 5: Classification:\n"
        f"  - High Risk if score ≥ 12 or flagged combo\n"
        f"  - Medium Risk if score ≥ 8\n"
        f"  - Low Risk otherwise\n"
        f"Final Risk Level: {risk_level}"
    )

    return question, solution



### ========== ADVANCED QUESTIONS (5+ steps) ==========
def template_kyc_advanced_customer_risk_rating():
    """5:Advanced: Multi-factor rule-based customer risk scoring system with conditional adjustments"""
    investor, company = get_random_entities()

    residency_risk_scores = {
        "Germany": 1,
        "France": 1,
        "USA": 2,
        "China": 3,
        "Russia": 4,
        "Iran": 5
    }

    account_risk_scores = {
        "savings": 1,
        "business": 3,
        "offshore": 4
    }

    volume = random.choice([5000, 12000, 25000, 60000])
    country = random.choice(list(residency_risk_scores.keys()))
    account_type = random.choice(list(account_risk_scores.keys()))

    residency_score = residency_risk_scores[country]
    account_score = account_risk_scores[account_type]
    volume_score = (
        1 if volume <= 10000 else
        2 if volume <= 25000 else
        3 if volume <= 50000 else
        4
    )

    # Apply additional policy logic:
    # - If transaction volume > 25k AND account is offshore → add 1 point
    escalation_flag = volume > 25000 and account_type == "offshore"
    escalation_bonus = 1 if escalation_flag else 0

    total_score = residency_score + account_score + volume_score + escalation_bonus

    # Risk band thresholds
    if total_score >= 9:
        final_rating = "High Risk"
    elif total_score >= 6:
        final_rating = "Medium Risk"
    else:
        final_rating = "Low Risk"

    question = (
        f"{investor} is onboarding at {company}.\n"
        f"Profile details:\n"
        f"- Country of Residency: {country}\n"
        f"- Account Type: {account_type}\n"
        f"- Expected Monthly Transaction Volume: ${volume:,}\n\n"
        f"Using a rule-based scoring model, what is the customer's KYC risk rating?"
    )

    solution = (
        f"Step 1: Residency score = {country} → {residency_score}\n"
        f"Step 2: Account type score = {account_type} → {account_score}\n"
        f"Step 3: Volume score = ${volume:,} → {volume_score}\n"
        f"Step 4: Check for conditional escalation:\n"
        f"  - Offshore account + volume > 25k → {'Yes' if escalation_flag else 'No'} → +{escalation_bonus}\n"
        f"Step 5: Total risk score = {residency_score} + {account_score} + {volume_score} + {escalation_bonus} = {total_score}\n"
        f"Step 6: Apply banding:\n"
        f"  - 0–5 = Low Risk\n"
        f"  - 6–8 = Medium Risk\n"
        f"  - 9+ = High Risk\n"
        f"Final Rating: {final_rating}"
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
        template_kyc_basic_customer_type,
        template_kyc_basic_id_required,
        template_kyc_intermediate_risk_level_by_country,
        template_kyc_intermediate_source_of_funds_analysis,
        template_kyc_advanced_customer_risk_rating
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
    output_file = "../../testset/finance_regulation/kyc.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")

    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")


if __name__ == "__main__":
   main()