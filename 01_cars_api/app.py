"""
API:  Cars API
post: https://blog.naver.com/dsz08082/223242278282
- Flask-RESTX GET/POST/PUT/DELETE 예제 및 pytest 테스트
URI:
- /ns_cars/cars: 전체 브랜드 데이터 조회
- /ns_cars/cars/<brand>: 단일 브랜드 데이터 CRUD
- /ns_cars/cars/<brand>/<model_id>: 특정 브랜드의 모델 데이터 CRUD
"""
# Flask 라이브러리 호출
from flask import Flask
from flask import Response
from flask import abort
from flask import request
# Flask-RESTX 라이브러리 호출
from flask_restx import Api
from flask_restx import Resource
from flask_restx import fields

app = Flask(__name__)
api = Api(app)

ns_cars = api.namespace('ns_cars', description='Car APIs')

car_data = api.model(
    'Car Data',
    {
      "name": fields.String(description="model name", required=True),
      "price": fields.Integer(description="car price", required=True),
      "fuel_type": fields.String(description="fuel type", required=True),
      "fuel_efficiency": fields.String(description="fuel efficiency",
                                       required=True),
      "engine_power": fields.String(description="engine power", required=True),
      "engine_cylinder": fields.String(description="engine cylinder",
                                       required=True)
    }
)

car_info = {}


@ns_cars.route('/cars')
class Cars(Resource):
    """자동차 전체를 관리하는 카테고리"""
    def get(self):
        """자동차 전체 목록 조회"""
        count = 0
        for _, models in car_info.items():
            count += len(models)

        return {
            'number_of_vehicles': count,
            'car_info': car_info
        }


@ns_cars.route('/cars/<string:brand>')
class CarsBrand(Resource):
    """브랜드 정보 관리"""
    def get(self, brand):
        """브랜드 정보 조회"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exist")
        data = car_info[brand]

        return {
            'number_of_vehicles': len(data),
            'data': data
        }

    def post(self, brand):
        """새로운 브랜드 생성"""
        if brand in car_info:
            abort(409, description=f"Brand {brand} already exists")

        car_info[brand] = dict()
        return Response(status=201)

    def delete(self, brand):
        """브랜드 정보 삭제"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exists")

        del car_info[brand]
        return Response(status=200)

    def put(self, brand):
        """브랜드 이름 변경"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exist")

        # 변경할 브랜드 이름을 request body에서 가져옵니다.
        new_brand_name = request.json.get('new_name')
        if new_brand_name is None:
            abort(400, description="New brand name not provided in the request body")

        # 브랜드 이름 변경 로직을 수행합니다.
        car_info[new_brand_name] = car_info.pop(brand)

        return Response(status=200)


@ns_cars.route('/cars/<string:brand>/<int:model_id>')
class CarsBrandModel(Resource):
    """자동차 브랜드에 모델을 관리"""
    def get(self, brand, model_id):
        """자동차 브랜드에 모델 조회"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exists")
        if model_id not in car_info[brand]:
            abort(404, description=f"Car ID {brand}/{model_id} doesn't exists")

        return {
            'model_id': model_id,
            'data': car_info[brand][model_id]
        }

    @api.expect(car_data)  # body
    def post(self, brand, model_id):
        """자동차 브랜드에 모델 추가"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exists")
        if model_id in car_info[brand]:
            abort(409, description=f"Car ID {brand}/{model_id} already exists")

        params = request.get_json()  # get body json
        car_info[brand][model_id] = params

        return Response(status=201)

    def delete(self, brand, model_id):
        """자동차 브랜드에 모델 삭제"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exists")
        if model_id not in car_info[brand]:
            abort(404, description=f"Car ID {brand}/{model_id} doesn't exists")

        del car_info[brand][model_id]

        return Response(status=200)

    @api.expect(car_data)
    def put(self, brand, model_id):
        """자동차 브랜드에 모델 수정"""
        if brand not in car_info:
            abort(404, description=f"Brand {brand} doesn't exists")
        if model_id not in car_info[brand]:
            abort(404, description=f"Car ID {brand}/{model_id} doesn't exists")

        params = request.get_json()
        car_info[brand][model_id] = params

        return Response(status=200)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
