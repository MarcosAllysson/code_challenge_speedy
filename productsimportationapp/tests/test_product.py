import requests


class TestPosts:
    endpoint_products_history = 'http://127.0.0.1:8000/api/v1/'

    def test_get_products_history(self):
        products = requests.get(url=self.endpoint_products_history)
        assert products.status_code == 200
