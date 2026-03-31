# 🎵 Spotify Data Mining Project

Dự án khai phá dữ liệu Spotify sử dụng **K-Means Clustering** và **FP-Growth Association Rules** để phân tích đặc điểm âm học và phát hiện quy tắc liên kết trong nhạc.

## 📊 Tổng quan dự án

**Mục tiêu:**
- Phân cụm bài hát dựa trên đặc trưng âm học (11 features)
- Khám phá quy tắc liên kết giữa các đặc điểm âm học
- Phân loại thể loại nhạc dựa trên clustering
- Rút ra insights về mối quan hệ giữa các tính chất âm nhạc

**Dữ liệu:**
- 4 nguồn từ Kaggle: Track Features, Top Hits, Grammy Awards, Hot Music
- Kết hợp với Spotify Audio Features API
- Tổng: 162,422 bài hát với 326 features

## 🔄 Quy trình thực hiện (CRISP-DM)

### 1️⃣ **Integration** (`01_integration.ipynb`)
- Tải dữ liệu từ 4 nguồn Kaggle
- Kết nối Spotify API để lấy audio features
- Merge dữ liệu và kiểm tra duplicates
- **Output:** `data/processed/spotify_merged.csv`

### 2️⃣ **Cleaning** (`02_cleaning.ipynb`)
- Loại bỏ giá trị NaN, duplicates
- Xử lý outliers
- Chuẩn hóa features (StandardScaler)
- **Output:** `data/processed/spotify_cleaned.csv`

### 3️⃣ **EDA** (`03_eda.ipynb`)
- Phân tích thống kê từng feature
- Trực quan hóa phân phối dữ liệu
- Kiểm tra tương quan (correlation)
- Phân tích target variable (is_hit)

### 4️⃣ **Feature Engineering** (`04_feature_engineering.ipynb`)
- Chọn lọc 11 audio features chính
- Tạo feature ML-ready (326 tổng features)
- Chuẩn hóa và scaling
- **Output:** `data/processed/spotify_for_ml.csv`

### 5️⃣ **Clustering** (`06_clustering.ipynb`)
- **Thuật toán:** K-Means Clustering
- **Optimization:** Elbow Method + Silhouette Score
- Visualize clusters bằng PCA 2D
- Phân tích đặc điểm của từng cluster
- **Outputs:**
  - `outputs/figures/elbow_silhouette.png` - Elbow curve
  - `outputs/figures/cluster_radar_charts.png` - Radar charts
  - `outputs/figures/clustering_pca_2d.png` - PCA visualization
  - `data/processed/spotify_with_clusters.csv` - Dữ liệu có cluster labels

### 6️⃣ **Association Rules** (`07_association_rules.ipynb`)
- **Thuật toán:** FP-Growth
- Categorize audio features (High/Low)
- Tìm frequent itemsets (min_support=5%)
- Tạo association rules (min_confidence=30%)
- Tính toán Support, Confidence, Lift
- **Outputs:**
  - `outputs/figures/association_rules_scatter.png` - Scatter plots
  - `outputs/association_rules_top50.csv` - Top 50 rules
  - `outputs/frequent_itemsets.csv` - Frequent itemsets

## 📋 Audio Features (11 đặc điểm)

