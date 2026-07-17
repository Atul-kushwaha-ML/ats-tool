# import streamlit as st
# import os
# import tempfile
# from pipeline.pipeline import ATSPipeline

# # UI Setup
# st.set_page_config(page_title="AI ATS Analyzer", page_icon="🎯", layout="wide")

# # Initialize Pipeline (Cache for performance)
# @st.cache_resource
# def get_pipeline():
#     return ATSPipeline()

# pipeline = get_pipeline()

# # Title and Layout
# st.title("🎯 AI ATS Resume Analyzer")
# st.markdown("Upload your resume and get instant feedback.")

# # Inputs
# col1, col2 = st.columns([1, 1])

# with col1:
#     uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# with col2:
#     job_description = st.text_area("Paste Job Description here...", height=150)

# # Execution
# if st.button("Analyze Resume", type="primary"):
#     if uploaded_file and job_description:
#         with st.spinner("Analyzing..."):
#             # 1. Create temporary file (Compatible with Windows/Linux)
#             suffix = os.path.splitext(uploaded_file.name)[1]
#             tfile = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
#             tfile.write(uploaded_file.getbuffer())
#             tfile.close() # Close file so the parser can read it
#             tmp_path = tfile.name
            
#             try:
#                 # 2. Logic Call
#                 result = pipeline.analyze(tmp_path, job_description)
                
#                 # 3. Results Section
#                 st.success("Analysis Complete!")
                
#                 # Metrics
#                 m1, m2 = st.columns(2)
#                 m1.metric("ATS Score", result['ats_score'])
#                 m2.metric("Match Percentage", f"{result['match_percentage']}%")
                
#                 # Summary
#                 st.write("### Executive Summary")
#                 st.info(result['summary'])
                
#                 # Lists
#                 c1, c2 = st.columns(2)
#                 with c1:
#                     st.write("✅ **Matched Skills**")
#                     st.write(", ".join(result['matched_skills']))
#                 with c2:
#                     st.write("❌ **Missing Skills**")
#                     st.write(", ".join(result['missing_skills']))

#                 # Recommendations
#                 st.write("### 📈 Actionable Improvements")
#                 for imp in result['improvements']:
#                     st.write(f"- {imp}")
                    
#             except Exception as e:
#                 st.error(f"Error occurred: {str(e)}")
            
#             finally:
#                 # 4. Cleanup: Delete the temp file after processing
#                 if os.path.exists(tmp_path):
#                     os.remove(tmp_path)
#     else:
#         st.warning("Please upload a file and enter a job description.")




# import streamlit as st
# import os
# import tempfile
# from pipeline.pipeline import ATSPipeline

# # 1. Custom CSS for Premium Look
# st.set_page_config(page_title="AI ATS Analyzer", page_icon="🎯", layout="wide")

# st.markdown("""
#     <style>
#     .stApp { background-color: #f8f9fa; }
#     .stMetric { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
#     .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
#     </style>
# """, unsafe_allow_html=True)

# @st.cache_resource
# def get_pipeline():
#     return ATSPipeline()

# pipeline = get_pipeline()

# # 2. Sidebar Layout
# with st.sidebar:
#     st.header("Upload & Configure")
#     uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])
#     job_description = st.text_area("📋 Job Description", height=200, placeholder="Paste JD here...")
#     analyze_btn = st.button("🚀 Analyze Resume", type="primary")

# # Main Area
# st.title("🎯 AI ATS Resume Analyzer")
# st.write("---")

# if analyze_btn:
#     if uploaded_file and job_description:
#         with st.spinner("Processing your profile..."):
#             suffix = os.path.splitext(uploaded_file.name)[1]
#             tfile = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
#             tfile.write(uploaded_file.getbuffer())
#             tfile.close()
            
#             try:
#                 result = pipeline.analyze(tfile.name, job_description)
                
#                 # 3. Visual Metrics
#                 col1, col2 = st.columns(2)
#                 col1.metric("ATS Score", f"{result['ats_score']}/100")
#                 col2.metric("Match Rate", f"{result['match_percentage']}%")
                
#                 st.progress(result['match_percentage'] / 100) # Progress Bar visual

#                 # 4. Tabbed Interface for clean UX
#                 tab1, tab2, tab3 = st.tabs(["📋 Summary", "⚡ Skills Analysis", "🛠️ Actionable Tips"])
                
#                 with tab1:
#                     st.info(result['summary'])
                
#                 with tab2:
#                     c1, c2 = st.columns(2)
#                     c1.success("✅ Matched: " + ", ".join(result['matched_skills']))
#                     c2.error("❌ Missing: " + ", ".join(result['missing_skills']))
                
#                 with tab3:
#                     for imp in result['improvements']:
#                         st.markdown(f"- **{imp}**")

#             except Exception as e:
#                 st.error(f"Analysis failed: {str(e)}")
#             finally:
#                 if os.path.exists(tfile.name): os.remove(tfile.name)
#     else:
#         st.warning("Please upload a file and fill the Job Description first.")
# else:
#     # Default Welcome State
#     st.markdown("### Welcome to the future of Job Hunting")
#     st.write("Upload your resume and the Job Description to get started with our AI-powered analysis.")




