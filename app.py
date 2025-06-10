import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(page_title="GS25 점포 지도", layout="wide")

st.title("📍 GS25 점포 지도 (서울 포함 전국)")
st.markdown("서울 및 전국 GS25 점포 위치를 지도에 표시합니다.")

# 엑셀 파일 불러오기
@st.cache_data
def load_data():
    url = 'GS25 점포정보_Sample.xlsx'
    df = pd.read_excel(url)
    # 서울 지역 필터링 (옵션)
    df_seoul = df[df['주소'].str.contains("서울")]
    return df_seoul

data = load_data()

# 서울 중심 지도 생성
map_center = [37.5665, 126.9780]
m = folium.Map(location=map_center, zoom_start=11)

# 지도에 마커 추가
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['y좌표'], row['x좌표']],
        popup=f"{row['매장명']}<br>{row['주소']}",
        icon=folium.Icon(color='blue', icon='shopping-cart', prefix='fa')
    ).add_to(m)

# 지도 출력
st_folium(m, width=900, height=600)
