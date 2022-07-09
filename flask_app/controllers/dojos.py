# controllers.dojos
# Import app
from flask_app import app
# Import modules from flask
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app.models import dojo

# Import models class
# Example: from flask_app.models.dojo import Dojo

# Create the routes

@app.route('/')
def index():
    """POST input"""
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    """Write values to db"""
    # check for errors
    # Call the staticmethod on Dojo model to validate
    if not dojo.Dojo.validate_dojo(request.form):
        # redirect back to form if return is False
        return redirect('/')
    # If returns True continue
    data = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment']
    }
    id = dojo.Dojo.add_dojo(data)
    return redirect(f'/result/{id}')

@app.route('/end_session')
def end_session():
    """"Clear the session and return to index"""
    session.clear()
    return redirect('/')

@app.route('/result/<int:id>')
def results(id):
    """Print Results"""
    data = {
        'dojo.id': id
    }
    one_dojo = dojo.Dojo.display_dojo(data)
    return render_template('result.html', dojo=one_dojo)

