# 0 - Bibliotecas.
    # pip install streamlit
    # pip install pandas
    # pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# streamlit run codigo4.py >> comando para rodar arquivo em lop via terminal
# python -m streamlit run "Aula 4\codigo4.py"  >> erro por verção code corrigindo.


# 3.1 - seção vendas cadastro
    # tabela com as vendas 
tabela_vendas = pd.read_csv("vendas.csv")


# 1 - titulos - sistema
st.write("# Sistema de Venda")
st.write("## Portifolio Ariel")

# 2 - seção de cadastro venda
    # campo data
    # vampo produto
    # campo valor
    # botão cadastrar vendas - atualizar vendas e sistema.


st.sidebar.write("## Cadastro de Vendas")
data = st.sidebar.date_input("Data", max_value="today")
vendedor = st.sidebar.selectbox("Vendedor", ["Ariel", "Duda", "Tayná"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")

Botao_cadastrar = st.sidebar.button("Cadastrar Vendas")
if Botao_cadastrar:
    if valor >= 1:
        # pode si usar condiçoes somadas com o comando "or"
        # exe: if valor == 0 or quantidad <= 0 or vndedor == "":
        if quantidade >= 1:
            nova_venda = [str(data), vendedor, produto, quantidade, valor] # cria uma linha 
            ultima_linha = len(tabela_vendas) # retorno numeero d linhas.
            tabela_vendas.loc[ultima_linha] = nova_venda # salva lina criana na ultima linha da tabla
            tabela_vendas.to_csv("vendas.csv", index=False) # atualisa a tabla vendas.
            st.sidebar.success("Venda cadastrada!")
        else:
            st.sidebar.warning("Quantidad Vazia")
    else:
        st.sidebar.warning("Valor Vazio")

# 3.2 - seção vendas cadastro
    # tabela com as vendas
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas)



# 4 - seção dashboard
    # card metricas - faturamento total
    # grafico de barras - venda por vendedor
    # grafico de pizza - venda por produto
st.write("## Dashboard")
faturamento =  tabela_vendas["valor"].sum()
st.metric("faturamento Total", f"R$ {faturamento}")

grafico_barra = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico_barra)

grafico_pizza = px.pie(tabela_vendas, names="produto", values="valor", hole=0.7)
st.plotly_chart(grafico_pizza)




