from django.contrib import admin

from durin.admin import AuthTokenAdmin
from durin.models import AuthToken, Client
from guardian.admin import GuardedModelAdmin

from .models import Job, Tag


class JobAdminView(GuardedModelAdmin):
    list_display = (
        "id",
        "status",
        "source",
        "observable_name",
        "observable_classification",
        "file_name",
        "file_mimetype",
        "received_request_time",
    )
    list_display_link = ("id", "status")
    search_fields = ("source", "md5", "observable_name")


class TagAdminView(GuardedModelAdmin):
    list_display = ("id", "label", "color")
    search_fields = ("label", "color")


# Auth Token stuff
class CustomAuthTokenAdmin(AuthTokenAdmin):
    """
    Custom admin view for AuthTokenAdmin model
    """

    exclude = ("token", "expiry", "client")

    def save_model(self, request, obj, form, change):
        client = Client.objects.get(name="pyintelowl")
        return AuthToken.objects.create(obj.user, client)


admin.site.register(Job, JobAdminView)
admin.site.register(Tag, TagAdminView)

admin.site.unregister(AuthToken)
admin.site.register(AuthToken, CustomAuthTokenAdmin)
