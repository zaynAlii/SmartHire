from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from app.api.v1 import connect  as router 


app:FastAPI=FastAPI(
    title="Email Service ",
    description="Send emails about their password , Registartions , etc "
    )


app.include_router(router.connect)
 
@app.get("/")
def roota():
    return RedirectResponse(url="/docs")
@app.get("/health")
def roota():
    return "good"
    # return "ok"

# http://email_service:8003/healthcheck