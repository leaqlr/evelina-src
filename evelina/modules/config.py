class EVELINA:
    """
    Change data relating to the bot.
    """
    OWNER_IDS: list[int] = [
        your_owner_id, 
        your_owner_id_2, 
        your_owner_id_3
    ]
    CLIENT_ID: int = yourbot_client_id

class LOGGING:
    """
    Change various logging variables.
    """
    LOGGING_GUILD: int = your_logging_guild_id
    JOIN_LEAVE: int = your_join_leave_channel_id
    REPORT: int = your_report_channel_id
    KEYS: int = your_keys_channel_id
    MONEY: int = your_money_channel_id
    BLACKLIST: int = your_blacklist_channel_id
    SYSTEM: int = your_system_channel_id
    FEEDBACK: int = your_feedback_channel_id
    LOGGING_READY: int = your_logging_ready_channel_id


class API:
    """
    Change various API keys.
    """
    EVELINA: str = ""
    RAPIDAPI: str = ""
    OMDB: str = ""
    GENIUS: str = ""
    LASTFM: str = [
        "your_lastfm_api_key"
    ]
    OPENAI: str = [
        "your_openai_api_key"
    ]
    VALORANT: str = [
        "your_valorent_api_key"
    ]
    CLASHOFCLANS: str = [
        "your_clashofclans_api_key"
    ]

class TWITCH:
    """
    Twitch API class.
    """
    TWITCH_CLIENT_ID: int = ""
    TWITCH_CLIENT_SECRET: str = ""


class CLOUDFLARE:
    """
    Change Cloudflare configuration settings.
    """
    R2_ENDPOINT_URL: str ="https://ed57b2c738838b61759d7f3aea14d4b7.r2.cloudflarestorage.com/yourbot"
    R2_ACCESS_KEY_ID: str = "r2_account_id"
    R2_SECRET_ACCESS_KEY: str = "r2_account_secret_key"

class POSTGRES:
    """
    Change database configuration settings.
    """
    HOST: str = "localhost"
    PORT: int = "5432"
    DATABASE: str = "evelina"
    USER: str = "postgres"
    PASSWORD: str = "admin"

