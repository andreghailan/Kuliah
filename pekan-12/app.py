import streamlit as st
# from streamlit_option_menu import option_menu


st.set_page_config(page_title="Bangun Datar", page_icon="🎶")

st.title("Aplikasi perhitungan bangun datar")
st.write("Silahkan pilih menu di samping untuk memulai")

def luas_persegi(sisi):
    return sisi * sisi  

def segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def lingkaran(jari2):
    return 3.14 * jari2 * jari2

# with st.sidebar:
#     menu = option_menu(
#         "Menu",
#         ["Luas Persegi", "Luas segitiga", "Luas lingkaran"],
#         icons=["square", "triangle", "circle"],
#         menu_icon="list",
#         default_index=0,
#     )   

menu = st.sidebar.selectbox('Menu', ['Luas Persegi', 'Luas segitiga', 'Luas lingkaran'])

if menu == "Luas Persegi":
    st.header("Luas Persegi")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVlFBO8LM3diq71WxoJjU3581SrrFNt6F4qA&s", caption="Rumus luas persegi")

    sisi = st.number_input("Masukkan panjang sisi persegi", min_value=0)
    if st.button("hitung"):
        luas = luas_persegi(sisi)
        st.success(f"Luas persegi adalah: {luas:.2f}")

elif menu == "Luas segitiga":
    st.header("Luas segitiga")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvnU93yw54EG4p3cL7lMuWFeCGlkPv0co7cA&s", caption="Luas Segitiga")

    alas = st.number_input('Masukkan Alas', min_value=0)
    tinggi = st.number_input('Masukkan Tinggi', min_value=0)

    if st.button('Hitung Luas Segitiga'):
        luas = segitiga(alas, tinggi)
        st.succes(f"Luas segitiga adalah: {luas:.2f}")

elif menu == 'Luas lingkaran':
    st.subheader('Hitung Luas Lingkaran')
    st.image(
        "https://thumb.viva.co.id/media/frontend/thumbs3/2022/04/11/6253bd91b52f8-rumus-luas-lingkaran_1265_711.jpg",
        caption="Ilustrasi Lingkaran",
        width=300,
    )

    jari2 = st.number_input('Masukkan Jari-Jari', min_value=0)

    if st.button('Hitung Luas Lingkaran'):
            luas = lingkaran(jari2)
            st.success(f"Luas lingkaran adalah: {luas:.2f}")