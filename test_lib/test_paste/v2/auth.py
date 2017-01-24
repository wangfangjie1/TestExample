

class UserManage(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        return self.app(environ, start_response)

    @staticmethod
    def factory(cls, global_conf, **kwargs):
        return UserManage