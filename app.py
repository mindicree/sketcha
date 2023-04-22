# imports
from flask import Flask, render_template
from flask_socketio import SocketIO
import yaml
from gamecode import *

# configuration load
try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
except Exception as e:
    print('Could not load config file. Using Default values')
    config = {
        'HOST': '127.0.0.1',
        'PORT': '5000',
        'DEBUG': True,
        'SECRET_KEY': 'secret!'
    }

# app initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
socketio =  SocketIO(app, async_mode=None)

# main application route
@app.route('/')
def index():
    return render_template('index.html')

# socket routes
@socketio.on('connect')
def connect():
    print('Connected')

@socketio.on('disconnect')
def disconnect():
    print('Disconnected')

if __name__ == '__main__':
    socketio.run(app, host=config['HOST'], port=config['PORT'], debug=config['DEBUG'])