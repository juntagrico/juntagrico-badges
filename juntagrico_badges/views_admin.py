from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from juntagrico.entity.member import Member


@permission_required('badge.can_change')
def members_list(request):
    return render(request, 'jbg/management_lists/badges.html', {
        'management_list': Member.objects.filter(badges__isnull=False).distinct()
    })
