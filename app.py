from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET','POST'])
def entryPoint():

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        content = request.form.get('post')
        create_post(name, content)

    tweets = get_posts()

    return render_template('index.html', posts=tweets)


if __name__ == "__main__":
    app.run(debug=True)