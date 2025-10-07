# from flask import  Flask


# # Static rout 
# app=Flask(__name__)
# @app.route('/')
# def home()->str:
#     return "<h3>Hello,World!</h3>"
 
# # Dinamic rout
# @app.route('/data')
# def data()->str:
#     return "<h3>sei uno studente Datanlyst!</h3>"

# # Dinamic rout
# @app.route('/user/<string:username>')
# def show_user_profile(username:str)->str:
#     return f"Profilo di {username}"


# # Dinamic rout
# @app.route('/post/<int:post_id>')
# def show_post(post_id:int)->str:
#     return f"Post {post_id}"


# app.run(debug=True,host='127.0.0.1',port=5000) 
