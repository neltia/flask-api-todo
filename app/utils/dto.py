from flask_restx import Namespace, fields


class TodoDto:
    api = Namespace('todo', description='Todo API')

    todo = api.model('Todo', {
        'id': fields.Integer(
            readonly=True,
            description='The task unique identifier'
        ),
        'task': fields.String(
            required=True,
            description='The task details'
        ),
        'priority': fields.String(
            required=False,
            default="Low",
            description=''
        ),
        'done': fields.Boolean(
            required=False, default=False,
            description='The task details'
        ),
        'created_at': fields.DateTime(
            readonly=True,
            description='The task created at time'
        ),
        'updated_at': fields.DateTime(
            readonly=True,
            description='The task updated at time'
        )
    })
