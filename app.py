import streamlit as st
import ollama
import json
import os
import pandas as pd
import re

# ===============================
# 1. PAGE CONFIG & STYLING
# ===============================
st.set_page_config(
    page_title="Teman Makan Tangsel | UAS",
    page_icon="🍴",
    layout="wide"
)

# CSS (Tetap sama dengan punyamu)
st.markdown("""
<style>
    .main { background-color: #f7f7f8; }
    [data-testid="stChatMessage"] { padding: 1.2rem; border-radius: 18px; margin-bottom: 12px; max-width: 80%; }
    [data-testid="stChatMessage"]:has(img[alt="user avatar"]) { 
        flex-direction: row-reverse; text-align: right; margin-left: auto; 
        background-color: #007bff; color: white; border-bottom-right-radius: 2px; 
    }
    [data-testid="stChatMessage"]:has(img[alt="assistant avatar"]) { 
        margin-right: auto; background-color: #ffffff; border: 1px solid #e5e5e5; 
        border-bottom-left-radius: 2px; color: #1a1a1a; 
    }
    .footer-text { 
        position: fixed; bottom: 10px; right: 20px; font-size: 11px; color: #999; 
        z-index: 100; background: rgba(255,255,255,0.8); padding: 5px 10px; border-radius: 10px; 
    }
</style>
<div class="footer-text">
    Lintangarif, Panji Arya, bayu dwi Kelompok 13 - ITTS
</div>
""", unsafe_allow_html=True)

# ===============================
# 2. DATA ENGINE (UPDATE KE chatbot9.json)
# ===============================
@st.cache_data
def load_data():
    path = "chatbot9.json"  
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

db = load_data()

# ===============================
# 3. ADMIN DASHBOARD
# ===============================
with st.sidebar:
    st.markdown("### **Admin Dashboard 🛠️**")
    st.write("---")
    if db:
        df = pd.DataFrame(db)
        st.metric("Total Restoran & Kafe", len(db))
        st.markdown("#### Sebaran Lokasi")
        st.bar_chart(df['area'].value_counts())
        
        with st.expander("Informasi Sistem"):
            st.write("• Model: Gemma 3 4B")
            st.write("• Data: chatbot9.json (Categorized)")
            st.write("• Engine: Ollama Local")
    
    st.write("---")
    if st.button("🗑️ Reset Riwayat Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ===============================
# 4. CHAT INTERFACE
# ===============================
st.title("🍴 Teman Makan Tangsel")
st.caption("Chatbot Rekomendasi Kuliner Terpercaya - Project UAS Informatika ITTS")
st.write("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ===============================
# 5. SEARCH ENGINE (OPTIMASI KEYWORDS BARU)
# ===============================
if user_input := st.chat_input("Kamu lagi pengen makan apa hari ini?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    q = user_input.lower().strip()
    is_greeting = q in ["halo", "hi", "p", "siang", "pagi", "malam"] and len(q.split()) == 1
    is_asking_list = any(x in q for x in ["list", "daftar", "banyak", "rekomendasi"])
    
    # Filter Budget (Regex)
    nums = re.findall(r'\d+', q.replace('.', ''))
    budget = int(nums[0]) if nums else None
    if budget and budget < 1000: budget *= 1000

    matches = []
    if not is_greeting:
        stopwords = ["di","ke","ada","dong","yang","cari","budget","harga","ribu","ga","under","aku","kamu"]
        keywords = [w for w in q.split() if w not in stopwords and len(w) > 2]

        for r in db:
            score = 0
            # Ambil data klasifikasi baru
            klasifikasi = r.get("klasifikasi", {})
            tag_label = klasifikasi.get("tag", "").lower()
            keywords_list = " ".join(klasifikasi.get("search_keywords", [])).lower()

            # Data Pool lama + Data baru (klasifikasi & keywords)
            pool = f"{r.get('name','')} {r.get('category','')} {r.get('area','')} {' '.join(r.get('tags', []))} {r.get('special_feature','')} {tag_label} {keywords_list}".lower()
            
            # Skor Bobot Relevansi
            if q in pool: score += 50 
            
            # Cek kecocokan di keywords baru (Alias)
            for kw in keywords:
                if kw in tag_label: score += 40  #
                if kw in keywords_list: score += 30 #
                if kw in r.get("category","").lower(): score += 20
                if kw in r.get("name","").lower(): score += 15
                if kw in pool: score += 5
            
            # Filter Budget Strict (Tetap dipertahankan)
            if budget:
                price_str = r.get("Price", "0").split('-')[0]
                price_val = int(re.sub(r'[^\d]', '', price_str))
                if price_val > budget:
                    score = 0
                else:
                    score += 25

            if score >= 15:
                matches.append((score, r))

        matches.sort(key=lambda x: (x[0], x[1].get('rating', 0)), reverse=True)
        limit = 10 if is_asking_list else 4
        top = [x[1] for x in matches[:limit]]
    else:
        top = []

    # ===============================
    # 6. RAKIT CONTEXT & CALL AI
    # ===============================
    context_data = ""
    if is_greeting:
        STATUS_CODE = "GREETING"
    elif top:
        STATUS_CODE = "ADA_DATA"
        context_data = "GUNAKAN DATA VALID INI:\n"
        for r in top:
            # Tambahkan info kategori
            tag_info = r.get('klasifikasi', {}).get('tag', 'Menengah')
            context_data += f"- {r['name']} ({tag_info}) | Rating: {r.get('rating')} | Alamat: {r['address']} | Harga: {r['Price']} | Review: {r['special_feature']}\n"
    else:
        STATUS_CODE = "KOSONG"

    system_prompt = f"""
    Kamu adalah 'Teman Makan Tangsel'. Kamu adalah asisten kuliner yang sopan, ramah, dan membantu.
    Gunakan panggilan 'Aku' dan 'Kamu' dalam percakapan.

    STATUS SISTEM: {STATUS_CODE}

    ATURAN JAWAB:
    1. GREETING: Sapa balik dengan ramah.
    2. ADA_DATA: Berikan rekomendasi berdasarkan DATA VALID. Sebutkan Nama, Kategori Harga, Rating, dan Alamatnya.
    3. KOSONG: Jujur kalau data tidak ada. JANGAN NGARANG.
    
    DATABASE:
    {context_data}
    """

    with st.chat_message("assistant"):
        with st.spinner("Aku lagi cari datanya ya..."):
            try:
                res = ollama.chat(
                    model="gemma3:4b", # Sesuaikan dengan model ollama
                    messages=[
                        {"role":"system","content":system_prompt},
                        {"role":"user","content":user_input}
                    ],
                    options={"temperature": 0}
                )
                answer = res["message"]["content"]
                st.markdown(answer)
                st.session_state.messages.append({"role":"assistant","content":answer})
            except Exception as e:
                st.error(f"Gagal terhubung ke AI: {e}")
