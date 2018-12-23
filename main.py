import logging
from aiohttp import web

from routes.base import setup_routes

def main():
    app = web.Application()
    setup_routes(app)
    app['config'] = {}
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app, host='localhost', port=8080)

if __name__ == '__main__':
    main()