# import streamlit as st
# import os
# import tempfile
# from pipeline.pipeline import ATSPipeline

# # 1. Page Config
# st.set_page_config(page_title="AI ATS Analyzer", page_icon="🎯", layout="wide")

# # 2. Custom CSS for "Design Lining" and "Pill Badges"
# st.markdown("""
#     <style>
#     .skill-pill { display: inline-block; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; margin: 3px; font-weight: 500; }
#     .matched { background-color: #d1fae5; color: #065f46; border: 1px solid #34d399; }
#     .missing { background-color: #fee2e2; color: #991b1b; border: 1px solid #f87171; }
#     </style>
# """, unsafe_allow_html=True)

# # Helper function to create skill badges
# def show_skills(skills, type):
#     color_class = "matched" if type == "match" else "missing"
#     for skill in skills:
#         st.markdown(f'<span class="skill-pill {color_class}">{skill}</span>', unsafe_allow_html=True)

# @st.cache_resource
# def get_pipeline():
#     return ATSPipeline()

# pipeline = get_pipeline()

# # --- Sidebar UI ---
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     uploaded_file = st.file_uploader("📂 Upload Resume", type=["pdf", "docx"])
#     job_description = st.text_area("📝 Job Description", height=250, placeholder="Enter target JD here...")
#     analyze_btn = st.button("🚀 Analyze Resume", type="primary", use_container_width=True)

# # --- Main Content UI ---
# st.title("🎯 AI ATS Resume Analyzer")
# st.markdown("Professional analysis for your career path.")
# st.divider() # <-- Design lining element

# if analyze_btn:
#     if uploaded_file and job_description:
#         with st.spinner("Analyzing..."):
#             suffix = os.path.splitext(uploaded_file.name)[1]
#             tfile = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
#             tfile.write(uploaded_file.getbuffer())
#             tfile.close()
            
#             try:
#                 result = pipeline.analyze(tfile.name, job_description)
                
#                 # Metrics in Lined Containers
#                 c1, c2 = st.columns(2)
#                 with c1.container(border=True): # <-- Lining
#                     st.metric("ATS Score", f"{result['ats_score']}/100")
#                 with c2.container(border=True): # <-- Lining
#                     st.metric("Match Percentage", f"{result['match_percentage']}%")
                
#                 # Executive Summary
#                 with st.container(border=True): # <-- Lining
#                     st.subheader("📝 Executive Summary")
#                     st.write(result['summary'])
                
#                 # Skills Analysis
#                 st.subheader("💡 Skills Gap Analysis")
#                 s1, s2 = st.columns(2)
#                 with s1.container(border=True): # <-- Lining
#                     st.write("✅ **Matched Skills**")
#                     show_skills(result['matched_skills'], "match")
#                 with s2.container(border=True): # <-- Lining
#                     st.write("❌ **Missing Skills**")
#                     show_skills(result['missing_skills'], "missing")
                
#                 # Improvements
#                 with st.container(border=True): # <-- Lining
#                     st.subheader("📈 Actionable Improvements")
#                     for imp in result['improvements']:
#                         st.markdown(f"• {imp}")

#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#             finally:
#                 if os.path.exists(tfile.name): os.remove(tfile.name)
#     else:
#         st.warning("⚠️ Please provide both a Resume and Job Description.")
# else:
#     # Empty State with better lining
#     with st.container(border=True):
#         st.info("👈 Use the sidebar to upload your documents and start the analysis.")







import streamlit as st
import os
import tempfile
from pipeline.pipeline import ATSPipeline

# 1. Page Config
st.set_page_config(page_title="AI ATS Analyzer", page_icon="🎯", layout="centered")

# 2. Custom CSS for Light, Clean & Professional Look
st.markdown("""
    <style>
    /* Global Background */
    .stApp { background-color: #ffffff; }
    
    /* Input Card Styling */
    .input-card { 
        background: #f8fafc; 
        padding: 2rem; 
        border-radius: 20px; 
        border: 1px solid #e2e8f0;
        margin-bottom: 2rem;
    }
    
    /* Skill Pills */
    .skill-pill { display: inline-block; padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; margin: 4px; font-weight: 500; }
    .matched { background-color: #d1fae5; color: #065f46; border: 1px solid #34d399; }
    .missing { background-color: #fee2e2; color: #991b1b; border: 1px solid #f87171; }
    
    /* Metric Cards */
    [data-testid="stMetricValue"] { font-size: 2rem !important; }
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
        # Spacer to align textarea with uploader
        st.write("") 
        job_description = st.text_area("📝 Job Description", height=80, placeholder="Paste JD here...")
    
    analyze_btn = st.button("🚀 Analyze My Resume", type="primary", use_container_width=True)
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
                
                # Metrics (Clean Lined Containers)
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