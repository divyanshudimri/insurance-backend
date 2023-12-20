from django.db import models
from django.utils import timezone

from insurance.utils import PolicyStates, PolicyTypes


class Policy(models.Model):
    type = models.CharField(
        max_length=40,
        choices=PolicyTypes.get_choices(),
        default=PolicyTypes.PERSONAL_ACCIDENT.value
    )
    state = models.CharField(
        max_length=40,
        choices=PolicyStates.get_choices(),
        default=PolicyStates.NEW.value
    )
    premium = models.PositiveIntegerField(default=0)
    cover = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(
        'users.User',
        null=True, related_name='policies',
        on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id}-{self.state}-{self.customer.get_full_name()}'


class PolicyHistory(models.Model):
    policy = models.ForeignKey(
        Policy,
        related_name='history',
        on_delete=models.PROTECT
    )
    new_state = models.CharField(
        max_length=40,
        choices=PolicyStates.get_choices(),
        default=PolicyStates.NEW
    )
    old_state = models.CharField(
        max_length=40,
        choices=PolicyStates.get_choices(),
        default=PolicyStates.NEW
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Policy id {self.policy_id}-{self.old_state}->{self.new_state}'
