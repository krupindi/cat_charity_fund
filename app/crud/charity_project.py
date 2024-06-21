from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectUpdate
)


class CRUDCharityProject(
    CRUDBase[CharityProject, CharityProjectCreate, CharityProjectUpdate]):
    async def get_by_name(
            self,
            name: str,
            db: AsyncSession
    ) -> Optional[CharityProject]:
        result = await db.execute(
            select(self.model).filter(self.model.name == name))
        return result.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
