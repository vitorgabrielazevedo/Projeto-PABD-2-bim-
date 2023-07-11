import streamlit as st
import controller.cliente as cliente
import services.database as db

def deletar():
    st.title('Deletar dados')

    with st.form(key='delete'):
        email = st.text_input(label='E-mail:')
        buttom_submit = st.form_submit_button('Deletar')

    if buttom_submit:
        cliente.deletar(email)
        st.success('Cliente excluído com sucesso')




