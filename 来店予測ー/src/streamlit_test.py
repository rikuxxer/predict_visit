#外部ライブラリのインストール
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_folium import st_folium
import folium
from geopy.distance import geodesic
from joblib import load

#タイトルの表示
st.header('Univerese GEO 来店率予測')

#サイドバーの入力項目

#ポテンシャルUBの入力
potential=st.sidebar.number_input ("▼ポテンシャルUB" , min_value=0)

#配信日数の入力
streaming_days=st.sidebar.number_input ("▼配信日数" , min_value=0)

#配信日数の入力
mesureing_days=st.sidebar.number_input ("▼計測日数" , min_value=0)

# TG半径の入力を受け取る\
T_radius = st.sidebar.selectbox("▼TG半径(m)",("50","100","200","300","400","500","600","700","800","900","1000","2000","3000","5000","6000","7000","8000","9000","10000"))

# 計測地点の入力

mesurement_visit = st.sidebar.text_area("▼ 計測地点の緯度経度 \n（例: 35.681236, 139.767125）", "35.1455957,136.9933597", key="mesurement_visit")
measurment_location1 = [tuple(map(float, loc.split(','))) for loc in mesurement_visit.strip().split('\n')]
measurement_location_2 = tuple(map(float, mesurement_visit.split(',')))


# TG地点の入力
TG_Iloc = st.sidebar.text_area("▼TG地点の緯度経度 \n（例: 35.681236, 139.767125）\n複数入力する場合は改行してください。", "35.681236, 139.767125\n35.6553809, 139.7571289\n33.5897275, 130.4207274", key="TG_Iloc")
TG_locations = [tuple(map(float, loc.split(','))) for loc in TG_Iloc.strip().split('\n')]

# 各TG地点と最初の計測地点間の距離を計算
distances = [geodesic(measurment_location1[0], tg_loc).kilometers for tg_loc in TG_locations]

# 各TG地点と計測地点間の距離を計算
sorted_distances = sorted(distances)

# distancesリストが空かどうかを確認し、空でない場合のみ平均と中央値を計算
if distances:
    average_distance = np.mean(distances)
    median_distance = np.median(distances)
else:
    average_distance = 0
    median_distance = 0

# 最も近い距離のトップ5と最も遠い距離のトップ5を取得する際に、リストの長さを確認
closest_distances_top5 = sorted_distances[:5] if len(sorted_distances) >= 5 else [0] * 5
furthest_distances_top5 = sorted_distances[-5:] if len(sorted_distances) >= 5 else [0] * 5

# 格納された数値が空（リストが空の場合を含む）の場合に0を出力
input_feature_5 = average_distance
input_feature_6 = median_distance
input_feature_7 = closest_distances_top5[0] if len(closest_distances_top5) > 0 else 0
input_feature_8 = closest_distances_top5[1] if len(closest_distances_top5) > 1 else 0
input_feature_9 = closest_distances_top5[2] if len(closest_distances_top5) > 2 else 0
input_feature_10 = closest_distances_top5[3] if len(closest_distances_top5) > 3 else 0
input_feature_11 = closest_distances_top5[4] if len(closest_distances_top5) > 4 else 0
input_feature_12 = furthest_distances_top5[-1] if furthest_distances_top5 > 0 else 0
input_feature_13 = furthest_distances_top5[-2] if len(furthest_distances_top5) > 1 else 0
input_feature_14 = furthest_distances_top5[-3] if len(furthest_distances_top5) > 2 else 0
input_feature_15 = furthest_distances_top5[-4] if len(furthest_distances_top5) > 3 else 0
input_feature_16 = furthest_distances_top5[-5] if len(furthest_distances_top5) > 4 else 0


# 入力されたテキストを改行で分割し、緯度経度のペアのリストを作成
TG_locations = [tuple(map(float, loc.split(','))) for loc in TG_Iloc.strip().split('\n')]

# 緯度経度のペアの数をカウント
num_tg_locations = len(TG_locations)
# カウントした緯度経度のペアの数をinput_feature_1に格納
input_feature_1 = num_tg_locations

