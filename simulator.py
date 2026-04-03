def simulate_attack(data):
    attacks = []

    name = data.get("possible_name")
    year = data.get("possible_year")

    # Password simulation
    if name and year:
        attacks.append(f"Password guess: {name}@{year}")
        attacks.append(f"Password guess: {name}{year}")
    elif name:
        attacks.append("Weak password pattern (name-based)")

    # Platform phishing
    platform = data.get("platform")

    if platform == "Instagram":
        attacks.append("Fake message: 'Your account will be deleted. Verify now.'")
    elif platform == "LinkedIn":
        attacks.append("Fake recruiter message with malicious link")
    elif platform == "Facebook":
        attacks.append("Fake friend request + phishing link")
    else:
        attacks.append("Generic phishing: 'Security alert - verify account'")

    return attacks