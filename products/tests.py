from rest_framework import status
from rest_framework.test import APITestCase



# test get and post request api/v1/porducts/
class ProductTestCase(APITestCase):
    
    def test_create_product(self):
        product = {
            'name': 'mobile test',
            'category': 'mobile',
            'colors': 'red, yellow',
            'product_features': '4G, 5G',
            'star_rating': 4.2,
            'percent_rating': '90%',
            'price': 1200,
            'description': 'some test text'
        }
        response = self.client.post("/api/v1/products/", product)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_product(self):
        response = self.client.get("/api/v1/products/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)