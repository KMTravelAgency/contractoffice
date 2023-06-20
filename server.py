from fastapi import FastAPI
from schemas import ContractModel
from rabbitmq_helper import rabbitmq

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/contractsubmit")
async def submit_contract(contract_query: ContractModel):
    """ submit a contract and add to rabbitmq server"""

    name = contract_query.contractor_name
    country = contract_query.contractor_country
    location = contract_query.contractor_location
    accommodation_type = contract_query.contractor_accommodation_type
    accommodation_unit_size = contract_query.contractor_accommodation_unit_size
    accommodation_price = contract_query.contractor_accommodation_price

    await rabbitmq.publish_message(
        message_body= {
            "name": name,
            "country": country,
            "location": location,
            "accommodation_type": accommodation_type,
            "accommodation_unit_size": accommodation_unit_size,
            "accommodation_price": accommodation_price
        }
    )

    return contract_query
