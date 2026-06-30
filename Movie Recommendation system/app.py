import streamlit as st
import pandas as pd

# Page Settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Title
st.title("🎬 Movie Recommendation System")
st.write("Get movie recommendations based on your favorite movie!")

# Load Dataset
movies = pd.read_csv("movies.csv")

# Show Dataset (Optional)
with st.expander("View Movie Dataset"):
    st.dataframe(movies)

# Select Favorite Movie
st.subheader("Choose Your Favorite Movie")

selected_movie = st.selectbox(
    "Select a movie",
    movies["Movie"].sort_values()
)

# Recommend Button
if st.button("🎥 Get Recommendations"):

    # Find selected movie genre
    movie_genre = movies[
        movies["Movie"] == selected_movie
    ]["Genre"].values[0]

    # Get recommendations
    recommendations = movies[
        (movies["Genre"] == movie_genre) &
        (movies["Movie"] != selected_movie)
    ].sort_values(
        by="Rating",
        ascending=False
    )

    st.success(
        f"Because you liked '{selected_movie}', you may also enjoy these {movie_genre} movies:"
    )

    st.dataframe(
        recommendations,
        use_container_width=True
    )

    st.subheader("⭐ Top 5 Recommended Movies")

    top5 = recommendations.head(5)

    for i in range(len(top5)):
        st.write(
            f"**{i+1}. {top5.iloc[i]['Movie']}**  |  "
            f"Genre: {top5.iloc[i]['Genre']}  |  "
            f"⭐ Rating: {top5.iloc[i]['Rating']}"
        )

# Statistics
st.divider()

st.subheader("📊 Dataset Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Movies",
        len(movies)
    )

with col2:
    st.metric(
        "Genres",
        movies["Genre"].nunique()
    )

with col3:
    st.metric(
        "Highest Rating",
        movies["Rating"].max()
    )

# Genre Distribution
st.subheader("Movies by Genre")

genre_count = movies["Genre"].value_counts()

st.bar_chart(genre_count)