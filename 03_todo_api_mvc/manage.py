"""
API:  Todo API
post: https://blog.naver.com/dsz08082/223244663091
refer.https://flask-restx.readthedocs.io/en/latest/example.html
- Flask-RESTX MVC Arch 기반 데이터 처리 예제 (MVC arch 분리 후)
"""
# flask
from app import create_app

app = create_app()


# test app run
if __name__ == '__main__':
    app.run(debug=True)
