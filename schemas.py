from uuid import UUID
from pydantic import BaseModel

class ContractModel(BaseModel):
    uuid: UUID
    contractor_name: str
    contractor_country: str
    contractor_location: str
    contractor_accommodation_type: str
    contractor_accommodation_unit_size: int
    contractor_accommodation_price: float

    class Config:
        schema_extra = {
            "example": {
                "uuid": "96581174-7d68-4fc8-9cb0-d5a8b263ab77",
                "contractor_name": "Bella Italia",
                "contractor_country": "Italy",
                "contractor_location": "lake garda",
                "contractor_accommodation_type": "mobilehomes",
                "contractor_accommodation_unit_size": 4,
                "contractor_accommodation_price": 6.499
        }
    }


