from pathlib import Path
import shutil
import uuid

from fastapi import UploadFile


UPLOAD_DIR = Path("uploads")

UPLOAD_DIR.mkdir(
    exist_ok=True
)


ALLOWED_EXTENSIONS = {
    ".csv",
    ".xlsx",
    ".xls",
    ".png",
    ".jpg",
    ".jpeg",
}


def validate_file(filename: str) -> bool:
    extension = Path(filename).suffix.lower()

    return extension in ALLOWED_EXTENSIONS


def save_file(file: UploadFile) -> dict:
    extension = Path(file.filename).suffix.lower()

    file_name = f"{uuid.uuid4()}{extension}"

    file_path = UPLOAD_DIR / file_name

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "original_file": file.filename,
        "stored_file": file_name,
        "path": str(file_path),
    }