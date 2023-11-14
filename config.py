import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6809579944:AAG5EVHBCkiPCr1o_CTptqWCHDyPkOX157Y")
    
    API_ID = int(os.environ.get("API_ID", 27359621))
    
    API_HASH = os.environ.get("6202d9add6fce5b6f8b71f731842d7bc")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1903592278"))

    SESSION_NAME = "LinkToFileConverterRobot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://shanucom9000:Shanucom101@cluster0.jfkut2d.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
