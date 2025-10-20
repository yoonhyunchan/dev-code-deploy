from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify the service is running
    """
    return {"status": "ok"}