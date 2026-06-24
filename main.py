from fastapi import FastAPI, File, UploadFile, HTTPException, status, Request, Depends, Security
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials
from src.config.base import API_KEY_VAR
from fastapi.security import APIKeyHeader
from src.recommender.base import orchestrate_recommendation
security_scheme = APIKeyHeader(name="X-API-KEY", auto_error=False)
from src.model.base import RequestModel

async def verify_api_key(credentials: str = Security(security_scheme)):
    token = credentials
    # Replace this with your actual key validation or database check
    if not token or not token.startswith("github_pat"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return token

app = FastAPI(title="AI Music Recommendation API")




# Middleware to extract the key from headers and assign it to the context
@app.middleware("http")
async def extract_api_key_middleware(request: Request, call_next):
    # Expecting header: "Authorization: Bearer YOUR_API_KEY"
    auth_header = request.headers.get("Authorization")

  
    
    if auth_header and auth_header.startswith("Bearer "):
        api_key = auth_header.split(" ")[1]
    else:
        # Fallback if you pass it as a custom header like X-API-Key
        api_key = request.headers.get("X-API-Key", "")

    # Set the token for the duration of this specific request execution
    token_token = API_KEY_VAR.set(api_key)
    try:
        response = await call_next(request)
        return response
    finally:
        # Clean up after the request finishes
        API_KEY_VAR.reset(token_token)


@app.get("/")
def health_check():
    """Simple endpoint to confirm the API is running"""
    return {
        "status": "ok",
        "message": "AI Music Recommendation API is running"
    }

@app.post("/generate")
async def generate_rec(req: RequestModel, token: str = Depends(verify_api_key)):
    """Send a request to get AI music recommendations"""

    response = await orchestrate_recommendation(req)
    return JSONResponse(response)