from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#root
def test_root():
    response = client.get('/')
    
    assert response.status_code == 200

# get tasks
def test_list_tasks():
    response = client.get('/tasks')
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
# post
def test_create_task():
    response = client.post(
        '/tasks',
        json = {
            'title': 'Task!', 
            'description': 'Description!'
        })
    
    assert response.status_code == 201
    assert response.json()['title'] == 'Task!'
    assert response.json()['description'] == 'Description!'

# get task
def test_get_task():
    response = client.get('/tasks/3')
    
    assert response.status_code == 200 #or 404

# put task 
def test_update_task():
    response = client.put(
        '/tasks/3',
        json= {
            'title': 'Title updated!', 
            'description': 'Description Updated!'
        })
    
    assert response.status_code == 200
    assert response.json()['title'] == 'Title updated!'
    assert response.json()['description'] == 'Description Updated!'

# Delete task
def test_delete_task():
    response = client.delete('/tasks/3')
    
    assert response.status_code == 200 #or 404
    
