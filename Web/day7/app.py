
# ----Phase1 (basic app)----------
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<h1>Hello World<h1>"

# if __name__ == "__main__":
#     app.run()
# ----Phase1 ends----------

# ----Phase2(routing)----------
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def home_page():
#     return "<h1>Hello World!! My name is Abhishek Sharma<h1>"

# @app.route("/about")
# def about_page():
#     return "<h1>I am Python developer,etc.</h1>"

# @app.route("/myprojects")
# def projects_page():
#     return "<h3>I have been  doing this and that recently.</h3>"
# if __name__ == "__main__":
#     app.run()
# ----Phase2(routing) ends----------

#-----Phase3 ( url paramaters )-------
# from flask import Flask
# app = Flask(__name__)

# @app.route("/<string:name>")
# def hello_world(name):
#     return f"<h1>Hello World from {name}<h1>"
# @app.route("/<int:id>")
# def get_user_id(id):
#     return f"<h1>User's id is: {id}<h1>"
# if __name__ == "__main__":
#     app.run()

#-----Phase3 ( url paramaters ) ends -------

#-----Phase4 ( templates and static(css))------
# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route("/")
# def home_page():
#     return render_template('home.html')

# @app.route("/about")
# def about_page():
#     return render_template('about.html')

# if __name__ == "__main__":
#     app.run()

#-----Phase5 ( context passing )------

# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route("/<string:name>")
# def home_page(name):
#     return render_template('home.html',name = name)

# @app.route("/about")
# def about_page():
#     return render_template('about.html')

# if __name__ == "__main__":
#     app.run()

# ------- ( more context now list )----------

from flask import Flask,render_template,url_for,redirect
from flask import request
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

fruits = ['apple','banana','mango']
@app.route("/fruits", methods = ['GET', 'POST'])
def my_fruits_page():
    if request.method == "POST" :
        print('post done')
        x = request.form.get('fruit')
        fruits.append(x)
        return redirect(url_for('my_fruits_page'))

    return render_template('fruits.html',fruits = fruits)

@app.route("/countries_caps")
def get_country_caps():
    countries_caps = {
    'Nepal': 'Kathmandu',
    'USA': 'Washington, D.C.',
    'Bhutan': 'Thimphu',
    'China': 'Beijing',
    'India': 'New Delhi'
    }
    return render_template('countries-caps.html',countries_caps = countries_caps)

if __name__ == "__main__":
    app.run()