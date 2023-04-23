# imports
from flask import Flask, render_template, request, make_response, jsonify, abort
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

@app.errorhandler(500)
def server_error(error):
    json_res = {
        'status': 'error',
        'message': 'there is a server error'
    }
    return make_response(jsonify(json_res), 500)

# main application route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-player', methods=['POST'])
def route_new_player():
    try:
        new_name = request.args.get('name')
        player_id = create_new_player(new_name, new_name)
        res = {
            'status': 'success',
            'message': 'created new player successfully',
            'data': {
                'name': new_name,
                'id': player_id
            }
        }
        return make_response(jsonify(res), 201)
    except Exception as e:
        logging.error(e)
        abort(500)

@app.route('/get-player-data', methods=['GET'])
def route_get_player_data():
    player_id = request.args.get('id')
    res = {
        'status': 'success',
        'message': 'player data retrieved successfully',
        'data': {
            'characters': [],
            'items': []
        }
    }
    return make_response(jsonify(res), 200)

# socket routes
@socketio.on('connect')
def connect():
    print('Connected')

@socketio.on('disconnect')
def disconnect():
    print('Disconnected')

if __name__ == '__main__':
    socketio.run(app, host=config['HOST'], port=config['PORT'], debug=config['DEBUG'])