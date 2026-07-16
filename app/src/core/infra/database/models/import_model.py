from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Text,
    DateTime,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from core.infra.database.base import Base


class Import(Base):

    __tablename__ = "imports"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )


    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )


    total_records: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )


    valid_records: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )


    invalid_records: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )


    error_file_path: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    items: Mapped[list["Item"]] = relationship(
        "Item",
        back_populates="import_record",
        cascade="all, delete-orphan",
    )