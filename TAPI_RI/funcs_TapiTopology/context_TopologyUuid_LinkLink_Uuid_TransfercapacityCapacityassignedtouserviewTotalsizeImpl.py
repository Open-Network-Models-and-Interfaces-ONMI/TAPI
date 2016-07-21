import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_LinkLink_Uuid_TransfercapacityCapacityassignedtouserviewTotalsizeImpl:

    @classmethod
    def get(cls, uuid, link_uuid, totalSize):
        print 'handling get'
        if uuid in be.Context._topology:
            if link_uuid in be.Context._topology[uuid]._link:
                if totalSize in be.Context._topology[uuid]._link[link_uuid]._transferCapacity.capacityAssignedToUserView:
                    return be.Context._topology[uuid]._link[link_uuid]._transferCapacity.capacityAssignedToUserView[totalSize]
                else:
                    raise KeyError('totalSize')
            else:
                raise KeyError('link_uuid')
        else:
            raise KeyError('uuid')
