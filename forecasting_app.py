import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from darts import TimeSeries
from darts.models import NBEATSModel
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Streamlit App
st.title("Demand Forecasting with N-BEATS")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        # Load the data
        data = pd.read_csv(uploaded_file)
        
        # Check if the file is loaded correctly
        st.write("Data Loaded Successfully!")
        st.write(data.head())

        # Dropdown for selecting columns dynamically
        product_col = st.selectbox("Select the Product ID column", data.columns)
        sales_col = st.selectbox("Select the Sales column", data.columns)
        date_col = st.selectbox("Select the Date column", data.columns)

        # Ensure the selected 'date' column is in datetime format
        if date_col:
            data[date_col] = pd.to_datetime(data[date_col], errors='coerce')
            # Check for invalid dates after conversion
            invalid_dates = data[data[date_col].isna()]
            if not invalid_dates.empty:
                st.warning(f"Warning: Some rows have invalid dates in the {date_col} column.")
            else:
                st.write(f"Valid {date_col} column.")

        # Ensure the selected columns are valid before proceeding
        if product_col and sales_col and date_col:
            # Input fields for date range
            start_date = st.date_input("Start date", min_value=data[date_col].min(), max_value=data[date_col].max())
            end_date = st.date_input("End date", min_value=data[date_col].min(), max_value=data[date_col].max())

            # Convert the selected start_date and end_date to pandas datetime
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

            # Filter the data based on the selected date range
            data_filtered = data[(data[date_col] >= start_date) & (data[date_col] <= end_date)]

            # Set the 'date' column as the index
            data_filtered.set_index(date_col, inplace=True)

            # Resample the data to fill missing dates (e.g., 'D' for daily, 'H' for hourly, etc.)
            # Using the daily frequency 'D' here as an example
            data_resampled = data_filtered.resample('D').sum()  # Resample to daily frequency
            data_resampled = data_resampled.fillna(0)  # Fill missing values with 0 (or other imputation)

            # Convert the data into a Darts TimeSeries object
            series = TimeSeries.from_dataframe(data_resampled, value_cols=sales_col)

            # Check if the series has at least 60 data points
            if len(series) < 60:
                st.error("The dataset is too small for the model to train. Please provide at least 60 data points.")
            else:
                # Split data into training and test sets (80-20 split)
                train, test = series.split_before(0.8)

                # Visualize the training and test data
                st.write("Train-Test Split Visualization:")
                fig, ax = plt.subplots()
                train.plot(label="Training Data", ax=ax)
                test.plot(label="Test Data", ax=ax)
                plt.title("Train-Test Split for Demand Forecasting")
                plt.legend()
                st.pyplot(fig)

                # Dynamic input from the user for model parameters
                input_chunk_length = st.number_input("Enter the input_chunk_length (e.g., 30)", min_value=1, value=30)
                output_chunk_length = st.number_input("Enter the output_chunk_length (e.g., 30)", min_value=1, value=30)
                n_epochs = st.number_input("Enter the number of epochs (e.g., 100)", min_value=1, value=100)

                # Input for the forecast period (in terms of number of future periods to predict)
                forecast_periods = st.number_input("Enter the number of future periods to forecast", min_value=1, value=30)

                # Train N-BEATS Model with user inputs
                model = NBEATSModel(input_chunk_length=input_chunk_length, output_chunk_length=output_chunk_length, n_epochs=n_epochs)
                model.fit(train)

                # Make predictions for the user-defined forecast period
                forecast = model.predict(forecast_periods)

                # Visualize the results
                st.write("Forecasting Results:")
                fig, ax = plt.subplots()
                train.plot(label="Training Data", ax=ax)
                test.plot(label="Test Data", ax=ax)
                forecast.plot(label="Forecast", ax=ax)
                plt.title(f"Demand Forecasting with N-BEATS (input_chunk_length={input_chunk_length}, output_chunk_length={output_chunk_length}, n_epochs={n_epochs})")
                plt.legend()
                st.pyplot(fig)

                # Evaluate the model
                mae = mean_absolute_error(test.values(), forecast.values())
                rmse = np.sqrt(mean_squared_error(test.values(), forecast.values()))

                st.write(f"Mean Absolute Error (MAE): {mae}")
                st.write(f"Root Mean Squared Error (RMSE): {rmse}")

    except Exception as e:
        # Catch and display any error during file loading or processing
        st.error(f"An error occurred while processing the CSV file: {e}")

else:
    st.warning("Please upload a CSV file to proceed.")
