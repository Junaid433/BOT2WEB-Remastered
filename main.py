from flask import Flask, render_template, request
from api import vbv_bp, chk_bp, process_bp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(process_bp)
app.register_blueprint(vbv_bp)
app.register_blueprint(chk_bp)

app.run(host='0.0.0.0')