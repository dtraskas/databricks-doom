import logging
import os

from flask import Flask, render_template

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 8000))

    app.run(debug=True, host=host, port=port)
    print(f"Flask app running on http://{host}:{port}")
