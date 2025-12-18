import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="BMI Ceria & Sehat",
    page_icon="🧸", # Icon diganti jadi lebih lucu
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS (Background Kartun & Glassmorphism Kuat)
st.markdown("""
    <style>
    /* --- BAGIAN BACKGROUND KARTUN --- */
    /* Target container utama Streamlit */
    [data-testid="stAppViewContainer"] {
        /* GANTI URL INI dengan link gambar kartun lain jika mau */
        background-image: url("https://img.freepik.com/free-vector/hand-drawn-flat-design-landscape-background_23-2149286523.jpg?w=1380&t=st=1708657000~exp=1708657600~hmac=a1b2c3d4e5");
        /* Opsi alternatif jika link di atas mati, uncomment yang bawah ini: */
        /* background-image: url("https://t4.ftcdn.net/jpg/03/22/56/87/360_F_322568792_N9H3q01b149d20570984865682875820.jpg"); */
        
        background-size: cover;      /* Memastikan gambar menutupi seluruh layar */
        background-position: center; /* Posisi gambar di tengah */
        background-repeat: no-repeat;/* Jangan diulang (tile) */
        background-attachment: fixed;/* Background tetap diam saat di-scroll (efek keren) */
    }
    
    /* Agar konten tidak terlalu nempel ke atas karena background gambar */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Global Font */
    html, body, [class*="css"] {
        font-family: 'Comic Sans MS', 'Sora', sans-serif; /* Font agak lebih santai/lucu */
        color: #333;
    }

    /* Header Styles */
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        color: #2c3e50;
        /* Menambah outline putih agar teks lebih pop-up di background kartun */
        text-shadow: 3px 3px 0px #fff, -1px -1px 0px #fff, 1px -1px 0px #fff, -1px 1px 0px #fff, 5px 5px 10px rgba(0,0,0,0.2);
        margin-bottom: 10px;
        line-height: 1.2;
    }
    .sub-header {
        font-size: 1.4rem;
        color: #2c3e50;
        background-color: rgba(255,255,255,0.7); /* Latar belakang putih tipis untuk sub-header */
        padding: 10px 20px;
        border-radius: 15px;
        display: inline-block;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-weight: 600;
    }
    .section-title {
        text-align: center;
        color: #2c3e50;
        font-weight: 800;
        margin-top: 50px;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 1px;
        text-shadow: 2px 2px 0px #fff;
    }

    /* --- GLASS CARD STYLE (Diperkuat) --- */
    /* Karena background ramai, efek kaca harus lebih buram dan putih */
    .glass-card {
        background: rgba(255, 255, 255, 0.80); /* Lebih putih (opacity 80%) */
        backdrop-filter: blur(15px);          /* Blur lebih kuat */
        -webkit-backdrop-filter: blur(15px);
        border-radius: 25px;                  /* Sudut lebih bulat (lucu) */
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        border: 2px solid rgba(255, 255, 255, 0.8); /* Border putih lebih tebal */
        margin-bottom: 20px;
        height: 100%;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-8px) scale(1.02); /* Efek loncat lebih terasa */
        background: rgba(255, 255, 255, 0.95);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }

    /* Styling untuk Tabs agar serasi */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(255,255,255,0.5);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 15px;
        font-weight: bold;
    }

    /* News Card Style */
    .news-card {
        background: rgba(255,255,255,0.9); /* Sedikit transparan */
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border: 1px solid #eee;
    }
    .news-tag {
        background-color: #FFEB3B; /* Kuning cerah */
        color: #d35400;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 800;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    /* Tombol Streamlit */
    .stButton>button {
        border-radius: 25px;
        font-weight: 800;
        border: 2px solid white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    /* Helper Classes */
    .highlight-red { color: #e74c3c; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- BAGIAN 1: HERO SECTION ---
col_hero1, col_hero2 = st.columns([1.5, 1], gap="large")

with col_hero1:
    st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)
    # Menambahkan emoji di judul
    st.markdown('<h1 class="main-header">✨ Tubuh Sehat,<br>Hati Riang! ✨</h1>', unsafe_allow_html=True)
    # Subheader diberi background tipis agar terbaca
    st.markdown('<div class="sub-header">Yuk, pahami BMI (Indeks Massa Tubuh) kamu. Langkah awal seru menuju hidup yang lebih bugar! 🚀</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Mulai Petualangan Sehat ⬇️", type="primary")

with col_hero2:
    # Gambar ilustrasi yang lebih kartun/lucu
    st.image("https://cdn3d.iconscout.com/3d/premium/thumb/woman-doing-yoga-pose-5650394-4708021.png", 
             use_container_width=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- BAGIAN 2: KLASIFIKASI BMI (Grid Layout) ---
st.markdown('<h2 class="section-title">🍭 Klasifikasi Standar WHO 🍭</h2>', unsafe_allow_html=True)

def create_bmi_card(emoji, title, range_val, desc, color):
    # Menambahkan border-bottom tebal agar seperti kartu mainan
    return f"""
    <div class="glass-card" style="border-top: 6px solid {color}; border-bottom: 6px solid {color}; text-align: center;">
        <div style="font-size: 50px; margin-bottom: 10px; text-shadow: 0 4px 8px rgba(0,0,0,0.1);">{emoji}</div>
        <h3 style="margin:0; color:#2c3e50; font-weight:800;">{title}</h3>
        <h2 style="color:{color}; margin: 10px 0; font-weight:900; font-size: 2.2rem;">{range_val}</h2>
        <p style="font-size: 14px; color: #555; font-weight:600;">{desc}</p>
    </div>
    """

c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown(create_bmi_card("🎈", "Kurus", "< 18.5", "Butuh tambahan nutrisi!", "#3498db"), unsafe_allow_html=True)
with c2: st.markdown(create_bmi_card("🌟", "Normal", "18.5 - 24.9", "Mantap! Pertahankan ya.", "#2ecc71"), unsafe_allow_html=True)
with c3: st.markdown(create_bmi_card("🍩", "Gemuk", "25.0 - 29.9", "Yuk, mulai aktif bergerak.", "#f1c40f"), unsafe_allow_html=True)
with c4: st.markdown(create_bmi_card("🚨", "Obesitas", "≥ 30.0", "Perlu perhatian serius.", "#e74c3c"), unsafe_allow_html=True)

# --- BAGIAN 3: BERITA & INSPIRASI ---
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown('<h2 class="section-title">🧩 Pojok Informasi & Inspirasi 🧩</h2>', unsafe_allow_html=True)

# Menggunakan Tabs
tab1, tab2, tab3 = st.tabs(["🏆 Cerita Sukses", "🌍 Fakta Dunia", "🍱 Resep Ceria"])

# TAB 1: KISAH SUKSES
with tab1:
    st.write("### 🎉 Mereka Berhasil, Kamu Juga Bisa!")
    story1, story2 = st.columns(2)
    
    with story1:
        st.markdown("""
        <div class="news-card">
            <span class="news-tag">Inspirasi Lokal</span>
            <h3>Perjalanan Tya Ariestya</h3>
            <p>Konsisten jalan kaki 45 menit tiap hari dan makan bersih (tanpa tepung & minyak berlebih). Berhasil turun 24kg demi kesehatan!</p>
        </div>
        """, unsafe_allow_html=True)
        
    with story2:
        st.markdown("""
        <div class="news-card">
            <span class="news-tag">Pola Makan</span>
            <h3>Metode Sarah Ayu</h3>
            <p>Mengatur "jendela makan" (Intermittent Fasting). Fokus mengurangi ngemil di malam hari dan memperbanyak air putih.</p>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: DATA WHO
with tab2:
    col_data, col_chart = st.columns([1, 1])
    with col_data:
        st.markdown("""
        <div class="glass-card" style="text-align:left;">
            <h3>📊 Tahukah Kamu? (Data WHO)</h3>
            <ul>
                <li><b>1 dari 8 orang</b> di dunia hidup dengan obesitas.</li>
                <li>Sejak 1990, jumlahnya naik <b>2x lipat!</b> 😱</li>
                <li>Kelebihan berat badan meningkatkan risiko <span class="highlight-red">Diabetes & Penyakit Jantung</span>.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_chart:
         st.markdown("""
        <div class="glass-card">
            <h5>📈 Tren Kenaikan Global</h5>
            <p style="font-size:12px;">Ilustrasi data menunjukkan tren yang terus meningkat jika kita tidak mengubah gaya hidup.</p>
            <div style="background:#eee; height:150px; border-radius:10px; display:flex; justify-content:center; align-items:center; color:#aaa;">
                (Area Grafik Data)
            </div>
        </div>
        """, unsafe_allow_html=True)

# TAB 3: RESEP & TIPS
with tab3:
    col_tips, col_food = st.columns(2)
    with col_tips:
        st.markdown("""
        <div class="glass-card" style="text-align:left; background: rgba(255,240,245,0.9);">
            <h3>🏃‍♀️ Tips Gerak Ceria</h3>
            <ul>
                <li>Jogging santai di taman.</li>
                <li>Menari di kamar diiringi lagu favorit! 🎵</li>
                <li>Naik tangga daripada lift.</li>
                <li>Target: 150 menit seminggu.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_food:
         st.markdown("""
        <div class="glass-card" style="text-align:left; background: rgba(240,255,240,0.9);">
            <h3>🥑 Ide Camilan Sehat</h3>
            <ul>
                <li>Potongan buah segar dingin.</li>
                <li>Yoghurt plain dengan sedikit madu.</li>
                <li>Kacang almond panggang (tanpa garam).</li>
                <li>Air kelapa murni.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div class="glass-card" style="text-align: center; font-size: 13px; padding: 15px; background: rgba(255,255,255,0.5);">
        <b>Catatan Ceria:</b> Halaman ini untuk edukasi ya! Selalu konsultasi dengan dokter atau ahli gizi untuk saran medis sungguhan. Tetap semangat! 💖<br>
        Sumber Data: Rangkuman WHO & Berita Kesehatan.
    </div>
<br>
""", unsafe_allow_html=True)