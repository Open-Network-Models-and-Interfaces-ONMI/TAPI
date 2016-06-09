import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
from backend.backend import Context


class Context_NotificationNotificationidAdditionalinfoValuenameImpl:

    @classmethod
    def get(cls, notificationId, valueName):
        print 'handling get'
        if notificationId in Context._notification:
            if valueName in Context._notification[notificationId].additionalInfo:
                return Context._notification[notificationId].additionalInfo[valueName]
            else:
                raise KeyError('valueName')
        else:
            raise KeyError('notificationId')
