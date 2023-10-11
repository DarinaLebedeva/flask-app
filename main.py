from flask import Flask

application = Flask(__name__)

@application.route("/")
def main_page():
    return "HELLO WEB"


if __name__ == '__main__':
    application.run()