import pandas as pd
import streamlit as st
import yfinance as yf
import datetime as dt


col1,col2 = st.columns(2)
with col1:
    st.image('image.jfif',width=200)
with col2:
    st.write(
        """
        # Stock Price Analyzer

        """
    )

ticker_symbol = st.text_input(
                    """ Enter Stock Symbol""",
                    'AAPL',
                    key='placeholder'
)
# ticker_symbol = 'AAPL'

col1,col2 = st.columns(2)

#Capturing Date Input
with col1:
    start_date = st.date_input("Start Date",dt.date(2019,1,1))
with col2:
    end_date = st.date_input("End Date",dt.date(2022,12,31))
   
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1D",start=f'{start_date}',end=f'{end_date}')

st.write(
    f"""
     # {ticker_symbol.upper()}'s EOD Prices
    """
)

st.dataframe(ticker_df)

##Display line chart as shown on google
st.write("""
    # Daily Closing Price Chart
""")
st.line_chart(ticker_df['Close'])

#Volume Traded
st.write("""
    # Daily Volume of Shares Traded
""")
st.line_chart(ticker_df['Volume'])
