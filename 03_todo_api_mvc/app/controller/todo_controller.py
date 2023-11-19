from flask_restx import Resource
from app.model.dao import TodoDAO
from app.utils.dto import TodoDto

DAO = TodoDAO()
api = TodoDto.api
_todo = TodoDto.todo


@api.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @api.doc('list_todos')
    @api.marshal_list_with(_todo)
    def get(self):
        '''List all tasks'''
        return DAO.todos

    @api.doc('create_todo')
    @api.expect(_todo)
    @api.marshal_with(_todo, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc('get_todo')
    @api.marshal_with(_todo)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @api.expect(_todo)
    @api.marshal_with(_todo)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)
