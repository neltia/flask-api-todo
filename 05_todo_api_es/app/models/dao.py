from elasticsearch_dsl import Document
from elasticsearch_dsl import Date, Text, Boolean, Keyword


class Todo(Document):
    class Index:
        name = "todo_index"

    task = Text(analyzer="nori")
    priority = Keyword()
    done = Boolean()
    created_at = Date()
    updated_at = Date()
