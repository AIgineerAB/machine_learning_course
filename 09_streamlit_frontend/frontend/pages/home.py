import streamlit as st 
from pathlib import Path

book_path = Path(__file__).parents[2] / "assets" / "fastapi_book.png"

st.markdown("# Bookies App")

st.markdown("""This is a streamlit app that consumes a FastAPI API about books.
            Purpose of this app is to demonstrate a simple streamlit app with some 
            of the possibilities in streamlit. Streamlit is a very easy way in Python
            to create a simple web application for demonstrating things quickly.
            """)

st.markdown(""" In this demo, we only use the get endpoints of the API, 
            feel free to also implement creating a book, updating and 
            deleting a book as well. Note that you need to also update
            the API to persist the data as this is a simplification we didn't do. 
""")

st.image(book_path)