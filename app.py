from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "my-secret-key"

@app.route('/api/hs/open', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def open_route():

    key = request.headers.get("X-API-Key")

    if key != API_KEY:
        return jsonify({"error": "invalid api key"}), 401

    return jsonify({
        "method": request.method,
        "headers": dict(request.headers),
        "query": request.args.to_dict(),
        "body": request.get_data(as_text=True)
    })
