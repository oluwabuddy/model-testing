import time
import numpy as np
from typing import Annotated
from uuid import uuid4
from fastapi import Query
from sqlmodel import Session, select
from datetime import datetime

from api.persistence.ai_model import AIModel


class AIModelService:

    @staticmethod
    def create(db: Session, name: str):
        ai_model = AIModel(
            id=uuid4().hex,
            name=name
        )

        db.add(ai_model)
        db.commit()
        db.refresh(ai_model)

        return ai_model

    @staticmethod
    def update(db: Session, model: AIModel):
        time.sleep(300)

        model.status = 'SUCCESS'
        model.updated_at = datetime.now()

        db.add(model)
        db.commit()
        db.refresh(model)

        return model

    @staticmethod
    def get(db: Session, model_id: str):
        return db.get(AIModel, model_id)


    @staticmethod
    def get_model_data(db: Session, model_id: str):
        _model =  db.get(AIModel, model_id)

        if _model.status == 'SUCCESS':
            return {
                 'a': np.random.randn(20).tolist(),
                 'b': np.random.randn(20).tolist(),
                 'c': np.random.randn(20).tolist(),
            }


    @staticmethod
    def list_models(
        db: Session,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        ) -> list[AIModel]:
            heroes = db.exec(select(AIModel).order_by('updated_at').offset(offset).limit(limit)).all()
            return heroes