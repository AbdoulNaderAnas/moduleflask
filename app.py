from flask import Flask, render_template,request
from classe import Student

app = Flask(__name__)

#routage
@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get("user_name")
        age = request.form.get("age")
        classe =request.form.get("classe")
        user = Student()
        user.add_student(name,age,classe)
       
    
    return render_template('index.html')

@app.route('/hello')
def students():
    return 'Hello, World coco'
@app.route('/students/<int:id>')
def get_students(id):
    return f"<h1>je suis l'eleve {id}</h1>:"
