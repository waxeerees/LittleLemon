from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from django.contrib.auth.models import User

menu_items = [
    {
        'title' : 'Chips',
        'price' : 1.49,
        'inventory' : 5,
    },
    {
        'title' : 'Beer',
        'price' : 2.49,
        'inventory' : 5,
    },
]

class MenuViewTest(TestCase):
    def setup(self):
        for item in menu_items:
            Menu.objects.create(
                title=item.title,
                price=item.price,
                inventory=item.inventory
            )
    
    def test_getall(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        menuitems = Menu.objects.all()
        serialized_menuitems = MenuSerializer(menuitems, many=True)
        request = self.client.get('/restaurant/menu/')
        
        self.assertEqual(request.data, serialized_menuitems.data)