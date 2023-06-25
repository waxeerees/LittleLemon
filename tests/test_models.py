from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Orange Fresh",
            price=4.33,
            inventory=5
        )
        self.assertEqual(str(item), "Orange Fresh : 4.33")