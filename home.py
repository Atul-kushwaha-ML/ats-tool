

import streamlit as st
 

 
FEATURES = [
    ("📄 Resume Analysis",
     "Upload your resume in PDF format and receive a detailed ATS "
     "compatibility report with professional recommendations."),
    ("🎯 Job Description Match",
     "Compare your resume against any job description and identify "
     "keyword gaps, missing skills and improvement areas."),
    ("🤖 AI Suggestions",
     "Receive intelligent feedback to improve formatting, content "
     "quality, ATS score and recruiter readability."),
]
 

 
STEPS = [
    ("① Upload Resume",
     "Upload your latest resume in PDF format. The application "
     "securely extracts the important information for analysis."),
    ("② Paste Job Description",
     "Copy the target job description and compare it with your "
     "resume to identify missing keywords and skills."),
    ("③ Get AI Report",
     "Receive ATS score, match percentage, missing skills, "
     "strengths and actionable improvement suggestions."),
]
 
BENEFITS_LEFT = [
    "✅ Improve ATS Score",
    "✅ Detect Missing Keywords",
    "✅ Resume Formatting Review",
    "✅ Professional AI Suggestions",
    "✅ Better Resume Quality",
]
 
BENEFITS_RIGHT = [
    "📌 Compare with Job Description",
    "📌 Find Skill Gaps",
    "📌 Recruiter Friendly Report",
    "📌 Increase Shortlisting Chances",
    "📌 Easy to Use Interface",
]
 

CSS = """
<style>
#MainMenu, header, footer { visibility: hidden; }
 
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    max-width: 1200px;
}
 
.hero {
    background: linear-gradient(135deg, #2563eb, #1d4ed8, #0f172a);
    padding: 80px 50px;
    border-radius: 25px;
    color: white;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0px 20px 40px rgba(0, 0, 0, .15);
}
 
.hero h1 {
    font-size: 58px;
    font-weight: 800;
    margin-bottom: 15px;
}
 
.hero p {
    font-size: 22px;
    line-height: 1.7;
    color: #e2e8f0;
    max-width: 850px;
    margin: auto;
}
 
.section-title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-top: 70px;
    margin-bottom: 40px;
}
 
.card {
    background: white;
    padding: 35px;
    border-radius: 18px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 10px 25px rgba(0, 0, 0, .06);
    transition: .3s;
    min-height: 270px;
}
 
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 20px 35px rgba(0, 0, 0, .12);
}
 
.card h3 { color: #2563eb; margin-bottom: 20px; }
 
.stats {
    background: #f8fafc;
    padding: 30px;
    border-radius: 20px;
    margin-top: 70px;
}
 
.stat-box { text-align: center; padding: 20px; }
.stat-number { font-size: 42px; font-weight: bold; color: #2563eb; }
.stat-title { font-size: 18px; color: #475569; }
</style>
"""
 
 
# ---------------------------------------------------------
# Small reusable render helpers
# ---------------------------------------------------------
 
def _card(title: str, body: str) -> None:
    st.markdown(
        f'<div class="card"><h3>{title}</h3><p>{body}</p></div>',
        unsafe_allow_html=True,
    )
 
 
def _stat(number: str, title: str) -> None:
    st.markdown(
        f'<div class="stat-box"><div class="stat-number">{number}</div>'
        f'<div class="stat-title">{title}</div></div>',
        unsafe_allow_html=True,
    )
 
 
def _hero(title: str, body: str) -> None:
    st.markdown(
        f'<div class="hero"><h1>{title}</h1><p>{body}</p></div>',
        unsafe_allow_html=True,
    )
 
 
def _section_title(text: str) -> None:
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)
 
 
def _cta_button(label: str, key: str | None = None) -> None:
    _, center, _ = st.columns([1, 2, 1])
    with center:
        if st.button(label, key=key, use_container_width=True, type="primary"):
            st.session_state.page = "analyzer"
            st.rerun()
 
 
def _cards_row(items: list[tuple[str, str]]) -> None:
    for col, (title, body) in zip(st.columns(len(items)), items):
        with col:
            _card(title, body)
 
 
# ---------------------------------------------------------
# Main page
# ---------------------------------------------------------
 
def render_home() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
 
    # Hero
    _hero(
        "📄 AI ATS Resume Analyzer",
        "Improve your resume, compare it with any job description, "
        "discover missing skills, receive professional recommendations "
        "and maximize your chances of getting shortlisted.",
    )
    st.write("")
    _cta_button("🚀 Analyze Resume", key="top_button")
    st.write("")
    st.write("")
 
    # Features
    _section_title("✨ Powerful Features")
    _cards_row(FEATURES)
    st.write("")
    st.write("")
 
   
 
    # How it works
    _section_title("⚙️ How It Works")
    _cards_row(STEPS)
    st.write("")
    st.write("")
 
    # Benefits
    _section_title("💡 Why Choose Our ATS Analyzer?")
    b1, b2 = st.columns(2)
    with b1:
        for text in BENEFITS_LEFT:
            st.success(text)
    with b2:
        for text in BENEFITS_RIGHT:
            st.info(text)
    st.write("")
    st.write("")

 
    # CTA
    _section_title("🚀 Ready to Improve Your Resume?")
    _hero(
        "Boost Your ATS Score Today",
        "Upload your resume and receive an AI-powered analysis with "
        "keyword matching, skill gap detection, ATS compatibility, "
        "and practical improvement suggestions.",
    )
    st.write("")
    _cta_button("🚀 Start Resume Analysis", key="bottom_button")
    st.write("")
    st.write("")
 
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <center>
        <h4>AI ATS Resume Analyzer</h4>
        <p>Helping job seekers create ATS-friendly resumes with
        intelligent analysis and actionable insights.</p>
        <p>© 2026 AI ATS Resume Analyzer • Built with Streamlit</p>
        </center>
        """,
        unsafe_allow_html=True,
    )