from django.db import models

from utils.model_mixins import BaseAppModelMixin


class SalesRep(BaseAppModelMixin):
    """class for sales rep"""

    DATA = 'da'
    GIFTCARD = 'gc'
    ALL = 'all'

    CATEGORY_CHOICES = [
        (DATA, 'Data'),
        (GIFTCARD, 'GIFTCARD'),
        (ALL, 'all'),
    ]

    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False,
        default=ALL
    )
    is_active = models.BooleanField(default=True)
    cash_balance = models.IntegerField(default=0)
    airtime_balance = models.IntegerField(default=0)

    class Meta:
        unique_together = ('category', 'name')