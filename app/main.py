import os
import openai
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Form
import json


openai.api_key = os.getenv("OPENAI_API_KEY")
content_system = """Bạn là một model trích xuất dữ liệu văn bản bất động sản từ thông tin miêu tả thành một data json với schema bên dưới
'location': Địa chỉ,
'area': Diện tích,
'price: Giá cho thuê hoặc bán,
'contact': {
'name' : Tên người bán,
'phone' : Số điện thoại người bán
},
"details": {
    "floors": Số tầng,
    "bedrooms": Số phòng ngủ,
    "bathrooms": Số phòng tắm,
    "living_rooms": Số phòng khách,
    "kitchens": Số phòng bếp,
    "toilets": Số phòng toilets,
    "balconies": Ban công (true hoặc false),
    "furniture": Nội thất như thế nào,
  }
"""





app = FastAPI(
    title="API",
    description="AI",
    version="1.0",
    docs_url='/docs',
    openapi_url='/openapi.json', # This line solved my issue, in my case it was a lambda function
    redoc_url='/redoc'
)

@app.get('//real_estate_information_extraction_model')
def get_service():
    return 'Real Estate Information Extraction Model'


    

@app.post("//real_estate_information_extraction_model")
def Real_Estate_Information_Extraction_Model(info: str = Form()):
    


    history_chat = [
            {"role": "system", "content": content_system},
        ]
    history_chat.append({"role": "user", "content": info})
    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-0301",
                        messages=history_chat
                        )
    result = completion.choices[0].message['content']
    return json.loads(result)

@app.post("//real_estate_information_extraction_model_no_config")
def Real_Estate_Information_Extraction_Model_No_Config(info: str = Form()):
    

    history_chat = [
            {"role": "system", "content": "Bạn là một model trích xuất dữ liệu văn bản bất động sản từ thông tin miêu tả thành một data json"},
        ]
    history_chat.append({"role": "user", "content": info})
    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-0301",
                        messages=history_chat
                        )
    result = completion.choices[0].message['content']
    return json.loads(result)


    

