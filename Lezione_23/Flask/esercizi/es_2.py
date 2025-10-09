
from flask import Flask

app=Flask(__name__)

#dianmic route 

@app.route('/user/<string:username>')
def show_user(username:str)->str:
    return f"Profilo di {username}"

@app.route('/square/<int:n>')
def show_id(n:int)->str:
    return f"id numero: {n}"
   



app.run(debug=True,host='127.0.0.1',port=5000) 