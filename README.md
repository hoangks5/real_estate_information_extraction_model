
# README

This is an API service built with FastAPI that utilizes OpenAI's GPT-3 model to extract real estate information from text descriptions and return it in JSON format.

## Getting Started

To use this API service, you'll need an OpenAI API key, which you can obtain from the [OpenAI website](https://beta.openai.com/signup/). Once you have your API key, create a file named `.env` in the root directory of this project and add your API key as follows:
``````
OPENAI_API_KEY=<your_api_key_here>
``````
Then, install the necessary packages by running the command:
``````
pip install -r requirements.txt
``````
You can then start the API service by running the command:
``````
uvicorn main:app --reload
``````
The API service will be available at `http://localhost:8000/`.

## API Endpoints

### GET /real_estate_information_extraction_model

Returns the name of the real estate information extraction model.

### POST /real_estate_information_extraction_model

Extracts real estate information from a text description and returns it in JSON format.

#### Request Body

| Parameter | Type   | Description                              |
|-----------|--------|------------------------------------------|
| info      | string | Text description of the real estate info |

#### Response

On success, returns a JSON object with the following schema:
``````
{
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
}
``````

### POST /real_estate_information_extraction_model_no_config

Extracts real estate information from a text description and returns it in JSON format. This endpoint does not provide a description of the expected JSON response.

#### Request Body

| Parameter | Type   | Description                              |
|-----------|--------|------------------------------------------|
| info      | string | Text description of the real estate info |

#### Response

On success, returns a JSON object with the same schema as the previous endpoint.
