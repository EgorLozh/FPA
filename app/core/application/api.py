from ninja import NinjaAPI

from core.application.routers.workers import worker_router
from core.application.routers.department import department_router
from core.application.routers.script import script_router
from core.application.routers.request import request_router

def get_api() -> NinjaAPI:
    api = NinjaAPI(title='API', version='1.0.0')
    
    api.add_router('worker', worker_router, tags=['Workers'])
    api.add_router('department', department_router, tags=['Departments'])
    api.add_router('script', script_router, tags=['Scripts'])
    api.add_router('request', request_router, tags=['Requests'])

    return api