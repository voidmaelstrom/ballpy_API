from unittest import result
from flask import ( Blueprint, request, redirect, jsonify )
import json
from . import models

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']

        new_reptile = models.Reptile(common_name=common_name,
                                     scientific_name=scientific_name,
                                     conservation_status=conservation_status,
                                     native_habitat=native_habitat,
                                     fun_fact=fun_fact)
        models.db.session.add(new_reptile)
        models.db.session.commit()

    # Only returning the first record from the DB here
    for reptile in models.Reptile.query.all():
      return {
        "id": reptile.id,
        "common_name": reptile.common_name,
        "scientific_name": reptile.scientific_name,
        "conservation_status": reptile.conservation_status,
        "native_habitat": reptile.native_habitat,
        "fun_fact": reptile.fun_fact
      }