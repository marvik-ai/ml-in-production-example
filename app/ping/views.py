from fastapi import APIRouter, Request

from core.settings import custom_logger


logger = custom_logger("Ping endpoint")


ping = APIRouter()


@ping.get("")
async def main(request: Request) -> str:
    """Ping endpoint, used to know if the app is up."""

    return "pong"
