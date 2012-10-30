from django.conf import settings
from django.db.models.aggregates import Sum
from django.db.models.sql.aggregates import Sum as BaseSQLSum


class SQLSum(BaseSQLSum):
    @property
    def sql_template(self):
        if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
            return '%(function)s(%(field)s::int)'
        return '%(function)s(%(field)s)'


class BooleanSum(Sum):
    def add_to_query(self, query, alias, col, source, is_summary):
        aggregate = SQLSum(col, source=source, is_summary=is_summary, **self.extra)
        query.aggregates[alias] = aggregate
