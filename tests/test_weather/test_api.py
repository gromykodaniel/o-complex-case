
import pytest

from httpx import AsyncClient

@pytest.mark.parametrize("city,status_code", [
    ("Moscow"   , 200),
    ("Moskooww", 404),

])
async def test_get_weather(city , status_code , ac : AsyncClient ):

    resp = await ac.post(f'/weather/?city={city}')
    assert resp.status_code == status_code