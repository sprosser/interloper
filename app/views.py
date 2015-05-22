from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'name': 'Steve'} # fake user
    teams = [
        {
            'team_captain': {'name': 'Joe Mama'},
            'members': 'Joe, Jim, and Jack'
        },
        {
            'team_captain': {'name': "Mr. Sea Otter"},
            'members': 'Mr. Sea Otter, Mrs. Sea Otter, and Nigel'
        }
            ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            teams=teams)

