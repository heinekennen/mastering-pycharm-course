from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b144b22105d4e5d9ca59d681dbe6c81316e1369c848d13dc'
bootstrap = Bootstrap(app)

keys_posts = [
    {
        'staff': 'Haydn M',
        'fob_number': 'Fob - 144717',
        'omega_AH1331KN_MKT': 'MKT 23',
        'omega_G61040_MK': 'MK 13',
        'omega_G61040_GL1': 'GL1 12',
        'date_assigned':'January 12, 2016',
        'date_returned': 'November 26, 2021'
    },
    {
        'staff': 'Steve',
        'fob_number': 'Fob - 144711',
        'omega_AH1331KN_MKT': 'MKT 22',
        'omega_G61040_MK': 'MK 13',
        'omega_G61040_GL1': 'GL1 12',
        'date_assigned': 'January 12, 2016',
        'date_returned': 'November 26, 2021'
    }
]


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template('index.html', posts=keys_posts)


@app.route('/admin')
def about():  # put application's code here
    return render_template('admin.html', posts=keys_posts)


@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/keys')
def keys():
    return render_template('keys.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()

