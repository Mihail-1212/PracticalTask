from django import template

from webdiary.models import Task


register = template.Library()

"""Retun bootstrap4 badge class for status"""
@register.filter
def get_badge_status_class(value):
    return {
        Task.AVAILABLE_STATUSES.not_done: 'badge-primary',
        Task.AVAILABLE_STATUSES.done: 'badge-success',
    }[value.status]
