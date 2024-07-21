
from fastapi import  APIRouter

from backend.src import weatherHelp

router = APIRouter(

    prefix='/weather'

)


@router.post('/')
async def get_weather(city:str):

    return await weatherHelp.get_coords(city)