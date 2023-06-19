from fastapi import FastAPI
from schemas import ContractModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.post("/contractsubmit")
def submit_contract(contract_query: ContractModel):
    """ submit a contract and add to rabbitmq server"""

    name = contract_query.contactor_name
    country = contract_query.contactor_country
    location = contract_query.contractor_location
    accommodation_type = contract_query.contractor_accommodation_type
    accommodation_unit_size = contract_query.contractor_accommodation_unit_size
    accommodation_price = contract_query.contractor_accommodation_price

    return contract_query
