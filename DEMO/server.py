from flask import Flask
import thread
from notification_factory import NotificationServerFactory
## EXAMPLE IMPORT SERVER MODELS
import Tapi_Interfaces_ConnectivityService
import Tapi_Interfaces_NotificationSubscriptionService
import Tapi_Interfaces_PathComputationService
import Tapi_Interfaces_TopologyService
import Tapi_Interfaces_VirtualNetworkService
import Tapi_ObjectClasses
import Tapi_TypeDefinitions
import backend_api

def launch_notification_server():
    return thread.start_new_thread(NotificationServerFactory,())



app = Flask(__name__)
app.register_blueprint(getattr(Tapi_Interfaces_ConnectivityService, "Tapi_Interfaces_ConnectivityService"))
app.register_blueprint(getattr(Tapi_Interfaces_NotificationSubscriptionService, "Tapi_Interfaces_NotificationSubscriptionService"))
app.register_blueprint(getattr(Tapi_Interfaces_PathComputationService, "Tapi_Interfaces_PathComputationService"))
app.register_blueprint(getattr(Tapi_Interfaces_TopologyService, "Tapi_Interfaces_TopologyService"))
app.register_blueprint(getattr(Tapi_Interfaces_VirtualNetworkService, "Tapi_Interfaces_VirtualNetworkService"))
app.register_blueprint(getattr(Tapi_ObjectClasses, "Tapi_ObjectClasses"))
app.register_blueprint(getattr(Tapi_TypeDefinitions, "Tapi_TypeDefinitions"))
app.register_blueprint(getattr(backend_api, 'backend_api'))

if __name__ == "__main__":
    nf = launch_notification_server()
    app.run(host='0.0.0.0', port = 8080, debug=True)
