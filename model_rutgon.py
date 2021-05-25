from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel

# tạo FastAPI instance
app = FastAPI()

# tạo class để xác định request body và gợi ý về kiểu mỗi thuộc tính
class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# load dataset
iris = load_iris()

# lấy features và targets
X = iris.data
Y = iris.target 

# tạo và fitting the model
clf = GaussianNB()
clf.fit(X, Y)

# tạo Endpoint để nhận data và dự đoán
@app.post('/predict')
def predict(data: request_body):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # predict the class
    class_idx = clf.predict(test_data)[0]

    # return kết quả
    return {'class': iris.target_names[class_idx]}

"""
    Nên mở docs để xem cách chạy sẽ dễ hơn.
"""