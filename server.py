from fastapi import FastAPI
from schemas import ContractModel
from rabbitmq_helper import rabbitmq
from uuid import UUID

app = FastAPI()

@app.post("/contractsubmit")
async def submit_contract(contract_query: ContractModel):
    """ submit a contract and add to rabbitmq server """
    uuid = str(contract_query.uuid)
    name = contract_query.contractor_name
    country = contract_query.contractor_country
    location = contract_query.contractor_location
    accommodation_type = contract_query.contractor_accommodation_type
    accommodation_unit_size = contract_query.contractor_accommodation_unit_size
    accommodation_price = contract_query.contractor_accommodation_price

    await rabbitmq.publish_message(
        message_body= {
            "uuid": uuid,
            "name": name,
            "country": country,
            "location": location,
            "accommodation_type": accommodation_type,
            "accommodation_unit_size": accommodation_unit_size,
            "accommodation_price": accommodation_price
        }
    )

    return contract_query