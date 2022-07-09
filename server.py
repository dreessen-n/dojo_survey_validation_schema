from flask_app import app
from flask_app.controllers import dojos

# @app.errorhandler(404)
# def page_not_found(e):
#     """""Error message for 404"""
#     return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
