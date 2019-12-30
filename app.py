from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fddddddddddd'

post = [
    {
        'id': '1',
        'title': 'Blog Post 1',
        'body': 'First post content',
        'author': 'Ansarul'
    },
    {
        'id': '5',
        'title': 'Blog Post 5',
        'body': 'First post content',
        'author': 'Ansarul Mulla2'
    }
]

@app.route('/')
def index():
    return render_template('index.html',post=post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return 'Logout Successfull'



if __name__=="__main__":
    app.run(debug=True)