from flask import Flask, jsonify, abort, make_response, request,render_template

app = Flask(__name__)

players = [
    {
        'id':1,
        'email': 'virat@xyz.com',
        'name': 'Virat',
        'skill': 'batsman',
        'team':'RCB',
        'price':'150000000'
    },
      {
        'id':2,
        'email': 'rohit@xyz.com',
        'name': 'Rohit',
        'skill': 'batsman',
        'team':'MI',
        'price':'140000000'
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/data')
@app.route('/ipl/api/v1.0/players', methods=['GET'])
def get_players():
    return jsonify({'players': players}),render_template('data.html',players=players)

@app.route('/ipl/api/v1.0/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    return jsonify({'player': player[0]})


@app.route('/ipl/api/v1.0/players', methods=['POST'])
def create_player():
    if not request.json or not 'email' in request.json:
        abort(400)
    player = {
        'id': players[-1]['id'] + 1,
        'email': request.json.get('email',""),
        'name': request.json.get('name',""),
        'skill': request.json.get('skill',""),
        'team': request.json.get('team',""),
        'price': request.json.get('price',""),
        #'description': request.json.get('description', ""),
    }
    players.append(player)
    return jsonify({'player': player}), 201


@app.route('/ipl/api/v1.0/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    if not request.json:
        abort(400)
    
    player[0]['email'] = request.json.get('email', player[0]['email'])
    player[0]['name'] = request.json.get('name', player[0]['name'])
    player[0]['skill'] = request.json.get('skill', player[0]['skill'])
    player[0]['team'] = request.json.get('team', player[0]['team'])
    player[0]['price'] = request.json.get('price', player[0]['price'])
    return jsonify({'player': player[0]})

@app.route('/ipl/api/v1.0/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    player = [player for player in players if player['id'] == player_id]
    if len(player) == 0:
        abort(404)
    players.remove(player[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True,port=8000)
