from fastapi import FastAPI
from sqladmin import Admin

# from src.admin import register_admin_views
from src.base_settings import base_settings
from src.common.databases.postgres import postgres
from src.routes import BaseRoutesPrefixes


def include_routes(application: FastAPI) -> None:
    application.include_router(

    )


def get_application() -> FastAPI:
    application = FastAPI(
        debug=base_settings.debug,
        openapi_url=BaseRoutesPrefixes.openapi if base_settings.debug else None,
        docs_url=BaseRoutesPrefixes.swagger if base_settings.debug else None,
    )

    @application.on_event('startup')
    def startup():
        postgres.connect(base_settings.postgres.url)
        engine = postgres.get_engine()
        admin = Admin(app=application, engine=engine)
        # register_admin_views(admin)

        @application.on_event('shutdown')
        async def shutdown():
            await postgres.disconnect()

        include_routes(application)

    return application


app = get_application()
