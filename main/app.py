from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
api = Api(app)

from cached_query import CachedQuery
from uncached_query import UncachedQuery

lru_query = CachedQuery('hpc_network','postgres','password','192.17.100.193','5432')
lru_query.setup_cache('lru',10)

fifo_query = CachedQuery('hpc_network','postgres','password','192.17.100.193','5432')
fifo_query.setup_cache('fifo',10)

random_query = CachedQuery('hpc_network','postgres','password','192.17.100.193','5432')
random_query.setup_cache('random',10)


class CachedQueryPoint(Resource):
    @cross_origin()
    def get(self,typ,query_string):
        print(query_string)
        fast = None
        if typ=='lru':
            fast = lru_query
        if typ=='fifo':
            fast = fifo_query
        if typ=='random':
            fast = random_query
        res1 = fast.exec_query_with_cache(query_string)
        return str(res1)
        
        
class UncachedQueryPoint(Resource):
    @cross_origin()
    def get(self,query_string):
        print(query_string)
        fast = UncachedQuery('hpc_network','postgres','password','192.17.100.193','5432')
        res1 = fast.exec_query(query_string)
        fast.close()
        return str(res1)
        
api.add_resource(CachedQueryPoint,'/cached/query/<string:typ>/<string:query_string>')
api.add_resource(UncachedQueryPoint,'/uncached/query/<string:query_string>')
app.run(debug=True,port=5050,host='127.0.0.1')
