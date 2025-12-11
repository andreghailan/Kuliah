import pandas as pd
import streamlit as st

df = pd.DataFrame({"Nama": ["Ali", "Budi", "Caca"], "Usia": [10, 30, 35]})
st.dataframe(df)

st.table(df)

st.json({"Nama": "Ali", "Usia": 10})

st.metric("Temperature", 25, 10)

st.image("gambar.png", caption="bobo", use_container_width=True)

if st.button("Klik Saya"):
    st.success("Berhasil")
else:
    st.warning("Gagal")