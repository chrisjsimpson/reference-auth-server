#Install

pip intall -r requirements.txt

# Run

```
export FLASK_APP=main.py
export FLASK_DEBUG=True

flask run

```

# Validate

Valid auth token:

`curl -v -X GET http://127.0.0.1:5000/verify-passthrough-token?passthrough-token=08517bfa-5227-43ff-9bdc-9ff81485103c`

Invalid token:

`curl -v -X GET http://127.0.0.1:5000/verify-passthrough-token?passthrough-token=d8fc02c2-2b76-4402-8c22-504527facc14`

Invalid Request:

`curl -v -X GET http://127.0.0.1:5000/verify-passthrough-token`
