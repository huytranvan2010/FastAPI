# FastAPI

API - Application pesornal iterface (giao diện ứng dụng người dùng).

Bình thường xây dựng model nhận diện khuôn mặt chẳng hạn, không thể bảo người dùng (kiểm tra) cài cắm môi trường, chạy câu lệnh để test thử. Lúc này chúng ta cần API. 

FastAPI có hỗ trợ:
* Đồng bộ Async
* Validate data (bên Flask phải thực hiện thủ công), dùng pydantic
* Tự sinh documents (hỗ trợ bên front end)

Cài đặt
```python
pip install fastapi
pip install uvicorn
```
# Tài liệu tham khảo
https://fastapi.tiangolo.com/
