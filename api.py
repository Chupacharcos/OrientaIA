from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router

app = FastAPI(title="OrientaIA", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://adrianmoreno-dev.com", "http://127.0.0.1", "http://localhost"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/orientaia")


@app.get("/health")
def health():
    return {"status": "ok", "service": "orientaia", "version": "1.0.0"}
