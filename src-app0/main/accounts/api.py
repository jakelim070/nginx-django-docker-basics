from ninja_jwt.controller import NinjaJWTDefaultController
from ninja_extra import NinjaExtraAPI

# User requested /api/auth.
# api is mounted at /api/auth/ in urls.py.
# So we need to prefix the controller with 'auth' or mount it differently.
# NinjaJWTDefaultController usually provides /token/pair etc.
# If we want /api/auth/pair, we need to register it with a prefix or change api mount.
# But "create api path /api/auth" was the instruction.
# Since api is at /api/, registering controller usually adds paths.
# Let's try to register it with prefix, or check docs.
# NinjaExtraAPI doesn't have a simple "register with prefix" for controllers that I recall easily without checking docs.
# But we can try just changing the mount in urls.py to /api/auth/ or modifying the router.

# Actually, the user said "create api path /api/auth".
# Currently it is /api/token/pair.
# If I change urls.py to path("api/auth/", api.urls), then it becomes /api/auth/token/pair.
# Let's do that.

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
