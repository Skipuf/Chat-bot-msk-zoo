from aiogram import Router


def setup_message_routers() -> Router:
    from . import start, contact

    router = Router()
    router.include_router(start.router)
    router.include_router(contact.router)
    return router