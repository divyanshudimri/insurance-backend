from rest_framework import serializers

from insurance.fsm import PolicyStateMachine as fsm
from insurance.models import Policy, PolicyHistory
from insurance.utils import PremiumCalculator
from users.models import User


class QuoteSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField(required=False)
    quote_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Policy
        fields = ('customer_id', 'type', 'state', 'premium', 'cover', 'quote_id')
        read_only_fields = ('premium', 'cover',)

    default_error_messages = {
        'user_not_found': 'Customer not found',
        'state_change_failed': 'Cannot move from {source} to {destination}'
    }

    def create(self, validated_data):
        user = User.objects.filter(pk=validated_data.get('customer_id')).first()
        premium_calculator = PremiumCalculator(user, validated_data['type'])
        premium, cover = premium_calculator.calculate_premium_and_cover()
        if not user:
            raise self.fail('user_not_found')
        validated_data['customer'] = user
        validated_data['premium'] = premium
        validated_data['cover'] = cover
        validated_data.pop('state', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        state = validated_data.pop('state', None)
        if state:
            machine = fsm(instance, instance.state, state)
            transition = machine.TRANSITIONS.get(f'{instance.state}_{state}')
            if transition:
                instance = getattr(machine, transition)()
            else:
                self.fail('state_change_failed', source=instance.state, destination=state)

        return instance


class PolicyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyHistory
        fields = '__all__'


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
