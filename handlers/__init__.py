from .ping import router as ping_router
from .tasks import router as tasks_router


routers = [tasks_router, ping_router]