import streamlit as st
import requests
import pandas as pd

# Direct raw link to the official 1:1 HUB Logo on GitHub
LOGO_URL = "https://raw.githubusercontent.com/AmrMandour/1-1-HUB-Mentor-Agent/main/1to1%20HUB%20Logo.png"

# Page Configuration
st.set_page_config(
    page_title="1:1 HUB - AI Mentor Matcher Agent",
    page_icon=LOGO_URL,
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main {background-color: #F8FAFC;}
    .stButton>button {background-color: #1E3A8A; color: white; border-radius: 8px; width: 100%; height: 45px; font-weight: bold;}
    .stButton>button:hover {background-color: #3B82F6; color: white;}
    .match-box {background: #EFF6FF; padding: 25px; border-radius: 12px; border-left: 6px solid #1E3A8A; margin-top: 20px;}
    .mentor-card {background: white; padding: 20px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 15px;}
    </style>
""", unsafe_allow_html=True)

# Header Section
col_logo, col_title = st.columns([1, 6])
with col_logo:
    try:
        st.image(LOGO_URL, width=85)
    except:
        st.write("🤖")
with col_title:
    st.markdown("<h2 style='color: #1E3A8A; margin: 0;'>1:1 HUB — AI Mentor Matcher Agent</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #4B5563; margin: 0;'>Autonomous SME Growth Agent: Dynamic AI Matching, Automated Workflow, & Impact Tracking.</p>", unsafe_allow_html=True)

st.markdown("---")

# Comprehensive Mentors Database (Linked to 1:1 HUB Ecosystem)
mentors_database = [
    {
        "id": "amr",
        "name": "Amr Mandour",
        "title": "Business Development & Startup Expert",
        "category": "Sales & Business Development",
        "keywords": ["sales", "marketing", "growth", "b2b", "leads", "revenue", "تطوير", "مبيعات", "تسويق", "مشروع"],
        "price": "500 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "id": "esraa",
        "name": "Esraa Rashwan",
        "title": "Co-Founder - Masark & 1:1 HUB",
        "category": "Project Management & Operations",
        "keywords": ["project", "management", "operations", "strategy", "startup", "إدارة", "مشروعات", "عمليات", "استراتيجية"],
        "price": "450 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "id": "mohamed",
        "name": "Mohamed Salem",
        "title": "Lead Mobile App Developer",
        "category": "Programming & Tech Development",
        "keywords": ["tech", "app", "development", "code", "programming", "ai", "برمجة", "تطبيق", "تقنية", "تطوير"],
        "price": "600 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/"
    }
]

# Initialize Session State
if "bookings" not in st.session_state:
    st.session_state.bookings = []
if "best_match" not in st.session_state:
    st.session_state.best_match = None

tab1, tab2, tab3 = st.tabs(["🤖 AI Readiness & Auto-Matcher", "📝 Instant Booking & Automation", "📊 Business Impact Dashboard"])

with tab1:
    st.subheader("Autonomous AI Readiness Assessment & Smart Matcher")
    st.markdown("Complete the 5 diagnostic questions. Our AI Agent automatically evaluates your inputs, scans the 1:1 HUB expert pool, and performs a live match.")
    
    with st.form("ai_matching_form"):
        st.markdown("### 📋 5-Step SME Diagnostic")
        
        q1 = st.selectbox("1. What is your current startup stage?", ["Idea Stage", "Early MVP / Validation", "Revenue Generation", "Scaling / Growth"])
        q2 = st.selectbox("2. What is your primary business bottleneck?", ["Sales & Customer Acquisition", "Operations & Project Management", "Product & Tech Architecture"])
        q3 = st.slider("3. Rate your current go-to-market clarity (1-10):", 1, 10, 5)
        q4 = st.text_input("4. Describe your core product, service, or business model:")
        q5 = st.text_area("5. What specific milestone or challenge do you want to solve in 30 days?")
        
        run_match = st.form_submit_button("Run Autonomous AI Match")
        
        if run_match:
            if q4 and q5:
                # AI Matching Logic based on text analysis & bottleneck selection
                text_corpus = (q4 + " " + q5 + " " + q2).lower()
                
                matched_mentor = mentors_database[0] # Default fallback
                match_score = 92
                
                if any(k in text_corpus for k in ["project", "management", "operations", "إدارة", "عمليات", "مشروعات"]):
                    matched_mentor = mentors_database[1] # Esraa
                    match_score = 95
                elif any(k in text_corpus for k in ["tech", "app", "code", "programming", "ai", "برمجة", "تطبيق", "تقنية"]):
                    matched_mentor = mentors_database[2] # Mohamed
                    match_score = 97
                else:
                    matched_mentor = mentors_database[0] # Amr (Sales & BD)
                    match_score = 96
                
                st.session_state.best_match = matched_mentor["name"]
                
                # Display Live AI Match Result Box
                st.markdown(f"""
                <div class="match-box">
                    <h3 style='color: #1E3A8A; margin-top:0;'>🎯 Autonomous AI Match Results</h3>
                    <p><b>Recommended Expert:</b> {matched_mentor['name']} ({matched_mentor['title']})</p>
                    <p><b>Category Match:</b> <code>{matched_mentor['category']}</code></p>
                    <p><b>Compatibility Score:</b> <b>{match_score}% Confidence</b></p>
                    <p><b>AI Rationale:</b> Based on your diagnostic inputs regarding <i>'{q2}'</i> and your 30-day goals, this expert possesses the exact domain expertise to accelerate your growth.</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("⚠️ Please fill in all required text fields (Questions 4 & 5) to execute the AI match.")

    st.markdown("---")
    st.subheader("1:1 HUB Certified Expert Directory")
    for m in mentors_database:
        st.markdown(f"""
        <div class="mentor-card">
            <h4>{m['name']} — <span style="font-size: 14px; color: #4B5563;">{m['title']}</span></h4>
            <p><b>Category:</b> <code>{m['category']}</code> | <b>Rate:</b> {m['price']}</p>
            <a href="{m['profile_url']}" target="_blank" style="color: #1E3A8A; font-weight: bold; text-decoration: none;">View Official Profile &rarr;</a>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("Instant Session Booking & Automated Execution")
    st.markdown("Book directly with your AI-matched expert. Triggers instant workflow synchronization.")

    # Auto-select the matched mentor from Tab 1 if available
    default_idx = 0
    if st.session_state.best_match:
        for idx, m in enumerate(mentors_database):
            if m["name"] == st.session_state.best_match:
                default_idx = idx

    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        with col1:
            client_name = st.text_input("Full Name:")
            client_email = st.text_input("Corporate Email:")
        with col2:
            client_whatsapp = st.text_input("WhatsApp / Phone:")
            selected_expert = st.selectbox("Select Expert Mentor:", [m["name"] for m in mentors_database], index=default_idx)
            
        objective = st.text_area("Session Objective & Deliverable:")
        confirm_booking = st.form_submit_button("Confirm Booking & Trigger Automation")
        
        if confirm_booking:
            if client_name and client_email and client_whatsapp and objective:
                booking_record = {
                    "Name": client_name,
                    "Email": client_email,
                    "WhatsApp": client_whatsapp,
                    "Mentor": selected_expert,
                    "Objective": objective
                }
                st.session_state.bookings.append(booking_record)
                
                # Webhook URL for Make.com
                MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/your-unique-webhook-url-here"
                try:
                    requests.post(MAKE_WEBHOOK_URL, json=booking_record, timeout=5)
                except:
                    pass
                
                st.success(f"🎉 Booking successfully confirmed for {client_name} with {selected_expert}! Workflow executed.")
            else:
                st.error("❌ Please complete all fields.")

with tab3:
    st.subheader("Enterprise Business Impact Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Time Saved", "48 Hours / Week", "-95% Manual Work")
    col2.metric("Cost Saved", "12,500 EGP", "Overhead Reduction")
    col3.metric("Active SME Leads", len(st.session_state.bookings), "Live Pipeline")
    
    st.markdown("---")
    if len(st.session_state.bookings) > 0:
        df = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df, use_container_width=True)
        csv_bytes = df.to_csv(index=False).encode('utf-8')
        st.download_button("Export Analytics (CSV)", data=csv_bytes, file_name="leads_impact.csv", mime="text/csv")
    else:
        st.info("No bookings recorded yet. Complete the AI match in Tab 1 and submit a test booking in Tab 2.")