| Feature | Mô tả |
|---------|------|
| **danceability** | 0-1: Bài hát bao lâu thích hợp để nhảy |
| **energy** | 0-1: Cường độ âm lượng và hoạt động |
| **key** | 0-11: Tonal center (C, C#, D, ..., B) |
| **loudness** | dB: Độ lớn trung bình |
| **mode** | 0-1: Major (1) hay Minor (0) |
| **speechiness** | 0-1: Lượng lời nói trong track |
| **acousticness** | 0-1: Độ acoustic (không điện tử) |
| **instrumentalness** | 0-1: Không có giọng hát |
| **liveness** | 0-1: Cảm giác live performance |
| **valence** | 0-1: Tích cực hay tiêu cực |
| **tempo** | BPM: Tốc độ nhạc |

## 💾 Cấu trúc dữ liệu

```
Spotify_Data_Mining_Project/
├── data/
│   ├── raw/                           # Dữ liệu gốc
│   │   ├── spotify_data_clean.csv
│   │   └── track_data_final.csv
│   ├── external/                      # Dữ liệu từ Kaggle
│   └── processed/                     # Dữ liệu sau xử lý
│       ├── spotify_merged.csv
│       ├── spotify_cleaned.csv
│       ├── spotify_for_ml.csv
│       ├── spotify_with_clusters.csv
│       ├── cluster_profiles.csv
│       ├── association_rules_top50.csv
│       └── frequent_itemsets.csv
├── notebooks/
│   ├── 01_integration.ipynb           # Tích hợp dữ liệu
│   ├── 02_cleaning.ipynb              # Làm sạch
│   ├── 03_eda.ipynb                   # Phân tích khám phá
│   ├── 04_feature_engineering.ipynb   # Feature engineering
│   ├── 06_clustering.ipynb            # K-Means clustering
│   └── 07_association_rules.ipynb     # FP-Growth rules
├── outputs/
│   ├── figures/                       # Biểu đồ và visualizations
│   │   ├── elbow_silhouette.png
│   │   ├── cluster_radar_charts.png
│   │   ├── clustering_pca_2d.png
│   │   └── association_rules_scatter.png
│   └── models/                        # Lưu models
├── src/
│   ├── __init__.py
│   └── spotify_api_utils.py           # Utility functions
├── requirements.txt                   # Dependencies
└── README.md
```

## 🚀 Cài đặt & Chạy

### 1. Clone repository
```bash
git clone https://github.com/tutrong2706/Spotify-DataMining.git
cd Spotify-DataMining
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Spotify API (nếu cần audio features)
```bash
# Tạo file ~/.kaggle/kaggle.json với credentials
# Hoặc setup Spotify API credentials
```

### 4. Chạy các notebook (theo thứ tự)
```bash
jupyter notebook
# Chạy: 01 → 02 → 03 → 04 → 06 → 07
```

## 📊 Kết quả chính

### Clustering Insights
- **Optimal Clusters:** K = ? (tùy thuộc Silhouette Score)
- **Cluster Interpretation:** 
  - Cluster 0: Energetic & Danceable Music
  - Cluster 1: Acoustic & Instrumental Music
  - Cluster 2: ... (tùy dữ liệu)
  
### Association Rules Insights
- **Frequent Patterns:** Những feature nào thường xuất hiện cùng nhau
- **Strong Rules (Lift > 2):** Những quy tắc mạnh nhất
- **Actionable Rules:** Insights cho recommendation systems

## 🛠️ Dependencies

| Package | Version | Mục đích |
|---------|---------|---------|
| pandas | >=1.3.0 | Xử lý dữ liệu |
| numpy | >=1.20.0 | Tính toán số học |
| scikit-learn | >=1.0.0 | Machine Learning |
| matplotlib | >=3.4.0 | Visualizations |
| seaborn | >=0.11.0 | Statistical plots |
| mlxtend | >=0.19.0 | FP-Growth & Association Rules |
| spotipy | >=2.20.0 | Spotify API |
| jupyter | >=1.0.0 | Notebooks |

## 📈 Kỳ vọng Output

### Figures (PNG)
- Elbow curve cho K-Means optimization
- Silhouette scores visualization
- Radar charts cho cluster profiles
- PCA 2D scatter plots
- Support vs Confidence vs Lift scatter plots

### Data Files (CSV)
- spotify_with_clusters.csv: 12,476 rows × 327 columns
- cluster_profiles.csv: Tóm tắt đặc điểm từng cluster
- association_rules_top50.csv: 50 quy tắc mạnh nhất
- frequent_itemsets.csv: Tất cả frequent itemsets

## 👨‍💻 Tác giả
**Trần Thanh Trọng** - Data Mining Student @ UTE

## 📝 Ghi chú
- Dữ liệu: 12,476 tracks sau cleaning
- Features: 11 audio features + các features khác
- Target: is_hit (binary classification)
- Thời gian chạy: ~5-10 phút tùy máy tính