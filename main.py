import streamlit as st
import os
import tempfile
from pipeline.pipeline import ATSPipeline

# 1. Page Config
st.set_page_config(page_title="AI ATS Analyzer", page_icon="🎯", layout="centered")

# 2. Custom CSS (Integrated Styling + Hiding Streamlit Branding)
st.markdown("""
    <style>
    /* 1. HIDE ALL SYSTEM UI (Branding & Menu) */
    [data-testid="stToolbar"], [data-testid="stHeader"], #MainMenu, footer, .stDeployButton {
        visibility: hidden !important;
        display: none !important;
    }

    /* 2. FORCE BACKGROUND COLOR (The "Flash" white fix) */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
    }

    /* 3. FORCE FONT AND TEXT COLOR */
    body, [data-testid="stAppViewContainer"], .stMarkdown, .stText {
        font-family: 'Inter', sans-serif !important;
        color: #1e293b !important;
    }

    /* 4. INPUT CARD OVERRIDE */
    .input-card { 
        background: #f8fafc !important; 
        padding: 2rem !important; 
        border-radius: 20px !important; 
        border: 1px solid #e2e8f0 !important;
        margin-bottom: 2rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
    }

    /* 5. METRIC CARDS OVERRIDE */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #1e293b !important;
    }
    
    /* 6. BUTTON OVERRIDE */
    div.stButton > button {
        background-color: #2563eb !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function
def show_skills(skills, type):
    color_class = "matched" if type == "match" else "missing"
    for skill in skills:
        st.markdown(f'<span class="skill-pill {color_class}">{skill}</span>', unsafe_allow_html=True)

@st.cache_resource
def get_pipeline():
    return ATSPipeline()

pipeline = get_pipeline()

# --- Main Interface ---
st.title("🎯 AI ATS Resume Analyzer")
st.markdown("Upload your resume and get professional insights in seconds.")

# Input Section (The "Input Card")
with st.container():
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        uploaded_file = st.file_uploader("📂 Upload Resume", type=["pdf", "docx"])
    with c2:
        st.write("") 
        job_description = st.text_area("📝 Job Description", height=80, placeholder="Paste JD here...")
    
    analyze_btn = st.button("🚀 Analyze My Resume", type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

# Results Section
if analyze_btn:
    if uploaded_file and job_description:
        with st.spinner("Analyzing your profile..."):
            suffix = os.path.splitext(uploaded_file.name)[1]
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            tfile.write(uploaded_file.getbuffer())
            tfile.close()
            
            try:
                result = pipeline.analyze(tfile.name, job_description)
                
                # Metrics
                col1, col2 = st.columns(2)
                with col1.container(border=True):
                    st.metric("ATS Score", f"{result['ats_score']}/100")
                with col2.container(border=True):
                    st.metric("Match %", f"{result['match_percentage']}%")
                
                # Summary Section
                with st.container(border=True):
                    st.subheader("📝 Executive Summary")
                    st.write(result['summary'])
                
                # Skills Gap
                st.subheader("💡 Skills Analysis")
                s1, s2 = st.columns(2)
                with s1.container(border=True):
                    st.write("✅ **Matched Skills**")
                    show_skills(result['matched_skills'], "match")
                with s2.container(border=True):
                    st.write("❌ **Missing Skills**")
                    show_skills(result['missing_skills'], "missing")
                
                # Improvements
                with st.container(border=True):
                    st.subheader("📈 Actionable Tips")
                    for imp in result['improvements']:
                        st.markdown(f"• {imp}")

            except Exception as e:
                st.error(f"Error: {str(e)}")
            finally:
                if os.path.exists(tfile.name): os.remove(tfile.name)
    else:
        st.warning("⚠️ Please provide both a Resume and Job Description to continue.")
