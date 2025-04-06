from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category

class ProductTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Laptops")
        self.product = Product.objects.create(
            name="High-End Gaming Laptop",
            description="A powerful laptop for gaming enthusiasts.",
            price=2000.00,
            stock_quantity=10,
            category=self.category
        )

    def test_get_product_list(self):
        url = reverse('product-list')  # Generated automatically by DRF router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
