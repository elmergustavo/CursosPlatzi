from flask import Blueprint, request, jsonify
from . import db
import json

bp = Blueprint('carreras', __name__, url_prefix='/carreras')


@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def carreras_func():
    carrera_id = request.args.get('id')
    skip = request.args.get('skip')
    limit = request.args.get('limit')

    request_body = request.get_json()
    if request.method == 'POST':
        # Crear carrera
        return jsonify({'_id': db.crear_carrera(request_body)})
    elif request.method == 'PUT':
        # Actualizar nombre y descripcion de la carrera
        return jsonify({'modificados': db.actualizar_carrera(request_body)})
    elif request.method == 'DELETE' and carrera_id is not None:
        # Borrar una carrera usando el _id
        return jsonify({'borrados': db.borrar_carrera_por_id(carrera_id)})
    elif carrera_id is not None:
        # Obtener carreras por _id
        result = db.consultar_carrera_por_id(carrera_id)
        return jsonify({'carrera': json.loads(result)})
    else:
        # Obtener carreras
        skip = (skip, 0)[skip is None]
        limit = (limit, 10)[limit is None]
        result = db.consultar_carreras(skip, limit)
        return jsonify({'carreras': json.loads(result)})


@bp.route('/agregar-curso', methods=['PUT', 'DELETE'])
def agregar_curso():
    request_body = request.get_json()
    if request.method == 'PUT':
        return jsonify({'modificados': json.loads(db.agregar_curso(request_body))})
    elif request.method == 'DELETE':
        return jsonify({'borrados': json.loads(db.borrar_curso_de_carrera(request_body))})


@bp.route('/test')
def test_connection():
    return jsonify({'collections': json.loads(db.test_connection())})
