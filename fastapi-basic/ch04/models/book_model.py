from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base 

# id : int
# title : str
# price : int
# isbn : int

class TodoModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    price: Mapped[str] = mapped_column(
        int(6),
        nullable=True
    )

    isbn: Mapped[str] = mapped_column(
        int(4),
        nullable=True
    )
   