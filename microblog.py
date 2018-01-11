from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
	"""register the function as a shell context function"""
	return {db:'db', 'User':User,'Post': Post}