import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Dashboard: Weekly Sales over 3 Years")

# Upload CSV và đọc dữ liệu
uploaded = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    df['Year'] = ((df['Week'] - 1) // 52) + 1
    df['MovingAvg_4weeks'] = df['Sales'].rolling(window=4).mean()

    st.write("### Preview Data", df.head())

    st.write("### Descriptive Statistics")
    st.write(df.describe())

    # Setup plots
    sns.set(style="whitegrid")

    # Plot từng biểu đồ
    fig1, ax1 = plt.subplots()
    sns.lineplot(data=df, x='Week', y='Sales', marker='o', ax=ax1)
    ax1.set_title("Sales Trend Over 3 Years")

    fig2, ax2 = plt.subplots()
    sns.histplot(df['Sales'], bins=20, kde=True, ax=ax2, color='green')
    ax2.set_title("Sales Distribution")

    fig3, ax3 = plt.subplots()
    sns.boxplot(x='Year', y='Sales', data=df, palette='pastel', ax=ax3)
    ax3.set_title("Yearly Sales Distribution")

    fig4, ax4 = plt.subplots()
    ax4.plot(df['Week'], df['Sales'], alpha=0.5, label='Weekly Sales')
    ax4.plot(df['Week'], df['MovingAvg_4weeks'], color='red', label='4‑week Moving Avg')
    ax4.set_title("Sales vs 4‑week Moving Avg")
    ax4.legend()

    yearly = df.groupby('Year')['Sales'].sum().reset_index()
    fig5, ax5 = plt.subplots()
    sns.barplot(data=yearly, x='Year', y='Sales', palette='Blues_d', ax=ax5)
    ax5.set_title("Total Sales per Year")

    # Show plots
    st.pyplot(fig1)
    st.pyplot(fig2)
    st.pyplot(fig3)
    st.pyplot(fig4)
    st.pyplot(fig5)
else:
    st.info("Please upload your sales_data_3_years.csv")
