from handlers import base

def setup_routes(app):
    app.router.add_get('/', base.index)
    app.router.add_get('/login', base.login)
    app.router.add_get('/signup', base.signup)