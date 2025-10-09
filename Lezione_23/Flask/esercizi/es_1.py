from flask import Flask


app=Flask(__name__)

@app.route('/about')
def about()->str:
    return f"<h3>Ciao sono il tuo assistente come posso aiutarti<h3/>"



app.run(debug=True,host='127.0.0.1',port=5000) 