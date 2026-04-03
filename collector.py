import re

def collect_user_data(email, username, platform):
    data = {}

    data["email"] = email.strip().lower() if email else ""
    data["username"] = username.strip().lower() if username else ""
    data["platform"] = platform

    # Email breakdown
    if "@" in data["email"]:
        user, domain = data["email"].split("@")
        data["email_user"] = user
        data["domain"] = domain
    else:
        data["email_user"] = ""
        data["domain"] = ""

    # Extract patterns from username
    name_match = re.findall(r'[a-zA-Z]+', data["username"])
    year_match = re.findall(r'\d{2,4}', data["username"])

    data["possible_name"] = name_match[0] if name_match else None
    data["possible_year"] = year_match[0] if year_match else None

    return data