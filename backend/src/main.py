from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "NeuralFlex",
    description="Task tracking, Habit formation and lifestyle adjustment",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure allowed info to be sent to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)