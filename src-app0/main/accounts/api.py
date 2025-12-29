from ninja import NinjaAPI
from django.contrib.auth import authenticate
from django.http import HttpRequest
from .schemas import LoginSchema, TokenSchema
from .utils import generate_tokens

api = NinjaAPI()

@api.post("/login", response=TokenSchema)
def login(request: HttpRequest, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)
    if user is not None:
        tokens = generate_tokens(user)
        return tokens
    else:
        return api.create_response(request, {"detail": "Invalid credentials"}, status=401)
