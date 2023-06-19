from fastapi import FastAPI

from app.ping import ping
from app.predict import predict

from core.settings import custom_logger


# Active endpoints noted as following: (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = (
    ("/ping", ping),
    ("/predict", predict),
)


logger = custom_logger("API initialization")


def create_app() -> FastAPI:
    """Function for creating a FastAPI app"""

    app = FastAPI(
        title="sentiment-analysis-app",
        debug=True,
        version="0.1",
    )

    # Register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        logger.debug(f"Registering router: {url} - {blueprint}")
        app.include_router(blueprint, prefix=url)

    return app
