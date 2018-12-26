from datetime import datetime
import aiohttp_jinja2

from aiohttp import web
from aiohttp_session import get_session


class Index(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        conf = self.app['config']
        session = await get_session(self)
        user = ''
        if 'user' in session:
            user = session['user']
        return dict(conf=conf, user=user)


class Login(web.View):
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        session = await get_session(self)
        session['last_visit'] = str(datetime.utcnow())
        last_visit = session['last_visit']
        return dict()

    @aiohttp_jinja2.template('login.html')
    async def post(self):
        data = await self.post()
        login = data['login']
        password = data['password']

        if login == 'admin' and password == 'admin':
            session = await get_session(self)
            user = dict(login=login, password=password)
            session['user'] = user
        else:
            exception = {'Invalid login or password, please enter admin admin'}
            return dict(exception=exception)

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)



class Logout(web.View):

    async def get(self):
        session = await get_session(self)
        del session['user']

        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location)