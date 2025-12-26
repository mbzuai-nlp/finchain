# ------------------------------------------------------------
# Risk and Return Templates
# ------------------------------------------------------------

import random

# Named entities for investors and projects
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
project_names = [
    "Tesla Gigafactory", "Apple iPhone Launch", "Amazon Web Services Expansion", "SpaceX Starship Development",
    "Google Data Center Build", "Microsoft Azure", "Netflix Content Production", "Uber Autonomous Driving Initiative",
    "Facebook Metaverse", "Samsung Semiconductor Factory"
]

asset_names = ["AlphaCorp", "BlueRiver", "CedarFund", "DeltaTrust", "EagleHoldings",
          "FalconInvest", "GoldenBridge", "HarborEquity", "IronPeak", "JadeCapital"]

portfolio_names = ["AlphaGrowth", "SteadyYield", "QuantumEdge", "BlueHorizon", "NovaCapital", 
                   "IroncladFund", "ZenithCore", "PhoenixRise", "AurumWave", "SummitAlpha"]



# ------------------------------------------------------------
#  Two‑Asset Portfolio Standard Deviation
# ------------------------------------------------------------
def template_portfolio_sd():
    """1: Basic: Risk: compute σ_p for a 2‑asset portfolio (2 steps)."""
    investor = random.choice(investor_names)
    asset_a, asset_b = random.sample(asset_names, 2)

    w_a = round(random.uniform(0.2, 0.8), 2)
    w_b = round(1 - w_a, 2)
    sd_a = round(random.uniform(5, 20), 2)        # %
    sd_b = round(random.uniform(5, 20), 2)        # %
    rho  = round(random.uniform(-0.2, 0.8), 2)     # correlation

    question = (
        f"{investor} holds a portfolio consisting of {w_a:.2f} "
        f"allocated to {asset_a} and {w_b:.2f} allocated to {asset_b}.\n"
        f"The annual return standard deviations are {sd_a:.2f}% and "
        f"{sd_b:.2f}%, with a correlation of {rho:.2f} between them.\n"
        f"What is the portfolio’s standard deviation?"
    )

    # Step 1: covariance
    cov = rho * sd_a * sd_b
    # Step 2: portfolio variance → σ_p
    var_p = (w_a**2)*(sd_a**2) + (w_b**2)*(sd_b**2) + 2*w_a*w_b*cov
    sd_p  = round(var_p**0.5, 2)

    solution = (
        "Step 1: Covariance = ρ × σ_A × σ_B "
        f"= {rho:.2f} × {sd_a:.2f}% × {sd_b:.2f}% = {cov:.2f}\n\n"
        "Step 2: σ_p = √[w_A²σ_A² + w_B²σ_B² + 2w_Aw_B Cov] "
        f"= √({w_a:.2f}²×{sd_a:.2f}² + {w_b:.2f}²×{sd_b:.2f}² "
        f"+ 2×{w_a:.2f}×{w_b:.2f}×{cov:.2f}) = {sd_p:.2f}%"
    )
    return question, solution


# ------------------------------------------------------------
# Sharpe Ratio
# ------------------------------------------------------------
def template_sharpe_ratio():
    """2: Basic: Return & Risk: compute Sharpe ratio (2 steps)."""
    investor = random.choice(investor_names)
    proj     = random.choice(project_names)

    exp_ret = round(random.uniform(6, 15), 2)   # %
    rf_rate = round(random.uniform(1, 5), 2)    # %
    stdev   = round(random.uniform(4, 12), 2)   # %

    question = (
        f"{investor} estimates an expected return of {exp_ret:.2f}% and a "
        f"standard deviation of {stdev:.2f}% for {proj}. "
        f"The risk‑free rate is {rf_rate:.2f}%.\n"
        f"What is the Sharpe ratio of {proj}?"
    )

    # Step 1: excess return
    excess = exp_ret - rf_rate
    # Step 2: Sharpe ratio
    sharpe = round(excess / stdev, 2)

    solution = (
        f"Step 1: Excess return = {exp_ret:.2f}% − {rf_rate:.2f}% = {excess:.2f}%\n\n"
        f"Step 2: Sharpe ratio = Excess / σ = {excess:.2f}% / {stdev:.2f}% = {sharpe:.2f}"
    )
    return question, solution

# ------------------------------------------------------------
# Jensen’s Alpha for a Portfolio
# ------------------------------------------------------------
def template_jensen_alpha():
    """3: Intermediate: α = R_p − [r_f + β_p × (R_m − r_f)]."""
    investor = random.choice(investor_names)
    port     = random.choice(portfolio_names)

    r_p = round(random.uniform(8, 18), 2)     # actual portfolio return %
    r_f = round(random.uniform(1, 4), 2)      # risk‑free %
    r_m = round(random.uniform(6, 14), 2)     # market return %
    beta_p = round(random.uniform(0.7, 1.4), 2)

    question = (
        f"{investor}'s portfolio {port} earned {r_p:.2f}% last year. "
        f"The risk‑free rate was {r_f:.2f}% and the market returned {r_m:.2f}%. "
        f"The portfolio’s beta is {beta_p:.2f}.\n"
        f"What is Jensen’s alpha for {port}?"
    )

    # --- 3 reasoning steps ---
    mkt_prem = r_m - r_f                          # Step 1  (market risk premium)
    capm_req = r_f + beta_p * mkt_prem            # Step 2  (CAPM required return)
    alpha    = round(r_p - capm_req, 2)           # Step 3  (α)

    solution = (
        f"Step 1: Market risk premium = {r_m:.2f}% − {r_f:.2f}% = {mkt_prem:.2f}%\n\n"
        f"Step 2: Required return (CAPM) = r_f + β_p×MRP "
        f"= {r_f:.2f}% + {beta_p:.2f}×{mkt_prem:.2f}% = {capm_req:.2f}%\n\n"
        f"Step 3: Jensen’s α = Actual − Required = {r_p:.2f}% − {capm_req:.2f}% = {alpha:.2f}%"
    )
    return question, solution

