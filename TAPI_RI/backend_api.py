import sys
from flask import Response, Blueprint
from flask.views import MethodView

from backend.backend import save_state, load_state

setattr(sys.modules[__name__], __name__,  Blueprint(__name__, __name__))

urls = [("/backend/save_state/" , "BackendSaveState", ["POST"]),
        ("/backend/load_state/" , "BackendLoadState", ["POST"])
]

class Successful(Response):
    def __init__(self, message, info=''):
        super(Successful, self).__init__()
        self.status = '200 '+message
        self.status_code = 200
        self.headers = {'Content-Type': 'application/json'}
        self.data = info

#/backend/save_state/
class BackendSaveState(MethodView):

    def post(self):
        print "Save state operation"
        retval = save_state()
        if retval:
            return Successful("Successful operation",'Saved state')

#/backend/load_state/
class BackendLoadState(MethodView):

    def post(self):
        print "Load state operation"
        retval = load_state()
        if retval:
            return Successful("Successful operation",'Loaded state')

for element in urls:
    getattr(sys.modules[__name__], __name__).add_url_rule(element[0], view_func = globals()[element[1]].as_view(''+element[1]+'_api'), methods=element[2])
