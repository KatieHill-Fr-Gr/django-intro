from django.urls import path
from records.views import RecordListView
from records.views import RecordDetailView


urlpatterns = [
    path('', RecordListView.as_view()),
    path('<int:pk>/', RecordDetailView.as_view())
]

# You can only have one path per end point (you can't do another ' ')
# Look up documentation on path converters