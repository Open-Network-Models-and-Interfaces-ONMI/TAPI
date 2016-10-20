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
        
        connection = Connection( json_struct={'uuid':conn_uuid, 'direction': 'BIDIRECTIONAL'})
        connection.layerProtocolName = Layerprotocolname('ETH')
        
        nep1_url = 'restconf/config/Context/_topology/_node/node1/_ownedNodeEdgePoint/pe113/'
        nep2_url = 'restconf/config/Context/_topology/_node/node1/_ownedNodeEdgePoint/pe11/'
        nep3_url = 'restconf/config/Context/_topology/_node/node4/_ownedNodeEdgePoint/pe42/'
        nep4_url = 'restconf/config/Context/_topology/_node/node4/_ownedNodeEdgePoint/pe41/'        
        nep5_url = 'restconf/config/Context/_topology/_node/node2/_ownedNodeEdgePoint/pe22/'
        nep6_url = 'restconf/config/Context/_topology/_node/node2/_ownedNodeEdgePoint/pe213/'
        
        cp1 = ConnectionPort( json_struct={'localId':'cp1', '_connectionEndPoint' : { 'uuid': 'cep1', '_clientNodeEdgePoint' : [ nep1_url ] } })
        cp2 = ConnectionPort( json_struct={'localId':'cp2', '_connectionEndPoint' : { 'uuid': 'cep2', '_clientNodeEdgePoint' : [ nep2_url ] } })
        cp3 = ConnectionPort( json_struct={'localId':'cp3', '_connectionEndPoint' : { 'uuid': 'cep3', '_clientNodeEdgePoint' : [ nep3_url ] } })
        cp4 = ConnectionPort( json_struct={'localId':'cp4', '_connectionEndPoint' : { 'uuid': 'cep4', '_clientNodeEdgePoint' : [ nep4_url ] } })
        cp5 = ConnectionPort( json_struct={'localId':'cp5', '_connectionEndPoint' : { 'uuid': 'cep5', '_clientNodeEdgePoint' : [ nep5_url ] } })
        cp6 = ConnectionPort( json_struct={'localId':'cp6', '_connectionEndPoint' : { 'uuid': 'cep6', '_clientNodeEdgePoint' : [ nep6_url ] } })
        
        connection._connectionPort['cp1'] = cp1
        connection._connectionPort['cp2'] = cp2
        connection._connectionPort['cp3'] = cp3
        connection._connectionPort['cp4'] = cp4
        connection._connectionPort['cp5'] = cp5
        connection._connectionPort['cp6'] = cp6
                        
        print connection
        be.Context._connection[conn_uuid] = connection
        conn_url = "restconf/config/Context/_connection/" + conn_uuid + "/"
        _connectivityserviceschema._connection.append(conn_url)
        be.Context._connectivityService[uuid] = _connectivityserviceschema

