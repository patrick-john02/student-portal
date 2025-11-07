# users.py
# FastAPI-Users configuration for Senior High School Portal

import uuid
from typing import Optional
from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from app.db import User, get_user_db

SECRET = "CHANGE_THIS_SECRET_KEY"  # Use os.getenv("SECRET_KEY") in production


# ---------- USER MANAGER ----------
class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request=None):
        print(f"✅ New user registered: {user.email}")

    async def on_after_forgot_password(self, user: User, token: str, request=None):
        print(f"🔑 Password reset for {user.email}: {token}")

    async def on_after_request_verify(self, user: User, token: str, request=None):
        print(f"📧 Verification requested for {user.email}: {token}")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


# ---------- AUTHENTICATION ----------
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


# ---------- FASTAPI-USERS INSTANCE ----------
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

# Dependency helpers
current_active_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
