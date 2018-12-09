# TAPI Python Client

## Overview
This is simple TAPI topology visualization client used to test topology retrieval APIs.

This implementation uses the [NetworkX](https://networkx.github.io/documentation/stable/index.html) library on top of [Matplotlib](https://matplotlib.org/).

## Requirements
Python 3.5.2+

Python3-tk


## Usage
To run the server, please execute the following from the TAPI_RI python_client base directory:

```
cd ~/workspace/tapi/RI/python_client/
pip3 install -r requirements.txt --user
python3 tapi_app.py <server_port1> <server_port2> ...
```
## Example
```
python3 -m tapi_server 8081 tpnd
python3 -m tapi_server 8082 ols
python3 tapi_app.py 8081 8082

```
