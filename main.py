"""Simple flask app returning hello world."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Return hello world as string."""
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
