from aiogram import Dispatcher
from Routs import routers


def include_routers(dp: Dispatcher):
    for router in routers:
        dp.include_routers(router)

# todo include for middleware and filters and next


def return_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    include_routers(dp)
    return dp
