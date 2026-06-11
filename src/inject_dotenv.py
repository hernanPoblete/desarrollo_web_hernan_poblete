import pathlib
from dotenv import load_dotenv


def __inject_dotenv__():
    if pathlib.Path('.env').exists:
        load_dotenv('.env')
    elif pathlib.Path('.example.env').exists():
        load_dotenv('.example.env')
    else:
        raise NameError("Environment variables not found")
