from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")
@router.get("/dashboard")
def tampilkan_dashboard(request: Request):
    # Tampilkan halaman dashboard
    return templates.TemplateResponse(request, "dashboard.html", {})