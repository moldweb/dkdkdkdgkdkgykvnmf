import json
import random
import datetime
import uuid
import re
import tornado.ioloop
import tornado.web
import tornado.options

import features
import settings
from os import listdir
from os.path import isfile, join
from base_handler import BaseHandler
from admin_handler import AdminHandler
import db
import email_sender


class MainHandler(BaseHandler):
    def get(self):
        return self.render('index.html')


class Login(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        next = self.get_argument('next', None)
        error = ''
        return self.render('admin/login.html', next=next, error=error, email='')

    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        password = self.get_argument('password')
        next = self.get_argument('next', None)
        user = db.get_user_by_email(email)
        if user:
            if password == user['password']:
                self.set_secure_cookie("user_id", user['user_id'])
                return self.redirect(next if next else '/admin')
            else:
                error = 'password invalid'
        else:
            error = 'no such email in db'
        return self.render("admin/login.html", error=error, next=next, email=email)


class LogOut(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("user_id")
        return self.redirect('/admin/login')


class AdminIndex(AdminHandler):
    def get(self, *args, **kwargs):
        return self.render('admin/index.html')


class Ad(AdminHandler):
    def get(self, *args, **kwargs):

        return self.render('admin/ad.html', extras=features.extras, construction_types=features.construction_types,
                           conditions=features.conditions, locations=features.get_locations(),
                           offer_types=features.offer_types, property_types=features.property_types, agents = db.get_agents())

    def post(self, *args, **kwargs):

        extra = self.get_arguments('extra')
        extras = []
        db_extras = features.get_extras()
        for item in db_extras:
            if item['ro'] in extra:
                item['value'] = True
            extras.append(item)
        offer_type = self.get_argument('offer_type')
        construction_type = self.get_argument('construction_type')
        condition = self.get_argument('condition')
        print 1
        return self.get()


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/admin/?", AdminIndex),
    (r"/admin/login", Login),
    (r"/admin/logout", LogOut),
    (r"/admin/ad", Ad),

],
    template_path=settings.template_path,
    static_path=settings.static_path,
    static_url_prefix='/statics/',
    login_url='admin/login',
    cookie_secret="86386c5c-c42a-469c-9d0a-c5cdc6bc0084",
    autoreload=True
)

if __name__ == "__main__":
    print 'started on http://127.0.0.1:{0}'.format(settings.listener_port)
    application.listen(settings.listener_port)
    tornado.ioloop.IOLoop.instance().start()
