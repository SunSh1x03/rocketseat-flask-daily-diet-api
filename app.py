from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

task= []
task_id_control = 1

@app.route('/task', methods=['POST'])
def create_task():
    global task_id_control
    data= request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1 
    task.append(new_task)
    return jsonify({"message": "Nova refeição adicionada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)