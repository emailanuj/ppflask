from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return '<h1>Index HTML</h1>'

@app.route('/render_html')
def render_html():
   return render_template('index.html')

@app.route('/template_inheritance')
def template_inheritance():
   return render_template('inheritance_sample.html')

if __name__ == '__main__':
   app.run()