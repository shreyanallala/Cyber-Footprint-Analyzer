def analyze_risk(data, breach_count):
    risks = []
    score = 0

    name = data.get("possible_name")
    year = data.get("possible_year")
    platform = data.get("platform")

    # -------------------------------
    # USERNAME RISKS
    # -------------------------------
    if name and year:
        risks.append("Username contains name + year (very easy to guess)")
        score += 30
    elif name:
        risks.append("Username contains real name (predictable)")
        score += 10

    # -------------------------------
    # PLATFORM-BASED RISKS
    # -------------------------------

    # High personal exposure platforms
    if platform in ["Instagram", "TikTok", "Snapchat"]:
        risks.append("High personal exposure platform (photos, lifestyle)")
        score += 10

    # Relationship/social platforms
    elif platform in ["Facebook", "WhatsApp", "Telegram"]:
        risks.append("Social connections exposed (impersonation risk)")
        score += 12

    # Professional platforms
    elif platform in ["LinkedIn", "GitHub", "Medium"]:
        risks.append("Professional data exposed (targeted phishing risk)")
        score += 15

    # Public discussion platforms
    elif platform in ["Reddit", "Quora", "Threads"]:
        risks.append("Public opinions exposed (profiling risk)")
        score += 8

    # Media/content platforms
    elif platform in ["YouTube", "Pinterest"]:
        risks.append("Content-based profiling possible")
        score += 6

    # Dating platforms
    elif platform in ["Tinder", "Bumble"]:
        risks.append("Sensitive personal interactions (high social engineering risk)")
        score += 18

    # Messaging / community
    elif platform == "Discord":
        risks.append("Community exposure (phishing via servers)")
        score += 10

    # Twitter/X
    elif platform == "Twitter / X":
        risks.append("Public posts enable behavioral profiling")
        score += 10

    # -------------------------------
    # EMAIL DOMAIN RISK (ONLY if valid email)
    # -------------------------------
    domain = data.get("domain")

    if domain in ["gmail.com", "yahoo.com", "outlook.com"]:
        risks.append("Common email provider (frequent phishing target)")
        score += 8

    # -------------------------------
    # BREACH RISK
    # -------------------------------
    if breach_count and breach_count > 0:
        risks.append(f"Email found in {breach_count} data breaches")
        score += 20 + breach_count * 5

    # -------------------------------
    # FINAL SCORE
    # -------------------------------
    return {
        "risks": risks,
        "score": min(score, 100)
    }