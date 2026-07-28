import pickle

from sqlalchemy import select
from sqlalchemy.orm import Session
from database import Clients
from schemas import ClientSchema


def get_best_pipe(path):
    with open(path, 'rb') as file:
        best_pipe = pickle.load(file)
    return best_pipe


def get_preprocessor_param(path) -> dict | list:
    with open(path, 'rb') as file:
        param = pickle.load(file)
    return param


class ClientRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.count_vec_dict = None
        self.col_to_drop = None

    def get_client(self, client_id: int) -> list[Clients] | None:
        query = select(Clients).where(Clients.id == client_id)
        with self.db_session() as session:
            client = session.execute(query).scalars().all()
        return client

    def set_preprocessor_params(self, count_dict_path: str, col_to_drop_path: str) -> None:
        self.count_vec_dict = get_preprocessor_param(count_dict_path)
        self.col_to_drop = get_preprocessor_param(col_to_drop_path)

    def set_client_data(self, client: ClientSchema) -> None:
        client_model = client.json()
        with self.db_session() as session:
            session.add(client_model)
            session.commit()


