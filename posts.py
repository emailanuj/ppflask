from flask import Flask,render_template
app = Flask(__name__)

@app.route('/posts')
def posts():
   all_posts=[
      {
         'title':'This is post One',
         'description':'This is post description One'
      },
       {
         'title':'This is post Two',
         'description':'This is post description Two'
      },
       {
         'title':'This is post Three',
         'description':'This is post description Three'
      }
   ]
   return render_template('posts.html',post_list=all_posts)

if __name__ == '__main__':
   app.run()