from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    JSON,
    Boolean,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from core.infra.database.base import Base


class Item(Base):

    __tablename__ = "items"


    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )


    import_id: Mapped[int] = mapped_column(
        ForeignKey("imports.id"),
        nullable=False,
        index=True,
    )


    product_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )


    enrich_data: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
    )


    review_status: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )


    comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


    import_record: Mapped["Import"] = relationship(
        "Import",
        back_populates="items",
    )