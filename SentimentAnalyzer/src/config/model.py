from configparser import ConfigParser


class AppConfig:
    db_user_name: str
    db_password: str
    db_host: str
    db_port: int

    def __init__(self, parser: ConfigParser) -> None:
        self.db_user_name = parser['db']['user_name']
        self.db_password = parser['db']['password']
        self.db_host = parser['db']['host']
        self.db_port = int(parser['db']['port'])
        self.db_name = parser['db']['name']

    @property
    def db_connection_str(self) -> str:
        return f'mongodb://{self.db_user_name}:{self.db_password}@{self.db_host}:{self.db_port}/'

    @staticmethod
    def create_from_file(file_path: str) -> "AppConfig":
        parser = ConfigParser()
        parser.read(file_path)
        return AppConfig(parser)
