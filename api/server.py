from fastapi import FastAPI
from data.market_data import get_crypto_data
from scoring.crypto_score import calculate_crypto_score

app = FastAPI()

@app.get("/score/{coin}")

def score_crypto(coin: str):

    data = get_crypto_data(coin)

    score = calculate_crypto_score(data)

    return {
        "coin": coin,
        "price": data["price"],
        "scoremyai_rating": score
    }
    

