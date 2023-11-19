from elasticsearch_dsl import Document
from elasticsearch_dsl import Date, Text, Boolean


class Todo(Document):
    class Index:
        name = "todo_index"

    task = Text()
    priority = Text()
    done = Boolean()
    created_at = Date()
    updated_at = Date()
