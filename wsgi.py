from src import app, db

#from src.routes import Smoke, S1
#import src.routes
# api.add_resource(Smoke, '/smoke')
# api.add_resource(S1, '/s1')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)