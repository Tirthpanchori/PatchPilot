import os

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer(auto_error=False)

API_KEY = os.getenv("PATCHPILOT_API_KEY")


async def verify_api_key(
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    if API_KEY is None:
        raise HTTPException(
            status_code=500,
            detail="PATCHPILOT_API_KEY is not configured",
        )

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization header",
        )

    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API key",
        )

    return True
