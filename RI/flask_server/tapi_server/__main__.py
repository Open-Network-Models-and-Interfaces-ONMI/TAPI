#!/usr/bin/env python3

import connexion
import json
import sys

from flask import current_app
from tapi_server import encoder
from tapi_server.models.tapi_common_context import TapiCommonContext
from tapi_server import database


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'tapi-photonic-media API'})
    with app.app.app_context():
        with current_app.open_resource("../../database/"+sys.argv[1], 'r') as f:
            data = json.load(f)
            database.context = TapiCommonContext.from_dict(data)
    app.run(port=sys.argv[2])


if __name__ == '__main__':
    main()
