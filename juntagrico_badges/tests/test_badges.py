from django.urls import reverse

from juntagrico_badges.entity.badges import Badge
from . import BadgesTestCase


class BadgesTests(BadgesTestCase):
    def test_home(self):
        self.assertGet(reverse('jbg:home'))

    def test_add_remove_badge(self):
        self_assignable_badge = Badge.objects.create(**self.badge_data(self_assignable=True))
        # should fail to add badge that is not self assignable
        self.assertGet(reverse('jbg:add-badge', args=[self.badge.id]), 302)
        self.badge.refresh_from_db()
        self.assertFalse(self.member in self.badge.members.all())
        # should succeed to add badge that is self assignable
        self.assertGet(reverse('jbg:add-badge', args=[self_assignable_badge.id]), 302)
        self_assignable_badge.refresh_from_db()
        self.assertTrue(self.member in self_assignable_badge.members.all())
        self.assertGet(reverse('jbg:remove-badge', args=[self_assignable_badge.id]), 302)
        self_assignable_badge.refresh_from_db()
        self.assertFalse(self.member in self_assignable_badge.members.all())

    def test_admin(self):
        self.assertGet(reverse('jbg:admin-memberslist'), 302)
        self.assertGet(reverse('jbg:admin-memberslist'), member=self.admin)
