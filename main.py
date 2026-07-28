from fastapi import FastAPI
from handlers import task_router, ping_router

app = FastAPI()

for router in [task_router, ping_router]:
    app.include_router(router=router)





