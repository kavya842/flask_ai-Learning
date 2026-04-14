# from flask import Flask

# app=Flask(__name__)

# @app.route('/')
# def kavya():
#     return 'This is my first flask app'

# if __name__=='__main__':
#     app.run()



"""URL building"""
# from flask import *

# app=Flask(__name__)

# @app.route('/admin')
# def admin():
#     return ' This is admin'

# @app.route('/student')
# def student():
#     return ' This is a student'

# @app.route('/staff')
# def staff():
#     return 'This is staff'

# @app.route('/user/<name>')
# def user(name):
#     if name=='admin':
#         return redirect(url_for('admin'))
#     if name=='student':
#         return redirect(url_for('student'))
#     if name=='staff':
#         return redirect(url_for('staff'))

# if __name__=='__main__':
#     app.run(debug=True)





# from flask import *

# app=Flask(__name__)

# @app.route('/kavya')
# def kavya():
#     return 'Kavya loves MI'

# @app.route('/mani')
# def mani():
#     return 'Mani Loves CSK'

# @app.route('/user/<name>')
# def user(name):
#     if name=='kavya':
#         return redirect(url_for('/kavya'))
#     if name=='mani':
#         return redirect(url_for('/mani'))

# if __name__=='__main__':
#     app.run(debug=True)

"""Flask app routing"""
# from flask import Flask

# app=Flask(__name__)

# @app.route('/hello')
# def kavya():
#     return 'Hello Kavya '

# if __name__=='__main__':
#     app.run()

"""adding string"""
# from flask import Flask

# app=Flask(__name__)

# @app.route('/hello/<name>')
# def kavya(name):
#     return " Kavya you are adding a string  "+name
# if __name__=='__main__':
#     app.run(debug=True)

"""adding integers"""
from flask import Flask

app=Flask(__name__)

@app.route('/hello/<int:numbers>')
def kavya(numbers):
    return "Kavya roll no= %d" %numbers
if __name__=='__main__':
    app.run(debug=True)

