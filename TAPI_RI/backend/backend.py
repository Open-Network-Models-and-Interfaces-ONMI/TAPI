# Example, only works for COP
import json
from onos_topology import onos_topology
from onos_flows import onos_flows
from objects_common.keyedArrayType import KeyedArrayType
from objects_Tapi.contextSchema import ContextSchema as ContextSchema_object



"""
class TopLevelObject(jsonObject):
    def __init__(self):
        self.calls = KeyedArrayType(Call, 'callId')
        self.connections = KeyedArrayType(Connection, 'connectionId')
        super(TopLevelObject, self).__init__()
"""

def json_dumps(js):
    # Pretty-print version of json.dumps
    return json.dumps(js, sort_keys=True, indent=4, separators=(',', ': '))


def byteify(input):
    # Convert JSON unicode strings to python byte strings, recursively on a json_struct
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

filename = 'server_backend_state.json'

Context = ContextSchema_object()

IP="127.0.0.1"
PORT="8181"
CTL_TYPE="ONOS"
USER="onos"
PASSWORD="rocks"
USE_CONTROLLER = 0

def save_state():
    json_struct = {}
    json_struct['Context'] = Context.json_serializer()

    json_string = json_dumps(json_struct)
    out = open(filename, 'w+')
    out.write(json_string)
    out.close()
    return True

def load_state():
    f = open(filename, 'rb')
    json_string = f.read()
    f.close()
    json_struct = byteify(json.loads(json_string))
    global Context
    Context = ContextSchema_object(json_struct['Context'])
    return True
    
def connect_sdn_controller():
    USE_CONTROLLER = 1
    if CTL_TYPE == "ONOS" and USE_CONTROLLER:
        onos_ctl=onos_topology()
        topo=onos_ctl.retrieveTopology(IP, PORT, USER, PASSWORD)
        print "connected"

def create_flow(uuid, node, src_port, dst_port):
    if CTL_TYPE == "ONOS" and USE_CONTROLLER:
        onos_ctl=onos_flows()
        topo=onos_ctl.insertFlow(uuid, node, src_port, dst_port)

def remove_flow(uuid):
    if CTL_TYPE == "ONOS" and USE_CONTROLLER:
        onos_ctl=onos_flows()
        topo=onos_ctl.deleteFlow(uuid)
        
def compute_path(_connectivityserviceschema):
    print "computing path for connectivity service " + str(_connectivityserviceschema)
    if CTL_TYPE=="ONOS" and USE_CONTROLLER:
        onos_ctl=onos_flows()
        seps=[]
        for sp in _connectivityserviceschema._servicePort:
            seps.append(_connectivityserviceschema._servicePort[sp]._serviceEndPoint)
        src=seps[0].split('/')[-1]
        dst=seps[1].split('/')[-1]     
        path=onos_ctl.compute_path( src, dst)
        return path
    return {}
