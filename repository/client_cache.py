import json
import redis

from sqlalchemy.inspection import inspect
from database import Clients


class ClientCacheRepository:

    def __init__(self, cache: redis.Redis) -> None:
        self.cache = cache

    def get_client(self, client_id: int) -> list[Clients] | None:
            with self.cache as cache:
                client_data = cache.get(str(client_id))
                if client_data:
                    client_data = json.loads(client_data)
                    return [Clients(**client) for client in client_data]
            return

    def set_client(self, client: list[Clients]) -> None:
        client_id = str(client[0].id)
        client = json.dumps([self.model_to_dict(row) for row in client])
        with self.cache as cache:
            cache.set(client_id, client)

    @staticmethod
    def model_to_dict(client_obj: Clients) -> dict:
        return {
            c.key: getattr(client_obj, c.key)
            for c in inspect(client_obj).mapper.column_attrs
        }



