from dotenv import find_dotenv
from pydantic import BaseSettings


class BaseProjectSettings(BaseSettings):

    class Config:
        env_file = find_dotenv(filename=".env.local")