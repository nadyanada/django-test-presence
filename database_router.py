class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'presence':
            if model.__name__ == 'AttendanceLongTerm':
                return 'long_term'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'presence':
            if model.__name__ == 'AttendanceLongTerm':
                return 'long_term'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'presence':
            if db == 'long_term':
                return model_name == 'attendancelongterm'
            else:
                return model_name == 'attendanceshortterm'
        return None