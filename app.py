
from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

cupcakes = Cupcake.query.all()


@app.route('/')
def index():
    cupcakes = Cupcake.query.all()
    return render_template("index.html", cupcakes = cupcakes)
    
def serialize_cupcakes(cupcakes):
    """Serialize a cupcake SQLAlchemy obj to dictionary."""
    return {
    "id": cupcakes.id,
    "flavor": cupcakes.flavor,
    "size": cupcakes.size,
    "rating": cupcakes.rating,
    "image": cupcakes.image
    }

@app.route('/api/cupcakes')
def show_all():
    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcakes(c) for c in cupcakes] 
    return jsonify(cupcakes=serialized)

@app.route('/api/cupcakes/<int:cupcake_id>')
def show_detail(cupcake_id):
    cupcake = serialize_cupcakes(Cupcake.query.get_or_404(cupcake_id))
    return jsonify(cupcake=cupcake)

@app.route('/api/cupcakes', methods=["POST"])
def create_all():

    cupcake = Cupcake(
        flavor=request.json['flavor'],
        rating=request.json['rating'],
        size=request.json['size'],
        image=request.json['image'] or None)
    
    db.session.add(cupcake)
    db.session.commit()
 
    cupcakes = serialize_cupcakes(cupcake)

    # POST requests should return HTTP status of 201 CREATED
    return (jsonify(cupcake=cupcakes), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update cupcake from data in request. Return updated data.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json['flavor']
    cupcake.rating = request.json['rating']
    cupcake.size = request.json['size']
    cupcake.image = request.json['image']

    db.session.add(cupcake)
    db.session.commit()
    
    cupcakes = serialize_cupcakes(cupcake)

    return jsonify(cupcake=cupcakes)



@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")





    

