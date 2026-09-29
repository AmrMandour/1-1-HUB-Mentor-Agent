import streamlit as st

# إعدادات صفحة التطبيق
st.title("1:1 HUB - Smart Mentor Agent")
st.write("مساعد ذكي مطور خصيصاً لمطابقة الخريجين مع الموجهين المناسبين.")

# وضع الديمو الآمن (Demo Mode - تطبيقاً لشروط الهاكاثون)
demo_mode = st.sidebar.checkbox("تفعيل وضع العرض (Demo Mode)", value=True)

# قاعدة المعرفة المبسطة للمنتورز (RAG Data Mock)
knowledge_base = {
    "تسويق": "الموجه المقترح: أحمد ممدوح - خبير تسويق رقمي وإدارة نمو للشركات الناشئة.",
    "برمجة": "الموجه المقترح: محمد وليد - مهندس برمجيات وخبير في تطوير الأنظمة الذكية.",
    "إدارة": "الموجه المقترح: عمرو منصور - متخصص في إدارة المشاريع وتنسيق ريادة الأعمال."
}

user_query = st.text_input("اكتب مجالك أو سؤالك (مثلاً: أريد موجه في التسويق أو البرمجة):")

if st.button("الحصول على توجيه"):
    if demo_mode:
        # وضع التشغيل الآمن بدون الحاجة لمفتاح API حقيقي
        found = False
        for key, mentor in knowledge_base.items():
            if key in user_query:
                st.success(mentor)
                found = True
                break
        if not found:
            st.info("الموجه المقترح العام: فريق 1:1 HUB للإرشاد المهني جاهز لمساعدتك.")
    else:
        # هنا يتم ربط كود الـ API الحقيقي (مثل Groq أو OpenAI)
        st.warning("يرجى إدخال مفتاح الـ API الخاص بالخدمة.")