from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from juntagrico.entity.member import Member


@permission_required('badge.can_change')
def members_list(request):
    render_dict = {
        'change_date_disabled': True,
        'management_list': Member.objects.filter(badges__isnull=False).distinct()
    }
    return render(request, 'jbg/management_lists/badges.html', render_dict)
