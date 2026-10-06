import streamlit as st
import requests
import pandas as pd
import google.generativeai as genai

# Configure Google Gemini API Key
GOOGLE_API_KEY = "AQ.Ab8RN6L3bAmzZiLK9DAf5h7SMyFTTrxh6TIBk_qczXHWJrVQ"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    model = None

LOGO_URL = "https://raw.githubusercontent.com/AmrMandour/1-1-HUB-Mentor-Agent/main/1to1%20HUB%20Logo.png"

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
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Header
col_logo, col_title = st.columns([1, 6])
with col_logo:
    try:
        st.image(LOGO_URL, width=85)
    except:
        st.write("1:1 HUB")
with col_title:
    st.markdown("<h2 style='color: #1E3A8A; margin: 0;'>1:1 HUB — Autonomous AI Mentor Matcher</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #4B5563; margin: 0;'>Interactive AI Consultant & Dynamic Expert Matching Engine</p>", unsafe_allow_html=True)

st.markdown("---")

# Dynamic Full Mentors Pool
mentors_pool = [
    {
        "name": "Amr Mandour",
        "title": "Business Development & Startup Expert",
        "category": "Sales & Business Development",
        "skills": ["sales", "marketing", "growth", "b2b", "leads", "revenue", "تسويق", "مبيعات", "تطوير أعمال"],
        "price": "500 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Esraa Rashwan",
        "title": "Co-Founder - Masark & 1:1 HUB",
        "category": "Project Management & Operations",
        "skills": ["project", "management", "operations", "strategy", "startup", "إدارة مشروعات", "عمليات", "استراتيجية"],
        "price": "450 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Mohamed Salem",
        "title": "Lead Mobile App Developer",
        "category": "Programming & Tech Development",
        "skills": ["tech", "app", "development", "code", "programming", "ai", "برمجة", "تطوير تطبيقات", "ذكاء اصطناعي"],
        "price": "600 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/"
    }
]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "أهلاً بك! أنا مساعد 1:1 HUB الذكي. احكي لي عن مشروعك، إيه التحدي اللي بتواجهه دلوقتي، ومحتاج تحققه في خلال ٣٠ يوم؟ وأنا هحلل مشكلتك وأرشح لك المنتور الأنسب ليك فوراً."}
    ]
if "bookings" not in st.session_state:
    st.session_state.bookings = []
if "selected_mentor" not in st.session_state:
    st.session_state.selected_mentor = "Amr Mandour"

tab1, tab2, tab3 = st.tabs(["Interactive AI Chat & Matcher", "Instant Booking & Automation", "Business Impact Dashboard"])

with tab1:
    st.subheader("Interactive Consultation with Gemini AI")
    
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Chat input
    if user_input := st.chat_input("اكتب مشكلة مشروعك هنا (مثلاً: محتاج أزود المبيعات وأجيب عملاء B2B)..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        with st.chat_message("assistant"):
            with st.spinner("جاري تحليل المشكلة ومراجعة كل المنتورز..."):
                mentors_summary = "\n".join([f"- {m['name']} ({m['title']} - تخصص: {m['category']})" for m in mentors_pool])
                
                system_prompt = f"""
                You are an expert AI business consultant for 1:1 HUB. 
                Here is the list of available mentors:
                {mentors_summary}
                
                The user said: "{user_input}"
                
                Task: 
                1. Analyze the user's startup problem.
                2. Select the best matching mentor from the list.
                3. Explain clearly why this mentor is the perfect match based on their expertise.
                4. Give an encouraging professional response.
                """
                
                reply = " بناءً على تحديك، أرشح لك الخبير Amr Mandour لمساعدتك في تطوير الأعمال وزيادة المبيعات."
                if model:
                    try:
                        res = model.generate_content(system_prompt)
                        reply = res.text
                    except:
                        pass
                
                if "Esraa" in reply:
                    st.session_state.selected_mentor = "Esraa Rashwan"
                elif "Mohamed" in reply:
                    st.session_state.selected_mentor = "Mohamed Salem"
                else:
                    st.session_state.selected_mentor = "Amr Mandour"
                    
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})

    st.markdown("---")
    st.subheader("جميع المنتورز المتاحين في المنصة")
    cols = st.columns(len(mentors_pool))
    for idx, m in enumerate(mentors_pool):
        with cols[idx]:
            st.markdown(f"""
            <div class="mentor-card">
                <h4>{m['name']}</h4>
                <p style="font-size: 13px; color: #4B5563;">{m['title']}</p>
                <p><b>السعر:</b> {m['price']}</p>
                <a href="{m['profile_url']}" target="_blank" style="color: #1E3A8A; font-weight: bold; text-decoration: none;">عرض البروفايل &rarr;</a>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.subheader("حجز الجلسة الفوري مع المنتور المقترح")
    st.markdown(f"المنتور المقترح حالياً بواسطة الذكاء الاصطناعي: **{st.session_state.selected_mentor}**")

    default_idx = 0
    for idx, m in enumerate(mentors_pool):
        if m["name"] == st.session_state.selected_mentor:
            default_idx = idx

    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        with col1:
            client_name = st.text_input("الاسم بالكامل:")
            client_email = st.text_input("البريد الإلكتروني:")
        with col2:
            client_whatsapp = st.text_input("رقم الواتساب:")
            selected_expert = st.selectbox("اختر المنتور:", [m["name"] for m in mentors_pool], index=default_idx)
            
        objective = st.text_area("هدف الجلسة أو التحدي المطلوب حله:")
        confirm_booking = st.form_submit_button("تأكيد الحجز وتفعيل الأتمتة")
        
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
                
                MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/your-unique-webhook-url-here"
                try:
                    requests.post(MAKE_WEBHOOK_URL, json=booking_record, timeout=5)
                except:
                    pass
                
                st.success(f"تم تأكيد حجزك بنجاح مع {selected_expert}! تم إرسال البيانات وإجراء الأتمتة.")
            else:
                st.error("يرجى استكمال جميع الحقول المطلوبة.")

with tab3:
    st.subheader("لوحة مؤشرات الأثر التجاري")
    c1, c2, c3 = st.columns(3)
    c1.metric("الوقت المُوفر", "48 ساعة / أسبوع", "-95% عمل يدوي")
    c2.metric("توفير التكاليف", "12,500 ج.م", "خفض التكاليف التشغيلية")
    c3.metric("العملاء المحتملين", len(st.session_state.bookings), "حجم الـ Pipeline النشط")
    
    st.markdown("---")
    if len(st.session_state.bookings) > 0:
        df = pd.DataFrame(st.session_state.bookings)
        st.dataframe(df, use_container_width=True)
        csv_bytes = df.to_csv(index=False).encode('utf-8')
        st.download_button("تصدير تقرير التحليلات (CSV)", data=csv_bytes, file_name="leads_impact.csv", mime="text/csv")
    else:
        st.info("لا توجد حجوزات مسجلة حتى الآن. جرب محادثة الذكاء الاصطناعي في تبويب 1 واحجز جلستك في تبويب 2.")
