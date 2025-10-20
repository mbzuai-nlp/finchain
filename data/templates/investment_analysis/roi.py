# https://en.wikipedia.org/wiki/Return_on_investment

import random

# Named entities for investors and projects
investor_names = ["John Doe", "Susan Lee", "Emily White", "Mark Smith", "David Brown"]
project_names = [
    "Tesla Gigafactory", "Apple iPhone Launch", "Amazon Web Services Expansion", "SpaceX Starship Development",
    "Google Data Center Build", "Microsoft Azure", "Netflix Content Production", "Uber Autonomous Driving Initiative",
    "Facebook Metaverse", "Samsung Semiconductor Factory"
]

property_names = [
    "Palm Oasis", "Skyline Heights", "Sunset Residences", "Crystal Waters",
    "Harbor View Towers", "Golden Dunes", "Azure Bay Villas", "Metro Luxe",
    "Emerald Creek", "Royal Crescent"
]

startup_names = ["FinSage", "ByteNest", "Zenlytix", "TradeNova", "EchoMint",
                 "NeuroVest", "DataForge", "VaultIQ", "OptimaX", "LumaChain"]

campaign_names = [
    "FutureFinance", "SmartInvestAI", "WealthWave", "FinVisionX", "MoneyMindset",
    "ProfitPilot", "FinSage", "AssetArc", "AIAlphaEdge", "CapitalCatalyst"
]

funds = ["Vanguard 500 Index", "Fidelity Contrafund", "T. Rowe Price Blue Chip", "Schwab Total Stock Market", 
                "BlackRock Equity Dividend", "American Funds Growth Fund", "Dodge & Cox Stock", "JPMorgan Equity Income", 
                "Franklin Income Fund", "Invesco Growth Opportunities"]



# ───────────────────────────────────────────────────────────── #
# 1. Property Flip: purchase + renovation, then sale
def template_property_roi():
    """1: Basic: Property Flip: purchase + renovation, then sale"""
    investor = random.choice(investor_names)
    property_name = random.choice(property_names)

    purchase_cost   = random.randint(120_000, 300_000)   # $
    renovation_cost = random.randint(20_000,  80_000)    # $
    sale_price      = random.randint(250_000, 500_000)   # $

    question = (
        f"{investor} bought {property_name} for ${purchase_cost:,}, spent "
        f"${renovation_cost:,} on renovations, and later sold it for "
        f"${sale_price:,}. What is the ROI on this property flip?"
    )

    total_investment = purchase_cost + renovation_cost           # $
    roi_raw = ((sale_price - total_investment) / total_investment) * 100
    roi_pct = round(roi_raw, 2)

    solution = (
        "Step 1 – Compute total investment:\n"
        f"  Total Investment = Purchase Cost + Renovation Cost\n"
        f"                   = ${purchase_cost:,} + ${renovation_cost:,} "
        f"= ${total_investment:,}\n\n"
        "Step 2 – Compute ROI:\n"
        f"  ROI = (Sale Price − Total Investment) ÷ Total Investment × 100\n"
        f"      = (${sale_price:,} − ${total_investment:,}) "
        f"÷ ${total_investment:,} × 100 = {roi_pct:.2f}%"
    )
    return question, solution

# ───────────────────────────────────────────────────────────── #
# 2. Project with Taxes on Profit
def template_after_tax_roi():
    """2: Basic: Project with Taxes on Profit"""
    entrepreneur = random.choice(investor_names)
    startup      = random.choice(startup_names)

    investment = random.randint(50_000, 120_000)    # $
    gross_profit = random.randint(70_000, 200_000)  # $
    tax_rate = random.randint(15, 30)               # %

    question = (
        f"{entrepreneur} invested ${investment:,} in {startup}. "
        f"The project earned a gross profit of ${gross_profit:,}, "
        f"and profits are taxed at {tax_rate}%. "
        f"What is the after‑tax ROI?"
    )

    net_profit = gross_profit * (1 - tax_rate/100)  # $
    roi_pct    = round((net_profit / investment) * 100, 2)

    solution = (
        "Step 1 – Compute net profit after tax:\n"
        f"  Net Profit = Gross Profit × (1 − Tax Rate)\n"
        f"             = ${gross_profit:,} × (1 − {tax_rate}% ) "
        f"= ${net_profit:,.2f}\n\n"
        "Step 2 – Compute ROI:\n"
        f"  ROI = (Net Profit ÷ Investment) × 100\n"
        f"      = (${net_profit:,.2f} ÷ ${investment:,}) × 100 "
        f"= {roi_pct:.2f}%"
    )
    return question, solution
# ───────────────────────────────────────────────────────────── #

# ──────────────────────────────────────────────────────────
# 3. Compound‑Growth Investment
def template_compound_roi():
    """3: Intermediate: Compound‑Growth Investment"""
    investor = random.choice(investor_names)

    principal = random.randint(5_000, 30_000)           # $
    rate      = random.randint(4, 10)                   # % p.a.
    years     = random.randint(2, 6)                    # yrs

    question = (
        f"{investor} deposited ${principal:,} at {rate}% annual compound "
        f"interest for {years} years. What is the ROI on this investment?"
    )

    fv          = round(principal * (1 + rate/100) ** years, 2)          # $
    net_profit  = round(fv - principal, 2)                               # $
    roi_pct     = round((net_profit / principal) * 100, 2)

    solution = (
        "Step 1 – Compute the future value with compounding:\n"
        f"  FV = Principal × (1 + r)^n = "
        f"${principal:,} × (1 + {rate}% )^{years} = ${fv:,.2f}\n\n"
        "Step 2 – Compute the net profit:\n"
        f"  Net Profit = FV − Principal = ${fv:,.2f} − ${principal:,} "
        f"= ${net_profit:,.2f}\n\n"
        "Step 3 – Compute ROI:\n"
        f"  ROI = (Net Profit ÷ Principal) × 100 "
        f"= (${net_profit:,.2f} ÷ ${principal:,}) × 100 = {roi_pct:.2f}%"
    )
    return question, solution

