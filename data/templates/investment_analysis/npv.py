# https://en.wikipedia.org/wiki/Net_present_value
import random

# Named entities for investors and projects
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
project_names = [
    "Tesla Gigafactory", "Apple iPhone Launch", "Amazon Web Services Expansion", "SpaceX Starship Development",
    "Google Data Center Build", "Microsoft Azure", "Netflix Content Production", "Uber Autonomous Driving Initiative",
    "Facebook Metaverse", "Samsung Semiconductor Factory"
]

# Simple ones with two steps in the solution:

# Template 1: NPV with one cash flow after 1 year
def template_single_year_npv():
    """1: Basic: NPV with one cash flow after 1 year"""
    investor = random.choice(investor_names)
    project  = random.choice(project_names)

    x = random.randint(10_000, 50_000)           # $ initial
    C = random.randint(15_000, 60_000)           # $ after 1 yr
    r = round(random.uniform(5, 15), 2)          # %

    question = (
        f"{investor} invests ${x} in {project} and expects ${C} in one year. "
        f"If the discount rate is {r:.2f}%, what is the NPV?"
    )

    PV  = round(C / (1 + r/100), 2)
    NPV = round(PV - x, 2)

    solution = (
        f"Step 1: Present value of the cash flow:\n"
        f"  PV = ${C} ÷ (1 + {r/100:.4f}) = ${PV:,.2f}\n\n"
        f"Step 2: Net present value:\n"
        f"  NPV = PV − initial investment = ${PV:,.2f} − ${x} = ${NPV:,.2f}"
    )
    return question, solution

# Template 2: NPV with cash flows in years 1 & 2 (common r)
def template_two_year_npv():
    """2: Basic: NPV with cash flows in years 1 & 2 (common r)"""
    investor = random.choice(investor_names)
    project  = random.choice(project_names)

    x  = random.randint(20_000, 70_000)
    C1 = random.randint(12_000, 35_000)          # after 1 yr
    C2 = random.randint(12_000, 35_000)          # after 2 yrs
    r  = round(random.uniform(6, 14), 2)

    question = (
        f"{investor} invests ${x} in {project}. It will generate "
        f"${C1} after one year and ${C2} after two years. "
        f"Using a {r:.2f}% discount rate, calculate the NPV."
    )

    PV_total = round(C1/(1+r/100) + C2/((1+r/100)**2), 2)
    NPV      = round(PV_total - x, 2)

    solution = (
        f"Step 1: Total present value of the two cash flows:\n"
        f"  PV₁ = ${C1}/(1 + {r/100:.4f})\n"
        f"  PV₂ = ${C2}/(1 + {r/100:.4f})²\n"
        f"  PV_total = PV₁ + PV₂ = ${PV_total:,.2f}\n\n"
        f"Step 2: NPV = PV_total − initial investment = "
        f"${PV_total:,.2f} − ${x} = ${NPV:,.2f}"
    )
    return question, solution

# Medium level: three steps in the solution

# Template 3: NPV: two annual inflows + salvage in year 3
def template_three_year_with_salvage_npv():
    """3: Intermediate: NPV: two annual inflows + salvage in year 3"""
    investor = random.choice(investor_names)
    project  = random.choice(project_names)

    x        = random.randint(30_000, 100_000)      # $ initial
    C1       = random.randint(12_000, 30_000)       # $ after yr 1
    C2       = random.randint(12_000, 30_000)       # $ after yr 2
    salvage  = random.randint(40_000, 90_000)       # $ at yr 3
    r        = round(random.uniform(6, 14), 2)      # %

    question = (
        f"{investor} invests ${x} in {project}. It is expected to generate "
        f"${C1} after one year, ${C2} after two years, and a salvage value of "
        f"${salvage} at the end of year three. Using a {r:.2f}% discount rate, "
        f"what is the NPV?"
    )

    PV_op      = round(C1/(1+r/100) + C2/((1+r/100)**2), 2)
    PV_salvage = round(salvage/((1+r/100)**3), 2)
    NPV        = round(PV_op + PV_salvage - x, 2)

    solution = (
        f"Step 1: Present value of operating inflows:\n"
        f"  PV₁ = ${C1}/(1+{r/100:.4f}),  PV₂ = ${C2}/(1+{r/100:.4f})²\n"
        f"  PV_op = PV₁ + PV₂ = ${PV_op:,.2f}\n\n"
        f"Step 2: Present value of the year‑3 salvage:\n"
        f"  PV_salvage = ${salvage}/(1+{r/100:.4f})³ = ${PV_salvage:,.2f}\n\n"
        f"Step 3: Net present value:\n"
        f"  NPV = PV_op + PV_salvage − initial investment\n"
        f"      = ${PV_op:,.2f} + ${PV_salvage:,.2f} − ${x} = ${NPV:,.2f}"
    )
    return question, solution

