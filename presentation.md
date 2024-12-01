# **Case Study: NCIF Data Integration Platform**

---

## **Slide 1: Project Overview**
### **Background**
- **Objective**: Build an AI-powered platform for integrating and analyzing multi-source data.
- **Target Users**:
  - Investors, financial institutions, and community organizations.

### **Features**
1. **Data Integration**:
   - Structured and unstructured datasets.
   - Census Tract as the geospatial key.
2. **Advanced Querying**:
   - Dynamic and NLP-based filtering.
3. **Data-Driven Insights**:
   - Visualizations and correlations using branch and air quality data.

---

## **Slide 2: Architecture & API**
### **Platform Architecture**
1. **Database**:
   - SQLite for local development.
2. **API Backend**:
   - FastAPI for dynamic queries and predictions.
3. **Compute**:
   - Python-based machine learning models.

### **API Endpoints**
1. `/density`: Branch density by Census Tract.
2. `/predict`: Predict PM2.5 based on branch density.
3. `/query-nlp`: Parse natural language queries dynamically.

---

## **Slide 3: Insights & Visualizations**
### **Key Findings**
1. **Branch Density**:
   - Most Census Tracts have fewer than 10 branches.
2. **Filtered Results**:
   - High PM2.5 (>10) and >5 branches in select Census Tracts.
3. **Correlation**:
   - Weak positive correlation between branch density and PM2.5 levels.

### **Visualizations**
- Histogram: Branch density distribution.
- Bar Chart: Filtered Census Tracts.
- Scatter Plot: PM2.5 vs. Branch density.

---

## **Slide 4: How to Run**
### **Steps**
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

### **Documentation**
- API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## **Slide 5: Future Enhancements**
1. **Scalability**:
   - Transition to cloud-hosted databases for larger datasets.
2. **Enhanced Analytics**:
   - Introduce advanced machine learning models.
3. **User Management**:
   - Add role-based access for secure data handling.
4. **Improved NLP**:
   - Broaden the natural language query capabilities.