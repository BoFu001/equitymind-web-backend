"""
api/routes/health.py

Health check endpoint for Railway uptime monitoring.
"""

from fastapi import APIRouter
from config import APP_NAME

router = APIRouter()


@router.get("/health")
def health():
    """Health check for Railway uptime monitoring."""
    return {"status": "ok", "app": APP_NAME}