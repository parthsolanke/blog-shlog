import requests
from flask import Flask, render_template
app = Flask(__name__)
ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"


@app.route('/')
def home():
    response = requests.get(ENDPOINT)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:index>')
def read(index):
    response = requests.get(ENDPOINT)
    all_posts = response.json()
    return render_template("post.html", post=all_posts[index-1])

if __name__ == "__main__":
    app.run(debug=True)
