import streamlit as st
import pandas as pd
import os

def load_data(subfolder_name):
    base_path = f"data/{subfolder_name}/stats"
    stats = pd.read_csv(os.path.join(base_path, "book_stats.csv"))
    books_per_category = pd.read_csv(os.path.join(base_path, "books_per_category.csv"))
    books_per_publisher = pd.read_csv(os.path.join(base_path, "books_per_publisher.csv"))
    books_per_year = pd.read_csv(os.path.join(base_path, "books_per_year.csv"))
    books_per_month = pd.read_csv(os.path.join(base_path, "books_per_month.csv"))
    page_count_per_year_month = pd.read_csv(os.path.join(base_path, "page_count_per_year_month.csv"))
    saved_per_year_month = pd.read_csv(os.path.join(base_path, "saved_per_year_month.csv"))
    return stats, books_per_category, books_per_publisher, books_per_year, books_per_month, page_count_per_year_month, saved_per_year_month

def display_visualizations(subfolder_name):
    base_path = f"data/{subfolder_name}/stats"
    st.image(os.path.join(base_path, 'collage.jpg'))
    st.image(os.path.join(base_path, 'books_per_year.png'))
    st.image(os.path.join(base_path, 'books_per_category.png'))
    st.image(os.path.join(base_path, 'books_per_publisher.png'))
    st.image(os.path.join(base_path, 'cumulative_percentage_per_year.png'))
    st.image(os.path.join(base_path, 'page_count_per_year_month.png'))
    st.image(os.path.join(base_path, 'saved_per_year_month.png'))
    st.image(os.path.join(base_path, 'summary_chart.png'))
    st.image(os.path.join(base_path, 'summary_table.png'))
    st.image(os.path.join(base_path, 'summary_month_chart.png'))
    st.image(os.path.join(base_path, 'summary_month_table.png'))

def main():
    st.title("Book Statistics Dashboard")
    subfolder_name = st.text_input("Enter subfolder name:", "dad")

    if st.button("Load Data"):
        stats, books_per_category, books_per_publisher, books_per_year, books_per_month, page_count_per_year_month, saved_per_year_month = load_data(subfolder_name)

        st.header("Overall Statistics")
        st.write(stats)

        st.header("Books per Category")
        st.write(books_per_category)

        st.header("Books per Publisher")
        st.write(books_per_publisher)

        st.header("Books per Year")
        st.write(books_per_year)

        st.header("Books per Month")
        st.write(books_per_month)

        st.header("Page Count per Year/Month")
        st.write(page_count_per_year_month)

        st.header("Saved Amounts per Year/Month")
        st.write(saved_per_year_month)

        st.header("Visualizations")
        display_visualizations(subfolder_name)

if __name__ == "__main__":
    main()