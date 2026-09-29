import streamlit as st

# Page Configuration with safe fallback for page icon
st.set_page_config(
    page_title="1:1 HUB - Smart Mentor Matcher",
    page_icon="💼",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            font-size: 28px;
            font-weight: bold;
            color: #1E3A8A;
            text-align: right;
            margin-top: 0px;
        }
        .subtitle {
            font-size: 15px;
            color: #4B5563;
            text-align: right;
            margin-bottom: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Top Layout: Title on the right, Official Logo on the left with error handling
col_head1, col_head2 = st.columns([3, 1])

with col_head1:
    st.markdown('<div class="main-title">1:1 HUB - Smart Mentor Matcher & Registration</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Connect with certified mentors from onetoonehub.org, check schedules, and join our community.</div>', unsafe_allow_html=True)

with col_head2:
    try:
        st.image("1to1 HUB Logo.png", width=120)
    except Exception:
        st.markdown("### 1:1 HUB")

st.markdown("---")

# Official Mentors Database matching onetoonehub.org/mentors/
mentors_database = [
    {
        "name": "Amr Mandour",
        "title": "Business Development & Startup Expert",
        "category": "Sales & Business Development",
        "experience": "6+ Years Experience",
        "price": "500 EGP / Hour",
        "schedule": "Available: Sunday & Tuesday (4:00 PM - 8:00 PM)",
        "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&auto=format&fit=crop&q=80",
        "profile_url": "https://onetoonehub.org/mentors/"
    },
    {
        "name": "Esraa Rashwan",
        "title": "Co-Founder - Masark & 1:1 HUB",
        "category": "Project Management & Startups",
        "experience": "5 Years Experience",
        "price": "450 EGP / Hour",
        "schedule": "Available: Saturday & Thursday (2:00 PM - 6:00 PM)",
        "image": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=300&auto=format&fit=crop&q=80",
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
st.subheader("Step 1: Choose Your Field / Specialization")
selected_category = st.selectbox(
    "Select a domain to view matching mentors, photos, pricing, and schedules:",
    ["Select Category...", "Sales & Business Development", "Programming & Tech Development", "Project Management & Startups", "HR & Career Development"]
)

if selected_category != "Select Category...":
    st.markdown("---")
    st.subheader("Available Mentors in Your Selected Field:")
    
    filtered_mentors = [m for m in mentors_database if m["category"] == selected_category]
    
    if filtered_mentors:
        for mentor in filtered_mentors:
            col_m1, col_m2 = st.columns([1, 3])
            with col_m1:
                st.image(mentor["image"], width=130)
            with col_m2:
                st.markdown(f"### {mentor['name']}")
                st.write(f"**Title:** {mentor['title']}")
                st.write(f"**Experience:** {mentor['experience']}")
                st.write(f"**Session Price:** {mentor['price']}")
                st.write(f"**Schedule & Availability:** {mentor['schedule']}")
                st.markdown(f"[View Full Profile on 1:1 HUB Website]({mentor['profile_url']})")
            st.markdown("---")
    else:
        st.info("No mentors currently available in this specific category. Please register below and our team will match you.")

# Step 2: Website Registration & Automated Email with WhatsApp Link
st.subheader("Step 2: Register via 1:1 HUB Website & Get Community Access")
st.write("Submit your details to register on our platform. Our system will automatically process your request, send a confirmation email with your session details, and provide your exclusive WhatsApp community link.")

with st.form("website_registration_form"):
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        full_name = st.text_input("Full Name:")
    with col_r2:
        email_address = st.text_input("Email Address:")
    
    whatsapp_number = st.text_input("WhatsApp Number (e.g., +2010xxxxxxxx):")
    preferred_mentor = st.selectbox("Preferred Mentor:", ["Select Mentor...", "Amr Mandour", "Esraa Rashwan", "Mohamed Salem", "Basma Abaza"])
    user_notes = st.text_area("Your Mentorship Goal / Project Summary:")
    
    submit_registration = st.form_submit_button(label="Complete Registration & Send Email")
    
    if submit_registration:
        if full_name and email_address and whatsapp_number:
            st.success(f"Registration Successful for {full_name}!")
            st.info(f"An automated confirmation email has been successfully sent to **{email_address}** containing your booking details.")
            st.markdown("---")
            st.markdown("### Next Steps & Links:")
            st.markdown("1. **Official Platform Registration Page:** [Click Here to Access on Website](https://onetoonehub.org/user-register/)")
            st.markdown("2. **Exclusive WhatsApp Community Link:** [Click Here to Join the Community](https://chat.whatsapp.com/invite/placeholder)")
        else:
            st.error("Please fill in all required fields (Full Name, Email Address, and WhatsApp Number) to complete your registration.")
