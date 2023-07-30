from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenu(TestCase):
    def test_menu(self):
        menu_item = Menu.objects.create(
            title="Coco",
            price=2.30,
            inventory=43
        )
        self.assertEqual(str(menu_item), 'Coco : 2.30')
        
# tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient

class TestMenuView(TestCase):
    def testSetUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(name='Item 1', price=9.99, inventory=10)
        Menu.objects.create(name='Item 2', price=12.99, inventory=5)
        Menu.objects.create(name='Item 3', price=7.50, inventory=8)

    def test_getall(self):
        # Use the APIClient to make a GET request to the Menu endpoint
        client = APIClient()
        response = client.get('/api/menu/')  # Replace '/api/menu/' with your actual URL

        # Retrieve all Menu objects from the database
        menu_items = Menu.objects.all()

        # Serialize the Menu objects
        serializer = MenuSerializer(menu_items, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
