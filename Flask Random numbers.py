import random
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import validators, StringField

random.seed(105)

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

	number = None

	@classmethod
	def new_number(cls, limit):
		cls.number = random.randint(1, limit)
		print('загадано число', cls.number)

	

@app.route('/', methods=['GET'])
def home():
	if request.method == 'GET':
		RandomNubmers.new_number(100)
		return 'Число загадано'


@app.route('/guess', methods=['POST'])
def guess():
	if request.method == 'POST':
		rn = RandomNubmers.randnum()
		randnum = 9
		print(randnum)
		guess = int(request.form['guess'])
		print(guess)
		if guess > randnum:
			return '>'
		elif guess < randnum:
			return '<'
		elif guess == randnum:
			randnum = next(rn)
			return '='


if __name__ == '__main__':
	app.run()
