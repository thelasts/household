# from .name_file import name_router
from Routs.command_router import command_router
from Routs.UserOptionsRouters.user_options_router import user_operations_router
from Routs.UserOptionsRouters.user_add_router import user_add_router
from Routs.UserOptionsRouters.user_change_router import user_change_router

# routers = (name_router,...)
routers = (command_router, user_operations_router, user_add_router, user_change_router)
