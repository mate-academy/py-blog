from django.db.models import Count
from django.db.models import functions
from django.db.models.query import QuerySet

from blog.models import Post


def get_publication_dates() -> list[list]:
    dates = (
        Post.objects.annotate(
            year=functions.ExtractYear("created_time"),
            month=functions.ExtractMonth("created_time"),
        )
        .values("year", "month")
        .annotate(count=Count("id"))
        .order_by("-year", "-month")
    )

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    publication_dates = [
        [
            f"{month_names[date['month']]} {date['year']}",
            date["month"],
            date["year"]
        ]
        for date in dates
    ]

    return publication_dates


def get_posts_by_month_and_year(year, month) -> QuerySet:
    posts_in_month_year = Post.objects.filter(
        created_time__year=year, created_time__month=month
    )
    return posts_in_month_year
