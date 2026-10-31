from fastapi import APIRouter, Depends, File, UploadFile, status ,HTTPException ,Query
from sqlalchemy.orm import Session
import uuid

from database import get_db
from models import Extraction, ExtractionStatus
from shemas import ExtractionOut,ExtractionListOut
from services.extraction import ExtractionError, extract

router = APIRouter(prefix="/extractions", tags=["extractions"])


@router.post("", response_model=ExtractionOut, status_code=status.HTTP_201_CREATED)
async def create_extraction(file: UploadFile = File(...), db: Session = Depends(get_db)):
    nouvelle_extraction = Extraction(
        filename=file.filename,
        content_type=file.content_type,
    )

    db.add(nouvelle_extraction)
    db.commit()
    db.refresh(nouvelle_extraction)

    file_bytes = await file.read()

    try:
        donnees_extraites = extract(file_bytes, file.content_type)
        nouvelle_extraction.extracted_data = donnees_extraites
        nouvelle_extraction.status = ExtractionStatus.completed
    except ExtractionError as erreur:
        nouvelle_extraction.status = ExtractionStatus.failed
        nouvelle_extraction.error_message = str(erreur)

    db.commit()
    db.refresh(nouvelle_extraction)


    return nouvelle_extraction

@router.get("/{extraction_id}", response_model=ExtractionOut)
async def get_extraction(extraction_id: uuid.UUID, db: Session = Depends(get_db)):
    extraction = db.get(Extraction, extraction_id)

    if extraction is None:
        raise HTTPException(status_code=404, detail="Extraction introuvable")

    return extraction


@router.get("", response_model=ExtractionListOut)
async def list_extractions(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    total = db.query(Extraction).count()

    items = (
        db.query(Extraction)
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return ExtractionListOut(total=total, page=page, page_size=page_size, items=items)


@router.delete("/{extraction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_extraction(extraction_id: uuid.UUID, db: Session = Depends(get_db)):
    extraction = db.get(Extraction, extraction_id)

    if extraction is None:
        raise HTTPException(status_code=404, detail="Extraction introuvable")

    db.delete(extraction)
    db.commit()

    return None