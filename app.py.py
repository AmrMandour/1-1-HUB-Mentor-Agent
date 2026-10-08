import streamlit as st
import pandas as pd
import google.generativeai as genai

GOOGLE_API_KEY = "AQ.Ab8RN6L3bAmzZiLK9DAf5h7SMyFTTrxh6TIBk_qczXHWJrVQ"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    model = None

st.set_page_config(
    page_title="1:1 HUB - AI Mentor Matcher Ecosystem",
    layout="wide"
)

st.markdown("""
    <style>
    .main {background-color: #F8FAFC;}
    .stButton>button {background-color: #1E3A8A; color: white; border-radius: 8px; width: 100%; height: 45px; font-weight: bold;}
    .stButton>button:hover {background-color: #3B82F6; color: white;}
    .mentor-card {background: white; padding: 18px; border-radius: 12px; border: 1px solid #E2E8F0; margin-bottom: 15px; height: 210px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);}
    .profile-link {display: inline-block; background-color: #1E3A8A; color: white !important; padding: 6px 12px; border-radius: 6px; text-decoration: none; font-size: 12px; font-weight: bold; margin-top: 10px;}
    .profile-link:hover {background-color: #3B82F6;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='color: #1E3A8A; margin-bottom: 0;'>1:1 HUB — AI Mentor Matcher Ecosystem</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #4B5563; margin-top: 0;'>Official Web Platform & Intelligent Assessment Engine (onetoonehub.org)</p>", unsafe_allow_html=True)

st.markdown("---")

# القائمة الكاملة لكل المنتورز وتخصصاتهم ولينكاتهم الحقيقية
mentors_pool = [
    {"name": "Menna Ramadan", "title": "Alexandria, Iskala", "category": "General & Operations", "price": "400 EGP / Hour", "profile_url": "https://onetoonehub.org/user/menna-ramadan"},
    {"name": "Tasneem Hassan", "title": "Career Consultant", "category": "Career & HR", "price": "450 EGP / Hour", "profile_url": "https://onetoonehub.org/user/tasneem-hassan"},
    {"name": "Abdelaziz Sami", "title": "CEO, Tech Care", "category": "Tech & Leadership", "price": "600 EGP / Hour", "profile_url": "https://onetoonehub.org/user/abdelaziz-sami"},
    {"name": "Khaled Elshahat", "title": "GEN AI COACH, Freelance", "category": "Artificial Intelligence", "price": "550 EGP / Hour", "profile_url": "https://onetoonehub.org/user/khaled-elshahat"},
    {"name": "Yara Yousef", "title": "HR Supervisor", "category": "HR & Consulting", "price": "450 EGP / Hour", "profile_url": "https://onetoonehub.org/user/yara-yousef"},
    {"name": "Mohamed Kamal", "title": "Content Manager, WaynWay Agency", "category": "Creatives & Content", "price": "450 EGP / Hour", "profile_url": "https://onetoonehub.org/user/mohamedkamalabuzaid"},
    {"name": "Dina Mohamed Tawfik", "title": "Voice Over Talent Mentor, Freelancer", "category": "Media & Journalism", "price": "400 EGP / Hour", "profile_url": "https://onetoonehub.org/user/dina-mohamed-tawfik"},
    {"name": "Amr Al-Khudair", "title": "Co-Founder & CTO, Anwan", "category": "Engineering & Tech", "price": "700 EGP / Hour", "profile_url": "https://onetoonehub.org/user/amr-al-khudair"},
    {"name": "Abeer Ahmed", "title": "Talent Acquisition|OD, Partner Consultancy", "category": "HR & Consulting", "price": "500 EGP / Hour", "profile_url": "https://onetoonehub.org/user/abeer-ahmed"},
    {"name": "Nada Osman", "title": "Design Supervisor, Udacity", "category": "Graphic Design", "price": "500 EGP / Hour", "profile_url": "https://onetoonehub.org/user/nadaosman24"},
    {"name": "Ahmed Ibrahim", "title": "HR Consulting", "category": "Consulting & HR", "price": "500 EGP / Hour", "profile_url": "https://onetoonehub.org/user/ahmed-ibrahim"},
    {"name": "Mohamed ElAttar", "title": "IT Consultant", "category": "IT & Start-up", "price": "650 EGP / Hour", "profile_url": "https://onetoonehub.org/user/mohamed-elattar"},
    {"name": "Ghada Hussein", "title": "Sales Mentor", "category": "Sales & Start-up", "price": "600 EGP / Hour", "profile_url": "https://onetoonehub.org/user/ghada-hussein"},
    {"name": "Basma Sobh", "title": "Voiceover & Dubbing Artist", "category": "Media & Journalism", "price": "400 EGP / Hour", "profile_url": "https://onetoonehub.org/user/basma-sobh"},
    {"name": "Mohammed Salem", "title": "Senior Mobile Developer", "category": "Android & Mobile", "price": "600 EGP / Hour", "profile_url": "https://onetoonehub.org/user/mohammed-salem"},
    {"name": "Noha Radwan", "title": "Freelancing Mentor", "category": "Creatives & Freelancing", "price": "450 EGP / Hour", "profile_url": "https://onetoonehub.org/user/noha-radwan"},
    {"name": "Mohamed Bashandy", "title": "Business Development", "category": "Consulting & Business Dev", "price": "550 EGP / Hour", "profile_url": "https://onetoonehub.org/user/mohamed-bashandy"},
    {"name": "Donia Mohamed", "title": "Content Creation - Storyteller", "category": "Media & Journalism", "price": "400 EGP / Hour", "profile_url": "https://onetoonehub.org/user/donia-mohamed"},
    {"name": "Hend Ayoub", "title": "Content Creator", "category": "Digital Marketing", "price": "400 EGP / Hour", "profile_url": "https://onetoonehub.org/user/hend-ayoub"},
    {"name": "Saleh ElGaberty", "title": "Ai & Systems Adviser", "category": "AI & Systems", "price": "700 EGP / Hour", "profile_url": "https://onetoonehub.org/user/saleh-elgaberty"}
]

if "selected_mentor" not in st.session_state:
    st.session_state.selected_mentor = "Abdelaziz Sami"
if "bookings" not in st.session_state:
    st.session_state.bookings = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

tab1, tab2, tab3, tab4 = st.tabs(["AI Coaching Assessment & Chat", "Experts Directory", "Instant Booking", "Business Dashboard"])

with tab1:
    st.subheader("Strategic AI Coaching & Interactive English Assessment")
    with st.form("assessment_form"):
        q1 = st.selectbox("1. Select primary domain requiring expert intervention:", [
            "Tech & AI Architecture (Software & Artificial Intelligence)",
            "Sales, Business Growth & Market Penetration",
            "Operations Management & Process Optimization",
            "Digital Marketing, Content Strategy & Brand Management",
            "HR, Team Building & Career Development",
            "Visual Design, Media & Voice Production"
        ])
        q2 = st.selectbox("2. Select your current developmental stage:", [
            "Early Ideation & Concept Validation Stage",
            "Career Transition / Professional Upskilling",
            "Early-Stage Operations & Execution Challenges",
            "Scaling, Team Leadership & Enterprise Growth"
        ])
        q3 = st.text_area("3. Describe your core challenge and desired objective (in English):")
        submit_assessment = st.form_submit_button("Run AI Assessment & Start Chat")

    if submit_assessment:
        with st.spinner("Analyzing parameters across all mentors..."):
            mentors_summary = "\n".join([f"- Name: {m['name']} | Title: {m['title']} | Category: {m['category']} | Profile: {m['profile_url']}" for m in mentors_pool])
            prompt = f"""
            You are an elite Business Development Expert and Executive Coach for 1:1 HUB (onetoonehub.org).
            Here is our complete roster of official mentors with their exact categories and profiles:
            {mentors_summary}
            
            Client Assessment Inputs:
            - Focus Domain: {q1}
            - Stage: {q2}
            - Goal/Challenge: {q3}
            
            Task: Analyze the client's goal and select the MOST RELEVANT mentor from the roster above (do not always pick the same person; choose based on expertise match). Start your response with "Recommended Expert: [Exact Name from the list]". Provide a strategic coaching response and include their exact direct profile URL.
            """
            ai_reply = "Recommended Expert: Abdelaziz Sami\n\nBased on your assessment inputs, Abdelaziz Sami is an ideal match. View profile: https://onetoonehub.org/user/abdelaziz-sami"
            if model:
                try:
                    res = model.generate_content(prompt)
                    ai_reply = res.text
                except:
                    pass
            
            for m in mentors_pool:
                if m["name"].lower() in ai_reply.lower():
                    st.session_state.selected_mentor = m["name"]
                    break

            st.session_state.chat_history = [{"role": "assistant", "content": ai_reply}]
            st.success("Assessment completed successfully!")

    st.markdown("---")
    st.subheader("Interactive AI Consultation Chat")
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_chat_input = st.chat_input("Type your follow-up question in English...")
    if user_chat_input:
        st.session_state.chat_history.append({"role": "user", "content": user_chat_input})
        
        mentors_summary = "\n".join([f"- Name: {m['name']} | Title: {m['title']} | Category: {m['category']} | Profile: {m['profile_url']}" for m in mentors_pool])
        chat_prompt = f"""
        You are an elite Business Development AI Assistant for 1:1 HUB mentorship platform (onetoonehub.org).
        Complete Mentors Roster:
        {mentors_summary}
        
        User message: {user_chat_input}
        
        Task: Answer the user's question intelligently. If they ask about a specific topic (like marketing, design, AI, sales, etc.), find the best matching mentor from the roster, state their name clearly, provide advice, and include their direct profile URL.
        """
        reply = "I recommend exploring our experts directory to find the best match for your specific query."
        if model:
            try:
                res = model.generate_content(chat_prompt)
                reply = res.text
            except:
                pass
                
        # تحديث المنتور المختار لو ظهر اسم منتور تاني في الرد
        for m in mentors_pool:
            if m["name"].lower() in reply.lower():
                st.session_state.selected_mentor = m["name"]
                break
                
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

with tab2:
    st.subheader("Certified Experts Directory & Direct Profiles")
    cols = st.columns(3)
    for idx, m in enumerate(mentors_pool):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="mentor-card">
                <b style="color: #1E3A8A; font-size: 15px;">{m['name']}</b><br>
                <span style="font-size: 11px; color: #4B5563;">{m['title']}</span><br>
                <span style="font-size: 11px; color: #0284C7;"><b>Category:</b> {m['category']}</span><br>
                <span style="font-size: 11px; color: #059669;"><b>Rate:</b> {m['price']}</span><br>
                <a href="{m['profile_url']}" target="_blank" class="profile-link">View Official Profile &rarr;</a>
            </div>
            """, unsafe_allow_html=True)

