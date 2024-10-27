from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from core.infra.models.department import Department
        from core.infra.models.script import Script
        from core.infra.models.script import ScriptAction
        from core.infra.models.worker import Worker
        from core.infra.models.mark import Mark