# ──────────────────────────────────────────────────────────
# 4. Online Marketing Campaign (impressions → conversions)
def template_conversion_campaign_roi():
    """4: Intermediate: Online Marketing Campaign (impressions → conversions)"""
    marketer = random.choice(investor_names)
    campaign = random.choice(campaign_names)

    impressions = random.randint(40_000, 200_000)
    ctr         = random.uniform(0.8, 2.5) / 100          # click‑through rate
    conv_rate   = random.uniform(1.5, 5.0) / 100          # conversion rate
    avg_sale    = random.randint(60, 150)                 # $ per sale
    ad_spend    = random.randint(8_000, 25_000)           # $

    question = (
        f"{marketer}'s {campaign} ad received {impressions:,} impressions. "
        f"The click‑through rate was {ctr*100:.2f}% and the conversion "
        f"rate was {conv_rate*100:.2f}%. Each sale averaged ${avg_sale}. "
        f"The campaign cost ${ad_spend:,}. What is the ROI?"
    )

    clicks      = impressions * ctr
    sales       = clicks * conv_rate
    revenue     = round(sales * avg_sale, 2)                                    # $
    net_profit  = round(revenue - ad_spend, 2)                                  # $
    roi_pct     = round((net_profit / ad_spend) * 100, 2)

    solution = (
        "Step 1 – Compute total revenue:\n"
        f"  Clicks = Impressions × CTR = {impressions:,} × {ctr*100:.2f}% "
        f"= {int(clicks):,}\n"
        f"  Sales  = Clicks × Conversion Rate = {int(clicks):,} × "
        f"{conv_rate*100:.2f}% = {int(sales):,}\n"
        f"  Revenue = Sales × Avg Sale = {int(sales):,} × "
        f"${avg_sale} = ${revenue:,.2f}\n\n"
        "Step 2 – Compute net profit:\n"
        f"  Net Profit = Revenue − Ad Spend = "
        f"${revenue:,.2f} − ${ad_spend:,} = ${net_profit:,.2f}\n\n"
        "Step 3 – Compute ROI:\n"
        f"  ROI = (Net Profit ÷ Ad Spend) × 100\n"
        f"      = (${net_profit:,.2f} ÷ ${ad_spend:,}) × 100 "
        f"= {roi_pct:.2f}%"
    )
    return question, solution

# 5. Mutual Fund (dividends − management fees + price gain)
def template_mutual_fund_roi():
    """5: Advanced: Mutual Fund (dividends − management fees + price gain)"""
    investor = random.choice(investor_names)
    fund     = random.choice(funds)

    shares       = random.randint(500, 2_000)
    buy_price    = random.randint(30, 70)            # $ per share
    sell_price   = random.randint(buy_price + 5, buy_price + 30)
    dividend_ps  = round(random.uniform(0.5, 2.0), 2)  # $ per share
    years        = random.randint(2, 5)
    fee_rate     = random.uniform(0.8, 2.0)          # % p.a.

    invest_cost  = shares * buy_price
    dividends    = shares * dividend_ps * years
    mgmt_fees    = invest_cost * fee_rate/100 * years
    price_gain   = shares * (sell_price - buy_price)
    net_profit   = price_gain + dividends - mgmt_fees
    roi_pct      = round((net_profit / invest_cost) * 100, 2)

    question = (
        f"{investor} bought {shares} shares of {fund} at ${buy_price} each. "
        f"The fund pays ${dividend_ps} per share annually and charges a "
        f"{fee_rate:.2f}% management fee. After {years} years, the shares "
        f"were sold for ${sell_price} each. What is the ROI?"
    )

    solution = (
        "Step 1 – Compute total dividends:\n"
        f"  Dividends = Shares × Dividend/Share × Years\n"
        f"            = {shares} × ${dividend_ps} × {years} "
        f"= ${dividends:,.2f}\n\n"
        "Step 2 – Compute total management fees:\n"
        f"  Fees = Initial Investment × Fee Rate × Years\n"
        f"       = ${invest_cost:,} × {fee_rate:.2f}% × {years} "
        f"= ${mgmt_fees:,.2f}\n\n"
        "Step 3 – Compute net profit:\n"
        f"  Price Gain = (Sell Price − Buy Price) × Shares "
        f"= (${sell_price} − ${buy_price}) × {shares} "
        f"= ${price_gain:,.2f}\n"
        f"  Net Profit = Price Gain + Dividends − Fees "
        f"= ${price_gain:,.2f} + ${dividends:,.2f} − ${mgmt_fees:,.2f} "
        f"= ${net_profit:,.2f}\n\n"
        "Step 4 – Compute ROI:\n"
        f"  ROI = (Net Profit ÷ Initial Investment) × 100\n"
        f"      = (${net_profit:,.2f} ÷ ${invest_cost:,}) × 100 "
        f"= {roi_pct:.2f}%"
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
        template_property_roi,
        template_after_tax_roi,
        template_compound_roi,
        template_conversion_campaign_roi,
        template_mutual_fund_roi
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
    output_file = "../../testset/investment_analysis/roi.jsonl"
    with open(output_file, "w") as file:
        for problem in all_problems:
            file.write(json.dumps(problem))
            file.write("\n")
    
    print(f"Successfully generated {len(all_problems)} problems and saved to {output_file}")

if __name__ == "__main__":
   main()