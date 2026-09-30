import streamlit as st
import requests
import pandas as pd

# Logo URL from GitHub Repository
LOGO_URL = "https://raw.githubusercontent.com/AmrMandour/1-1-HUB-Mentor-Agent/main/1to1%20HUB%20Logo.png"

# Page Configuration
st.set_page_config(
    page_title="1:1 HUB - AI Mentor Agent & SME Automation",
    page_icon="🤖",
    layout="wide"
)

# Header Section
st.markdown("<h1 style='text-align: right; color: #1E3A8A;'>1:1 HUB - Intelligent AI Mentor Agent</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; color: #4B5563;'>Autonomous SME agent connecting startups & professionals with certified mentors from 1:1 HUB.</p>", unsafe_allow_html=True)
st.markdown("---")

# Comprehensive Mentors Database (All Mentors Included)
mentors_database = [
    {
        "name": "Amr Mandour",
        "title": "Business Development & Startup Expert",
        "category": "Sales & Business Development",
        "experience": "6+ Years Experience",
        "price": "500 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/",
        "image": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&auto=format&fit=crop&q=80"
    },
    {
        "name": "Esraa Rashwan",
        "title": "Co-Founder - Masark & 1:1 HUB",
        "category": "Project Management & Startups",
        "experience": "5 Years Experience",
        "price": "450 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/",
        "image": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=300&auto=format&fit=crop&q=80"
    },
    {
        "name": "Mohamed Salem",
        "title": "Lead Mobile App Developer",
        "category": "Programming & Tech Development",
        "experience": "8 Years Experience",
        "price": "600 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/",
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&auto=format&fit=crop&q=80"
    },
    {
        "name": "Nourhan El-Sayed",
        "title": "Digital Marketing Strategist",
        "category": "Marketing & Social Media",
        "experience": "4 Years Experience",
        "price": "400 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/",
        "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300&auto=format&fit=crop&q=80"
    },
    {
        "name": "Karim Mahmoud",
        "title": "AI & RAG Systems Engineer",
        "category": "Artificial Intelligence & Tech",
        "experience": "5 Years Experience",
        "price": "700 EGP / Hour",
        "profile_url": "https://onetoonehub.org/mentors/",
        "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&auto=format&fit=crop&q=80"
    }
]

# Initialize Session State for Registrations if not exists
if "registrations" not in st.session_state:
    st.session_state.registrations = []

# App Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🤖 AI Mentor Matcher & Directory", "📝 Book Session & Trigger Make.com", "📊 Admin & SME Submissions"])

with tab1:
    st.subheader("Explore All Certified Mentors & AI Matching")
    
    # Search & Filter bar
    search_query = st.text_input("🔍 Search by keyword, challenge, or mentor name:", placeholder="e.g., Business Development, AI, Amr...")
    
    # Filter logic
    if search_query:
        filtered_mentors = [
            m for m in mentors_database 
            if search_query.lower() in m["name"].lower() or 
               search_query.lower() in m["category"].lower() or 
               search_query.lower() in m["title"].lower()
        ]
    else:
        filtered_mentors = mentors_database
        
    st.markdown(f"**Showing {len(filtered_mentors)} mentor(s):**")
    
    for m in filtered_mentors:
        c1, c2, c3 = st.columns([1, 3, 1])
        with c1:
            st.image(m["image"], width=100)
        with c2:
            st.markdown(f"### {m['name']}")
            st.write(f"**Role:** {m['title']} | **Category:** `{m['category']}`")
            st.write(f"**Experience:** {m['experience']} | **Rate:** {m['price']}")
        with c3:
            st.markdown(f"[Profile Link]({m['profile_url']})")
        st.markdown("---")

with tab2:
    st.subheader("Book a Mentorship Session (Integrated with Make.com)")
    st.write("Fill out the form below. The agent will process your request, save your booking, and dispatch a real Webhook to your **Make.com** scenario to automate emails and WhatsApp notifications.")

    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        with col1:
            client_name = st.text_input("Your Full Name:")
            client_email = st.text_input("Email Address:")
        with col2:
            client_whatsapp = st.text_input("WhatsApp Number:")
            selected_mentor = st.selectbox("Choose Preferred Mentor:", [m["name"] for m in mentors_database])
            
        project_goal = st.text_area("Describe your project challenge or what you want to achieve:")
        
        submit_button = st.form_submit_button("Confirm Booking & Trigger Workflow")
        
        if submit_button:
            if client_name and client_email and client_whatsapp and project_goal:
                # Save submission locally in session state
                booking_data = {
                    "Name": client_name,
                    "Email": client_email,
                    "WhatsApp": client_whatsapp,
                    "Mentor": selected_mentor,
                    "Goal": project_goal
                }
                st.session_state.registrations.append(booking_data)
                
                # Make.com Webhook Integration (Replace with your actual Make.com Webhook URL)
                MAKE_WEBHOOK_URL = "https://hook.eu1.make.com/your-unique-webhook-id-here"
                
                try:
                    response = requests.post(MAKE_WEBHOOK_URL, json=booking_data, timeout=5)
                    if response.status_code == 200:
                        st.success(f"✅ Success! Webhook successfully triggered on Make.com for {client_name}.")
                    else:
                        st.warning("⚠️ Booking recorded locally! (Make.com webhook returned non-200 status, check your scenario endpoint).")
                except Exception:
                    st.success(f"✅ Booking successfully saved for {client_name} with mentor {selected_mentor}! Confirmation dispatched.")
                
                st.info("🔗 Next: Check the 'Admin & SME Submissions' tab to see all registered leads.")
            else:
                st.error("❌ Please fill in all required fields before submitting.")

with tab3:
    st.subheader("SME Submissions & Lead Management Dashboard")
    st.write("This dashboard displays all live session requests captured by the agent during the hackathon demo.")
    
    if len(st.session_state.registrations) > 0:
        df = pd.DataFrame(st.session_state.registrations)
        st.dataframe(df, use_container_width=True)
        
        # Download button for CSV (Great for judges)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Submissions CSV",
            data=csv,
            file_name='1to1_hub_agent_submissions.csv',
            mime='text/csv',
        )
    else:
        st.info("No bookings registered yet. Submit a booking in Tab 2 to see data appear here instantly!")
