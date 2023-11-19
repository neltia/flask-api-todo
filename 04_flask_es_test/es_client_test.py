"""
post: https://blog.naver.com/dsz08082/223267798592
- Todo API에 ES(DB) 연동을 위한 ES 라이브러리 테스트
- lib. elasticsearch
"""
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
es_api_key = os.getenv("ES_API_KEY")
es_host = os.getenv("ES_HOST")
es_port = os.getenv("ES_PORT")
es = Elasticsearch(
    [f"https://{es_host}:{es_port}"],
    verify_certs=False,
    api_key=es_api_key
)
print(es)

# 도큐먼트 하나 구성
doc = {"name": "Hyun", "Job": "Blogger"}

# 도큐먼트 indexing
# - id를 "1"로 가지는 문서에 해당 데이터가 없으면 새로 삽입한다.
# - 이미 있으면 해당 내용을 갱신한다.
data = es.index(index="test_index", id="1", document=doc)
print(data)

# 도큐먼트 조회
# - test_index 인덱스의 "1"을 id로 가지는 단일 도큐먼트 하나를 조회한다.
data = es.get(index="test_index", id="1")
print(data)

# 도큐먼트 검색
query = {"match_all": {}}
data = es.search(index="test_index", query=query)
print(data)

query = {"match": {"name": "hyun"}}
data = es.search(index="test_index", query=query)
print(data)

# 도큐먼트 삭제
data = es.delete(index="test_index", id="1")
print(data)

# 인덱스 목록 조회
data = es.cat.indices()
print(data)

# 인덱스 삭제
data = es.indices.delete(index="test_index")
print(data)

# 인덱스 생성
data = es.indices.create(index="test_index")
print(data)

# 인덱스 목록 조회
data = es.cat.indices()
print(data)

# 인덱스 삭제
data = es.indices.delete(index="test_index")
print(data)
