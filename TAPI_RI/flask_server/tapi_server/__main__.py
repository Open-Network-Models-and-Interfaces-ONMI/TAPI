#!/usr/bin/env python3

import connexion
import json

from flask import current_app
from tapi_server import encoder
from tapi_server.models.tapi_context import TapiContext
from tapi_server.database import database


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'tapi-connectivity API'})
    with app.app.app_context():
        with current_app.open_resource("database/context.json", 'r') as f:
            data = json.load(f)
            database.context = TapiContext.from_dict(data)
    app.run(port=8080)


if __name__ == '__main__':
    main()
