from fastapi import status



URL_PRODUCTOS = "/v1/products/"

class TestCrudProduct:
    async def test_create_product_successful(self, async_client):
        payload = {"name": "Prueba", "price": 200}
        response = await async_client.post(URL_PRODUCTOS, json=payload)
        assert (response.status_code == status.HTTP_201_CREATED and
                response.json()["name"] == payload["name"] and
            response.json()["price"] == payload["price"])


    async def test_get_product_successful(self, async_client, fake_product):
        response = await async_client.get(f"{URL_PRODUCTOS}{fake_product.id}")
        assert (    response.status_code == status.HTTP_200_OK and
                response.json()["id"] == fake_product.id and
                response.json()["name"] == fake_product.name and
                response.json()["price"] == fake_product.price
        )

    async def test_delete_product_successful(self, async_client, fake_product):
        response = await async_client.delete(f"{URL_PRODUCTOS}{fake_product.id}")
        assert (response.status_code == status.HTTP_200_OK and
                response.json()["id"] == fake_product.id and
                response.json()["name"] == fake_product.name and
                response.json()["price"] == fake_product.price
        )

    async def test_update_product_successful(self, async_client, fake_product):
        payload = {"name": "Prueba Update", "price": 300}
        response = await async_client.put(f"{URL_PRODUCTOS}{fake_product.id}", json=payload)
        assert (response.status_code == status.HTTP_200_OK and
                response.json()["id"] == fake_product.id and
                response.json()["name"] == payload["name"] and
                response.json()["price"] == payload["price"]
        )   

    async def test_patch_product_successful(self, async_client, fake_product):
        payload = {"price": 400}
        response = await async_client.patch(f"{URL_PRODUCTOS}{fake_product.id}", json=payload)
        assert (response.status_code == status.HTTP_200_OK and
                response.json()["id"] == fake_product.id and
                response.json()["name"] == fake_product.name and
                response.json()["price"] == payload["price"]
        )

    async def test_patch_product_not_found(self, async_client):
        payload = {"price": 400}
        response = await async_client.patch(f"{URL_PRODUCTOS}9999", json=payload)
        assert response.status_code == status.HTTP_404_NOT_FOUND