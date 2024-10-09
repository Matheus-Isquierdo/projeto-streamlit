import streamlit as st
import pandas as pd
from datetime import date

def gravar_cadastro (nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open('Clientes.csv', 'a', encoding= 'utf-8') as file:
            file.write(f'{nome},{dt_nasc},{tipo}\n')
        st.session_state['Sucesso'] = True
    else:
        st.session_state['Sucesso'] = False

st.set_page_config(
    page_title= 'Cadastro de Clientes',
    page_icon= '🎁'
)

st.title('Cadastro de Clientes')
st.divider()

nome = st.text_input('Digite o Nome do Cliente: ', key= 'nome_cliente')
data = st.date_input('Coloque a Data de Aniversário do Cliente: ', format= 'DD/MM/YYYY')
tipo = st.selectbox('Tipo do Cliente: ',
                    ['Pessoa Jurídica', 'Pessoa Física'])
btn_cadastrar = st.button('Cadastrar',
                          on_click= gravar_cadastro,
                          args= [nome, data, tipo])

if btn_cadastrar:
    if st.session_state['Sucesso']:
        st.success('Cadastro Realizado com Sucesso.', icon= '✔')
    else:
        st.error('Houve Algum Problema no Cadastro.', icon= '🚨')