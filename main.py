from fastapi import FastAPI

from database import Base, engine
from routers import extractions

app = FastAPI()
app.include_router(extractions.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}