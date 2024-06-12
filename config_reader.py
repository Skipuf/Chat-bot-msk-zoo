import configparser
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


config = Settings()


def ini_config(conf: str, _key: str, _value: str) -> str:
    _config = configparser.ConfigParser()
    _config.read(f'{conf}.ini', encoding='utf-8')
    return _config[_key][_value]