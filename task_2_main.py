from fastapi import FastAPI
from task_2.routes.ukpostcode import ukpostcode_router


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ukpostcode_router)

    return application


app = create_application()
