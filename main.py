from flask import Flask, render_template
from flask.helpers import make_response
from data import clients, portfolios, testimonials
import config


MODE = True if config.ENV == "DEV" else False


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    response = make_response(
        render_template(
            "base.html",
            clients=clients,
            portfolios=portfolios,
            testimonials=testimonials
        )
    )
    response.cache_control.max_age = 86400
    return response


if __name__ == "__main__":
    app.run(debug=MODE)
