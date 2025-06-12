"""Placeholder recommendation engine."""

from .main import FormData


def generate_recommendation(data: FormData) -> dict:
    """Return a trivial recommendation based on provided data."""
    recommendation = {
        "society_type": data.taxation_type or "autonomo",
        "tax_rate": "standard",
        "deductions": [],
    }
    if data.forecast_revenue and data.forecast_revenue > 1_000_000:
        recommendation["tax_rate"] = "reduced for large revenue"
    if data.deductions:
        recommendation["deductions"].append("I+D+i")
    return recommendation
