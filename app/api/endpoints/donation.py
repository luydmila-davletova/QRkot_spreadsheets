from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.donation import (
    CreateDonationBase, DonationBaseDB,
    DonationUserDB
)
from app.api.controllers import create_donation_and_update_information
from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User


router = APIRouter()


@router.post(
    '/',
    response_model=DonationUserDB,
    response_model_exclude_none=True,
)
async def create_donation(
    donation: CreateDonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """
    Cоздает новое пожертвование.
    """
    new_donation = await create_donation_and_update_information(
        donation, session, user
    )
    return new_donation


@router.get(
    '/',
    response_model=List[DonationBaseDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возвращает список всех пожертвований.
    """
    all_donation = await donation_crud.get_multi(session)
    return all_donation


@router.get(
    '/my',
    response_model=List[DonationUserDB],
)
async def get_my_donations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Возвращает список пожертвований пользователя.
    """
    reservations = await donation_crud.get_by_user(
        session=session, user=user
    )
    return reservations


@router.delete(
    '/{donat_id}',
    tags=('donation'),
    deprecated=True
)
async def delete_donation(donat_id: int):
    """
    Удаляет пожертвование с указанным идентификатором.
    """
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail='Удаление донатов запрещено!'
    )


@router.patch(
    '/{donat_id}',
    tags=('donation'),
    deprecated=True
)
def update_donation(donat_id: str):
    """
    Обновляет пожертвование с указанным идентификатором.
    """
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail='Изменение донатов запрещено!'
    )
