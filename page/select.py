import streamlit as st

import controller.cliente as cliente


def consultar():
    st.title('Consultar Dados')
    colunas = st.columns((2,2,2,2,2,2,2))
    campos = ['Nome', 'CPF', 'Data de nascimento', 'Telefone', 'E-mail', 'Senha', 'Excluir']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in cliente.selecionar():
        col1, col2, col3, col4, col5, col6, col7 = st.columns((2,2,2,2,2,2,2))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])
        col6.write(item[5])
        button_excluir = col7.empty()
        on_click_excluir = button_excluir.button('x', 'btnExcluir' + str(item[0]))
        
        if on_click_excluir:
            continue
            #cliente.excluir(item[0])   
            