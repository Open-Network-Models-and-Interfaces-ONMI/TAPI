import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_NodeNode_Uuid_OwnednodeedgepointOwnednodeedgepoint_UuidLabelValuenameImpl:

    @classmethod
    def get(cls, uuid, node_uuid, ownedNodeEdgePoint_uuid, valueName):
        print 'handling get'
        if uuid in be.Context._topology:
            if node_uuid in be.Context._topology[uuid]._node:
                if ownedNodeEdgePoint_uuid in be.Context._topology[uuid]._node[node_uuid]._ownedNodeEdgePoint:
                    if valueName in be.Context._topology[uuid]._node[node_uuid]._ownedNodeEdgePoint[ownedNodeEdgePoint_uuid].label:
                        return be.Context._topology[uuid]._node[node_uuid]._ownedNodeEdgePoint[ownedNodeEdgePoint_uuid].label[valueName]
                    else:
                        raise KeyError('valueName')
                else:
                    raise KeyError('ownedNodeEdgePoint_uuid')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
