import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_NodeNode_Uuid_ExtensionsExtensionsspecificationImpl:

    @classmethod
    def get(cls, uuid, node_uuid, extensionsSpecification):
        print 'handling get'
        if uuid in be.Context._topology:
            if node_uuid in be.Context._topology[uuid]._node:
                if extensionsSpecification in be.Context._topology[uuid]._node[node_uuid]._extensions:
                    return be.Context._topology[uuid]._node[node_uuid]._extensions[extensionsSpecification]
                else:
                    raise KeyError('extensionsSpecification')
            else:
                raise KeyError('node_uuid')
        else:
            raise KeyError('uuid')
