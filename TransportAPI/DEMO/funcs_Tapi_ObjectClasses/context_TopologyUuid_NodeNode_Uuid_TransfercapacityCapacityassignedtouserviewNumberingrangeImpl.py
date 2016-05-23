import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_TopologyUuid_NodeNode_Uuid_TransfercapacityCapacityassignedtouserviewNumberingrangeImpl:

    @classmethod
    def get(cls, uuid, node_uuid, numberingRange):
        print 'handling get'
        if uuid in Context._topology:
            if node_uuid in Context._topology[uuid]._node:
                if numberingRange in Context._topology[uuid]._node[node_uuid]._transferCapacity.capacityAssignedToUserView:
                    return Context._topology[uuid]._node[node_uuid]._transferCapacity.capacityAssignedToUserView[numberingRange]
                else:
                    raise KeyError('numberingRange')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
