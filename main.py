from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str
    
tasks = []

@app.get('/')
def root():
    return "Hello!"

@app.get('/tasks')
def list_tasks():
    return tasks       

@app.get('/tasks/{task_id}')
def get_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
        
    raise HTTPException(
        status_code=404,
        detail="Task not found."
    )     
    
@app.post('/tasks', status_code=201)
def create_task(data_task: TaskCreate):
    task_id = 1
    
    for task in tasks:
        if task['id'] >= task_id:
            task_id = task['id'] + 1
            
    new_task = {
        'id': task_id, 
        'title': data_task.title,
        'description': data_task.description,
        'status': False
    }
    tasks.append(new_task)
    return new_task

@app.put('/tasks/{task_id}')
def update_task(task_id: int, new_data: TaskCreate):
    task = get_task(task_id)
    
    task['title'] = new_data.title
    task['description'] = new_data.description
    
    return tasks


@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    task = get_task(task_id)
    
    tasks.remove(task)
    return tasks





