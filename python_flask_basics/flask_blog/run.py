from flask_blog import create_app

app = create_app()

## to run in python directly
if __name__ == '__main__':
    app.run(debug=True)