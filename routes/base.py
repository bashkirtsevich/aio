from handlers.base import Index, Login, Logout, Calculator

def setup_routes(app):
    app.router.add_get('/', Index.get, name='index')

    app.router.add_get('/login', Login.get, name='login')
    app.router.add_post('/login', Login.post)
    app.router.add_get('/logout', Logout.get, name='logout')

    #app.router.add_get('/', Calculator.get, name='calculator')
    app.router.add_post('/', Calculator.post)




    
