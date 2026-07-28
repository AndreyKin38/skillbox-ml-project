from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str = 'Clients'
    POSTGRES_CONNECTION: str = "postgresql+psycopg2://postgres:password@0.0.0.0:5436/client_db"
    FULL_CLIENT_DATA_PATH: str = '/model/data/full_train_data.parquet'
    MODEL_PATH: str = 'model/best_pipe/best_model.pkl'
    COUNT_VEC_DICT_PATH: str = 'model/prep_params/max_value_dict.pkl'
    COL_TO_DROP_PATH: str = 'model/prep_params/col_to_drop.pkl'




