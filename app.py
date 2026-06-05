from pickle import TRUE
import streamlit as st
import pandas as pd

st.set_page_config(page_title="mini görev panosu", layout="centered", page_icon="pictures/indir.ico")

#style css kısmı 
st.markdown(
    """
    <style>
    .app-header {
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#durum görev durumlarını belirleme 
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"text": "streamlit hesabı aç", "done": True},
        {"text": "görev panosu oluştur", "done": True},
        {"text": "görev ekleme özelliği ekle", "done": True},
    ]
#bslık html div
st.markdown(
    """
    <div class="app-header">
        <h1 style="color: #333;">Mini Görev Panosu</h1>
        <p style="color: #666;">Görevlerinizi kolayca yönetin ve takip edin!</p>
    </div>
    """,
    unsafe_allow_html=True
)
#görevler ekleme 
col_input, col_btn = st.columns([4, 1])
with col_input:
    new_task = st.text_input("Yeni görev ekle", placeholder="Görev metnini girin...", label_visibility="visible")
with col_btn:
    if st.button("Ekle", use_container_width=True):
        if new_task.strip() != "":
            st.session_state.tasks.append({"text": new_task, "done": False})
            st.success("Görev başarıyla eklendi!")
            st.rerun()
        else:
            st.error("Lütfen geçerli bir görev metni girin.")
st.write("")
#görevlerin listesi 
if not st.session_state.tasks:
    st.info("Henüz görev eklenmedi. Yukarıdaki kutuya bir görev ekleyin!")

for i , task  in enumerate(st.session_state.tasks):
    c1,c2,c3 = st.columns([6, 1, 1])
    with c1:
        checked = st.checkbox(task["text"], value=task["done"], key=f"task_{i}", label_visibility="collapsed")
        if checked != task["done"]:
            st.session_state.tasks[i]["done"] = checked
            st.rerun()
    with c2:
        st.markdown(
        f"""
        
        <div>{task["text"]}</div>
        
        """,unsafe_allow_html=True
        )
    with c3:
        if st.button("Sil", key=f"delete_{i}", use_container_width=True):
            del st.session_state.tasks[i]
            st.success("Görev başarıyla silindi!")
            st.rerun()
            

#özet