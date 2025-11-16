from fastapi import APIRouter
from app.api.v1 import routes

router = APIRouter()

# All v1 routes
router.include_router(routes.router, prefix="/v1")
