import datetime

from sqlalchemy import select, and_, update, func, desc
from sqlalchemy.ext.asyncio import AsyncSession, async_session, create_async_engine
from sqlalchemy.orm import sessionmaker
import typing
from .models import Base, User, BannedUser, Ticket


class Userdb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_user(
            self,
            user_id: int,
            username: str,
            name: str,
            surname: str
    ) -> None:
        """Add user in db"""

        async with self.async_session() as s:
            u = User(
                user_id=user_id, username=username, name=name, surname=surname)
            s.add(u)
            await s.commit()

    async def delete_user(self, user_id: int) -> None:
        """Delete user from db"""
        async with self.async_session() as s:
            q = select(User).where(
                and_(User.user_id == user_id)
            )
            u = (await s.execute(q)).scalar()
            await s.delete(u)
            await s.commit()

    async def update_user(self, user_id: int, **kwargs) -> None:
        """Update user in db"""
        async with self.async_session() as s:
            q = select(User).where(User.user_id == user_id)
            u = (await s.execute(q)).scalar()
            for key, value in kwargs.items():
                setattr(u, key, value)
            await s.commit()

    async def get_user(self, user_id: int) -> typing.Optional[User]:
        """Get info a user from db"""
        async with self.async_session() as s:
            q = select(User).where(User.user_id == user_id)
            u = await s.execute(q)

            try:
                return u.fetchone()[0]
            except TypeError:
                return None

    async def get_all(self) -> typing.Union[typing.List[User], list]:
        async with self.async_session() as s:
            q = select(User)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0].user_id for i in all]
            except:
                return []

    async def get_all_users_obj(self) -> typing.Union[typing.List[User], list]:
        async with self.async_session() as s:
            q = select(User)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0] for i in all]
            except:
                return []


class Ticketdb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_ticket(
            self,
            user_id: int,
            number: int,
    ) -> None:
        """Add user in db"""

        async with self.async_session() as s:
            u = Ticket(
                user_id=user_id, date=datetime.datetime.now(), number=number)
            s.add(u)
            await s.commit()

    async def delete_ticket(self, user_id: int) -> None:
        """Delete user from db"""
        async with self.async_session() as s:
            q = select(Ticket).where(
                and_(Ticket.user_id == user_id)
            )
            u = (await s.execute(q)).scalar()
            await s.delete(u)
            await s.commit()

    async def update_ticket(self, user_id: int, **kwargs) -> None:
        """Update user in db"""
        async with self.async_session() as s:
            q = select(Ticket).where(Ticket.user_id == user_id)
            u = (await s.execute(q)).scalar()
            for key, value in kwargs.items():
                setattr(u, key, value)
            await s.commit()

    async def get_ticket(self, user_id: int) -> typing.Optional[Ticket]:
        async with self.async_session() as s:
            q = select(Ticket).where(Ticket.user_id == user_id)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0] for i in all][-1]
            except TypeError:
                return None

    async def get_ticket_by_id(self, id: int) -> typing.Optional[Ticket]:
        async with self.async_session() as s:
            q = select(Ticket).where(Ticket.id == id)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0] for i in all][-1]
            except TypeError:
                return None

    async def get_all_users_obj(self) -> typing.Union[typing.List[Ticket], list]:
        async with self.async_session() as s:
            q = select(Ticket)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0] for i in all]
            except:
                return []

class BannedUserdb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_user(self, user_id: int) -> None:
        """Add user in db"""
        async with self.async_session() as s:
            u = BannedUser(user_id=user_id)
            s.add(u)
            await s.commit()

    async def delete_user(self, user_id: int) -> None:
        """Delete user from db"""
        async with self.async_session() as s:
            q = select(BannedUser).where(BannedUser.user_id == user_id)
            u = (await s.execute(q)).scalar()
            await s.delete(u)
            await s.commit()

    async def get_all(self) -> typing.Union[typing.List[BannedUser], list]:
        async with self.async_session() as s:
            q = select(BannedUser)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0].user_id for i in all]
            except:
                return []