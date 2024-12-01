# **NCIF Data Integration API**

## **Overview**
The NCIF Data Integration API is a backend service designed to aggregate, process, and analyze data from multiple sources. It supports dynamic querying, machine learning predictions, and natural language processing (NLP)-based filtering.

This project aims to facilitate data-driven decision-making for stakeholders by providing easy access to actionable insights derived from integrated datasets.

---

## **Features**
1. **Dynamic Querying**:
   - Retrieve branch density by Census Tract with optional filters for PM2.5 levels and branch count.

2. **Machine Learning Prediction**:
   - Predict PM2.5 levels based on branch density using a simple machine learning model.

3. **NLP-Based Querying**:
   - Parse natural language queries and dynamically retrieve results based on specified conditions.

4. **Database Integration**:
   - Combines datasets from EPA Air Quality, FFIEC SOD, and NCUA Credit Union Data.

---

## **Setup Instructions**
### **Prerequisites**
- Python 3.8 or later
- SQLite
- Dependencies listed in `requirements.txt`:
  ```bash
  fastapi
  uvicorn
  pandas
  sqlite3
  ```

### **Installation**
1. Clone the repository or download the source code.
2. Navigate to the project directory and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create the SQLite database:
   - Load the integrated data (`merged_data`) into an SQLite database (`merged_data.db`).

### **Run the Server**
Start the FastAPI server using Uvicorn:
```bash
uvicorn ncif_api:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## **API Endpoints**

### **1. Root Endpoint**
- **URL**: `/`
- **Method**: `GET`
- **Description**: Welcome message.
- **Example Response**:
  ```json
  {
    "message": "Welcome to NCIF Data Integration API"
  }
  ```

### **2. Retrieve Branch Density**
- **URL**: `/density`
- **Method**: `GET`
- **Query Parameters**:
  - `census_tract`: Optional list of Census Tracts.
  - `pm25_threshold`: Optional PM2.5 threshold (float).
  - `branch_threshold`: Optional branch count threshold (integer).
- **Description**: Retrieve branch density by Census Tract with optional filters.
- **Example**:
  ```bash
  curl "http://127.0.0.1:8000/density?pm25_threshold=10&branch_threshold=5"
  ```

### **3. Predict PM2.5 Levels**
- **URL**: `/predict`
- **Method**: `POST`
- **Body**: JSON with `branch_count` (integer).
- **Description**: Predict PM2.5 levels using branch density.
- **Example**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"branch_count": 10}'
  ```

### **4. NLP Querying**
- **URL**: `/query-nlp`
- **Method**: `POST`
- **Body**: JSON with `nlp_query` (string).
- **Description**: Parse a natural language query and retrieve results.
- **Example**:
  ```bash
  curl -X POST "http://127.0.0.1:8000/query-nlp" -H "Content-Type: application/json" -d '{"nlp_query": "Show tracts with PM2.5 > 15 and more than 10 branches."}'
  ```

---

## **Data Pipeline**
1. **Data Integration**:
   - Datasets from EPA, FFIEC, and NCUA were integrated using Census Tract as the master key.

2. **Preprocessing**:
   - Cleaned and standardized data for querying.

3. **Database**:
   - Integrated data stored in an SQLite database (`merged_data.db`).

---

## **Assumptions**
1. **Data**:
   - All datasets are correctly preprocessed and integrated into the SQLite database.
2. **NLP Parsing**:
   - Basic parsing for predefined query formats. Can be extended with advanced NLP tools.

---

## **Future Enhancements**
1. Incorporate advanced machine learning models for better PM2.5 predictions.
2. Extend NLP functionality for more flexible and varied query formats.
3. Add user authentication and role-based access controls.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

## **Contact**
For issues or contributions, please contact the project maintainer.

---

This README file provides a comprehensive guide for setup, usage, and understanding of the API. Let me know if you need any changes!