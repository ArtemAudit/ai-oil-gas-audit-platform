from fastapi import FastAPI
app = FastAPI(
   title="AI Oil & Gas Audit Platform",
   description="AI Powered Audit Platform for Oil & Gas",
   version="0.1"
)
@app.get("/")
def root():
   return {"message": "AI Oil & Gas Audit Platform Running"}
