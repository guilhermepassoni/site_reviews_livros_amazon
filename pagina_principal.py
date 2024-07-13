#Imports
import streamlit as st
import pandas as pd
import plotly.express as px


# Configurações da página padrão
st.set_page_config(layout = 'wide')

# Carregamento dos dados
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Composição do slider de preços
price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()
price_mean = df_top100_books['book price'].mean()
slicer_preco = st.sidebar.slider('Preço do livro:', price_min, price_max, price_mean)

#Composição do slider de anos
ano_min = df_top100_books['year of publication'].sort_values(ascending = True).unique()[0]
ano_max = df_top100_books['year of publication'].sort_values(ascending = False).unique()[0]
slicer_ano = st.sidebar.slider('Ano de lançamento:', ano_min, ano_max, ano_max)

#Composição do slider de rating
rate_max = df_top100_books['rating'].max()
rate_min = df_top100_books['rating'].min()
rate_medio = df_top100_books['rating'].mean()
slicer_rating = st.sidebar.slider('Nota do livro:', rate_min, rate_max, rate_medio)

# Filtro no df
df_books = df_top100_books[(df_top100_books['book price'] <= slicer_preco) & (df_top100_books['year of publication'] <= slicer_ano) & (df_top100_books['rating'] <= slicer_rating)]
df_books

# Plot Quantidade de Livros
qtd_livros = df_top100_books['year of publication'][(df_top100_books['book price'] <= slicer_preco) & (df_top100_books['year of publication'] <= slicer_ano) & (df_top100_books['rating'] <= slicer_rating) ].value_counts()
fig = px.bar(qtd_livros)

# Plot Histograma de preço
hist_preco = df_top100_books['book price'][(df_top100_books['book price'] <= slicer_preco) & (df_top100_books['year of publication'] <= slicer_ano) & (df_top100_books['rating'] <= slicer_rating) ]
fig_2 = px.histogram(hist_preco)

#Plotagem de gráficos um ao lado do outro
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig_2)


