import datetime
import tornado.web


class AdminHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def prepare(self):
        pass

    def get_current_user(self):
        sc = self.get_secure_cookie('user_id')
        if sc:
            return sc
        else:
            return None

    def get_int_argument(self, name, default=None, ignore=False):
        arg = self.get_argument(name, default)
        try:
            result = int(arg)
            return result
        except:
            if ignore:
                return default
            else:
                return self.finish('parameter {0} is invalid'.format(name))

    def get_float_argument(self, name, default=None, ignore=False):
        arg = self.get_argument(name, default)
        try:
            result = float(arg)
            return result
        except:
            if ignore:
                return default
            else:
                return self.finish('parameter {0} is invalid'.format(name))

    def get_string_argument(self, name, default=None, ignore=False):
        arg = self.get_argument(name, -1)
        if arg == -1:
            if ignore:
                return default
            else:
                return self.finish('parameter {0} is invalid'.format(name))
        else:
            return arg

    def render_params(self, page, params):
        result = u'?page=' + str(page)
        for name, value in params.items():
            if value is not None and value != u'' and name != u'page':
                if isinstance(value, datetime.datetime):
                    result += u'&{name}={value}'.format(name=name, value=value.strftime('%d/%m/%Y'))
                else:
                    result += u'&{name}={value}'.format(name=name, value=unicode(value))
        return result
