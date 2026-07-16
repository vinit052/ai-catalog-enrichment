from sqlalchemy.orm import Session

from core.exceptions.database import DatabaseSaveException


class BaseRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db


    def commit(self):

        try:
            self.db.commit()

        except Exception as e:
            self.db.rollback()

            raise DatabaseSaveException(
                str(e)
            )


    def refresh(
        self,
        obj
    ):
        self.db.refresh(obj)
        return obj