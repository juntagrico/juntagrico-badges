from juntagrico.tests import JuntagricoTestCase
from juntagrico_badges.entity.badges import Badge


class BadgesTestCase(JuntagricoTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.load_members()
        cls.set_up_badge()

    @classmethod
    def set_up_badge(cls):
        cls.member_with_badge = cls.create_member('member_with_badge@email.org')
        cls.badge = Badge.objects.create(**cls.badge_data('test_badge'))
        cls.badge.members.add(cls.member_with_badge)
        cls.badge.save()

    @staticmethod
    def badge_data(name='Badge1', **kwargs):
        data = {
            'name': name,
            'description': 'description',
            'self_assignable': False
        }
        data.update(**kwargs)
        return data
