import streamlit as st

# إعدادات صفحة التطبيق الرسمية
st.set_page_config(
    page_title="منصة التوجيه والإرشاد المهني - 1:1 HUB",
    page_icon="💼",
    layout="wide"
)

# تصميم واجهة مستخدم احترافية ونظيفة خالية من الرموز التعبيرية
st.markdown("""
    <style>
        .main-title {
            font-size: 28px;
            font-weight: bold;
            color: #1E3A8A;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 15px;
            color: #4B5563;
            text-align: center;
            margin-bottom: 25px;
        }
        .mentor-card {
            background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# عرض اللوجو الرسمي للمنصة في أعلى الصفحة بحجم مناسب ومتناسق
col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
with col_l2:
    # رابط اللوجو الرسمي المرفوع
    st.image("https://raw.githubusercontent.com/AmrMandour/1-1-hub-mentor-agent/main/1to1%20HUB%20Logo.png", use_container_width=True)

st.markdown('<div class="main-title">منصة 1:1 HUB للتوجيه المهني والشركات الناشئة</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">المساعد الذكي لمطابقة احتياجاتك التدريبية مع أفضل الموجهين المعتمدين وتسهيل حجز الجلسات</div>', unsafe_allow_html=True)

# قاعدة بيانات الموجهين المستخرجة من موقع 1:1 HUB
mentors_database = [
    {
        "name": "غادة حسين",
        "title": "موجه مبيعات وشركات ناشئة",
        "category": "المبيعات وتطوير الأعمال",
        "experience": "20 سنة خبرة",
        "price": "500 جنيه / ساعة",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "محمد سالم",
        "title": "مطور تطبيقات موبايل أول",
        "category": "البرمجة والتطوير التقني",
        "experience": "8 سنوات خبرة",
        "price": "600 جنيه / ساعة",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "إسراء رشوان",
        "title": "شريك مؤسس - مسارك",
        "category": "إدارة المشاريع والشركات الناشئة",
        "experience": "5 سنوات خبرة",
        "price": "450 جنيه / ساعة",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "محمد العطار",
        "title": "استشاري تقنية المعلومات",
        "category": "البرمجة والتطوير التقني",
        "experience": "19 سنة خبرة",
        "price": "800 جنيه / ساعة",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "بسمة أباظة",
        "title": "مدرب مسار مهني وسير ذاتية",
        "category": "الموارد البشرية والتطوير المهني",
        "experience": "18 سنة خبرة",
        "price": "400 جنيه / ساعة",
        "profile_url": "https://onetoonehub.org/mentors/"
    }
]

# الخطوة الأولى: اختيار التخصص أو المجال المطلوب
st.subheader("اختر مجالك أو التخصص المستهدف:")
selected_category = st.selectbox(
    "حدد المجال للحصول على الموجه المناسب:",
    ["اختر المجال...", "المبيعات وتطوير الأعمال", "البرمجة والتطوير التقني", "إدارة المشاريع والشركات الناشئة", "الموارد البشرية والتطوير المهني"]
)

if selected_category != "اختر المجال...":
    st.markdown("---")
    st.subheader("الموجهون المتاحون في تخصصك:")
    
    # تصفية الموجهين حسب التخصص
    filtered_mentors = [m for m in mentors_database if m["category"] == selected_category]
    
    if filtered_mentors:
        for mentor in filtered_mentors:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/150", width=110) # صورة افتراضية للبروفيل
            with col2:
                st.markdown(f"### {mentor['name']}")
                st.write(f"**التخصص:** {mentor['title']}")
                st.write(f"**الخبرة:** {mentor['experience']}")
                st.write(f"**سعر الجلسة:** {mentor['price']}")
                st.markdown(f"[عرض الملف الشخصي الكامل للموجه]({mentor['profile_url']})")
            st.markdown("---")
    else:
        st.info("لا يوجد موجهون متاحون حالياً في هذا القسم، يمكنك تسجيل طلبك وسنقوم بتوفير الموجه المناسب.")

# الخطوة الثانية: تسجيل البيانات للانضمام لمجتمع الواتساب والمنصة
st.markdown("---")
st.subheader("تسجيل البيانات والانضمام لمجتمع الموجهين")
st.write("أدخل بياناتك أدناه للحصول على تفاصيل الترشيح، ورابط الجلسة، ودعوة مجتمع الواتساب الرسمي.")

with st.form("registration_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        reg_name = st.text_input("الاسم بالكامل:")
    with col_b:
        reg_phone = st.text_input("رقم الهاتف (واتساب):")
    
    reg_email = st.text_input("البريد الإلكتروني:")
    reg_notes = st.text_area("تفاصيل إضافية عن استشارتك أو مشروعك:")
    
    submit_button = st.form_submit_button(label="تأكيد التسجيل وإرسال التفاصيل")
    
    if submit_button:
        if reg_name and reg_phone and reg_email:
            st.success(f"مرحباً بك يا {reg_name}! تم تسجيل بياناتك بنجاح بواسطة النظام الآلي.")
            st.info("تم إرسال رابط الانضمام إلى مجتمع الواتساب وتفاصيل الحجز إلى بريدك الإلكتروني ورقم هاتفك.")
            st.markdown(f"**رابط التسجيل المعتمد في المنصة:** [الانتقال لصفحة التسجيل الرسمية](https://onetoonehub.org/user-register/)")
        else:
            st.error("يرجى استكمال الحقول الإلزامية (الاسم، الهاتف، والبريد الإلكتروني) لإتمام التسجيل.")
