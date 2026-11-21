import streamlit as st
import os
from dotenv import load_dotenv
from sentinel_agent import SparkSentinelEngine

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Mr. Spark | Elite DevOps Sentinel",
    page_icon="⚡",
    layout="wide"
)

# Custom Cyberpunk / Yellow-Black Theme with Perfect Vertical Alignment
st.markdown("""
    <style>
    /* Main App Background & Font Styling */
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    
    /* Perfect Center Alignment Container for Pikachu & Header */
    .hero-box {
        display: flex;
        align-items: center;
        gap: 20px;
        background: linear-gradient(135deg, #121824 0%, #1a1f2c 100%);
        padding: 20px 30px;
        border-radius: 16px;
        border: 2px solid rgba(255, 215, 0, 0.3);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        margin-bottom: 25px;
    }
    
    .main-header { 
        font-size: 2.6rem; 
        font-weight: 800; 
        color: #ffffff; 
        display: inline-flex;
        align-items: center;
        letter-spacing: -0.5px;
        margin: 0;
        line-height: 1.2;
    }
    
    .highlight-name {
        color: #ffd700;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
    }
    
    .sub-text { 
        color: #9ca3af; 
        font-size: 1.15rem; 
        margin-top: 5px;
        margin-bottom: 25px;
    }

    /* Custom Text Area Styling */
    .stTextArea textarea {
        background-color: #121824 !important;
        color: #ffd700 !important;
        border: 1px solid #374151 !important;
        border-radius: 10px !important;
        font-family: 'Courier New', monospace;
    }
    .stTextArea textarea:focus {
        border-color: #ffd700 !important;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.3) !important;
    }

    /* Super Cool Glow Buttons with Hover & Shine Effect */
    .stButton button {
        background: linear-gradient(135deg, #ffd700 0%, #ffaa00 100%) !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.2);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.6), 0 0 10px rgba(255, 255, 255, 0.4) !important;
        background: linear-gradient(135deg, #ffea00 0%, #ffc107 100%) !important;
    }

    /* Sidebar Theming */
    [data-testid="stSidebar"] {
        background-color: #07090e;
        border-right: 1px solid #1f2937;
    }
    
    [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label {
        color: #ffd700 !important;
        font-weight: 600;
    }

    [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: #121824 !important;
        border-color: #374151 !important;
        color: #ffd700 !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stSidebar"] input {
        background-color: #121824 !important;
        color: #ffd700 !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stMetric"] {
        background-color: #121824;
        border: 1px solid #1f2937;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Perfectly Aligned Header Box with Pikachu & Title
st.markdown("""
    <div class="hero-box">
        <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/25.gif" width="85" style="vertical-align: middle;" />
        <div>
            <h1 class="main-header">Meet <span class="highlight-name">&nbsp;Mr. Spark</span></h1>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<p class="sub-text">Your elite autonomous DevOps sentinel for deep security audits, code optimization, and instant architecture docs.</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar Configuration
st.sidebar.header("⚙️ Mr. Spark Config")
model_choice = st.sidebar.selectbox("Select Intelligence Core", ["openai/gpt-4o", "openai/gpt-4o-mini"])
repo_name_input = st.sidebar.text_input("Repository Target", "mr-spark-sentinel-core")

# Initialize Engine
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ OPENAI_API_KEY is missing in your .env file! Please add it and restart.")

engine = SparkSentinelEngine(model=model_choice)

# Main Code Input Area
st.subheader("📝 Source Code Ingestion Panel")
default_code = '''# Example target code for Mr. Spark inspection
import os

API_KEY = "sk-proj-fakeapikey1234567890"  # Critical secret exposure vulnerability

def authenticate_user(username, password):
    # Vulnerable direct string interpolation query pattern
    query = f"SELECT * FROM accounts WHERE user = '{username}' AND pass = '{password}'"
    print("Executing query:", query)
    return True

def process_metrics(data_list):
    total = 0
    for i in range(len(data_list)):
        total += data_list[i]['val']
    return total
'''

code_input = st.text_area("Paste code repository snippet below:", value=default_code, height=220)

if st.button("⚡ Initialize Mr. Spark Pipeline", type="primary"):
    if not code_input.strip():
        st.warning("Please provide code input for Mr. Spark to analyze.")
    else:
        with st.status("🤖 Mr. Spark subsystems engaging...", expanded=True) as status:
            
            # Agent 1: Security
            st.write("🔒 Deploying Security & Vulnerability Auditor Agent...")
            sec_report = engine.run_security_agent(code_input)
            
            # Agent 2: Quality
            st.write("⚡ Deploying Code Quality & Performance Optimization Agent...")
            qual_report = engine.run_quality_agent(code_input)
            
            # Agent 3: Docs
            st.write("📚 Deploying Technical Writer & Documentation Sentinel...")
            docs_report = engine.run_docs_agent(code_input, repo_name=repo_name_input)
            
            status.update(label="✨ Mr. Spark Pipeline Executed Successfully!", state="complete", expanded=False)

        # Display Results in Modern Styled Tabs
        tab1, tab2, tab3 = st.tabs(["🔒 Security Audit Report", "⚡ Quality & Refactoring", "📚 Generated Documentation"])

        with tab1:
            st.subheader(f"Security Index Score: {sec_report.security_score}/100")
            st.info(sec_report.summary)
            
            if sec_report.vulnerabilities:
                st.write("### 🚨 Detected Vulnerabilities")
                for idx, v in enumerate(sec_report.vulnerabilities, 1):
                    severity_color = "🔴" if v.severity == "HIGH" else "🟡" if v.severity == "MEDIUM" else "🟢"
                    with st.expander(f"{severity_color} [{v.severity}] {v.vulnerability_type}"):
                        st.write(f"**Description:** {v.description}")
                        st.write(f"**Recommendation:** {v.recommendation}")
            else:
                st.success("No security vulnerabilities detected!")

        with tab2:
            st.subheader(f"Code Quality Index: {qual_report.code_quality_score}/100")
            if qual_report.issues:
                st.write("### ⚠️ Performance & Architecture Issues")
                for idx, issue in enumerate(qual_report.issues, 1):
                    with st.expander(f"Issue {idx}: {issue.issue_type} (Section: `{issue.line_or_section}`)"):
                        st.write(f"**Explanation:** {issue.explanation}")
                        st.write(f"**Suggested Fix:** {issue.suggested_fix}")
            
            st.write("### ✨ Optimized Code Preview")
            st.code(qual_report.refactored_code_snippet, language="python")

        with tab3:
            st.subheader(f"Generated README for: {docs_report.project_title}")
            st.markdown(docs_report.readme_markdown)
            
            st.markdown("---")
            st.subheader("📦 Release Changelog Entry")
            st.code(docs_report.changelog_entry, language="markdown")