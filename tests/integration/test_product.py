from fastapi import status

URL_PRODUCTOS = "/v1/products/"

async def test_create_product_successful(async_client):
    payload = {"name": "Prueba", "price": 200}
    response = await async_client.post(URL_PRODUCTOS, json=payload)
    assert (response.status_code == status.HTTP_201_CREATED and
            response.json()["name"] == payload["name"] and
            response.json()["price"] == payload["price"])

# async def test_get_product(async_client):
#     response = await async_client.get(f"{URL_PRODUCTOS}/1")
#     assert response.status_code == status.HTTP_200_OK
#     data = response.json()
#     assert data["id"] == 1
#     assert data["name"] == "Product 1"