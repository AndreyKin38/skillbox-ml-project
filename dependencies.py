from repository import ClientRepository, ClientCacheRepository
from database import get_db_session
from cache import get_redis_connection
from service import ClientService, ClientCacheService


def get_client_repository() -> ClientRepository:
    db_session = get_db_session()
    return ClientRepository(db_session=db_session)


def get_client_service() -> ClientService:
    client_repository = get_client_repository()
    return ClientService(client_repository=client_repository)


def get_cache_repository() -> ClientCacheRepository:
    cache = get_redis_connection()
    return ClientCacheRepository(cache=cache)


def get_client_from_cache() -> ClientCacheService:
    client_cache_repository = get_cache_repository()
    return ClientCacheService(client_cache_repository=client_cache_repository)





