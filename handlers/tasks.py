from typing import Annotated

from fastapi import APIRouter, Depends
from schemas import ClientSchema, PredictionSchema
from service import ClientService, ClientCacheService
from dependencies import get_client_service, get_client_from_cache


router = APIRouter(prefix="/task", tags=["task"])


@router.get(
    "/client",
    response_model=list[ClientSchema]
)
def get_client(
        client_id: int,
        client_service: Annotated[
            ClientService, Depends(get_client_service)
        ],
        client_cache_service: Annotated[
            ClientCacheService, Depends(get_client_from_cache)
        ]
):
    if client_data := client_cache_service.get_client(client_id):
        return client_data
    client_data = client_service.get_client(client_id)
    client_cache_service.set_client(client_data)
    return client_data


@router.get(
    "/model",
    response_model=PredictionSchema
)
def client_prediction(
        client_id: int,
        client_service: Annotated[
            ClientService,Depends(get_client_service)
        ]
):
    client_service.get_client(client_id)
    client_service.set_client_preprocessor()
    prediction = client_service.get_prediction()
    return prediction



# @router.post(
#     "/",
#     response_model=ClientSchema
# )
# def create_client(
#         client: ClientSchema,
#         client_repository: Annotated[
#             ClientRepository,
#             Depends(get_client_repository)
#         ]
# ):
#     client_repository.create_client(client)
#     return client
#
