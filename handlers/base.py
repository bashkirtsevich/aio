from datetime import datetime
import aiohttp_jinja2

from aiohttp import web
from aiohttp_session import get_session


class Index(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        conf = self.app['config']
        session = await get_session(self)
        user = {'I am var user'}
        return dict(conf=conf, user=user)

    @aiohttp_jinja2.template('index.html')
    async def post(self):
        data = await self.post()
        msg=data['test']
        if msg == 'asd':
            msg = 'welcome'
            user = {'I am var user'}
            return dict(msg=msg, user=user)
        else:
            return dict(msg=msg)




class Login(web.View):
    @aiohttp_jinja2.template('login.html')
    async def get(self):
        session = await get_session(self)
        session['last_visit'] = str(datetime.utcnow())
        last_visit = session['last_visit']
        return dict()

    async def post(self):
        data = await self.post()
        login = data['login']
        password = data['password']
        if login == 'admin' and password == 'admin':
            export = {'yep'}
            return dict(export=export)

        session = await get_session(self)
        session['user'] = {'login': login}
        location = self.app.router['index'].url_for()
        return web.HTTPFound(location=location, login=login)

class Signup(web.View):

    async def get(self):
        return web.Response(text='signup Aiohttp')