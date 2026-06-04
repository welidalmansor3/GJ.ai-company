import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="GJ.AI | Great Job AI Company", page_icon="🚀", layout="wide")

# --- ÖZEL CSS TASARIMI (BEYAZ KURUMSAL TEMA) ---
st.markdown("""
<style>
    /* Genel Arka Plan ve Yazı Tipi (BEYAZ) */
    .main { background-color: #f8f9fa; color: #1f1f1f; font-family: 'Inter', sans-serif; }
    
    /* Streamlit'in çirkin üst barını ve alt yazısını gizle */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Başlıklar (KOYU) */
    h1, h2, h3 { color: #0d0d0d !important; font-weight: 800 !important; letter-spacing: -0.5px; }
    
    /* Butonlar (Mavi-Mor Gradient) */
    .stButton>button {
        background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
        color: white; border: none; padding: 14px 28px; font-size: 16px; font-weight: bold;
        border-radius: 12px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(37, 117, 252, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-3px); box-shadow: 0 8px 25px rgba(37, 117, 252, 0.4);
    }
    
    /* Kart Tasarımı (Beyaz, Hafif Gölgeli) */
    .card {
        background: #ffffff; padding: 30px; border-radius: 16px; 
        border: 1px solid #e2e8f0; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        transition: all 0.3s ease; height: 100%;
    }
    .card:hover {
        border: 1px solid #2575fc;
        box-shadow: 0 10px 15px rgba(37, 117, 252, 0.1);
        transform: translateY(-5px);
    }
    
    /* Status Badge */
    .badge-live { background-color: #10b981; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    .badge-dev { background-color: #f59e0b; color: black; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    
    /* Kurucu Kartları */
    .founder-card {
        background-color: #ffffff; padding: 30px; border-radius: 16px; text-align: center;
        border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Linkler */
    a { color: #2575fc !important; text-decoration: none; font-weight: 600; }
    a:hover { color: #6a11cb !important; }
    
    /* Ayırıcı Çizgi */
    hr { border: 1px solid #e2e8f0 !important; margin: 40px 0px; }
    
    /* Gri Alt Metin (Beyaz arka plana uygun koyu gri) */
    .subtext { color: #4a5568; font-size: 18px; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# --- LOGO VE ANA SAYFA (HERO SECTION) ---
LOGO_URL = "https://z-cdn-media.chatglm.cn/files/97efb701-480f-41e8-a54d-d828ce634224.jpeg?auth_key=1880000279-e3e53963895d4cb2b17766ad29dd2480-0-3f2ced5648a41f4923250c661dc275fd"

st.image(LOGO_URL, width=120)
st.markdown("<h1 style='font-size: 56px; margin-bottom: 0px;'>GJ.AI Company</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtext' style='font-size: 22px;'>Protecting Human Labor, Time & Data through Next-Gen Artificial Intelligence.</p>", unsafe_allow_html=True)

st.markdown("---")

# --- MENÜ / SEKMELER ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home & Vision", "🚀 Solutions", "🛡️ IP & Legal", "👤 Founders", "📞 Contact"])

# ==========================================
# TAB 1: HOME
# ==========================================
with tab1:
    st.markdown("## 🌍 Reshaping the Future of Work & AI")
    st.markdown("<p class='subtext'>GJ.AI is a multi-industry technology ecosystem designed to eliminate fraud, optimize logistics, and drastically reduce AI infrastructure costs globally.</p>", unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown("<div class='card'><h3>🛡️ Protection</h3><p class='subtext'>Shielding job seekers from Ghost Jobs and corporate fraud, ensuring their data and time are respected.</p></div>", unsafe_allow_html=True)
    with col_m2:
        st.markdown("<div class='card'><h3>🚛 Transparency</h3><p class='subtext'>Transforming logistics from cold point-tracking to transparent, driver-centric experiences.</p></div>", unsafe_allow_html=True)
    with col_m3:
        st.markdown("<div class='card'><h3>🧠 Optimization</h3><p class='subtext'>Making AI accessible by ending the Token Tax for morphologically rich languages (Turkish, Arabic, Hindi).</p></div>", unsafe_allow_html=True)

# ==========================================
# TAB 2: SOLUTIONS
# ==========================================
with tab2:
    st.markdown("## 🚀 Our Enterprise Solutions")
    st.markdown("<p class='subtext'>We build the engines. You integrate them. B2B API Licensing & On-Premise Solutions.</p>", unsafe_allow_html=True)
    
    # PROJE 1: GHOST JOB
    st.markdown("### 👻 EYE Ghost Job AI v2 <span class='badge-live'>LIVE</span>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
    **Purpose:** Protect job seekers from fake (Ghost) and fraudulent job postings, and match CVs to legitimate opportunities using our 4-Stage AI Pipeline.
    """)
    st.link_button("🔗 Access Live Platform", "https://eye-ghost-job-gj.streamlit.app/?count=0&unlock=true")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # PROJE 2: LOGISTICS
    st.markdown("### 🚛 EYE Logistics AI <span class='badge-dev'>UNDER DEVELOPMENT</span>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
    **Purpose:** Transform shipment tracking into a transparent, secure, and driver-honoring experience with real-time telemetry, AI risk analysis, and driver motivation systems.
    """)
    st.markdown("*Status: Core architecture complete. B2B API will be available soon.*")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")

    # PROJE 3: IQ.AI
    st.markdown("### 🧠 IQ.ai <span class='badge-dev'>UNDER DEVELOPMENT</span>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
    **Purpose:** End the "Token Tax". A multilingual optimization engine reducing LLM token consumption by 70-80% for Turkish, Arabic, and Hindi, alongside 4-bit Quantization.
    """)
    st.markdown("*Status: Tokenizer Lab active. Surgery Scripts being optimized for enterprise release.*")
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# TAB 3: IP & LEGAL
# ==========================================
with tab3:
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
# TAB 4: FOUNDERS
# ==========================================
with tab4:
    st.markdown("## 👥 Meet the Founders")
    st.markdown("<p class='subtext'>GJ.AI is built by visionary engineers dedicated to solving complex global problems through AI.</p>", unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.markdown("""
        <div class="founder-card">
            <h3>Welid Almansor</h3>
            <p style="color: #2575fc; font-weight: bold; font-size: 18px;">Founder & Chief Architect</p>
            <p style="color: #4a5568; text-align: left; margin-top: 20px;">Architect of the GJ.AI ecosystem. Welid designed the core AI pipelines, token optimization strategies, and B2B licensing models. He holds all IP and strategic direction for the company's future in global markets.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_f2:
        st.markdown("""
        <div class="founder-card">
            <h3>Hanna</h3>
            <p style="color: #2575fc; font-weight: bold; font-size: 18px;">Co-Founder & Lead Developer</p>
            <p style="color: #4a5568; text-align: left; margin-top: 20px;">Driving the technical execution and development of the GJ.AI platforms. Hanna ensures the seamless integration of AI models, user experience optimization, and robust infrastructure for enterprise partners.</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 5: CONTACT
# ==========================================
with tab5:
    st.markdown("## 📞 Contact & Business Inquiries")
    st.markdown("<p class='subtext'>For B2B API Licensing, Partnership Offers, or Legal Inquiries, please reach out to us directly.</p>", unsafe_allow_html=True)
    
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
    st.info("💡 **We do not apply for jobs; we offer partnerships.** \n\nWe provide our technology to companies via B2B API Licenses. Code is not for sale, but the engine is licensed. If you want to integrate our AI into your HR, Logistics, or AI infrastructure, contact us.")
