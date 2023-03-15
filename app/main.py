import os
import openai
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, Form
import json


openai.api_key = os.getenv("OPENAI_API_KEY")
content_system = """Bạn là một model trích xuất dữ liệu văn bản bất động sản từ thông tin miêu tả thành một data json cực nhanh và chính xác với schema bên dưới
'location': Địa chỉ,
'area': Diện tích,
'price: Giá cho thuê hoặc bán,
'contact': {
'name' : Tên người bán,
'phone' : Số điện thoại người bán
},
"transaction_type" : Loại giao dịch (Cần bán hoặc Cho thuê),
"type_of_real_estate": Loại bất động sản ( Nhà cấp 4, Đất không, Chỉ vườn, Nhà mới, Chung cư, Nhà mặt phố),
"details": {
    "floors": Số tầng,
    "bedrooms": Số phòng ngủ,
    "bathrooms": Số phòng tắm,
    "living_rooms": Số phòng khách,
    "kitchens": Số phòng bếp,
    "toilets": Số phòng toilets,
    "balconies": Ban công (true hoặc false),
    "furniture": Nội thất như thế nào,
    "facade" : Mặt tiền như thế nào ( 1 mặt thoáng, 2 mặt thoáng, 3 mặt thoáng, 4 mặt thoáng, lô góc),
    "front_width" : Kích thước mặt tiền bao nhiêu mét,
    "end_width" : Kích thước mặt hậu bao nhiêu mét,
    "floor_no" : Tầng số bao nhiêu ( chỉ áp dụng với chung cư ),
    "house_orientation" : Hướng cửa ( Đông, Tây, Nam, Bắc ),
    "year_of_construction" : Năm xây dựng
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


    

