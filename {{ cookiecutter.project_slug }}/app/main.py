from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.common.config import SWAGGER_TAGS, VERSION
from app.common.database import engine
from app.common.interfaces import Base
from app.common.ratelimits import limiter
from app.common.uri import HOME_URI, SWAGGER_DOCS_URI, VERSION_URI
from app.routers import chat, users


# Startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


# App creation
app = FastAPI(
    title="A FastAPI project",
    version=VERSION.__str__(),
    openapi_tags=SWAGGER_TAGS,
    contact={
        "name": "{{ cookiecutter.user_name }}",
        "email": "{{ cookiecutter.user_email }}",
    },
    docs_url=SWAGGER_DOCS_URI,
    description="{{ cookiecutter.project_short_description }}",
    lifespan=lifespan,
)

# Configure router
router = APIRouter()
router.include_router(chat.router, prefix="/chat")
router.include_router(users.router, prefix="/users")
app.include_router(router, prefix=f"/v{VERSION.major}")

# Middleware
############

# CORS
origins = [
    "*",
    # "https://mydomain.com",
    # "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HTTPS redirect
# app.add_middleware(HTTPSRedirectMiddleware)

# Rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


@app.get(HOME_URI, tags=["Common"], include_in_schema=False)
async def read_root():
    return "App is running"


@app.get(VERSION_URI, tags=["Common"], include_in_schema=False)
async def read_version():
    return VERSION.__str__()
