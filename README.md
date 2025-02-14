# Demand Forecasting with N-BEATS - Streamlit App
This project is a Streamlit app for demand forecasting using the N-BEATS model from the darts library. The app allows users to upload a CSV file containing time-series data (e.g., sales data), select relevant columns for analysis, and apply the N-BEATS model to forecast future demand. The app also provides visualizations and evaluation metrics to assess the model's performance.

## Features:
File Upload: Users can upload a CSV file containing time-series data.

Dynamic Column Selection: Users can select the columns for Product ID, Sales, and Date from the uploaded CSV file.

Date Range Filtering: Users can specify a start and end date to filter the data for analysis.

Data Resampling: The app resamples the data to fill missing dates and prepare it for training.

Model Configuration: Users can configure the N-BEATS model by specifying:

Input chunk length
Output chunk length
Number of epochs for training

Forecasting: The app predicts future demand for a user-defined forecast period.

Visualizations: Users can view visualizations of the training, test, and forecast data.

Model Evaluation: The app evaluates the model's performance using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

## Prerequisites:

To run this app, you'll need to install the following Python libraries:

pandas

numpy

matplotlib

streamlit

darts

scikit-learn

You can install these libraries using the following command:


## pip install pandas numpy matplotlib streamlit darts scikit-learn
# How to Run:

Clone or download the project repository to your local machine.

Install the required dependencies (as mentioned above).

In the terminal, navigate to the directory where the script is saved.

Run the Streamlit app with the following command:


## streamlit run app.py

Open the web interface in your browser as indicated by the terminal (usually at http://localhost:0000).

# How to Use the App:

Upload a CSV file: Choose a CSV file that contains time-series data for demand forecasting. The file should have at least three columns: Product ID, Sales, and Date.

Select Columns: From the dropdown menus, select the appropriate columns for Product ID, Sales, and Date.

Set Date Range: Define the start and end date to filter the dataset.

Train the Model:

Set the input chunk length (e.g., 30).
Set the output chunk length (e.g., 30).
Specify the number of epochs (e.g., 100).

Make Predictions: Define the forecast period (how many future periods you want to predict).

View Results: The app will display visualizations of the training data, test data, and forecast. It will also show the evaluation metrics, including MAE and RMSE.

# Evaluation Metrics:
Mean Absolute Error (MAE): Measures the average absolute difference between predicted and actual values.

Root Mean Squared Error (RMSE): Measures the square root of the average squared differences between predicted and actual values.

# Notes:
The app expects the data to have at least 60 data points for training the model. If the dataset is too small, an error message will be displayed.

The date column in the CSV file must be in a valid datetime format (e.g., "YYYY-MM-DD"). The app will automatically handle any invalid dates.

Missing data will be filled with zeroes, but users can adjust the imputation method if needed.

Example Data:

The CSV file should have a structure like this:


Date	Product_ID	Sales
2025-01-01	A	100
2025-01-02	A	120
2025-01-03	A	110
...	...	...

# Troubleshooting:
Error during file upload: Ensure that the CSV file is properly formatted, with a valid date column and numerical sales data.

Invalid date format: If there are invalid dates in the date column, the app will display a warning message.

# Contributions:

Feel free to fork and modify the app to suit your needs. Contributions are welcome!


# outputs

![image](https://github.com/user-attachments/assets/a631c1ec-972e-430e-9dd8-47fe5ddbf5c5)
![image](https://github.com/user-attachments/assets/3e6263a0-4265-40f4-8e7e-fe51dca804f5)
![image](https://github.com/user-attachments/assets/6ef347f0-136c-46dc-b660-837243440e0d)
![image](https://github.com/user-attachments/assets/8d0606eb-fbaa-4539-89b6-dd151337ca45)
![image](https://github.com/user-attachments/assets/14e2fdd2-302c-46e5-ae60-1d8de6c9b15d)




