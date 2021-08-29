from django.urls import path
from juntagrico_badges import views, views_admin

urlpatterns = [
    path('jbg/home/', views.home, name='jbg-home'),
    path('jbg/add/<int:badge_id>/', views.add_badge, name='jbg-add-badge'),
    path('jbg/remove/<int:badge_id>/', views.remove_badge, name='jbg-remove-badge'),

    # admin
    path('jbg/admin/memberslist/', views_admin.members_list, name='jbg-admin-memberslist')
]
