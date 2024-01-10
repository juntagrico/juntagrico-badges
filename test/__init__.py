from django.test import TestCase

from juntagrico.entity.member import Member

from juntagrico_badges.entity.badges import Badge


class BadgesTestCase(TestCase):
    def setUp(self):
        self.set_up_member()
        self.set_up_badge()

    def set_up_member(self):
        self.member = self.create_member('member@email.org')
        self.member_with_badge = self.create_member('member_with_badge@email.org')

    def set_up_badge(self):
        self.badge = Badge.objects.create(**self.badge_data('test_badge'))
        self.badge.members.add(self.member_with_badge)
        self.badge.save()

    def assertGet(self, url, code=200, member=None):
        login_member = member or self.member
        self.client.force_login(login_member.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, code)

    def assertPost(self, url, data=None, code=200, member=None):
        login_member = member or self.member
        self.client.force_login(login_member.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, code)

    @staticmethod
    def create_member(email):
        member_data = {'first_name': 'first_name',
                       'last_name': 'last_name',
                       'email': email,
                       'addr_street': 'addr_street',
                       'addr_zipcode': 'addr_zipcode',
                       'addr_location': 'addr_location',
                       'phone': 'phone',
                       'confirmed': True,
                       }
        member = Member.objects.create(**member_data)
        member.user.set_password('12345')
        member.user.save()
        return member

    @staticmethod
    def create_admin():
        """
        admin member
        """
        admin_data = {'first_name': 'admin',
                      'last_name': 'last_name',
                      'email': 'admin@email.org',
                      'addr_street': 'addr_street',
                      'addr_zipcode': 'addr_zipcode',
                      'addr_location': 'addr_location',
                      'phone': 'phone',
                      'confirmed': True,
                      }
        admin = Member.objects.create(**admin_data)
        admin.user.set_password("123456")
        admin.user.is_staff = True
        admin.user.is_superuser = True
        admin.user.save()
        return admin

    @staticmethod
    def badge_data(name='Badge1', **kwargs):
        data = {
            'name': name,
            'description': 'description',
            'self_assignable': False
        }
        data.update(**kwargs)
        return data
