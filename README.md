Vehicle Price and Listing Duration Dashboard

# Project Overview
This project is a web application dashboard built with Streamlit to visualize vehicle price and the listing duration data. It allows users to explore summarized statistics of vehicle the prices and listing durations. They are grouped by vehicle condition (e.g., excellent, fair, good, like new, new, salvage). The dashboard includes an interactive scatter plot showing the mean (or median) price versus the mean (or median) days listed for all conditions in the DataSet. The dot (point) sizes are reflecting the standard deviation of price in each condition. Users can toggle between mean and median values using a checkbox, providing a more robust view of the data in the presence of outliers.

The project is designed as a tool to simulate and analyze how vehicle condition impacts price and selling speed. It provides insights into the average price, variability, and listing duration for vehicles in different conditions.

## Methods and Libraries
The project uses the following methods and libraries to implement the dashboard:

- **Data Processing**:
  - `pandas`: Used to load, manipulate, and summarize the vehicle dataset into a DataFrame. The dataset (`vehicles_us.csv`) contains raw vehicle data, which is grouped by condition to calculate mean, median, and standard deviation for price and days listed.
  
- **Visualization**:
  - `plotly.express`: Used to create an interactive scatter plot visualizing the summarized statistics. The scatter plot displays mean/median price vs. mean/median days listed, with colors representing conditions and point sizes indicating price variability.

- **Web Application**:
  - `streamlit`: Used to build the web application dashboard. Streamlit provides an easy way to create interactive web apps with Python, including components like headers, checkboxes, and Plotly chart displays.

## Project Structure
The project consists of the following files:
- `app.py`: The main Streamlit application file that creates the dashboard, including the scatter plot/interactive checkbox.
- `vehicles_us.csv`: The raw dataset containing vehicle data.
- `README.md`: Provides an overview and instructions for this project.

## Setup and Installation
To run this project on your local machine, follow these steps:

### Prerequisites
- Python 3.7 or higher installed on your machine.
- A code editor (e.g., VS Code, PyCharm) to edit the project files.
- Git installed (optional, if you want to clone the repository).

### Installation Steps
1. **Clone the Repository** (if you’re accessing it from GitHub):
   ```bash
   git clone <https://github.com/CoastalBotany/my_python_project.git>
   cd <https://github.com/CoastalBotany/my_python_project.git> # my_python_project
