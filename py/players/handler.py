import json

def _player(player_id, name):
    return {
        "id": player_id,
        "name": name
    }

playersData = [
    _player("1", "Scott"),
    _player("2", "Ross"),
    _player("3", "Peter"),
    _player("3", "Andy")
]

def players(event, context):
    body = {"players": playersData}

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def player(event, context):
    player_id = event["pathParameters"]["id"]
    single_player_as_list = [p for p in playersData if p["id"] == player_id]
    selected_player = {
        "_meta": "single player",
        "data": next(iter(single_player_as_list), None)
    }

    return {
        "statusCode": 200,
        "body": json.dumps(selected_player)
    }
