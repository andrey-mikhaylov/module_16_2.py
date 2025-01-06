import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "main"

if __name__ == '__main__':
    uvicorn.run(app, reload=True)
