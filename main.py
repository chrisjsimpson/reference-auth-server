from flask import Flask, request
app = Flask(__name__)

mock_auth_tokens = [
    'df600655-1c19-4d2d-b430-356bbff070de',
    'd9095f53-eaf5-4097-9828-d46450e1519b'
]

@app.route('/verify-passthrough-token')
def verify_passthrough_token():
    """
    Example valid request:
    http://127.0.0.1/verify-passthrough-token?passthrough-token=08517bfa-5227-43ff-9bdc-9ff81485103c
    """
    passthrough_token = request.args.get('passthrough-token', None)

    if passthrough_token is None:
        return "passthrough-token not specified", 401

    # Validate passthrough_token
    if passthrough_token in mock_auth_tokens:
        return "Valid", 200
    else:
        return "Unauthorized", 401

    return "Unknown error", 500
