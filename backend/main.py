from fastapi import FastAPI
from pydantic import BaseModel

from .recommendation_engine import generate_recommendation

app = FastAPI(title="FiscalAI")

class FormData(BaseModel):
    company_name: str
    state: str
    partners: int
    sector: str | None = None
    business_model: str | None = None
    forecast_revenue: float | None = None
    employees: int | None = None
    international: bool | None = None
    taxation_type: str | None = None
    investors: bool | None = None
    deductions: bool | None = None
    advanced_structure: bool | None = None
    location: str | None = None
    accounting_software: str | None = None
    audit_required: bool | None = None
    inspections: bool | None = None
    risk_profile: str | None = None

@app.post("/api/form")
def submit_form(data: FormData):
    """Receive form data and return a basic recommendation."""
    recommendation = generate_recommendation(data)
    return {"message": "Form received", "recommendation": recommendation}
