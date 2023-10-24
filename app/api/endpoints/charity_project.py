from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.controllers import (
    create_project,
    chek_validate_update_project,
    remove_and_check_validation_project
)
from app.api.validators import get_project_or_404
from app.schemas.charity_project import (
    CharityProjectDB,
    CharityProjectUpdate,
    CharityProjectCreate
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud

router = APIRouter()


@router.get(
    '/',
    response_model_exclude_none=True,
    response_model=List[CharityProjectDB]
)
async def get_project(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Получение списка всех проектов благотворительности
    """
    all_projects = await charity_project_crud.get_multi(session)
    return all_projects


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Создание нового проекта благотворительности
    """

    new_project = await create_project(project, session)
    return new_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Обновление информации о проекте благотворительности
    """
    project = await get_project_or_404(
        project_id, session
    )

    return await chek_validate_update_project(
        project, obj_in, session
     )


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def remove_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """
    Удаление проекта благотворительности
    """
    project = await remove_and_check_validation_project(
        project_id, session
    )
    return project
