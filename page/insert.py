import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Inserir Dados')
    
    with st.form(key='insert'):
        nome_completo = st.text_input(label='Insira o nome:')
        cpf = st.number_input(label='Insira o seu CPF:', format='%d')
        data_nascimento = st.date_input(label='Insira a data de nascimento:')
        telefone = st.text_input(label='Insira o número de telefone:')
        email = st.text_input(label='E-mail:')
        senha = st.text_input(label='Senha:', type='password')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(nome_completo, int(cpf), data_nascimento, telefone, email, senha)
            st.success('Cliente incluido com sucesso')