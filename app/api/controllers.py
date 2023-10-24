from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_name_duplicate,
    get_project_or_404,
    check_update_fully_invested,
    check_update_project,
    check_invested_amount_is_null,
    check_fully_invested
)
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate
)
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import CreateDonationBase
from app.services.investment import charges


async def create_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Проверка на дублирование имени проекта.
    Создание нового проекта благотворительности
    """

    await check_name_duplicate(project.name, session)
    project = await charity_project_crud.create(project, session)
    await charges(
        undivided=project,
        crud_class=donation_crud,
        session=session
    )
    return project


async def chek_validate_update_project(
    project,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Проверка благотворительного проекта на инсветирование.
    Обновление информации о проекте благотворительности.
    """

    check_update_fully_invested(project)
    if obj_in.full_amount is not None:
        project = check_update_project(
            project,
            obj_in.full_amount
        )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    project = await charity_project_crud.update(
        project, obj_in, session
    )
    return project


async def remove_and_check_validation_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Проверка проекта на валидность для удаления,
    и его удаление.
    """
    project = await get_project_or_404(project_id, session)
    check_invested_amount_is_null(project)
    check_fully_invested(project)
    project = await charity_project_crud.remove(project, session)

    return project


async def create_donation_and_update_information(
    donation: CreateDonationBase,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """
    Создание нового пожертвования
    и обновление информации о нем в базе данных.
    """
    new_donation = await donation_crud.create(
        donation, session, user
    )
    await charges(
        undivided=new_donation,
        crud_class=charity_project_crud,
        session=session
    )
    return new_donation
