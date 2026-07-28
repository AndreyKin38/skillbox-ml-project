from repository import ClientRepository, get_best_pipe
from database import Clients
from model import DataPreprocessor
from settings import Settings
from schemas import PredictionSchema, ClientSchema


class ClientService:

    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository
        self.client = None
        self.preprocessor = None

    def get_client(self, client_id: int) -> list[Clients]:
        self.client = self.client_repository.get_client(client_id)
        return self.client

    def set_client_data(self, client: ClientSchema) -> None:
        self.client_repository.set_client_data(client)

    def set_client_preprocessor(self):

        if self.client is None:
            print("Error: The client was not found. Use 'set_client' method.")
            raise ValueError

        self.client_repository.set_preprocessor_params(
            count_dict_path=Settings().COUNT_VEC_DICT_PATH,
            col_to_drop_path=Settings().COL_TO_DROP_PATH
        )
        count_vec_dict = self.client_repository.count_vec_dict
        col_to_drop = self.client_repository.col_to_drop

        self.preprocessor = DataPreprocessor(
            client=self.client,
            count_vec_dict=count_vec_dict,
            col_to_drop=col_to_drop
        )

    def get_prediction(self) -> dict | PredictionSchema:
        if self.preprocessor is None:
            print("Error: The preprocessor was not found. Use 'set_client_preprocessor' method.")
            raise ValueError

        client_prep_data = self.preprocessor.transform()
        model = get_best_pipe(Settings().MODEL_PATH)
        prediction = model.predict(client_prep_data)[0]
        prediction_proba = model.predict_proba(client_prep_data)[:, 1][0]

        return PredictionSchema(
            client_id=self.client[0].id,
            prediction=prediction,
            prediction_proba=prediction_proba
        )

