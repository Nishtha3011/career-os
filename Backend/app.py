from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

from edu_navigator.trend_engine import get_market_demand
from edu_navigator.gap_engine import calculate_gap
from edu_navigator.roadmap_engine import generate_roadmap
from edu_navigator.salary_engine import estimate_salary

app = FastAPI(title="CareerOS - Edu Navigator")


# -------- REQUEST MODEL --------
class UserInput(BaseModel):
    user_skills: List[str]
    target_role: str


# -------- RESPONSE MODEL --------
class AnalyzeResponse(BaseModel):
    readiness_percent: str
    confidence_score: float
    career_level: str
    progress_color: str
    top_missing_skills: List[str]
    market_demand_trend: Dict[str, float]
    weekly_roadmap: Dict[str, str]
    estimated_salary_band: str


# -------- HOME ENDPOINT --------
@app.get("/")
def home():
    return {"message": "Edu Navigator Running 🚀"}


# -------- ROLE SKILL DEMAND --------
@app.get("/role-skills/{role}")
def role_skills(role: str):
    return get_market_demand(role)


# -------- MAIN ANALYZE ENDPOINT --------
@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: UserInput):
    readiness, missing = calculate_gap(data.user_skills, data.target_role)
    roadmap, learning = generate_roadmap(missing)
    salary = estimate_salary(readiness)

    confidence = round(readiness * 0.9 + 5, 2)

    progress_color = (
        "red" if readiness < 40
        else "orange" if readiness < 70
        else "green"
    )

    return {
        "readiness_percent": f"{readiness}%",
        "confidence_score": confidence,
        "career_level": (
            "Beginner" if readiness < 40
            else "Intermediate" if readiness < 70
            else "Interview Ready"
        ),
        "progress_color": progress_color,
        "top_missing_skills": missing[:3],
        "market_demand_trend": get_market_demand(data.target_role),
        "weekly_roadmap": roadmap,
        "estimated_salary_band": salary
    }