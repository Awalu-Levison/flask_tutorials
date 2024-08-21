from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

"""Set up secret key to avoid cross site scripting attacks"""
app.config['SECRET_KEY'] = '82f3b2a95b230b4941abe57a985edebc'

posts = [
    {
        'author': 'Awalu Levison',
        'title': 'My Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Augut 3, 2024'
    },
    {
        'author': 'Innocent Mkuleza',
        'title': 'My Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Augut 4, 2024'
    }
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
