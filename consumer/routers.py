USERS_APP = ('sessions', 'auth', 'admin')

class UserRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label in USERS_APP:
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in USERS_APP:
            return 'users'
        return None

    def allow_migrate(self, db, model):
        if model._meta.app_label in USERS_APP:
            return db == 'users'
        return None

