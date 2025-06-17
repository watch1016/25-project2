# Creating the Streamlit app file
app_code = """
import streamlit as st
import pandas as pd
import pydeck as pdk
import koreanize_matplotlib  # 한글 폰트를 위한 설정 (스트림릿 클라우드 requirements.txt에 포함 필요)

# ---- 데이터 불러오기 ------------------------------------------------------
@st.cache_data
def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # 필요한 컬럼만 남기고 결측치 처리
    df = df[['store_name', 'address', 'latitude', 'longitude']].copy()
    df[['latitude', 'longitude']] = df[['latitude', 'longitude']].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=['latitude', 'longitude'])
    return df

# ---- 앱 본문 -------------------------------------------------------------
st.set_page_config(page_title='Seoul Food Permits Map', layout='wide')
st.title('서울시 휴게음식점 인허가 현황 지도')

csv_file = 'seoul_food_permits_open_only.csv'
df = load_data(csv_file)

# 검색 기능
keyword = st.text_input('가게 이름 또는 주소 키워드로 검색', '')
if keyword:
    df = df[df['store_name'].str.contains(keyword, case=False, na=False) |
            df['address'].str.contains(keyword, case=False, na=False)]

st.write(f'표시 중인 업소 수: {len(df):,}곳')

# ---- 지도 시각화 ---------------------------------------------------------
st.map(df[['latitude', 'longitude']], zoom=11)

# ---- 세부 데이터 보기 -----------------------------------------------------
with st.expander('데이터 표 보기'):
    st.dataframe(df)
"""

app_path = "/mnt/data/streamlit_food_map.py"
with open(app_path, "w", encoding="utf-8") as f:
    f.write(app_code)

# Also create a minimal requirements.txt
req_code = """
streamlit
pandas
pydeck
koreanize_matplotlib
"""

req_path = "/mnt/data/requirements.txt"
with open(req_path, "w", encoding="utf-8") as f:
    f.write(req_code)

app_path, req_path
