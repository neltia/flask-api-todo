# flask
from app import create_app
from config.es_config import es_init


es_init()
app = create_app()


# test app run
if __name__ == '__main__':
    app.run(debug=True)
