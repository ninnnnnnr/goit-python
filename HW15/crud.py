import db_models
from sqlalchemy.orm import Session


def get_first_source_item(db: Session, item_id: int):
    return db.query(db_models.FirstSource).filter(db_models.FirstSource.id == item_id).first()


def get_second_source_item(db: Session, item_id: int):
    return db.query(db_models.SecondSource).filter(db_models.SecondSource.id == item_id).first()


def get_first_source_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.FirstSource).offset(skip).limit(limit).all()


def get_second_source_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.SecondSource).offset(skip).limit(limit).all()