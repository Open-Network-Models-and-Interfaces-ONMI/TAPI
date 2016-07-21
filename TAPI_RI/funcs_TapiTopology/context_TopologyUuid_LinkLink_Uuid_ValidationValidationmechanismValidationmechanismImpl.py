import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_LinkLink_Uuid_ValidationValidationmechanismValidationmechanismImpl:

    @classmethod
    def get(cls, uuid, link_uuid, validationMechanism):
        print 'handling get'
        if uuid in be.Context._topology:
            if link_uuid in be.Context._topology[uuid]._link:
                if validationMechanism in be.Context._topology[uuid]._link[link_uuid]._validation.validationMechanism:
                    return be.Context._topology[uuid]._link[link_uuid]._validation.validationMechanism[validationMechanism]
                else:
                    raise KeyError('validationMechanism')
            else:
                raise KeyError('link_uuid')
        else:
            raise KeyError('uuid')
