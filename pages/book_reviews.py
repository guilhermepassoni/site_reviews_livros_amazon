import streamlit as st
import pandas as pd

# Configurações da página padrão
st.set_page_config(layout = 'wide')

# Carregamento dos dados
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# Criação da caixa da lista suspensa de livros
books = df_top100_books['book title'].sort_values(ascending = True).unique()
book = st.sidebar.selectbox('Livros:', books)

# filtro no df
df_book = df_top100_books[ df_top100_books['book title'] == book]
df_reviews_filtered = df_reviews[ df_reviews['book name'] == book]

# Definição de títulos e demais dados do livro selecionado
book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = f"$ {df_book['book price'].iloc[0]}"
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

# Plotagem dos títulos e demais dados do livro selecionado
st.title(book_title)
st.subheader(book_genre)

# Criando 3 colunas para inserir o preço, a avaliação e o ano um ao lado do outro
col1, col2, col3 = st.columns(3)
col1.metric('Preço', book_price)
col2.metric('Avaliação', book_rating)
col3.metric('Ano de Publicação', book_year)

# Inserção de uma divisória na página
st.divider()

# Loop dos reviews dos livros
for row in df_reviews_filtered.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])


#Exibição dos dfs
#df_book
#df_reviews_filtered