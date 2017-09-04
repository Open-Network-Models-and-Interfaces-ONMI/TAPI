#!/usr/bin/env python3

import connexion

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'tapi-connectivity API generated from tapi-connectivity.yang'})
    app.run(port=8080)
