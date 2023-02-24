# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = 10956858
    API_HASH = "cceefd3382b44d4d85be2d83201102b7"
    BOT_TOKEN = "5016192324:AAGhlRDIAb5vxH1gOeRLgJ0oW0dJKckPGnU"
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = "-1001862157634"
    PORT = int(getenv('PORT', 8000))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1125671241").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = ""
    OWNER_USERNAME = "ellisa_world"
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = "mongodb+srv://dsbotzz:786or786@cluster0.wrbdm8z.mongodb.net/?retryWrites=true&w=majority"
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "ellisa_world"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
