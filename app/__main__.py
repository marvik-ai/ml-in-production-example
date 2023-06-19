import uvicorn

from app import create_app
from core.settings import custom_logger


logger = custom_logger("Main API")


app = create_app()


# Run API
if __name__ == "__main__":
    logger.info("Running FastAPI with uvicorn")
    uvicorn.run(app, host="0.0.0.0", port=80)
