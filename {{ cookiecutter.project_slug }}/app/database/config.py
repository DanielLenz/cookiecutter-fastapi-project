from pydantic import Field
from pydantic_settings import BaseSettings


class PostgresConfig(BaseSettings):
    hostname: str = Field(..., alias="POSTGRES_SERVER")
    user: str = Field(..., alias="POSTGRES_USER")
    password: str = Field(..., alias="POSTGRES_PASSWORD")
    database: str = Field(..., alias="POSTGRES_DB")

    def get_database_url(self):
        return (
            f"postgresql://{self.user}:{self.password}@{self.hostname}/{self.database}"
        )


class SQLiteConfig(BaseSettings):
    filename: str = Field(...)

    def get_database_url(self):
        return f"sqlite:///{self.filename}"


# Not used in the current setup,
# just a sample for future reference
# postgres_config = PostgresConfig()

sqlite_config = SQLiteConfig(filename="test.db")
DATABASE_URL = sqlite_config.get_database_url()
