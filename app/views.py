from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID-"%s", remember_me=%s' %
                (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])
