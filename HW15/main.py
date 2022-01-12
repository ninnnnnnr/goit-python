import uvicorn, databases, crud, models
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from parser_news import DBSession


database = databases.Database('sqlite:///parser_news.db')
app = FastAPI()


def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


@app.get("/first_source/", response_model=List[models.FirsSource])
def read_first_source_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    first_source_all = crud.get_first_source_all(db, skip=skip, limit=limit)
    return first_source_all


@app.get("/first_source/{item_id}", response_model=models.FirsSource)
def read_first_source_item(item_id: int, db: Session = Depends(get_db)):
    first_source_item = crud.get_first_source_item(db, item_id=item_id)
    if first_source_item is None:
        raise HTTPException(status_code=404, detail="Item first source not found")
    return first_source_item


@app.get("/second_source/", response_model=List[models.SecondSource])
def read_second_source_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    second_source_all = crud.get_second_source_all(db, skip=skip, limit=limit)
    return second_source_all


@app.get("/second_source/{item_id}", response_model=models.SecondSource)
def read_second_source_item(item_id: int, db: Session = Depends(get_db)):
    second_source_item = crud.get_second_source_item(db, item_id=item_id)
    if second_source_item is None:
        raise HTTPException(status_code=404, detail="Item second source not found")
    return second_source_item


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8080,
        reload=True
    )
