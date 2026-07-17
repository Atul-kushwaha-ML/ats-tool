import streamlit as st
import os
import tempfile
from pipeline.pipeline import ATSPipeline

# 1. Page Config
st.set_page_config(page_title="AI ATS Analyzer", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    /* 1. HIDE ALL STREAMLIT SYSTEM UI */
    #MainMenu, footer, header, .stDeployButton {visibility: hidden !important; display: none !important;}
    
    /* 2. PAGE BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background-color: #fcfcfd !important;
    }

    /* 3. INPUT CARD (Modern Glassmorphism-ish Card) */
    .input-card { 
        background: #ffffff !important; 
        padding: 2.5rem !important; 
        border-radius: 24px !important; 
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 2rem !important;
    }

    /* 4. BUTTON STYLING */
    div.stButton > button {
        background-color: #2563eb !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        background-color: #1d4ed8 !important;
        transform: translateY(-2px);
    }

    /* 5. METRIC CARDS & HEADERS */
    [data-testid="stMetricValue"] { font-size: 2.5rem !important; color: #1e293b !important; }
    h1, h2, h3 { color: #0f172a !important; font-weight: 700 !important; }

    /* 6. SKILL PILLS IMPROVEMENT */
    .skill-pill { 
        display: inline-block; 
        padding: 8px 16px; 
        border-radius: 12px; 
        font-size: 0.85rem; 
        margin: 5px; 
        font-weight: 600; 
        text-transform: capitalize;
    }
    .matched { background-color: #f0fdf4 !important; color: #166534 !important; border: 1px solid #bbf7d0 !important; }
    .missing { background-color: #fef2f2 !important; color: #991b1b !important; border: 1px solid #fecaca !important; }
    
    /* 7. CONTAINER BORDER RADIUS */
    [data-testid="stVerticalBlock"] > [style*="border:"] {
        border-radius: 20px !important;
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
