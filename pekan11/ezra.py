import streamlit as st
st.header("Hello, Streamlit!")  

with st.form("my_form"):
    nama = st.text_input("Nama :")
    alamat = st.text_input("Alamat : ")
    usia = st.number_input("Usia :", min_value=0)

    submit = st.form_submit_button("Submit")
if submit:
    st.write(f"Nama kamu {nama}, alamat kamu di {alamat}, dan usia kamu {usia} tahun.") 
