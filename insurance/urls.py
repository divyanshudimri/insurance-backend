from backend.router import router
from insurance.views import PolicyViewSet, QuoteViewSet

app_name = 'insurance'

router.register(r'quote', QuoteViewSet, basename='quote')
router.register(r'policies', PolicyViewSet, basename='policies')
