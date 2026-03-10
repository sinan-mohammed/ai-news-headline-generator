import streamlit as st
from headline_generator import generate_headlines
from headline_ranker import rank_headlines

st.title("AI News Headline Generator")

article = st.text_area("Paste News Article")

if st.button("Generate Headlines"):

    headlines = generate_headlines(article)

    ranked = rank_headlines(headlines)

    st.subheader("Generated Headlines")

    for h, s in ranked:
        st.write(f"{h} (Score: {s})")

    st.success(f"Best Headline: {ranked[0][0]}")