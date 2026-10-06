# 0 - Bibliotecas
# pip install streamlit 
# pip install openai
import streamlit as st  # importando comando e dando apelo
from openai import OpenAI # IMPORTA A BIBLIOTECA DESEJADA DA IA.
# streamlit run codigo3.py >> comando para rodar arquivo em lop via terminal
# python -m streamlit run "Aula 3\codigo3.py"  >> erro por verção code corrigindo.

# 5.1 Tornar respostas in teligentes.
modelo_ia = OpenAI(api_key="AQ.Ab8RN6JbH9kmn4xWzbe63GNCt2xMB_kmT4MVCm6ymZ7NGqYugA",
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")



# 1 - Titulos

st.write("## ChatBot de IA feita pelo Ariel")

# 4 Criar memoria >> em lista

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)

# 2 - campo de mensagens (input)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

# 3 - quandop usuario envia mensagens
    # mostrar a mensagem 
     # manda para ia
     # mostrar resposta da ia

if mensagem_usuario:
    # mensagem do usuario
    st.chat_message("user").write(mensagem_usuario)
    pergunta = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(pergunta)
    # user >> usuario
    # assistant >> chat boot

    # 5.2 Tornar respostas in teligentes.
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )
    print(resposta_modelo)
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    resposta = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(resposta)

    
    