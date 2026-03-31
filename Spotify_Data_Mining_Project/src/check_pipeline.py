import pandas as pd
import os

print('='*80)
print('KIỂM TRA 4 BƯỚC PIPELINE')
print('='*80)

# Bước 1: INTEGRATION
print('\n1. INTEGRATION (01_integration.ipynb)')
if os.path.exists('data/processed/spotify_final_imputed.csv'):
    df_int = pd.read_csv('data/processed/spotify_final_imputed.csv')
    print(f'   File: spotify_final_imputed.csv OK')
    print(f'   Shape: {df_int.shape}')
    missing = df_int[['danceability','energy','tempo']].isnull().any(axis=1).sum()
    print(f'   Missing audio features: {missing}')
else:
    print('   File NOT FOUND')

# Bước 2: CLEANING
print('\n2. CLEANING (02_cleaning.ipynb)')
if os.path.exists('data/processed/spotify_cleaned_v2.csv'):
    df_clean = pd.read_csv('data/processed/spotify_cleaned_v2.csv')
    print(f'   File: spotify_cleaned_v2.csv OK')
    print(f'   Shape: {df_clean.shape}')
    print(f'   Missing values total: {df_clean.isnull().sum().sum()}')
else:
    print('   File NOT FOUND')

# Bước 3: EDA
print('\n3. EDA (03_eda.ipynb)')
if os.path.exists('data/processed/spotify_cleaned_scaled_v3.csv'):
    df_eda = pd.read_csv('data/processed/spotify_cleaned_scaled_v3.csv')
    print(f'   File: spotify_cleaned_scaled_v3.csv OK')
    print(f'   Shape: {df_eda.shape}')
    numeric_cols = df_eda.select_dtypes(include=['float64'])
    print(f'   Scaled range: Min={numeric_cols.min().min():.2f}, Max={numeric_cols.max().max():.2f}')
else:
    print('   File NOT FOUND')

# Bước 4: FEATURE ENGINEERING
print('\n4. FEATURE ENGINEERING (04_feature_engineering.ipynb)')
if os.path.exists('data/processed/spotify_for_ml.csv'):
    df_fe = pd.read_csv('data/processed/spotify_for_ml.csv')
    print(f'   File: spotify_for_ml.csv OK')
    print(f'   Shape: {df_fe.shape}')
    if 'is_hit' in df_fe.columns:
        hit_0 = (df_fe['is_hit']==0).sum()
        hit_1 = (df_fe['is_hit']==1).sum()
        print(f'   Target: is_hit (0:{hit_0}, 1:{hit_1})')
else:
    print('   File NOT FOUND')

print('\n' + '='*80)
