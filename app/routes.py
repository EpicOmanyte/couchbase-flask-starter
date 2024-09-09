from flask import Blueprint, jsonify, request, current_app
from app.models import Document

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Welcome to Couchbase Flask Starter Kit"})

@bp.route('/documents', methods=['POST'])
def create_document():
    data = request.json
    doc = Document(id=data['id'], content=data['content'])
    current_app.couchbase_collection.upsert(doc.id, doc.to_dict())
    return jsonify(doc.to_dict()), 201

@bp.route('/documents/<string:doc_id>', methods=['GET'])
def get_document(doc_id):
    result = current_app.couchbase_collection.get(doc_id)
    doc = Document.from_dict(result.content_as[dict])
    return jsonify(doc.to_dict())