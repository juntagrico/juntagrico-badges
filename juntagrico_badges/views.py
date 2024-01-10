from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from juntagrico.view_decorators import highlighted_menu

from juntagrico_badges.entity.badges import Badge


@login_required
@highlighted_menu('badges')
def home(request):
    renderdict = {
        'badges': Badge.objects.filter(members=request.user.member),
        'available_badges': Badge.objects.filter(self_assignable=True).exclude(members=request.user.member)
    }
    return render(request, "jbg/home.html", renderdict)


@login_required
def add_badge(request, badge_id):
    badge = get_object_or_404(Badge, id=badge_id)
    if badge.self_assignable:
        member = request.user.member
        member.badges.add(badge)
        member.save()
    return redirect('jbg:home')


@login_required
def remove_badge(request, badge_id):
    badge = get_object_or_404(Badge, id=badge_id)
    if badge.self_assignable:
        member = request.user.member
        member.badges.remove(badge)
        member.save()
    return redirect('jbg:home')
