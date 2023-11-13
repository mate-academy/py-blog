from datetime import datetime, timedelta

from django.contrib import admin
from django.contrib.auth.models import Group
from blog.models import User, Post, Commentary

admin.site.unregister(Group)


class DateTimeFilter(admin.SimpleListFilter):
    title = "Created time"
    parameter_name = "created_time"
    parameter_date = "date"
    parameter_time = "time"
    template = "admin/date_time_filter.html"

    def __init__(self, request, params, model, model_admin):
        super().__init__(request, params, model, model_admin)
        if self.parameter_date in params:
            value = params.pop(self.parameter_date)
            self.used_parameters[self.parameter_date] = value

        if self.parameter_time in params:
            value = params.pop(self.parameter_time)
            self.used_parameters[self.parameter_time] = value

    def lookups(self, request, model_admin):
        return (("", ""),)

    def queryset(self, request, queryset) -> None:
        if self.date_value():
            start_date = datetime.strptime(
                self.date_value(),
                "%Y-%m-%d"
            )
            end_date = datetime(
                start_date.year,
                start_date.month,
                start_date.day,
                23,
                59,
                59
            )
            queryset = queryset.filter(
                created_time__range=(start_date, end_date)
            )
        if self.time_value():
            start_time = datetime.strptime(
                self.time_value(),
                "%H:%M"
            ).time()
            end_time = datetime.strptime(
                f"{start_time.hour}:59",
                "%H:%M"
            ).time()
            queryset = queryset.filter(
                created_time__time__range=(start_time, end_time)
            )

        return queryset

    def date_value(self):
        return self.used_parameters.get(self.parameter_date)

    def time_value(self):
        return self.used_parameters.get(self.parameter_time)


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")


@admin.register(Commentary)
class CommentaryModelAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "content", "created_time")
    list_filter = ("post", "user", DateTimeFilter)
    ordering = ("-created_time",)


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("owner", DateTimeFilter)
    ordering = ("-created_time",)
