# https://github.com/505598397/django-jwt-decorator
# pip install pyjwt

import jwt

SECRET = "abc"
USERS = [
    {"id": 1, "username": "yassine"},
    {"id": 2, "username": "mohammed"},
]


def generate_token(user_id: int) -> str:
    token = jwt.encode({"id": user_id}, SECRET, algorithm="HS256")
    return token


def check_jwt_token(func):
    def wrapper(*args, **kwargs):
        token = args[0].get("token")
        # bearer_token = request.headers.get("Authorization", None)
        # token = bearer_token.split()[1]

        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        user_id = payload.get("id")

        existing_user = False
        for user in USERS:
            if user.get("id") == user_id:
                existing_user = True

        # this query will return the user if exist , else None
        # existing_user = User.objects.filter(id=id).first()

        if existing_user:
            func(*args, **kwargs)
        else:
            print("invalid token")

    return wrapper


@check_jwt_token
def sign_in(request):
    print("you are signed in")


sign_in({"token": "xyz"})
sign_in({"token": "xyzA"})
