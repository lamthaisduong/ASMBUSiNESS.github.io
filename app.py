import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Weekly Sales Dashboard (3-Year Analysis)")

# Đọc dữ liệu từ file nội bộ (CSV đặt cùng thư mục app.py)
df = pd.read_csv("sales_data_3_years.csv")
df['Year'] = ((df['Week'] - 1) // 52) + 1
df['MovingAvg_4weeks'] = df['Sales'].rolling(window=4).mean()

# Hiển thị bảng dữ liệu
st.subheader("📋 Data Preview")
st.dataframe(df.head(10))

# Mô tả thống kê
st.subheader("📈 Descriptive Statistics")
st.write(df.describe())

# Thiết lập biểu đồ
sns.set(style="whitegrid")

# Biểu đồ 1
st.subheader("1. Sales Trend Over 3 Years")
fig1, ax1 = plt.subplots()
sns.lineplot(data=df, x='Week', y='Sales', marker='o', ax=ax1)
st.pyplot(fig1)
st.caption("This line chart shows weekly sales trend over 3 years, reflecting business growth.")

# Biểu đồ 2
st.subheader("2. Sales Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(df['Sales'], bins=20, kde=True, color='green', ax=ax2)
st.pyplot(fig2)
st.caption("Histogram displaying distribution and frequency of sales.")

# Biểu đồ 3
st.subheader("3. Yearly Sales Distribution (Boxplot)")
fig3, ax3 = plt.subplots()
sns.boxplot(x='Year', y='Sales', data=df, palette='pastel', ax=ax3)
st.pyplot(fig3)
st.caption("Boxplot compares weekly sales across years and shows outliers.")

# Biểu đồ 4
st.subheader("4. Weekly Sales vs 4-week Moving Average")
fig4, ax4 = plt.subplots()
ax4.plot(df['Week'], df['Sales'], label='Weekly Sales', alpha=0.5)
ax4.plot(df['Week'], df['MovingAvg_4weeks'], label='4-week MA', color='red')
ax4.legend()
st.pyplot(fig4)
st.caption("Red line shows smoothed trend via 4-week moving average.")

# Biểu đồ 5
st.subheader("5. Total Sales per Year")
fig5, ax5 = plt.subplots()
yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()
sns.barplot(x='Year', y='Sales', data=yearly_sales, palette='Blues_d', ax=ax5)
st.pyplot(fig5)
st.caption("Bar chart shows increasing total sales per year.")
