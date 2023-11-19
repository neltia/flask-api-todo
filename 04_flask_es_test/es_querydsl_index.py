"""
post: https://blog.naver.com/dsz08082/223268465509
- Todo API에 ES(DB) 연동을 위한 ES 라이브러리 테스트
- lib. elasticsearch_dsl
- refer. https://elasticsearch-dsl.readthedocs.io/en/latest
"""
from datetime import datetime
from elasticsearch_dsl import connections
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
es_api_key = os.getenv("ES_API_KEY")
es_host = os.getenv("ES_HOST")
es_port = os.getenv("ES_PORT")
connections.create_connection(
    hosts=[f"https://{es_host}:{es_port}"],
    verify_certs=False,
    api_key=es_api_key
)


class Article(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    class Index:
        name = 'blog'
        settings = {
          "number_of_shards": 2,
        }

    def save(self, ** kwargs):
        self.lines = len(self.body.split())
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now() > self.published_from


# create the mappings in elasticsearch
Article.init()

# create and save and article
article = Article(meta={'id': 42}, title='Hello world!', tags=['test'])
article.body = ''' looong text '''
article.published_from = datetime.now()
article.save()

article = Article.get(id=42)
print(article)
