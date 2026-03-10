def calculate_crypto_score(data):

    score = 0

    if data["market_cap"] > 100000000000:
        score += 30

    if data["volume"] > 1000000000:
        score += 20

    if data["github_repos"] > 100:
        score += 20

    score += 30

    return min(score, 100)
