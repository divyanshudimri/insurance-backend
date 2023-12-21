from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from insurance.models import Policy, PolicyHistory
from insurance.serializers import PolicyHistorySerializer, PolicySerializer, QuoteSerializer
from insurance.utils import PolicyStates


class QuoteViewSet(ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Policy.objects.exclude(state=PolicyStates.ACTIVE.value).order_by('-created_at')
    filterset_fields = ['customer_id', 'type']


class PolicyViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PolicySerializer
    queryset = Policy.objects.filter(state=PolicyStates.ACTIVE.value).order_by('-created_at')
    filterset_fields = ['customer_id', 'type']

    @action(detail=True)
    def history(self, request, pk=None):
        history = PolicyHistory.objects.filter(policy_id=pk)
        return Response(PolicyHistorySerializer(history, many=True).data)
