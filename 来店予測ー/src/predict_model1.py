# ライブラリインストール
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


# CSVファイルの読み込み
df = pd.read_csv("C:\\Users\\sakamoto_riku_microa\\Desktop\\来店予測ー\\Data\\raw\\Visit_prediction20240315.csv")

# データ確認
print(df.head()) 

# 欠損値確認
missing_values = df.isnull().sum()

# 特徴量と目的変数を定義
X = df.drop('来店率', axis=1)
y = df['来店率']

# 訓練用データとテスト用データに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルの作成
gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_model.fit(X_train, y_train)

# テストデータに対する予測
y_pred_gb = gb_model.predict(X_test)

# 勾配ブースティングモデルの評価
mse_gb = mean_squared_error(y_test, y_pred_gb)
rmse_gb = np.sqrt(mse_gb)
r2_gb = r2_score(y_test, y_pred_gb)

(rmse_gb, r2_gb)

from joblib import dump
dump(gb_model,'gb_model.joblib')

