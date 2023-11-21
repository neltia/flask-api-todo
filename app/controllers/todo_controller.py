from flask_restx import Resource
from app.services.todo_service import TodoService
from app.utils.dto import TodoDto


api = TodoDto.api
todo_model = TodoDto.todo


@api.route('/')
@api.response(404, 'Todo not found')
class TodoList(Resource):
    ''' Shows a list of all todos, and lets you POST to add new tasks '''
    @api.doc('list_todos')
    def get(self):
        # List all tasks
        todo_list = TodoService.all_todo()

        # 검색 결과가 비어있는 경우 404 응답 반환
        if not todo_list:
            return {"status_code": 404, "result": "no results found"}, 404

        # 결과가 있을 경우 200 응답 반환
        data = {"status_code": 200, "result": todo_list}
        return data


@api.route('/create')
@api.response(201, 'New task created')
class TodoCreateResource(Resource):
    @api.doc("create_todo")
    @api.expect(todo_model, validate=True)
    def post(self):
        req = api.payload
        todo_id = TodoService.create_todo(
            task=req["task"], priority=req["priority"]
        )
        data = {"status_code": 201, "result": todo_id}
        return data, 201


@api.route('/<todo_id>')
@api.response(404, 'Todo not found')
@api.param('todo_id', 'The task identifier')
class TodoResource(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc("get_todo")
    def get(self, todo_id):
        todo = TodoService.get_todo(todo_id)
        data = {"status_code": 200, "result": todo}
        return data

    @api.doc("update_todo")
    @api.expect(todo_model, validate=True)
    def put(self, todo_id):
        req = api.payload
        todo = TodoService.update_todo(
            todo_id, task=req["task"], priority=req["priority"],
            done=req["done"]
        )
        data = {"status_code": 200, "result": todo}
        return data

    @api.doc("delete_todo")
    def delete(self, todo_id):
        req = TodoService.delete_todo(todo_id)
        data = {"status_code": 200, "result": req}
        return data
