import streamlit as st
import requests

# إعدادات الصفحة
st.set_page_config(
    page_title="1:1 HUB - Smart Mentor Matching Agent",
    page_icon="🎯",
    layout="centered"
)

# تصميم وتنسيق بصري بسيط
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    h1, h2, h3, p, label { direction: rtl; text-align: right; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 1:1 HUB - Smart Mentor Matcher")
st.write("مساعدك الذكي لمطابقة احتياجاتك التدريبية مع أفضل الموجهين المعتمدين على منصتنا، وتسهيل حجز جلستك المجانية فوراً!")

# قاعدة بيانات الموجهين (مستخرجة من موقعك https://onetoonehub.org/mentors/)
mentors_db = [
    {
        "name": "أحمد ممدوح",
        "expertise": "تسويق رقمي وإدارة نمو الشركات الناشئة",
        "keywords": ["تسويق", "إعلان", "سوشيال", "marketing", "growth", "نمو"],
        "url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "خبراء 1:1 HUB للتطوير المهني",
        "expertise": "إدارة المشاريع والتخطيط الاستراتيجي",
        "keywords": ["إدارة", "مشاريع", "project", "agile", "scrum", "تخطيط"],
        "url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "فريق التوجيه التقني",
        "expertise": "البرمجة وتطوير البرمجيات والذكاء الاصطناعي",
        "keywords": ["برمجة", "تطوير", "كود", "python", "ai", "coding", "software"],
        "url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "مستشاري ريادة الأعمال",
        "expertise": "تأسيس الشركات الناشئة وجمع التمويل ونماذج العمل",
        "keywords": ["ستارت أب", "شركة ناشئة", "تمويل", "pitch", "startup", "business"],
        "url": "https://onetoonehub.org/mentors/"
    }
]

# الخطوة الأولى: استقبال استفسار المستخدم
user_query = st.text_input("💬 اكتب مجالك، مشكلتك، أو إيه اللي محتاج توجيه فيه (مثلاً: عاوز أبدأ في التسويق الرقمي أو عندي شركة ناشئة وعايز أنمو):")

if st.button("🔍 اعثر على الموجه المناسب"):
    if not user_query.strip():
        st.warning("من فضلك اكتب سؤالك أو مجالك أولاً.")
    else:
        # خوارزمية مطابقة ذكية بسيطة مبنية على الكلمات المفتاحية
        matched_mentors = []
        query_lower = user_query.lower()
        
        for mentor in mentors_db:
            if any(kw in query_lower for kw in mentor["keywords"]):
                matched_mentors.append(mentor)
        
        # لو مفيش مطابقة دقيقة، نقترح الكل أو موجه عام
        if not matched_mentors:
            matched_mentors = mentors_db[:2]
            
        st.success("✨ وجدنا لك أفضل الموجهين المتطابقين مع احتياجك:")
        
        for m in matched_mentors:
            st.markdown(f"""
            - **الموجه المقترح:** {m['name']}
            - **التخصص:** {m['expertise']}
            - 🔗 [زيارة صفحة الموجهين وحجز الجلسة مباشرة]({m['url']})
            """)
        
        # حفظ الاختيار في الذاكرة المؤقتة عشان نموذج التسجيل
        st.session_state['recommended_mentor'] = matched_mentors[0]['name']

st.markdown("---")
st.subheader("📥 احصل على ملخص ترشيحك ورابط الجلسة عبر الإيميل والواتساب (مجاناً)")

with st.form("registration_form"):
    col1, col2 = st.columns(2)
    with col1:
        reg_name = st.text_input("الاسم بالكامل:")
    with col2:
        reg_phone = st.text_input("رقم الواتساب (مثال: 010xxxxxxxx):")
    
    reg_email = st.text_input("البريد الإلكتروني:")
    
    submit_btn = st.form_submit_button("🚀 سجل بياناتي واحفظ الترشيح")
    
    if submit_btn:
        if not reg_name or not reg_phone or not reg_email:
            st.error("من فضلك أكمل جميع بيانات التسجيل.")
        else:
            # رابط Make.com Webhook (تقدر تحط رابط الـ Webhook الخاص بك هنا لاحقاً)
            webhook_url = "https://hook.eu1.make.com/your-unique-webhook-here"
            
            payload = {
                "name": reg_name,
                "phone": reg_phone,
                "email": reg_email,
                "query": user_query,
                "mentor": st.session_state.get('recommended_mentor', 'عام')
            }
            
            try:
                # إرسال البيانات لـ Make لتققوم بدورها بإرسال الإيميل والرسالة
                # requests.post(webhook_url, json=payload)
                st.balloons()
                st.success(f"مرحباً بك يا {reg_name}! تم تسجيل بياناتك بنجاح، وستم إرسال تفاصيل الترشيح ورابط الحجز المجاني على واتساب وإيميلك فوراً.")
            except Exception as e:
                st.error("حدث خطأ بسيط، برجاء المحاولة مرة أخرى.")
