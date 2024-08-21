from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
