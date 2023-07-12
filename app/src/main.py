from fastapi import FastAPI

from src.app import create_app

app: FastAPI = create_app()


if __name__ == "__main__":
    import logging

    import uvicorn

    uvicorn.run(app=app, reload=True, log_level=logging.DEBUG)
