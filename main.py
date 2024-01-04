from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from route import auth, util

app = FastAPI()

@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse("/docs")

app.include_router(auth.app, prefix="/auth", tags=["Auth"])
app.include_router(util.app, prefix="/util", tags=["Util"])

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9001, reload=True)

