# from .name_file import name_router
from .command_router import command_router
from Routs.UserOptionsRouters.user_options_router import user_operations_router
from Routs.UserOptionsRouters.user_add_router import user_add_router

# routers = (name_router,...)
routers = (command_router, user_operations_router, user_add_router)
