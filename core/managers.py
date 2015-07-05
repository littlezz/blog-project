from django.db.models import Manager, Q
from django.utils.timezone import now

__author__ = 'zz'


class PublishManager(Manager):
    def publish(self, for_user=None):
        if for_user is not None and for_user.is_staff:
            return self.all()

        return self.filter(
            Q(publish_date__lte=now())| Q(publish_date__isnull=True) ,
            Q(expire_date__gte=now()) | Q(expire_date__isnull=True),
        )


