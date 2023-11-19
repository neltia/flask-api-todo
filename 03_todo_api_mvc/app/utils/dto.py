from flask_restx import Namespace, fields


class TodoDto:
    api = Namespace('todos', description='user related operations')

    todo = api.model('Todo', {
        'id': fields.Integer(
            readonly=True,
            description='The task unique identifier'
            ),
        'task': fields.String(
            required=True,
            description='The task details'
        )
    })
