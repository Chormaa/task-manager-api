from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Task

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str
    
def find_task(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task is None:
        raise HTTPException(
            status_code=404,
            detail='Task not found.'
        )
    return task
    

@app.get('/')
def root():
    return {'message': 'Hello!'}

@app.get('/tasks')
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@app.post('/tasks', status_code=201)
def create_task(data_task: TaskCreate, db: Session = Depends(get_db)):
    task = Task(
        title = data_task.title,
        description = data_task.description
    )
    
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.get('/tasks/{task_id}')
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = find_task(task_id, db)

    return task

@app.put('/tasks/{task_id}')
def update_task(task_id: int, new_data: TaskCreate, db: Session = Depends(get_db)):
    task = find_task(task_id, db)
    
    task.title = new_data.title
    task.description = new_data.description
    
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = find_task(task_id, db)
    
    db.delete(task)
    db.commit()
    
    return {'message': 'Task deleted successfully!'}
