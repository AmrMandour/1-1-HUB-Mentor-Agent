import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="1:1 HUB - Smart Mentor Matcher",
    page_icon="💼",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            font-size: 30px;
            font-weight: bold;
            color: #1E3A8A;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        .subtitle {
            font-size: 16px;
            color: #4B5563;
            text-align: center;
            margin-bottom: 30px;
        }
        .mentor-card {
            background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Display Official Logo
col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
with col_l2:
    st.image("https://raw.githubusercontent.com/AmrMandour/1-1-hub-mentor-agent/main/1to1%20HUB%20Logo.png", use_container_width=True)

st.markdown('<div class="main-title">1:1 HUB - Smart Mentor Matcher & Registration</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Connect with certified mentors, check their schedules, and join our exclusive community.</div>', unsafe_allow_html=True)

# Mentors Database with Images, Schedules, and Prices (matching onetoonehub.org/mentors/)
mentors_database = [
    {
        "name": "Ghada Hussein",
        "title": "Sales & Startup Mentor",
        "category": "Sales & Business Development",
        "experience": "20 Years Experience",
        "price": "500 EGP / Hour",
        "schedule": "Available: Sunday & Tuesday (4:00 PM - 8:00 PM)",
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300&auto=format&fit=crop&q=80",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Mohamed Salem",
        "title": "Lead Mobile App Developer",
        "category": "Programming & Tech Development",
        "experience": "8 Years Experience",
        "price": "600 EGP / Hour",
        "schedule": "Available: Monday & Wednesday (6:00 PM - 10:00 PM)",
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&auto=format&fit=crop&q=80",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Esraa Rashwan",
        "title": "Co-Founder - Masark",
        "category": "Project Management & Startups",
        "experience": "5 Years Experience",
        "price": "450 EGP / Hour",
        "schedule": "Available: Saturday & Thursday (2:00 PM - 6:00 PM)",
        "image": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=300&auto=format&fit=crop&q=80",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Mohamed El-Attar",
        "title": "IT & Tech Consultant",
        "category": "Programming & Tech Development",
        "experience": "19 Years Experience",
        "price": "800 EGP / Hour",
        "schedule": "Available: Friday & Sunday (5:00 PM - 9:00 PM)",
        "image": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=300&auto=format&fit=crop&q=80",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Basma Abaza",
        "title": "Career Coach & CV Specialist",
        "category": "HR & Career Development",
        "experience": "18 Years Experience",
        "price": "400 EGP / Hour",
        "schedule": "Available: Tuesday & Thursday (1:00 PM - 5:00 PM)",
        "image": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=300&auto=format&fit=crop&q=80",
        "profile_url": "https://onetoonehub.org/mentors/"
    }
]

# Step 1: Select Category / Specialization
st.subheader("Step 1: Select Your Field / Specialization")
selected_category = st.selectbox(
    "Choose a domain to view matching mentors:",
    ["Select Category...", "Sales & Business Development", "Programming & Tech Development", "Project Management & Startups", "HR & Career Development"]
)

if selected_category != "Select Category...":
    st.markdown("---")
    st.subheader("Available Mentors in Your Field:")
    
    filtered_mentors = [m for m in mentors_database if m["category"] == selected_category]
    
    if filtered_mentors:
        for mentor in filtered_mentors:
            with st.container():
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(mentor["image"], width=130)
                with col2:
                    st.markdown(f"### {mentor['name']}")
                    st.write(f"**Title:** {mentor['title']}")
                    st.write(f"**Experience:** {mentor['experience']}")
                    st.write(f"**Session Price:** {mentor['price']}")
                    st.write(f"**Schedule & Availability:** {mentor['schedule']}")
                    st.markdown(f"[View Full Profile on 1:1 HUB]({mentor['profile_url']})")
                st.markdown("---")
    else:
        st.info("No mentors currently available in this specific category. Please register your details below and our team will match you.")

# Step 2: User Registration & WhatsApp Community Access (matching onetoonehub.org/user-register/)
st.subheader("Step 2: User Registration & Community Access")
st.write("Complete your registration to save your profile on our platform and receive your instant WhatsApp Community invitation link.")

with st.form("user_registration_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        full_name = st.text_input("Full Name:")
    with col_b:
        whatsapp_number = st.text_input("WhatsApp Number (e.g., +2010xxxxxxxx):")
    
    email_address = st.text_input("Email Address:")
    user_goal = st.text_area("Your Mentorship Goal / Project Details:")
    
    submit_reg = st.form_submit_button(label="Register & Get WhatsApp Community Link")
    
    if submit_reg:
        if full_name and whatsapp_number and email_address:
            st.success(f"Registration Successful, {full_name}! Your data has been recorded in our system.")
            st.info("Check your email and WhatsApp for your exclusive community invitation link and session booking details.")
            st.markdown("**Official Platform Registration Link:** [1:1 HUB Register Page](https://onetoonehub.org/user-register/)")
            st.markdown("**Instant WhatsApp Community Link:** [Join 1:1 HUB Community](https://chat.whatsapp.com/invite/placeholder)")
        else:
            st.error("Please fill in all required fields (Full Name, WhatsApp Number, and Email Address) to complete registration.")