# 緯度経度の入力と地図の表示を行う関数
def display_map():

    # 地図を作成（最初の計測地点を中心に設定）
    if measurment_location1 or TG_locations:
        m = folium.Map(location=measurment_location1[0] if measurment_location1 else TG_locations[0], tiles="cartodbdark_matter", zoom_start=5)

        # 計測地点のマーカーと半径を追加
        for loc in measurment_location1:
            folium.Marker(location=loc, icon=folium.Icon(color='blue')).add_to(m)
            folium.Circle(location=loc, radius=T_radius, color='blue', fill=True, fill_opacity=0.7).add_to(m)

        # TG地点のマーカーと半径を追加
        for loc in TG_locations:
            folium.Marker(location=loc, icon=folium.Icon(color='red')).add_to(m)
            folium.Circle(location=loc, radius=T_radius, color='red', fill=True, fill_opacity=0.7).add_to(m)

        # Streamlitで地図を表示
        st_folium(m, width=700, height=400)
    else:
        st.error("有効な緯度経度を入力してください。")

# 関数を実行
display_map()

input_feature_2 = streaming_days
input_feature_3 = mesureing_days
input_feature_4 = potential

# 結果を変数に格納
input_feature_5 = average_distance
input_feature_6 = median_distance
input_feature_7 = closest_distances_top5[0]
input_feature_8 = closest_distances_top5[1]
input_feature_9 = closest_distances_top5[2]
input_feature_10 = closest_distances_top5[3]
input_feature_11 = closest_distances_top5[4]
input_feature_12 = furthest_distances_top5[-1]
input_feature_13 = furthest_distances_top5[-2]
input_feature_14 = furthest_distances_top5[-3]
input_feature_15 = furthest_distances_top5[-4]
input_feature_16 = furthest_distances_top5[-5]

# 入力値をデータフレームに変換
input_df = pd.DataFrame([[input_feature_1,
                          input_feature_2,
                          input_feature_3, 
                          input_feature_4,
                          input_feature_5, 
                          input_feature_6,
                          input_feature_7, 
                          input_feature_8,
                          input_feature_9, 
                          input_feature_10,
                          input_feature_11, 
                          input_feature_12,
                          input_feature_13, 
                          input_feature_14,
                          input_feature_15, 
                          input_feature_16]], 
                 columns=['TG地点数', 
                          '配信日数',
                          '計測日数', 
                          '対象人数',
                          '平均(km)',
                          '中央値（km）', 
                          '1番近いTG距離',
                          '2番近いTG距離',
                          '3番近いTG距離', 
                          '4番近いTG距離',
                          '5番近いTG距離',
                          '1番遠いTG距離', 
                          '2番遠いTG距離',
                          '3番遠いTG距離',
                          '4番遠いTG距離', 
                          '5番遠いTG距離'])

# 予測ボタンを表示するかどうかの条件を設定
# 全ての必要な入力がされているかどうかをチェック
is_input_complete = potential > 0 and streaming_days > 0 and mesureing_days > 0 and T_radius and mesurement_visit and TG_Iloc

import os

# スクリプトの絶対パスを取得
script_path = os.path.abspath(__file__)

# スクリプトがあるディレクトリを取得
script_dir = os.path.dirname(script_path)

# ターゲットファイルへの相対パス
relative_path = 'gb_model.joblib'

# ターゲットファイルの絶対パスを生成
file_path = os.path.join(script_dir, relative_path)

# file_pathを使用してファイルを読み込む
gb_model = load(file_path)

# 予測ボタン（条件に応じて無効化）
if is_input_complete and st.button('予測'):
    # '1番近いTG距離'が90km以上の場合は来店率を0.00001にする
    if  input_feature_7 >= 90:
        predicted_percentage = 0.00001 * 100  # 0.00001をパーセント表示に変換
        st.metric(label="予想来店率", value=f"{predicted_percentage:.5f}%")
        st.info("※指定された距離に基づき、来店率は0.001%と予測されます。")
    else:
        # モデルを使用して予測を行う
        prediction = gb_model.predict(input_df)
        # 予測結果をパーセント表示に変換
        predicted_percentage = prediction[0] * 100
        st.metric(label="予想来店率", value=f"{predicted_percentage:.2f}%")
        st.info("※上記数値は想定値となり、実際の来店率と異なる場合がございます。")
        st.info("※TGがエリア指定の場合や滞在時間の条件指定がある場合は数値の変動が大きくなります。")
else:
    # 入力が完了していない場合はメッセージを表示
    st.warning("全ての入力項目を完了してください。")
