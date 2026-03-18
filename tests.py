import pytest
import requests

#CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
        }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    print("BASE_URL:", repr(BASE_URL))
    print("URL final:", f"{BASE_URL}/tasks")
    print(response.text)  #ajuda a ver o retorno do servidor
    assert response.status_code == 200
    
    