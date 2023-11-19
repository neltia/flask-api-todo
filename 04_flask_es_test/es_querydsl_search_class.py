"""
post: https://blog.naver.com/dsz08082/223268465509
- Todo API에 ES(DB) 연동을 위한 ES 라이브러리 테스트
- lib. elasticsearch_dsl
- refer. https://elasticsearch-dsl.readthedocs.io/en/latest
"""
from es_querydsl_index import Article
from elasticsearch_dsl import connections
from elasticsearch_dsl import FacetedSearch, TermsFacet
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


class BlogSearch(FacetedSearch):
    doc_types = [Article, ]
    # fields that should be searched
    fields = ['tags', 'title', 'body']

    facets = {
        # use bucket aggregations to define facets
        'tags': TermsFacet(field='tags')
    }


# empty search
bs = BlogSearch()
response = bs.execute()

# Iterate through search results
for hit in response:
    # Check if 'title' attribute exists in the Hit object
    title = getattr(hit, 'title', None)
    if title:
        print(hit.meta.score, title)
    else:
        print(f"No 'title' attribute found in the document.")

# If you still face issues, print the entire hit to inspect its structure
for hit in response:
    print(hit.to_dict())
