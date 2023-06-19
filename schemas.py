from pydantic import BaseModel

class ContractModel(BaseModel):
    contractor_name: str
    contractor_country: str
    contractor_location: str
    contractor_accommodation_type: str
    contractor_accommodation_unit_size: int
    contractor_accommodation_price: float

    class Config:
        schema_extra = {
            "example": {
                "contractor_name": "Bella Italia",
                "contractor_country": "Italia",
                "contractor_location": "lake garda",
                "contractor_accommodation_type": "mobilehomes",
                "contractor_accommodation_unit_size": 4,
                "contractor_accommodation_price": 6.499
        }
    }


