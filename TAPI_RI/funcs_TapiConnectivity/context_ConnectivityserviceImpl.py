import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be

from objects_TapiConnectivity.connection import Connection, Direction
from objects_TapiConnectivity._connectivityServiceSchema import _connectivityServiceSchema 
from objects_TapiConnectivity.operationalStatePac import OperationalStatePac
from objects_TapiConnectivity.layerProtocol import Layerprotocolname
from objects_TapiConnectivity.connectionPort import ConnectionPort

class Context_ConnectivityserviceImpl:

    @classmethod
    def get(cls, ):
        print 'handling get'
        if be.Context:
            array_cs=[]
            for cs in be.Context._connectivityService:
                uri="restconf/config/Context/_connectivityService/"+be.Context._connectivityService[cs].uuid+"/"
                print uri
                array_cs.append(uri)
            json = { 'itemlist' : array_cs }
            return json
        else:
            raise KeyError('')
            
    @classmethod
    def post(cls, uuid, _connectivityserviceschema):
        _connectivityserviceschema.uuid=uuid
        print str(_connectivityserviceschema)
        
        print 'handling post'
        conn_uuid='con'+uuid
        print 'Creating connection...' + conn_uuid
        paths=be.compute_path(_connectivityserviceschema)
        cp_id = 0
        connection = Connection( json_struct={'uuid':conn_uuid, 'direction': 'BIDIRECTIONAL'})
        connection.layerProtocolName = Layerprotocolname('ETH')
        flows={}
        if paths:
            for path in paths["paths"][0]["links"]:
                print path
                cp_id += 2
                nep_src = 'restconf/config/Context/_topology/_node/'+ path["src"]["device"] + '/_ownedNodeEdgePoint/' + path["src"]["port"] +'/'
                nep_dst = 'restconf/config/Context/_topology/_node/'+ path["dst"]["device"] + '/_ownedNodeEdgePoint/' + path["dst"]["port"] +'/'
                cp_src = ConnectionPort( json_struct={'localId':'cp'+str(cp_id), '_connectionEndPoint' : { 'uuid': 'cep'+str(cp_id), '_clientNodeEdgePoint' : [ nep_src ] } })
                cp_dst = ConnectionPort( json_struct={'localId':'cp'+str(cp_id+1), '_connectionEndPoint' : { 'uuid': 'cep'+str(cp_id+1), '_clientNodeEdgePoint' : [ nep_dst ] } })
                connection._connectionPort['cp'+str(cp_id)] = cp_src
                connection._connectionPort['cp'+str(cp_id+1)] = cp_dst
                if len(paths["paths"][0]["links"])*2 >= (cp_id + 2):
                    flows[cp_id]={"node": path["dst"]["device"], "src_port": path["dst"]["port"], "dst_port": ""}            
                if cp_id > 2:
                    flows[cp_id-2]["dst_port"]=path["src"]["port"]
            
            print flows
            for flow in flows:
                be.create_flow(uuid,flows[flow]["node"], flows[flow]["src_port"], flows[flow]["dst_port"])
            
        print "Connection:" + str(connection)
        be.Context._connection[conn_uuid] = connection
        conn_url = "restconf/config/Context/_connection/" + conn_uuid + "/"
        _connectivityserviceschema._connection.append(conn_url)
        be.Context._connectivityService[uuid] = _connectivityserviceschema

