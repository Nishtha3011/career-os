from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from edu_navigator.trend_engine import get_market_demand
from edu_navigator.gap_engine import calculate_gap
from edu_navigator.roadmap_engine import generate_roadmap
from edu_navigator.salary_engine import estimate_salary

app = FastAPI(title="CareerOS - Edu Navigator")


class AnalyzeRequest(BaseModel):
    user_skills: Dict[str, float]
    target_role: str


@app.get("/")
def home():
    return {"message": "Edu Navigator Running 🚀"}


@app.post("/analyze")
def analyze(data: AnalyzeRequest):

    result = calculate_gap(data.user_skills, data.target_role)

    readiness = result["readiness_score"]
    missing = result["missing_skills"]

    roadmap, learning = generate_roadmap(missing)
    salary = estimate_salary(readiness)

    confidence = round(readiness * 0.9 + 5, 2)

    progress_color = (
        "red" if readiness < 40
        else "orange" if readiness < 70
        else "green"
    )

    career_level = (
        "Beginner" if readiness < 40
        else "Intermediate" if readiness < 70
        else "Interview Ready"
    )

    return {
        "readiness_percent": f"{readiness}%",
        "confidence_score": confidence,
        "career_level": career_level,
        "progress_color": progress_color,
        "top_missing_skills": missing[:3],
        "weekly_roadmap": roadmap,
        "learning_resources": learning,
        "estimated_salary_band": salary
    }
