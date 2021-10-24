from flask import Blueprint, request, jsonify
from . import db
import json

bp = Blueprint('cursos', __name__, url_prefix='/cursos')


@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cursos_func():
    curso_id = request.args.get('id')
    request_body = request.get_json()
    if request.method == 'POST':
        # Crear curso
        return jsonify({"_id": db.crear_curso(request_body)})
    elif request.method == 'PUT':
        # Actualizar nombre y descripcion de la carrera
        return jsonify({'modificados': db.actualizar_curso(request_body)})
    elif request.method == 'DELETE' and curso_id is not None:
        # Borrar una carrera usando el _id
        return jsonify({'borrados': db.borrar_curso_por_id(curso_id)})
    elif curso_id is not None:
        # Obtener curso por id
        result = db.consultar_curso_por_id(curso_id)
        return jsonify({"clase": json.loads(result)})


@bp.route('/porNombre', methods=['POST'])
def cursos_por_nombre():
    request_body = request.get_json()
    result = db.consultar_curso_por_nombre(request_body["nombre"])
    return jsonify({"cursos": json.loads(result)})


@bp.route('/stats')
def stats_collection():
    return jsonify({"collections": json.loads(db.collection_stats("cursos"))})