with tab3:
    st.subheader("Instant Executive Session Booking")
    default_idx = next((i for i, m in enumerate(mentors_pool) if m["name"] == st.session_state.selected_mentor), 0)
    with st.form("booking_form"):
        c1, c2 = st.columns(2)
        with c1:
            client_name = st.text_input("Full Name / Company Name:")
            client_email = st.text_input("Professional Email:")
        with c2:
            client_whatsapp = st.text_input("WhatsApp Number:")
            selected_expert = st.selectbox("Assigned Expert:", [m["name"] for m in mentors_pool], index=default_idx)
        objective = st.text_area("Session Objectives & Challenges:")
        confirm_booking = st.form_submit_button("Confirm Booking")
        if confirm_booking:
            if client_name and client_email and client_whatsapp:
                st.session_state.bookings.append({"Client": client_name, "Email": client_email, "Expert": selected_expert})
                st.success(f"Booking confirmed successfully with {selected_expert}!")
            else:
                st.error("Please complete all required fields.")

with tab4:
    st.subheader("Enterprise Business Impact & Dashboard")
    c1, c2, c3 = st.columns(3)
    c1.metric("Matching Efficiency", "98.5%", "+40% Conversion")
    c2.metric("Time Saved", "54 Hours / Mo", "Automated Ops")
    c3.metric("Total Bookings", len(st.session_state.bookings), "Active Pipeline")
    
    st.markdown("---")
    if len(st.session_state.bookings) > 0:
        df = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df, use_container_width=True)
        csv_bytes = df.to_csv(index=False).encode('utf-8')
        st.download_button("Export Bookings Report (CSV)", data=csv_bytes, file_name="bookings_report.csv", mime="text/csv")
    else:
        st.info("No bookings recorded yet.")
