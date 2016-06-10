#Transport API Reference Implementation
Using the [EAGLE JsonCodeTools](https://github.com/OpenNetworkingFoundation/EAGLE-Open-Model-Profile-and-Tools/blob/JsonCodeTools/README.md) we have created a stub server which implements the Transport API semantic.
A small database is incorporated in order to be able to load an scenario, as well as create new requests.

The necessary libraries are the following:
- [Flask](http://flask.pocoo.org/)
```
pip install flask
```
 - [Twisted](https://twistedmatrix.com/trac/)
```
pip install twisted
```
 - [Autobahn] (https://pypi.python.org/pypi/autobahn)
```
pip install autobahn
```

##Run T-API Server
```
python server.py
```

##Run T-API notification client (uses websocket on port 8182)
```
python notification_client.py
```

##Run some T-API examples
```
.\client.sh
```
