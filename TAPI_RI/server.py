from flask import Flask
import thread
from notification_factory import NotificationServerFactory
## EXAMPLE IMPORT SERVER MODELS
import Tapi
import TapiTopology
import TapiConnectivity
import TapiPathComputation
import TapiVirtualNetwork
import TapiNotification
import backend_api

def launch_notification_server():
    return thread.start_new_thread(NotificationServerFactory,())



app = Flask(__name__)
app.register_blueprint(getattr(Tapi, "Tapi"))
app.register_blueprint(getattr(TapiTopology, "TapiTopology"))
app.register_blueprint(getattr(TapiConnectivity, "TapiConnectivity"))
app.register_blueprint(getattr(TapiPathComputation, "TapiPathComputation"))
app.register_blueprint(getattr(TapiVirtualNetwork, "TapiVirtualNetwork"))
app.register_blueprint(getattr(TapiNotification, "TapiNotification"))
app.register_blueprint(getattr(backend_api, 'backend_api'))

if __name__ == "__main__":
    nf = launch_notification_server()
    app.run(host='0.0.0.0', port = 8080, debug=False)
    
