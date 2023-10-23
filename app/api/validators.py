from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    """
    Проверяет наличие другого проекта с таким же именем.
    """
    project_id = await charity_project_crud.get_project_id_by_name(
        project_name,
        session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_exists_and_return(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """
    Проверяет существование проекта по его идентификатору
    И возвращает его, если он существует.
    """
    project = await charity_project_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найден!'
        )
    return project


def check_update_project(
        project,
        full_amount: int,
) -> CharityProject:
    """
    Проверяет возможность обновления проекта.
    """
    if project.invested_amount is not None:
        if project.invested_amount > full_amount:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=('Сумма для закрытия проекта не может'
                        ' быть меньше чем сумма, которую внесли в проект')
            )
        if project.invested_amount == full_amount:
            project.fully_invested = True
    return project


def check_invested_amount_is_null(project) -> None:
    """
    Проверяет, что сумма внесенных средств в проект равна нулю.
    """
    if project.invested_amount != 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )


def check_fully_invested(project) -> None:
    """
    Проверяет, что проект полностью закрыт и не может быть удален.
    """
    if project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Нельзя удалять закрытые проекты'
        )


def check_update_fully_invested(project) -> CharityProject:
    """
    Проверяет, что проект не является закрытым и может быть отредактирован.
    """
    if project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )
    return project
