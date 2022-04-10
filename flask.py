from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6eb950d66f41f9cb7abd79a9f3b498c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(20), unique=True, nullable=False)
                email = db.Column(db.String(20), unique=True, nullable=False)
                    password = db.Column(db.String(40), nullable=False)

                        def __repr__(self):
                                    return f"User('{self.username}', '{self.email}')"


                                posts = [
                                            {
                                                        'author' : 'Hriddhiraj S',
                                                                'title' : 'Blog Post 1',
                                                                        'content' : 'Contents of 1st blog',
                                                                                'date' : 'Feb 14th, 2022'

                                                                                    },
                                                {
                                                            'author' : 'Anupam R',
                                                                    'title' : 'Blog Post 2',
                                                                            'content' : 'Contents of 2st blog',
                                                                                    'date' : 'Feb 14th, 2022'

                                                                                        }
                                                ]


                                @app.route("/")
                                @app.route("/home")
                                def home():
                                        return render_template('home.html', posts =  posts)

                                    @app.route("/about")
                                    def about():
                                            return render_template('about.html', title = 'About')

                                        @app.route("/register", methods= ['GET', 'POST'])
                                        def register():
                                                form = RegistrationForm()
                                                    if form.validate_on_submit():
                                                                flash(f'Account created for {form.username.data}!', 'success')
                                                                        return redirect(url_for('home'))
                                                                        return render_template('register.html', title = 'Register', form=form)

                                                                    @app.route("/login" , methods= ['GET', 'POST'])
                                                                    def login():
                                                                            form = LoginForm()
                                                                                return render_template('login.html', title = 'Login', form=form)
                                                                              
                                                                            if __name__== '__main__':
                                                                                    app.run(debug=True)
