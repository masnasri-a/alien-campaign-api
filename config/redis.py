from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()


def connect(db: int = 0):
    red = Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')), db=db, decode_responses=True)
    return red
