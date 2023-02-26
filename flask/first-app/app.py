"""
FLASK NOTES:
-The first step to create a flask app is to create a flask object.
-The second step is to create different functions to perform actions over the app
    -Every function will be decorated to add the route that will call that function
"""

# Imports
from flask import Flask, render_template, request, redirect, url_for



# Create flask first-app (an instance of flask)
app = Flask(__name__)


# --------- Database ---------
# We use a dictionary to store data to simplify things so our app will not have persistance
POSTS = {
    0: {
        'post_id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


# --------- Functions ---------

@app.route('/')
def home():
    """
    @app.route is a decorator that adds the route that will call the function
        -It basically calls the route function from our flask object

    Return a rendered template to the home page
    The connection goes as follows:
        -User types a website into the browser
        -Browser sends us a request for the indicated website
        -Then, we run the function for the proper website and return something
    """
    return render_template('home.jinja2', posts=POSTS)


@app.route('/hello')
def hello_world():
    # Display a message in the browser
    return 'Hello, World!'


@app.route('/post/<int:post_id>')
def post(post_id):
    """
    Return a rendered template to a post

    <int:post_id> is flask syntax to indicate that the value here is the value of the integer parameter post_id

    render_template('template_name', *args) -> render a template from templates into the browser
        -We can pass named arguments that will become variables in the html file
    """
    # Assign values from our dictionary based on post_id
    v_post = POSTS.get(post_id)

    if not v_post:
        # if post_id not found
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')
    else:
        return render_template(template_name_or_list='post.jinja2', post=v_post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    """
    This method return two different urls:
        -If the user loads our website, return rendered template 'create.jinja2' to create a form
        -If the user submits a form, save data to our database and redirect the browser to 'post' function
        to display that data

    methods=[...] is a parameter that indicates what kind of requests can accept our function

    Browsers always sends 'GET' to load the page and 'POST' once a user press submit in a form
        -To hide information when sending data to an HTML form, we use 'request.form' instead of 'request.args'

    redirect(url)              -> return a response object that, if called, redirects the client to the target location
    url_for('function', *args) -> return the route associated with the indicated function
        -We can pass named arguments that will become variables in the html file
    """
    if request.method == 'POST':
        # Save title and content from the submitted form
        title = request.form.get('title')
        content = request.form.get('content')
        # Get post_id integer value
        post_id = len(POSTS)
        # Add data to POSTS
        POSTS[post_id] = {'id': post_id, 'title': title, 'content': content}
        # Redirect browser to 'post' function
        return redirect(url_for('post', post_id=post_id))
    # If the method is 'GET', we have just loaded the '/post/create' url so we can render the form.
    return render_template('create.jinja2')








# --------- Run flask app ---------

if __name__ == '__main__':
    print(POSTS.items())

    # Set debug=True for development purposes only
    app.run(debug=True)
