from django.db import transaction

from insurance.models import Policy, PolicyHistory
from insurance.utils import PolicyStates


class PolicyStateMachine:
    TRANSITIONS = {
        'new_quoted': 'transition_from_new_to_quoted',
        'quoted_active': 'transition_from_quoted_to_active'
    }

    def __init__(self, policy: Policy, old_state: str, new_state: str) -> None:
        self.old_state = old_state
        self.new_state = new_state
        self.instance = policy.__class__.objects.filter(
            pk=policy.pk
        ).select_for_update(nowait=True).first()

    def _save_transition_event(self) -> None:
        PolicyHistory.objects.create(
            policy=self.instance,
            old_state=self.old_state,
            new_state=self.new_state
        )

    @transaction.atomic
    def transition_from_new_to_quoted(self) -> Policy:
        self.instance.state = PolicyStates.QUOTED.value
        self.instance.save(update_fields=['state'])
        self._save_transition_event()
        return self.instance

    @transaction.atomic
    def transition_from_quoted_to_active(self) -> Policy:
        self.instance.state = PolicyStates.ACTIVE.value
        self.instance.save(update_fields=['state'])
        self._save_transition_event()
        return self.instance
