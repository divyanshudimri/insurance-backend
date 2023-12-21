from backend.router import router
from users.views import UserViewSet

app_name = 'users'

router.register(r'customer', UserViewSet, basename='customer')