# Template 4: NPV: 4‑year annuity of savings + salvage
def template_annuity_plus_salvage_npv():
    """4: Intermediate: NPV: 4‑year annuity of savings + salvage"""
    investor = random.choice(investor_names)
    project  = random.choice(project_names)

    x            = random.randint(40_000, 120_000)
    annual_save  = random.randint(10_000, 22_000)
    salvage      = random.randint(20_000, 45_000)   # at end of yr 4
    r            = round(random.uniform(4, 10), 2)
    n            = 4

    question = (
        f"{investor} can invest ${x} in {project}. It will save "
        f"${annual_save} each year for {n} years and then be sold for "
        f"${salvage}. If the discount rate is {r:.2f}%, find the NPV."
    )

    annuity_factor  = (1 - 1/((1+r/100)**n))/(r/100)
    PV_annuity = round(annual_save * annuity_factor, 2)
    PV_salvage = round(salvage / ((1+r/100)**n), 2)
    NPV        = round(PV_annuity + PV_salvage - x, 2)

    solution = (
        f"Step 1: Present value of the annual savings (annuity):\n"
        f"  PV_annuity = ${annual_save} × [(1 − 1/(1+{r/100:.4f})^{n}) / ({r/100:.4f})]\n"
        f"            = ${PV_annuity:,.2f}\n\n"
        f"Step 2: Present value of the year‑{n} salvage:\n"
        f"  PV_salvage = ${salvage}/(1+{r/100:.4f})^{n} = ${PV_salvage:,.2f}\n\n"
        f"Step 3: Net present value:\n"
        f"  NPV = PV_annuity + PV_salvage − initial investment\n"
        f"      = ${PV_annuity:,.2f} + ${PV_salvage:,.2f} − ${x} = ${NPV:,.2f}"
    )
    return question, solution

def template_annuity_salvage_cleanup_npv():
    """5: Advanced: 4‑step: 4‑yr savings annuity, salvage & cleanup cost at yr 4"""
    investor = random.choice(investor_names)
    project  = random.choice(project_names)

    x           = random.randint(60_000, 140_000)
    annual_save = random.randint(12_000, 25_000)
    salvage     = random.randint(30_000, 65_000)
    cleanup     = random.randint(15_000, 35_000)     # env. cleanup
    r           = round(random.uniform(4, 9), 2)
    n           = 4

    pv_factor   = (1 - 1/((1+r/100)**n)) / (r/100)
    PV_annuity  = round(annual_save * pv_factor, 2)
    PV_salvage  = round(salvage / ((1+r/100)**n), 2)
    PV_cleanup  = round(cleanup / ((1+r/100)**n), 2)
    NPV         = round(PV_annuity + PV_salvage - PV_cleanup - x, 2)

    question = (
        f"{investor} can invest ${x} in {project}. The project will save "
        f"${annual_save} per year for {n} years, after which it can be sold for "
        f"${salvage} but will incur an environmental cleanup cost of ${cleanup}. "
        f"Given a discount rate of {r:.2f}%, what is the NPV?"
    )

    solution = (
        f"Step 1 – PV of the annual savings (annuity):\n"
        f"  PV_annuity = ${annual_save} × [(1 − 1/(1+{r/100:.4f})^{n})/({r/100:.4f})] "
        f"= ${PV_annuity:,.2f}\n\n"
        f"Step 2 – PV of the salvage value:\n"
        f"  PV_salvage = ${salvage}/(1+{r/100:.4f})^{n} = ${PV_salvage:,.2f}\n\n"
        f"Step 3 – PV of the cleanup cost:\n"
        f"  PV_cleanup = ${cleanup}/(1+{r/100:.4f})^{n} = ${PV_cleanup:,.2f}\n\n"
        f"Step 4 – Net present value:\n"
        f"  NPV = PV_annuity + PV_salvage − PV_cleanup − initial\n"
        f"      = ${PV_annuity:,.2f} + ${PV_salvage:,.2f} − ${PV_cleanup:,.2f} − ${x} "
        f"= ${NPV:,.2f}"
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
        template_single_year_npv,
        template_two_year_npv,
        template_three_year_with_salvage_npv,
        template_annuity_plus_salvage_npv,
        template_annuity_salvage_cleanup_npv
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
    output_file = "../../testset/investment_analysis/npv.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem, ensure_ascii=False))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()