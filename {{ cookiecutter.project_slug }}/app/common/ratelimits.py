from slowapi import Limiter
from slowapi.util import get_remote_address

# You'd want to use a proper persistent backend to store the limits, e.g.
# limiter = Limiter(key_func=get_remote_address, storage_uri="redis://<host>:<port>/n")
# The fallback for slowapi is an in-memory storage, which is not shared between processes
limiter = Limiter(key_func=get_remote_address, default_limits=["10/second"])