# ------------------------------------------------------------
# M‑squared (Modigliani–Modigliani) Measure
# ------------------------------------------------------------
def template_m2_measure():
    """4: Intermediate: M² = r_f + Sharpe×σ_bench."""
    investor = random.choice(investor_names)
    port     = random.choice(portfolio_names)

    r_p   = round(random.uniform(7, 16), 2)     # portfolio exp return %
    σ_p   = round(random.uniform(4, 10), 2)     # portfolio σ %
    σ_b   = round(random.uniform(5, 12), 2)     # benchmark σ %
    r_f   = round(random.uniform(1, 4), 2)      # risk‑free %

    question = (
        f"{investor} evaluates portfolio {port}: expected return {r_p:.2f}%, "
        f"standard deviation {σ_p:.2f}%. The benchmark’s σ is {σ_b:.2f}%; "
        f"the risk‑free rate is {r_f:.2f}%.\n"
        f"What is the M‑squared (M²) measure for {port}?"
    )

    sharpe = (r_p - r_f) / σ_p                  # Step 1 Sharpe ratio
    adj_er = sharpe * σ_b                       # Step 2 risk‑matched excess %
    m2     = round(r_f + adj_er, 2)             # Step 3 add r_f

    solution = (
        f"Step 1: Sharpe = (R_p − r_f)/σ_p = ({r_p:.2f}% − {r_f:.2f}%)/{σ_p:.2f}% = {sharpe:.4f}\n\n"
        f"Step 2: Risk‑matched excess = Sharpe × σ_b = {sharpe:.4f} × {σ_b:.2f}% = {adj_er:.2f}%\n\n"
        f"Step 3: M² = r_f + excess = {r_f:.2f}% + {adj_er:.2f}% = {m2:.2f}%"
    )
    return question, solution

# ------------------------------------------------------------
# CAPM Required Return for a 3‑Asset Dollar‑Weighted Portfolio
#    (weights → β_p → market premium → required return)
# ------------------------------------------------------------
def template_capm_portfolio():
    """5: Advanced: capm portfolio"""
    investor = random.choice(investor_names)
    a1, a2, a3 = random.sample(asset_names, 3)

    # Dollar allocations
    inv1 = random.randint(15_000, 50_000)
    inv2 = random.randint(15_000, 50_000)
    inv3 = random.randint(15_000, 50_000)
    tot  = inv1 + inv2 + inv3

    # Betas
    β1 = round(random.uniform(0.6, 1.5), 2)
    β2 = round(random.uniform(0.6, 1.5), 2)
    β3 = round(random.uniform(0.6, 1.5), 2)

    r_f = round(random.uniform(1, 4), 2)      # %
    r_m = round(random.uniform(6, 12), 2)     # %

    w1 = round(inv1 / tot, 2)
    w2 = round(inv2 / tot, 2)
    w3 = round(1 - w1 - w2, 2)

    question = (
        f"{investor} holds ${inv1:,} of {a1} (β={β1:.2f}), "
        f"${inv2:,} of {a2} (β={β2:.2f}), and ${inv3:,} of {a3} (β={β3:.2f}). "
        f"The risk‑free rate is {r_f:.2f}% and the expected market return is {r_m:.2f}%.\n"
        f"Using CAPM, what is the required return for the portfolio?"
    )

    # ----- 4‑step solution -----
    β_p   = round(w1*β1 + w2*β2 + w3*β3, 2)                # Step 1 weights → β_p
    prem  = r_m - r_f                                      # Step 2 market premium
    add_r = round(β_p * prem, 2)                           # Step 3 portfolio risk premium
    req_r = round(r_f + add_r, 2)                          # Step 4 required return

    solution = (
        f"Step 1: Portfolio β = {w1:.2f}×{β1:.2f} + {w2:.2f}×{β2:.2f} + "
        f"{w3:.2f}×{β3:.2f} = {β_p:.2f}\n\n"
        f"Step 2: Market risk premium = {r_m:.2f}% − {r_f:.2f}% = {prem:.2f}%\n\n"
        f"Step 3: Portfolio risk premium = β_p × MRP = {β_p:.2f}×{prem:.2f}% = {add_r:.2f}%\n\n"
        f"Step 4: Required return = r_f + premium = {r_f:.2f}% + {add_r:.2f}% = {req_r:.2f}%"
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
        template_portfolio_sd,
        template_sharpe_ratio,
        template_jensen_alpha,
        template_m2_measure,
        template_capm_portfolio
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
    output_file = "../../testset/investment_analysis/rar.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()