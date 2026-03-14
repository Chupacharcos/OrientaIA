from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import uuid
from orienta import chat, extract_profile, simulate_day
from careers_data import get_all_careers

router = APIRouter()


class ChatIn(BaseModel):
    session_id: Optional[str] = None
    message: str


class SimulateIn(BaseModel):
    session_id: str
    career_id: str


@router.post("/chat")
def orientaia_chat(body: ChatIn):
    session_id = body.session_id or str(uuid.uuid4())
    result = chat(session_id, body.message)
    return result


@router.post("/profile")
def get_profile(body: dict):
    session_id = body.get("session_id", "")
    return extract_profile(session_id)


@router.post("/simulate")
def simulate(body: SimulateIn):
    return simulate_day(body.session_id, body.career_id)


@router.get("/careers")
def careers():
    all_careers = get_all_careers()
    return [
        {"id": k, "name": v["name"], "demand": v["demand"], "salary_range": v["salary_range"]}
        for k, v in all_careers.items()
    ]


@router.post("/session/new")
def new_session():
    return {"session_id": str(uuid.uuid4()), "phase": "exploration"}
