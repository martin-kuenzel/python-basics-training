from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Mike Miller",
        "title" : "First Post",
        "content": "Post Content",
        "date_created": "10/10/1924"
    },
    {
        "author": "Mike Miller",
        "title" : "Second Post",
        "content": "Post Content",
        "date_created": "15/10/1954"
    }
]

@app.route('/')
@app.route('/home')
@app.route('/Home')
def posts_list():
    return render_template('home.html',posts=posts)

@app.route('/posts_detail')
def posts_detail():
    post_id = int(request.args.get("id"))
    if posts[post_id] is None: 
        return f'post with this id does not exist'
    return render_template('posts_detail.html',post=posts[post_id])

@app.route('/about')
def about():
    return render_template('about.html',title="About")

## to run in python directly
if __name__ == '__main__':
    app.run(debug=True)