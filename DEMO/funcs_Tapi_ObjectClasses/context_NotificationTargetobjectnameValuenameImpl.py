import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotificationTargetobjectnameValuenameImpl:

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context._notification.targetObjectName:
            return Context._notification.targetObjectName[valueName]
        else:
            raise KeyError('valueName')
