from flask import Flask, render_template, request
from flask.helpers import make_response, url_for
from werkzeug.utils import redirect
from data import clients, portfolios, testimonials
from flask_mail import Mail, Message
import config
import os


MODE = True if config.ENV == "DEV" else False
# ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
# print(ASSETS_DIR)


app = Flask(__name__)


mail = app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='tankchaitanya333@gmail.com',
    MAIL_PASSWORD='@Akshardham1837'
)


mail = Mail(app)
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        full_name = request.form.get('Full Name')
        email = request.form.get('Email')
        msg = request.form.get('Message')
        msg = Message(
            'Test',
            sender='joister333@gmail.com',
            recipients=[email]
        )
        msg.body = f'Hello {full_name}<br>Thanks for Contacting Us <br> We will revert Back to you soon'
        mail.send(msg)
        return redirect(url_for('/'))
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
    context = ('saprabrothers.crt', 'saprabrothers.key')
    app.run(debug=MODE, ssl_context=context)
