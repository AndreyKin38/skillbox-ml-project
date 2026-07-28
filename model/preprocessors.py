import pandas as pd
import numpy as np
import pickle

from database import Clients


# def get_best_pipe(path):
#     with open(path, 'rb') as file:
#         best_pipe = pickle.load(file)
#     return best_pipe
#
#
# def get_preprocessor_param(path) -> dict | list:
#     with open(path, 'rb') as file:
#         param = pickle.load(file)
#     return param


class DataPreprocessor:

    def __init__(self, client: list[Clients], count_vec_dict: dict, col_to_drop: list) -> None:
        self.client = pd.DataFrame([{c.name: getattr(row, c.name) for c in Clients.__table__.columns} for row in client])
        self.count_vec_dict = count_vec_dict
        self.col_to_drop = col_to_drop

    def transform(self):
        return self.get_prep_client_data()

    def get_prep_client_data(self) -> pd.DataFrame:

        df_list = []
        for col_name, array_size in self.count_vec_dict.items():
            df = self.unique_feature_value_counter(
                col_name=col_name,
                array_size=array_size
            )

            df_list.append(df)

        df_rn_count = self.client.groupby(['id'], as_index=False).agg({'rn': 'count'}).reset_index(drop=True)

        df_train = pd.concat([df_rn_count] + df_list, axis=1)
        df_train = df_train.drop(self.col_to_drop + ['id'], axis=1)

        return df_train

    def unique_feature_value_counter(self, col_name: str, array_size: int) -> pd.DataFrame:
        array_ = self.client[['id', col_name]].to_numpy()

        data = {}
        for i, j in array_:
            if i not in data:
                data[i] = np.zeros(array_size)
            data[i][j] += 1

        return pd.DataFrame(data=data.values(), columns=[str(i) + '_' + col_name for i in range(array_size)])



