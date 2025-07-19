from fastapi import FastAPI
from api.api_v1.endpoints.first_preprocessing import router as first
from api.api_v1.endpoints.second_preprocessing import router as second
from api.api_v1.endpoints.third_preprocessing import router as third

import os 

app = FastAPI()

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app.include_router(first, prefix='/first')
app.include_router(second, prefix='/second')
app.include_router(third, prefix='/third')
