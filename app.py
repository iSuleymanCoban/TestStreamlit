import streamlit as st

st.title("Ders 8: Streamlit ile Web Uygulaması Geliştirme")

if st.button("Tıkla"):
    st.write("Butona tıklandı!")
else:
    st.write("Butona tıklanmadı.")
    
#veri alma 
kilo = st.number_input("Kilonuzu girin (kg):", min_value=0.0)
yas = st.number_input("Yaşınızı girin:", min_value=0.0)

if st.button("Hesapla"):
    if kilo > 0 and yas > 0:
        vk = kilo / (yas ** 100)
        st.metric("sonuc:", f"{vk}")
        
    else:
        st.write("Lütfen geçerli bir kilo ve yaş girin.")