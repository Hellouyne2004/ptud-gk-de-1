# ptud-gk-de-1

## Thông tin cá nhân
- Nguyễn Thái Uy - 22656171
- 
## Mô tả project
Đây là một ứng dụng blog đơn giản được phát triển bằng Django với các chức năng chính :
- Đăng Ký và Đăng Nhập
- Quản lý bài viết
- Quản lý bình luận
- Tìm kiếm bài viết
- Theo dõi bài viết

## Hướng dẫn cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.9 trở lên
- pip (Python package installer)
- Virtual environment (venv)

### Cài đặt
1. Clone repository về máy của bạn:
    ```sh
    git clone https://github.com/Hellouyne2004/ptud-gk-de-1.git
    cd ptud-gk-de-1
    ```

2. Tạo và kích hoạt môi trường ảo:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Trên Linux/macOS
    # venv\Scripts\activate   # Trên Windows
    ```
    
3. Cài đặt các thư viện cần thiết:
    ```sh
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. Chạy migrations để tạo cơ sở dữ liệu:
    ```sh
    cd website
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Tạo tài khoản admin:
    ```sh
    python manage.py createsuperuser
    ```

### Chạy server
1. Chạy file fake data để hiện tạo dữ liệu và hình ảnh random:
    ```sh
    python manage.py create_fake_data
    ```
    
2. Chạy server:
    ```sh
    python manage.py runserver
    ```

3. Truy cập ứng dụng tại địa chỉ:
    ```
    http://127.0.0.1:8000/
    ```
