# handlers.py
# file takes care of all the error handling for 403,404&405 errors by redirectinf them to another page
#
#
#



from flask import Blueprint, render_template

errors = Blueprint('errors', __name__) #creating instance of bp



#error handler decorator
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404 #need to also return the 404 status
#404 is a page not found


#403 error is a forbidden instance
@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403 #need to also return the 404 status

#500 is a general server error, server side problem
@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/404.html'), 500 #need to also return the 404 status
