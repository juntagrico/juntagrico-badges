from django.urls import path
from juntagrico_badges import views, views_admin

app_name = 'jbg'
urlpatterns = [
    path('jbg/home/', views.home, name='home'),
    path('jbg/add/<int:badge_id>/', views.add_badge, name='add-badge'),
    path('jbg/remove/<int:badge_id>/', views.remove_badge, name='remove-badge'),

    # admin
    path('jbg/admin/memberslist/', views_admin.members_list, name='admin-memberslist')
]
