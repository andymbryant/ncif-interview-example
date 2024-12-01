# **NCIF Data Integration API and Visualization**

## **Overview**
The NCIF Data Integration API is a backend service designed to integrate, process, and analyze data from multiple sources. It provides endpoints for querying branch density, predicting PM2.5 levels, and handling NLP-based queries. Additionally, a separate visualization script generates business insights and visualizations using the API data.

---

## **Features**
1. **API Features**:
   - Dynamic querying of branch density and PM2.5 levels.
   - Machine learning-based predictions for PM2.5 levels.
   - NLP query support for flexible data retrieval.

2. **Visualization Features**:
   - Distribution of branch density across Census Tracts.
   - Filtered data analysis for specific PM2.5 and branch count thresholds.
   - Correlation analysis and scatter plots of branch density vs. PM2.5 levels.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or later
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### **2. Database Setup**
- Ensure the `20241125 Case Study for Position SE_Data.xlsx` file is located in the `data/` directory.
- Populate the SQLite database by running:
  ```bash
  python process_csv.py
  ```

### **3. Start the API**
- Run the FastAPI server using Uvicorn:
  ```bash
  uvicorn app.api:app --reload
  ```
- The API will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).
- View interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### **4. Generate Visualizations**
- Run the visualization script:
  ```bash
  python visualization.py
  ```

---

## **Usage**

### **API Endpoints**
1. **Root Endpoint**:
   - **URL**: `/`
   - **Method**: `GET`
   - **Description**: Welcome message.

2. **Retrieve Branch Density**:
   - **URL**: `/density`
   - **Method**: `GET`
   - **Query Parameters**:
     - `census_tract`: Optional list of Census Tracts.
     - `pm25_threshold`: Optional PM2.5 threshold (float).
     - `branch_threshold`: Optional branch count threshold (integer).
   - **Description**: Retrieve branch density by Census Tract with optional filters.

3. **Predict PM2.5 Levels**:
   - **URL**: `/predict`
   - **Method**: `POST`
   - **Body**: JSON with `branch_count` (integer).
   - **Description**: Predict PM2.5 levels using branch density.

4. **NLP Querying**:
   - **URL**: `/query-nlp`
   - **Method**: `POST`
   - **Body**: JSON with `nlp_query` (string).
   - **Description**: Parse a natural language query and retrieve results.

### **Visualizations**
1. **Run Visualization Script**:
   - The script fetches data from the API and generates:
     - Histogram: Distribution of branch density.
     - Bar chart: Filtered Census Tracts with high PM2.5 and branch count.
     - Scatter plot: Correlation analysis of branch density and PM2.5.

---

## **Project Structure**
```
NCIF-Data-Integration/
│
├── app/
│   ├── api.py               # FastAPI application
│   ├── database.py          # SQLite database utilities
│   └── process_csv.py       # Script to process Excel file and populate database
│
├── data/
│   ├── 20241125 Case Study for Position SE_Data.xlsx  # Input Excel file
│   └── merged_data.db       # SQLite database
│
├── visualization.py         # Script for generating visualizations
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
```

---

## **Example Workflow**
1. Populate the database:
   ```bash
   python app/process_csv.py
   ```
2. Start the API:
   ```bash
   uvicorn app.api:app --reload
   ```
3. Generate visualizations:
   ```bash
   python visualization.py
   ```

---

## **Future Enhancements**
- Add user authentication and role-based access controls.
- Enhance NLP query capabilities for more flexible formats.
- Implement more sophisticated ML models for PM2.5 predictions.