from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Arcana Pulse online"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/signals")
def signals():
    return {
        "signals": [
            {
                "coin": "BTC",
                "signal": "HOLD",
                "score": 72
            },
            {
                "coin": "ETH",
                "signal": "BUY ZONE",
                "score": 81
            }
        ]
    }
