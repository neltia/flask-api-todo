import elasticsearch
from elasticsearch_dsl import Search
from app.models.dao import Todo
from app.utils.dto import TodoDto
from app.utils import common
from datetime import datetime

api = TodoDto.api


class TodoService:
    @staticmethod
    def all_todo():
        search = Search(index='todo_index')
        res = search.query('match_all').execute()
        todo_list = []
        for hit in res.hits:
            todo_data = hit.to_dict()
            todo_data['id'] = hit.meta.id
            todo_list.append(todo_data)
        return todo_list

    @staticmethod
    def create_todo(task, priority):
        todo = Todo(task=task, priority=priority)
        todo.done = False
        todo.created_at = datetime.now()
        todo.updated_at = datetime.now()
        todo.save()

        todo_id = todo.meta.id
        return todo_id

    @staticmethod
    def get_todo(todo_id):
        try:
            todo = Todo.get(id=todo_id)
        except elasticsearch.NotFoundError:
            msg = f"todo_id: {todo_id} doesn't exist"
            res = {"status_code": 404, "result": msg}
            api.abort(404, res)
        todo = todo.to_dict()
        todo = common.conversed_json(todo)
        return todo

    @staticmethod
    def update_todo(todo_id, task=None, priority=None, done=None):
        todo = Todo.get(id=todo_id)
        if task:
            todo.task = task
        if priority:
            todo.priority = priority
        if done:
            todo.done = done
        todo.updated_at = datetime.now()
        res = todo.save()
        return res

    @staticmethod
    def delete_todo(todo_id):
        try:
            todo = Todo.get(id=todo_id)
        except elasticsearch.NotFoundError:
            msg = f"todo_id: {todo_id} doesn't exist"
            res = {"status_code": 404, "result": msg}
            api.abort(404, res)

        todo.delete()
        res = "deleted"
        return res
