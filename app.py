import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="GJ.AI Company", page_icon="🚀", layout="wide")

# --- CSS TASARIMI (Karanlık ve Profesyonel) ---
st.markdown("""
<style>
    .main { background-color: #0e1117; color: #ffffff; }
    h1, h2, h3, h4 { color: #ffffff !important; }
    .stButton>button {
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white; border: none; padding: 12px 24px; font-size: 16px; font-weight: bold;
        border-radius: 8px; transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: translateY(-2px); box-shadow: 0 8px 15px rgba(37, 117, 252, 0.3);
    }
    .card {
        background-color: #1e2028; padding: 25px; border-radius: 12px; 
        border: 1px solid #333333; box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        height: 100%;
    }
    .founder-card {
        background-color: #161b22; padding: 20px; border-radius: 10px; text-align: center;
        border: 1px solid #30363d;
    }
    hr { border: 1px solid #333333 !important; }
    a { color: #2575fc !important; text-decoration: none; }
    a:hover { color: #6a11cb !important; }
</style>
""", unsafe_allow_html=True)

# --- LOGO VE ANA BAŞLIK ---
LOGO_URL = "https://z-cdn-media.chatglm.cn/files/97efb701-480f-41e8-a54d-d828ce634224.jpeg?auth_key=1880000279-e3e53963895d4cb2b17766ad29dd2480-0-3f2ced5648a41f4923250c661dc275fd"

col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image(LOGO_URL, width=120)
with col_title:
    st.markdown("<h1 style='margin-bottom:0; padding-top: 20px;'>GJ.AI (Great Job AI) Company</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px; color: #aaaaaa;'>Protecting Human Labor, Time & Data through Artificial Intelligence.</p>", unsafe_allow_html=True)

st.markdown("---")

# --- MENÜ / SEKMELER ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "🛡️ IP & Legal Rights", "🚀 Solutions", "👤 Founders", "📞 Contact"])

# ==========================================
# TAB 1: HOME
# ==========================================
with tab1:
    st.markdown("## 🌍 Our Vision")
    st.markdown("""
    Welcome to **GJ.AI Company**. We are a next-generation technology and artificial intelligence ecosystem dedicated to solving real-world problems. 
    Our core mission is to protect human labor from fraudulent systems, secure logistics infrastructures, and break down language barriers in AI by ending the "Token Tax" for morphologically rich languages.
    """)
    
    st.markdown("## 🎯 Our Mission")
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown("<div class='card'><h3>🛡️ Protection</h3><p>Shielding job seekers from Ghost Jobs and scams, ensuring their data and time are respected.</p></div>", unsafe_allow_html=True)
    with col_m2:
        st.markdown("<div class='card'><h3>🚛 Transparency</h3><p>Transforming logistics from cold tracking to transparent, driver-centric experiences.</p></div>", unsafe_allow_html=True)
    with col_m3:
        st.markdown("<div class='card'><h3>🧠 Optimization</h3><p>Making AI accessible globally by reducing LLM token costs by 70-80% for non-English languages.</p></div>", unsafe_allow_html=True)

# ==========================================
# TAB 2: IP & LEGAL RIGHTS
# ==========================================
with tab2:
    st.markdown("## ⚖️ Intellectual Property & Legal Rights")
    st.warning("⚠️ **Strictly Enforced Policies. Read carefully before using any of our platforms.**")
    
    st.markdown("""
    **1. Copyrights & Ownership**
    All algorithms, software code, AI pipelines (including the 4-Stage Ghost Job Pipeline and Unigram Tokenization architecture), user interfaces, and underlying technologies are the exclusive intellectual property (IP) of **Welid Almansor** and **GJ.AI (Great Job AI) Company**. All rights are strictly reserved.

    **2. Trademark & Logo Protection**
    The GJ.AI logo (Blue-Purple gradient eye icon + "GJ AI" text) is a registered trademark of GJ.AI Company. 
    - **Prohibition:** Any unauthorized use, reproduction, distribution, or modification of the logo or brand name in any context is strictly prohibited.
    - **Legal Action:** GJ.AI reserves the full legal right to open a lawsuit and take immediate legal action against any individual or entity that uses the logo or brand without explicit written permission.

    **3. Code & Technology Licensing**
    We do not sell source code. We license our technology. B2B API integrations and enterprise solutions are provided under strict licensing agreements. Reverse engineering, redistributing, or copying our AI mechanics is a direct violation of our IP rights.

    **4. Data Privacy (GDPR/KVKK Compliant)**
    - **EYE Ghost Job AI:** CVs and job postings are processed for real-time analysis and are NOT permanently stored on our servers.
    - **EYE Logistics AI:** Driver locations are anonymized during off-duty hours.
    - **IQ.ai:** Trained tokenizer models are temporarily hosted; users must download them. We retain zero corporate data.

    **5. Terms of Access**
    Accessing our platforms (via web or API) constitutes acceptance of these terms. If you do not agree, you must immediately cease using our services.
    """)

