import httpx
import os
from pydantic import BaseModel, Field
from pydantic_core import Url


class MobileXClient(BaseModel):
    base_url: Url = Field(
        default=Url("http://localhost:8000"),
    )

    def call[
        To: BaseModel
    ](self, function: str, input: BaseModel, output_model: type[To],) -> To | None:
        try:

            response = httpx.post(
                url=f"{self.base_url}func/{function}",
                json=input.model_dump(mode="json"),
                timeout=300.0,
            )

            data = response.json()
            if data is None:
                return None

            return output_model.model_validate(data)
        except Exception as e:
            # print(e)
            os.write(1, str(e).encode())
            return None
