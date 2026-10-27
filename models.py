"""SQLAlchemy ORM models that map Python classes to database tables."""

from sqlalchemy import Boolean, Integer, String, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# SQLAlchemy provides shared model metadata through DeclarativeBase.
class Base(DeclarativeBase):
    pass

class Task(Base):
    """Python representation of a row in the existing 'tasks' table."""
    
    # Tell SQLAlchemy which database table this model represents.
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text('false')
    )

