from aiogram import Router


def setup_callback_routers() -> Router:
    from . import question, guardianship, assess

    router = Router()
    
    router.include_router(question.router)
    router.include_router(guardianship.router)
    router.include_router(assess.router)

    return router