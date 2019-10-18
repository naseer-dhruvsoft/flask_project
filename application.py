
from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_name():
  return 'Hello World! This is Naseer'

# @application.route('/')
# def hello_guest():
# 	return render_template('hello.html',name='guest')

if __name__ == '__main__':
  application.run()

