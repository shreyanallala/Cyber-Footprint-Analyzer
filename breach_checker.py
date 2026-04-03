import pandas as pd
import random

def check_breach(email):
    # If invalid email → no breach
    if not email or "@" not in email:
        return None, []

    try:
        email = email.strip().lower()

        # Load dataset
        data = pd.read_csv("data/breach_data.csv")

        # Normalize dataset emails
        data["email"] = data["email"].str.strip().str.lower()

        # Find match
        row = data[data["email"] == email]

        # -------------------------------
        # IF FOUND IN DATASET
        # -------------------------------
        if not row.empty:
            count = int(row["breaches"].values[0])

            # Split sources (LinkedIn;Adobe → list)
            sources = row["source"].values[0].split(";")

            return count, sources

        # -------------------------------
        # IF NOT FOUND → SIMULATE
        # -------------------------------
        count = random.randint(0, 3)

        possible_sources = [
            "LinkedIn", "Adobe", "Facebook", "Dropbox",
            "Twitter", "Yahoo", "Canva", "MySpace"
        ]

        sources = random.sample(possible_sources, count) if count > 0 else []

        return count, sources

    except Exception as e:
        print("Error:", e)
        return None, []