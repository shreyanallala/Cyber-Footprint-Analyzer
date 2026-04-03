import streamlit as st
from collector import collect_user_data
from analyzer import analyze_risk
from simulator import simulate_attack
from breach_checker import check_breach
import time
import base64

# -------------------------------
# BACKGROUND
# -------------------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: 80%;
        background-position: center;
        background-repeat: no-repeat;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
        z-index: 0;
    }}

    .block-container {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """, unsafe_allow_html=True)

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="Cyber Footprint Analyzer", layout="wide")
set_bg("asset/background.png")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1 style='text-align:center; color:#00FFAA;'>
🔐 CYBER FOOTPRINT ANALYZER
</h1>
""", unsafe_allow_html=True)

st.markdown("### 🛡️ Manage your digital footprint")
st.divider()

# -------------------------------
# INPUT
# -------------------------------
st.subheader("👤 Enter User Details")

email = st.text_input("📧 Email")
username = st.text_input("👤 Username")

platform = st.selectbox(
    "🌐 Platform",
    [
        "General",
        "Instagram",
        "Facebook",
        "LinkedIn",
        "Twitter / X",
        "Snapchat",
        "TikTok",
        "YouTube",
        "WhatsApp",
        "Telegram",
        "Reddit",
        "Pinterest",
        "Discord",
        "GitHub",
        "Medium",
        "Quora",
        "Threads",
        "Tinder",
        "Bumble"
    ]
)

# -------------------------------
# VALIDATION
# -------------------------------
def is_valid_email(email):
    return "@" in email and "." in email

# -------------------------------
# BUTTON
# -------------------------------
if st.button("🚀 Analyze Now"):

    if not email and not username:
        st.warning("Enter email or username")
        st.stop()

    if email and not is_valid_email(email):
        st.error("Invalid email format")
        st.stop()

    # Loading animation
    with st.spinner("Analyzing..."):
        time.sleep(1)

    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    # -------------------------------
    # PROCESSING
    # -------------------------------
    data = collect_user_data(email, username, platform)

    # FIXED: proper handling
    if email:
        breach_count, breach_sources = check_breach(email)
    else:
        breach_count, breach_sources = None, []

    result = analyze_risk(data, breach_count if breach_count else 0)
    attacks = simulate_attack(data)

    st.divider()

    # -------------------------------
    # TABS
    # -------------------------------
    tab1, tab2, tab3 = st.tabs(["📊 Risk", "⚠️ Issues", "💀 Attacks"])

    # -------------------------------
    # TAB 1: RISK + BREACH DETAILS
    # -------------------------------
    with tab1:
        score = result["score"]

        if score < 30:
            st.success(f"🟢 Low Risk: {score}")
        elif score < 70:
            st.warning(f"🟡 Medium Risk: {score}")
        else:
            st.error(f"🔴 High Risk: {score}")

        # Breach details
        if breach_count is not None:
            if breach_count > 0:
                st.error(f"⚠️ Found in {breach_count} breaches")

                st.subheader("📂 Breach Sources")
                for src in breach_sources:
                    st.write(f"• {src}")

            else:
                st.success("No breaches found")

    # -------------------------------
    # TAB 2: RISKS
    # -------------------------------
    with tab2:
        if result["risks"]:
            for r in result["risks"]:
                st.write("•", r)
        else:
            st.success("No major risks")

    # -------------------------------
    # TAB 3: ATTACKS
    # -------------------------------
    with tab3:
        for a in attacks:
            st.write("•", a)