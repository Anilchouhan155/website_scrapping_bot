# Define the Pydantic model for JSON response
from typing import Union
from pydantic import BaseModel

class WebsiteDetails(BaseModel):
    industry: Union[str, None] = None
    company_size: Union[str, None] = None
    company_location: Union[str, None] = None