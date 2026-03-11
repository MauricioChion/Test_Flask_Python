from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

#CRUD
#Create, Read, Updade and Delete = Criar, Ler, Atualizar e Deletar
#Tabela: Tarefa

#Segue a abaixo a classe Task que foi importada
# class Task:
#     def __init__(self, id, title, description, completed=False):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.completed = completed

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "description": self.description,
#             "completed": self.completed
#         }

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control, 
        title=data["title"],
        description=data.get("description", ""),
        completed=data.get("completed", False)
        )
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"nessage": "Nova tarefa criada com sucesso"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data ["title"]
    task.description = data ["description"]
    task.completed = data["completed"]
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"}), 200

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = None
    for i in tasks:
        if i.id == id:
            task = i
            break

    if task is None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa removida com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)