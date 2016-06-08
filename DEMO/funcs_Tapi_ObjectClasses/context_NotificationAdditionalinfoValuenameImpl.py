import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotificationAdditionalinfoValuenameImpl:

    @classmethod
    def get(cls, valueName):
        print 'handling get'
        if valueName in Context._notification.additionalInfo:
            return Context._notification.additionalInfo[valueName]
        else:
            raise KeyError('valueName')
