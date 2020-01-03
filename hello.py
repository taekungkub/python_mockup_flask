from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/') 
def index():

    return "hello world"

if __name__=='__main__':
    app.run(debug=True, port=5000)