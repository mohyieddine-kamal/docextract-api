from fastapi import FastAPI
from routers import extractions



app=FastAPI()
app.include_router(extractions.router)

@app.get("/health")            
def health():
    return {"status": "ok"}