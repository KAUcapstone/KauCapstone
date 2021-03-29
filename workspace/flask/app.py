from flask import Flask, jsonify, request, make_response, send_file
import datetime as dt

app = Flask(__name__)
app.config["CORS_HEADERS"] = 'Content-Type'
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def main():
    return "this is main page"

@app.route('/image_search')
def search_by_image():
    return "image search page"

@app.route("/mypage")
def mypage():
    return "my page"

@app.route("/login")
def login():
    return "login"

@app.route("/write_post")
def write_post():
    return "write posting page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000", debug=True)
