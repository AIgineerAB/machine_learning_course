import streamlit as st
import httpx

all_books = httpx.get("http://127.0.0.1:8000/books").json()
all_titles = [book.get("title") for book in all_books]

st.markdown("# Find your book")

selected_title = st.selectbox("Choose a book title", options=all_titles)

selected_book = httpx.get(f"http://127.0.0.1:8000/books/title/{selected_title}").json()[0]

st.markdown(f"**Author:** {selected_book.get('author')}")
st.markdown(f"**Title:** {selected_book.get('title')}")
st.markdown(f"**Publish year:** {selected_book.get('year')}")
st.markdown(f"**Description:** {selected_book.get('description')}")




