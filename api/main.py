import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.stream import router as stream_router
from config import APP_NAME

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)

app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stream_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok", "app": APP_NAME}
