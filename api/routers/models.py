from sqlmodel import Session
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from typing import Sequence

from api.config.db import get_session
from api.persistence.ai_model import AIModel
from api.services.ai_model_service import AIModelService


router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}},
)


class AIModelRequest(BaseModel):
    name: str


@router.post("/")
async def create_model(model: AIModelRequest, background_task: BackgroundTasks, db: Session = Depends(get_session)):
    _model =  AIModelService.create(
        db=db,
        name=model.name
    )

    background_task.add_task(AIModelService.update, db=db, model=_model)

    return _model


@router.get("/")
async def list_models(db: Session = Depends(get_session)) -> Sequence[AIModel]:
    # TODO: inject pagination from GET parameters
    return AIModelService.list_models(db=db)


@router.get("/{model_id}")
async def get_model(model_id: str, db: Session = Depends(get_session)) -> AIModel:
    _model = AIModelService.get(db=db, model_id=model_id)

    if not _model:
        raise HTTPException(status_code=404, detail="Model not found")

    return _model


@router.get("/{model_id}/data")
async def get_model_results(model_id: str, db: Session = Depends(get_session)):
    _data = AIModelService.get_model_data(db=db, model_id=model_id)

    if not _data:
        raise HTTPException(status_code=404, detail="Model is either not ready or not found")

    return _data