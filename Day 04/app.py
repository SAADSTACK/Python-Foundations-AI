import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="Premium Freelance AI Tools Suite", layout="wide")

# Sidebar Setup - Models & Navigation Controls
with st.sidebar:
    st.title("💼 Client Console")
    st.subheader("Configuration Panel")
    selected_model = st.selectbox("Select LLM Core", ["gpt-4o-mini", "gpt-4o"])
    ai_temperature = st.slider("Creativity Level (Temperature)", 0.0, 1.0, 0.3)
    st.info("Built by Saad Malik | Premium AI Solutions Provider")

# Main Product Multi-App Navigation Mappings
st.title("🚀 Saad's Premium AI Product Suite")
st.write("Deployable High-End Freelance MVP Frameworks")

product_mode = st.radio(
    "Choose a Client-Side Product to Deploy:",
    ["Premium Chatbot", "AI Freelance Copywriter", "SaaS Resume Screener Expert"]
)
st.markdown("---")
# Core Client Init Validation
api_key = os.getenv("OPENAI_API_KEY") if os.getenv("OPENAI_API_KEY") else "sk-proj-paste-your-actual-key-here"
client = OpenAI(api_key=api_key)
if product_mode == "Premium Chatbot":
    st.subheader("🤖 Smart Assistant Module")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Render existing history blocks
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_prompt = st.chat_input("Ask your premium assistant anything...")
    if user_prompt:
        with st.chat_message("user"):
            st.write(user_prompt)
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})

        response = client.chat.completions.create(
            model=selected_model,
            temperature=ai_temperature,
            messages=[{"role": "system", "content": "You are a world-class AI SaaS tool built by Saad Malik. Answer sharply."}] + st.session_state.chat_history
        )
        ai_res = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(ai_res)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_res})

elif product_mode == "AI Freelance Copywriter":
    st.subheader("✍️ Automated Copywriting Engine")
    business_niche = st.text_input("Enter Product/Business Niche Name:", placeholder="e.g., Luxury Watch Brand, Coding Bootcamps")
    ad_platform = st.selectbox("Select Target Copy Format:", ["Facebook High-Converting Ad Copy", "Fiverr Gigs Title & Description Generator", "LinkedIn Viral Authority Hooks"])

    if st.button("Generate Premium Copy Assets"):
        if business_niche:
            with st.spinner("Writing optimized copywriting assets..."):
                response = client.chat.completions.create(
                    model=selected_model,
                    temperature=ai_temperature,
                    messages=[
                        {"role": "system", "content": "You are a professional conversion copywriter trained in psychological triggers and high-retention content marketing frameworks."},
                        {"role": "user", "content": f"Generate ultra high-converting copy assets for a business named '{business_niche}' optimized specifically for '{ad_platform}'. Use structured formats and call-to-actions."}
                    ]
                )
                st.success("Generation Complete!")
                st.markdown(response.choices[0].message.content)
        else:
            st.warning("Please provide a business niche first.")

elif product_mode == "SaaS Resume Screener Expert":
    st.subheader("📄 Automated Enterprise Resume Matcher")
    target_job_role = st.text_input("Enter Target Job Title/Role:", placeholder="e.g., Senior Full-Stack Python Developer")
    resume_raw_text = st.text_area("Paste Raw Resume Contents Here:", height=200, placeholder="Paste entire text dump from the applicant's resume...")

    if st.button("Analyze Applicant Profiles"):
        if target_job_role and resume_raw_text:
            with st.spinner("Evaluating profile against domain metrics..."):
                response = client.chat.completions.create(
                    model=selected_model,
                    temperature=ai_temperature,
                    messages=[
                        {"role": "system", "content": "You are an elite corporate technical recruiter scanner. Rank alignment and return feedback broken down strictly into: 1. Core Score (0-100), 2. Keyword Matches, 3. Critical Gaps, 4. Immediate Upgrades Suggestions."},
                        {"role": "user", "content": f"Evaluate this candidate's raw profile for the '{target_job_role}' role. Candidate profile data: {resume_raw_text}"}
                    ]
                )
                st.subheader("📋 Analytical Feedback Breakdown Report")
                st.markdown(response.choices[0].message.content)
        else:
            st.warning("Please provide both job role and profile dump text.")
