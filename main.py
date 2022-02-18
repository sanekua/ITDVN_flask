# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# def get_films():
#     return [
#         {
#             'id': 1,
#             'title': 'Avatar',
#             'release': "Novenber 4",
#         },
#         {
#             'id': 2,
#             'title': 'Forcase',
#             'release': "11 jan",
#         },
#     ]
#
#
# @app.route('/')
# @app.route('/vl')
# def my_func():
#     films = get_films()
#     return render_template('hello.html', films=films)
#
#
# @app.route('/write/<string:parameter1>')
# def my_gretings(parameter1: str):
#     return f"<h1> Hello {parameter1 * 2} , it is our site </h1>"
#     # return render_template('hello.html')
#
#
# @app.route('/about')
# def my_about():
#     return render_template('about.html', title="About")
#     # return "<h1> About </h1>"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
