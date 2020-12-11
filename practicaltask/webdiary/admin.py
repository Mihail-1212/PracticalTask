import json

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.template.defaultfilters import date

from . import models


@admin.register(models.Task)
class TaskScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_start', 'user')
    ordering = ("-date_start",)

    def changelist_view(self, request, extra_context=None):
        """
        Create chart data for tasks chart
        """
        chart_data = (
            self.get_queryset(request)
            .annotate( date=TruncMonth("date_start") )
            .values("date")
            .annotate(y=Count("id"))
            .order_by("date")
        )
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
