
import pytest
from httpx import AsyncClient

from backend.src.main import app as fastapi_app


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient( app=fastapi_app , base_url="http://test") as ac:
        yield ac