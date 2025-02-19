import httpx

class GenericApi:
    base_url = None
    headers = None
    timeout = None

    async def get(self, endpoint, params=None):
        """Common GET request method."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/{endpoint}",
                    headers=self.headers,
                    params=params,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                return {"error": str(e)}

    async def post(self, endpoint, data=None, json=None):
        """Common POST request method."""
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/{endpoint}",
                    headers=self.headers,
                    data=data,
                    json=json,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as e:
                return {"error": str(e)}
