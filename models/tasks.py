from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Tasks(Base):

    __tablename__ = 'Tasks'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int] = mapped_column(nullable=False)



class Categories(Base):

    __tablename__ = 'Categories'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    type: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str]
