from flask import Flask
app = Flask(__name__)

@app.route('/abc')
def hello_world():
   return 'ABC Page'

@app.route('/hello/<string:name>')
def hello_param(name):
   return 'Hello '+name

@app.route('/hello/users/<string:name>/<int:id>')
def hello_multi_param(name,id):
   return 'Hello '+name+' your id is '+str(id)

if __name__ == '__main__':
   app.run()