import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("hostel_life_expense_tracker.csv")
df = df.dropna()

# Title
st.title("Personal Expense Analytics Dashboard")

# Data preview
st.subheader("Dataset Preview")
st.write(df.head())

# Total expense
st.subheader("Total Expense")
st.write(df["Amount"].sum())

# Category-wise expense
st.subheader("Expense by Category")
category_data = df.groupby("Expense_Type")["Amount"].sum()
st.bar_chart(category_data)

# Pie chart
st.subheader("Expense Distribution")

fig, ax = plt.subplots()
ax.pie(category_data, labels=category_data.index, autopct="%1.1f%%")
st.pyplot(fig)

# Monthly trend (if Date exists)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    monthly = df.groupby("Month")["Amount"].sum()

    st.subheader("Monthly Expense Trend")
    st.line_chart(monthly)