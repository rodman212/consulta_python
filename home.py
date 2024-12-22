import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Carregar a lista de ativos de um arquivo CSV
file_path = 'meu_arquivo.csv'  # Substitua pelo caminho do arquivo
ativos_df = pd.read_csv(file_path)

# Adicionar ".SA" ao final dos tickers e ordenar alfabeticamente
acoes_brasileiras = sorted(ativos_df['Ticker'].apply(lambda x: x + '.SA').tolist())

# Título da aplicação
st.title("Gráfico de Ações da Bolsa Brasileira")

# Selecionar uma ação com menu suspenso
acao_selecionada = st.selectbox("Selecione uma ação:", acoes_brasileiras)

# Selecionar o tipo de preço (Adjusted Close ou Close)
tipo_preco = st.radio("Selecione o tipo de preço:", ['Adj Close', 'Close'])

# Botão para carregar os dados
if st.button("Exibir Gráfico"):
    # Baixar os dados da ação selecionada
    with st.spinner(f"Carregando dados da ação {acao_selecionada} com o tipo {tipo_preco}..."):
        try:
            dados = yf.download(acao_selecionada)[tipo_preco]

            # Verificar se há dados
            if not dados.empty:
                # Criar o gráfico
                fig, ax = plt.subplots(figsize=(10, 6))
                dados.plot(ax=ax, color='blue', label=f'Preço {tipo_preco}')
                ax.set_title(f"Histórico de {tipo_preco} - {acao_selecionada}", fontsize=16)
                ax.set_xlabel("Data", fontsize=12)
                ax.set_ylabel("Preço (R$)", fontsize=12)
                ax.legend()

                # Exibir o gráfico no Streamlit
                st.pyplot(fig)

                # Mostrar os dados na tabela (opcional)
                # st.write("Dados das ações:")
                # st.dataframe(dados)
            else:
                st.warning("Não foi possível obter dados para a ação selecionada.")
        except Exception as e:
            st.error(f"Erro ao carregar os dados: {e}")
