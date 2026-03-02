from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

#CRUD
#Create, Read, Updade and Delete = Criar, Ler, Atualizar e Deletar
#Tabela: Tarefa

task = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"],description=data.get("description", ""))
    task_id_control += 1
    task.append(new_task)
    print(tasks)
    return jsonify({"nessage": "Nova tarefa criada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)