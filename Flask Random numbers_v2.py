import random
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import validators, StringField



app = Flask(__name__)
app.config.update(
	DEBUG=True,
	SECRET_KEY='This key must be secret!',
	WTF_CSRF_ENABLED=False
)

class GuessNumbers(FlaskForm):
	guess = StringField(label='Guess', validators=[
		validators.Length(min=1, max=1)
	])

class RandomNubmers(object):
	random.seed(105)

	def __init__(self, number):
		self.number = number

	def new_number(self):
		self.number = random.randint(1, 100)
		print('загадано число', self.number)

RANDNUM = RandomNubmers(None)


@app.route('/', methods=['GET'])
def home():
	if request.method == 'GET':
		RANDNUM.new_number()
		return 'Число загадано'


@app.route('/guess', methods=['POST'])
def guess():
	if RANDNUM.number is None:
		return 'Число не загадано'
	if request.method == 'POST':
		print(RANDNUM.number)
		guess = int(request.form['guess'])
		print(guess)
		if guess > RANDNUM.number:
			return '>'
		elif guess < RANDNUM.number:
			return '<'
		elif guess == RANDNUM.number:
			RANDNUM.new_number()
			return '='


if __name__ == '__main__':
	app.run()
