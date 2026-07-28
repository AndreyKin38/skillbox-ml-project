from database import Clients
from repository import ClientCacheRepository


class ClientCacheService:

    def __init__(self, client_cache_repository: ClientCacheRepository):
        self.client_cache_repository = client_cache_repository

    def get_client(self, client_id) -> list[Clients] | None:
        return self.client_cache_repository.get_client(client_id)

    def set_client(self, client: list[Clients]) -> None:
        self.client_cache_repository.set_client(client)

