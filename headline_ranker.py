keywords = ["NASA", "climate", "satellite"]

def score_headline(headline):

    score = 0

    # keyword relevance
    for k in keywords:
        if k.lower() in headline.lower():
            score += 2

    # clarity (length)
    word_count = len(headline.split())

    if 6 <= word_count <= 12:
        score += 3

    return score


def rank_headlines(headlines):

    scored = []

    for h in headlines:
        s = score_headline(h)
        scored.append((h, s))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored