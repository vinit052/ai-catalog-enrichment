from fastapi import Depends
from sqlalchemy.orm import Session

from core.infra.database.session import get_db
from core.repositories.import_repository import ImportRepository
from core.repositories.item_repository import ItemRepository
from core.services.import_service import ImportService


def get_import_service(
    db: Session = Depends(get_db),
):

    import_repository = ImportRepository(
        db
    )

    item_repository = ItemRepository(
        db
    )


    return ImportService(
        db=db,
        import_repository=import_repository,
        item_repository=item_repository,
    )