
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


def register_user(db: Session, user_data):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        return None

    user = User(
        full_name=user_data.full_name,
        email=str(user_data.email).lower(),
        password_hash=hash_password(user_data.password),
        role="CUSTOMER",
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
):
    user = (
        db.query(User)
        .filter(User.email == email.lower())
        .first()
    )

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    if not user.is_active:
        return None

    token = create_access_token(
        user_id=user.id,
        role=user.role,
    )

    return {
        "user": user,
        "access_token": token,
        "token_type": "bearer",
    }


def change_user_password(
    db: Session,
    user: User,
    current_password: str,
    new_password: str,
):
    if not verify_password(
        current_password,
        user.password_hash,
    ):
        return False

    user.password_hash = hash_password(new_password)

    db.commit()
    db.refresh(user)

    return True
