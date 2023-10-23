from fastapi import FastAPI

app = FastAPI()

def calculator(a, b):
    return a + b

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calc")
async def root():
    return calculator(10, 10)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
