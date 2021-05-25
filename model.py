from fastapi import FastAPI
import uvicorn

# taoj FastAPI instance
app = FastAPI()

# xác định path operation for rooy endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to my home!'}

# Xác định path operation for /name endpoint
@app.get('/{name}')
def hello_name(name: str):
    # xác định hàm lấy chuỗi (string) làm input
    return {'message': f'Welcome to my channel, {name}'}

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# loading iris dataset
iris = load_iris()

# lấy features and targets from the dataset
X = iris.data
Y = iris.target

# Fitting the model on the dataset
clf = GaussianNB()
clf.fit(X, Y)

""" 
    The data sent from the sclient side to the API is called a request body 
    The data sent from API to the client is calles a response body

    Để xác định request body chúng ta sẽ sử dụng "BaseModel" trong 'pydantic' module và xác định
    format dữ liệu khi gửi vào API.
    Để xác định request body chúng ta tạo một lớp kế thừa của lớp "BaseModel" và xác định các features
    hay các thuộc tính (attributes) của class cũng như type của chúng.

    Pydantic sẽ tạo ra các gợi ý về type trong suốt quá trình chạy và báo lỗi khi data is invalid.
"""
from pydantic import BaseModel

class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

"""
    Bây giờ chúng ta đã có request body. Việc cần làm cuối là thêm an endpoint cái mà chúng ta sẽ dụ đoán và
    return nó như một response
"""
@app.post('/predict')
def predict(data: request_body):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    class_idx = clf.predict(test_data)[0]   
    return {'class': iris.target_names[class_idx]}