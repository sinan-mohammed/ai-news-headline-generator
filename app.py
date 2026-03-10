from headline_generator import generate_headlines
from headline_ranker import rank_headlines

article = """
NASA successfully launched a new satellite designed to monitor climate change 
and provide real-time environmental data to scientists worldwide.
"""

# Generate headlines
headlines = generate_headlines(article)

# Rank headlines
ranked = rank_headlines(headlines)

print("\nGenerated Headlines\n")

for h, s in ranked:
    print(f"{h}  ---> Score: {s}")

print("\nBest Headline:")
print(ranked[0][0])