import os

from httpx import Client, Response
from dotenv import load_dotenv

load_dotenv()

class ApiClient(Client):
    

    def __init__(self):
        
        super().__init__(base_url=f"http://{os.getenv('RESOURSE_URL')}", cookies={})
        

    def request(self, method: str, url: str, **kwargs) -> Response:
       
        if "json" in kwargs:
            kwargs["data"] = kwargs.pop("json")

        return super().request(method, url, **kwargs)