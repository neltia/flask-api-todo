"""
post: https://blog.naver.com/dsz08082/223268465509
- Todo API에 ES(DB) 연동을 위한 ES 라이브러리 테스트
- lib. elasticsearch_dsl
"""
from elasticsearch_dsl import connections
from elasticsearch_dsl import Search, Index
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


s = Search(index='blog')
res = s.query('match_all')
search_result = []
for hit in res.scan():
    search_result.append(hit)
# print(search_result)

res = s.query('match', title="world")
search_result = []
for hit in res.scan():
    search_result.append(hit)
print(search_result)
exec = res.execute()
print(exec)
print(exec.to_dict())
