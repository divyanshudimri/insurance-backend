from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from insurance.models import Policy, PolicyHistory


class PolicyHistoryAdmin(admin.TabularInline):
    model = PolicyHistory
    verbose_name = 'Policy history'
    verbose_name_plural = 'Policy history'
    extra = 1
    readonly_fields = ('policy_link', 'old_state', 'new_state', 'created_at')
    classes = ['collapse']

    def policy_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:insurance_policy_change", args=(obj.policy.pk,)),
            obj.policy.pk
        ))
    policy_link.short_description = 'policy'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'state', 'user_link')
    list_filter = ('state', 'type')
    readonly_fields = ('user_link',)
    inlines = [PolicyHistoryAdmin]

    def user_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:users_user_change", args=(obj.customer.pk,)),
            obj.customer.username
        ))
    user_link.short_description = 'user'
