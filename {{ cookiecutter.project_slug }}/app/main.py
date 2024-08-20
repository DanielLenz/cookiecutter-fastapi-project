from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI

from app.common.config import SWAGGER_TAGS, VERSION
from app.common.uri import HOME_URI, SWAGGER_DOCS_URI
from app.routers import chat


@asynccontextmanager
async def lifespan(app: FastAPI):
    pass
    yield


app = FastAPI(
    title="A FastAPI project",
    version=VERSION.__str__(),
    openapi_tags=SWAGGER_TAGS,
    contact={"name": "{{ cookiecutter.name }}", "email": "{{ cookiecutter.email }}"},
    docs_url=SWAGGER_DOCS_URI,
    description="{{ cookiecutter.short_description }}",
    lifespan=lifespan,
)

# Configure router
router = APIRouter()
router.include_router(chat.router, prefix="/chat")
app.include_router(router, prefix=f"/v{VERSION.major}")


@app.get(HOME_URI, tags=["Common"])
async def read_root():
    return "App is running"
