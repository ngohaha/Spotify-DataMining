import os
import json

# Tên dự án
project_root = "Spotify_Data_Mining_Project"

# Cấu trúc thư mục chi tiết theo luồng CRISP-DM và yêu cầu của bạn
structure = {
    "data/raw": [],         # Chứa 2 file CSV gốc
    "data/external": [],    # Chứa dữ liệu Audio Features từ API
    "data/processed": [],   # Chứa các file sau từng bước (merged, cleaned, final)
    "notebooks": [
        "01_integration.ipynb",         # Gộp CSV và gọi API
        "02_cleaning.ipynb",            # Xử lý Null, đồng nhất đơn vị (ms -> min)
        "03_eda.ipynb",                 # Phân tích khám phá, vẽ biểu đồ tương quan
        "04_feature_engineering.ipynb",  # Tạo nhãn is_hit, chuẩn hóa (Scaling)
        "05_classification.ipynb",      # Decision Tree & ANN
        "06_clustering.ipynb",          # K-means & DBSCAN
        "07_association_rules.ipynb"    # Apriori & FP-Growth
    ],
    "src": [
        "__init__.py", 
        "spotify_api_utils.py"          # Nơi viết hàm gọi API để dùng lại
    ],
    "outputs/figures": [],              # Lưu các biểu đồ xuất ra từ EDA và Model
    "outputs/models": []                # Lưu các file model đã train (.pkl, .h5)
}

# Nội dung mặc định cho các file cấu hình gốc
root_files = {
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\nscikit-learn\nspotipy\nmlxtend\njupyter",
    ".gitignore": "*.csv\n*.zip\n__pycache__/\n.ipynb_checkpoints/\n.env\n.DS_Store",
    "README.md": "# Spotify Data Mining Project\n\n## Quy trình thực hiện (CRISP-DM)\n1. **Integration**: Kết hợp dữ liệu gốc và Spotify API.\n2. **Cleaning**: Làm sạch và chuẩn hóa dữ liệu.\n3. **EDA**: Phân tích khám phá và trực quan hóa.\n4. **Feature Engineering**: Biến đổi đặc trưng.\n5. **Modeling**: Triển khai các thuật toán khai phá."
}

def create_notebook(path):
    """Tạo file .ipynb trống với cấu trúc JSON chuẩn"""
    nb_content = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb_content, f, indent=4)

def initialize_project():
    print(f"--- Bắt đầu khởi tạo cấu trúc dự án ---")
    
    # Tạo thư mục và file trong structure
    for folder, files in structure.items():
        folder_path = os.path.join(project_root, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"[+] Đã tạo thư mục: {folder}")
        
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                if file.endswith('.ipynb'):
                    create_notebook(file_path)
                else:
                    open(file_path, 'w').close()
                print(f"    - Đã tạo file: {file}")
            else:
                # Tạo .gitkeep cho thư mục trống để có thể push lên git
                if not files:
                    open(os.path.join(folder_path, ".gitkeep"), 'w').close()

    # Tạo các file ở thư mục gốc
    for file_name, content in root_files.items():
        if not os.path.exists(file_name):
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[+] Đã tạo file cấu hình: {file_name}")

    print(f"--- Hoàn thành! Hệ thống đã sẵn sàng ---")

if __name__ == "__main__":
    initialize_project()