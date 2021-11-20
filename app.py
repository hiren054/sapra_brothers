from flask import Flask, render_template,request
from flask.helpers import url_for
from werkzeug.utils import redirect
from data import clients, portfolios, testimonials
from flask_mail import Mail, Message

app = Flask(__name__)

mail = app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'your@gmail.com',
	MAIL_PASSWORD = 'yourpassword'
	)
    
mail = Mail(app)

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
	if request.method == 'POST' :
		full_name = request.form.get('Full Name')
		email = request.form.get('Email')
		msg = request.form.get('Message')
		msg = Message('Test', sender='Our_id@gmail.com',recipients=[email])
		msg.body = f'Hello {full_name}<br>Thanks for Contacting Us <br> We will revert Back to you soon'
		mail.send(msg)
		print('MESSAGE SENT')
		return redirect(url_for('/'))
	return render_template("base.html",clients = clients,portfolios = portfolios,testimonials = testimonials)

app.run(debug=True)