# ==========================================
# TAB 3: SOLUTIONS
# ==========================================
with tab3:
    st.markdown("## 🚀 Our Solutions & Products")
    
    # PROJE 1: GHOST JOB
    st.markdown("### 👻 EYE Ghost Job AI v2 - *Live*")
    st.markdown("""
    **Purpose:** Protect job seekers from fake (Ghost) and fraudulent job postings, and optimally match CVs to legitimate opportunities.
    """)
    st.link_button("🔗 Access Live Platform", "https://eye-ghost-job-gj.streamlit.app/?count=0&unlock=true")
    st.markdown("- **Features:** 4-Stage AI Pipeline, Risk Scoring, External Evidence Evaluation, CV Match Engine.")
    st.markdown("---")
    
    # PROJE 2: LOGISTICS
    st.markdown("### 🚛 EYE Logistics AI - *Under Development*")
    st.markdown("""
    **Purpose:** Transform shipment tracking into a transparent, secure, and driver-honoring experience with real-time telemetry and AI risk analysis.
    """)
    st.info("🚧 **Status:** Currently in the active development and testing phase. B2B API will be available soon.")
    st.markdown("---")

    # PROJE 3: IQ.AI
    st.markdown("### 🧠 IQ.ai - *Under Development*")
    st.markdown("""
    **Purpose:** End the "Token Tax" for Turkish, Arabic, and Hindi. A multilingual optimization engine that reduces LLM token consumption by 70-80% and shrinks model sizes via 4-bit Quantization.
    """)
    st.info("🚧 **Status:** Core engine developed. Tokenizer Lab and Surgery Scripts are being optimized for enterprise release.")
    st.markdown("---")

# ==========================================
# TAB 4: FOUNDERS
# ==========================================
with tab4:
    st.markdown("## 👥 Meet the Founders")
    st.markdown("GJ.AI is built by visionary engineers dedicated to solving complex global problems.")
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("""
        <div class="founder-card">
            <h3>Welid Almansor</h3>
            <p style="color: #2575fc; font-weight: bold;">Founder & Chief Architect</p>
            <p>Architect of the GJ.AI ecosystem. Welid designed the core AI pipelines, token optimization strategies, and B2B licensing models. He holds all IP and strategic direction for the company's future in global markets.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_f2:
        st.markdown("""
        <div class="founder-card">
            <h3>Hanna</h3>
            <p style="color: #2575fc; font-weight: bold;">Co-Founder & Lead Developer</p>
            <p>Driving the technical execution and development of the GJ.AI platforms. Hanna ensures the seamless integration of AI models, user experience optimization, and robust infrastructure for our enterprise partners.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 5: CONTACT
# ==========================================
with tab5:
    st.markdown("## 📞 Contact & Business Inquiries")
    st.markdown("For B2B API Licensing, Partnership Offers, or Legal Inquiries, please reach out to us directly.")
    
    st.markdown("---")
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        st.markdown("### 📧 Email Addresses")
        st.markdown("- **Founder Direct:** velitgone31@gmail.com")
        st.markdown("- **Corporate (Zoho):** founder@eyeghostjob.ai")
        st.markdown("- **Support & Feedback:** doktorv333@gmail.com")
    
    with col_c2:
        st.markdown("### 🌐 Links")
        st.markdown("- **Live Demo:** [Ghost Job AI Platform](https://eye-ghost-job-gj.streamlit.app/?count=0&unlock=true)")
        st.markdown("- **Portfolio:** eyeghostjobai.carrd.co")
        
    st.markdown("---")
    st.markdown("### 🤝 Partnership Model")
    st.info("💡 **We do not apply for jobs; we offer partnerships.** \n\nWe provide our technology to companies via B2B API Licenses. Code is not for sale, but the engine is licensed. If you want to integrate our AI into your HR or Logistics platform, contact us.")