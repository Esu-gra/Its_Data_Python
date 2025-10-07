
from flask import Flask,url_for

app2=Flask(__name__)


@app2.route('/home')
def home()->str:
   return "Benvenuto nel profilo!" 

@app2.route('/show_user_profile/<string:username>')
def show_user_profile(username:str)->str:
    return f"Bentornato {username}"

@app2.route('/show_post/<int:post_id>')
def show_post(post_id:int)->str:
    return f"Post:{post_id}"

with app2.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile',username='Nino Gallo'))
    print(url_for('show_post',post_id=43))


app2.run(debug=True, host='127.0.0.1', port=5000) 
