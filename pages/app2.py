import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 제목
st.title("CU 점포 지도")

# CSV 데이터 불러오기
df = pd.read_csv("seoul_food_permits_open_only.csv")

# 위도/경도 결측치 제거
df = df.dropna(subset=["latitude", "longitude"])

# 지도 생성 (서울 중심 좌표)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 지도에 마커 추가
for _, row in df.iterrows():
    popup_info = f"{row['store_name']}<br>{row['address']}"
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=popup_info,
        icon=folium.Icon(color="blue", icon="cutlery", prefix='fa')
    ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)
