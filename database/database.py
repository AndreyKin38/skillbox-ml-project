import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import Settings


settings = Settings()
engine = create_engine(settings.POSTGRES_CONNECTION)
Session = sessionmaker(engine)

# full_dataset = pd.read_parquet(settings.FULL_CLIENT_DATA_PATH)
# full_dataset = full_dataset[:100000]
#
# full_dataset.to_sql('Clients', engine, if_exists='replace', index=False, chunksize=10000)


def get_db_session() -> Session:
    return Session


