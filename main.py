from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from app.database_utils import create_tables, query_data, is_initialized

# Initialize FastAPI app
app = FastAPI()

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    if not is_initialized():
        create_tables()

# Endpoint Models
class PredictionRequest(BaseModel):
    branch_count: int

class NLPQueryRequest(BaseModel):
    nlp_query: str

# Root Endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the NCIF Data Integration API"}

# Endpoint: Retrieve Branch Density
@app.get("/density")
def get_branch_density(
    census_tract: Optional[List[str]] = Query(None),
    pm25_threshold: Optional[float] = Query(None),
    branch_threshold: Optional[int] = Query(None),
):
    """
    Retrieve branch density by Census Tract with optional filters for PM2.5 levels
    and branch count.
    """
    query = "SELECT * FROM density_table"
    filters = []
    params = []

    # Dynamic filters
    if census_tract:
        filters.append(f"census_tract IN ({','.join(['?'] * len(census_tract))})")
        params.extend(census_tract)
    if pm25_threshold is not None:
        filters.append("PM25 >= ?")
        params.append(pm25_threshold)
    if branch_threshold is not None:
        filters.append("branch_count >= ?")
        params.append(branch_threshold)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    # Query database
    results = query_data(query, params)
    return results.to_dict(orient="records")

# Endpoint: Predict PM2.5 Levels
@app.post("/predict")
def predict_pm25(request: PredictionRequest):
    """
    Predict PM2.5 levels based on branch density using a mock ML model.
    """
    def mock_model(branch_count):
        return 10 + 0.5 * branch_count  # Simple linear regression example

    prediction = mock_model(request.branch_count)
    return {"branch_count": request.branch_count, "predicted_PM2.5": prediction}

# Endpoint: NLP Query
@app.post("/query-nlp")
def query_nlp(request: NLPQueryRequest):
    """
    Parse NLP query to filter Census Tracts dynamically.
    Example query: "Show tracts with PM2.5 > 15 and more than 10 branches."
    """
    nlp_query = request.nlp_query.lower()
    if "pm2.5 >" in nlp_query and "more than" in nlp_query:
        try:
            pm25_threshold = float(nlp_query.split("pm2.5 >")[1].split()[0])
            branch_threshold = int(nlp_query.split("more than")[1].split()[0])
            return get_branch_density(pm25_threshold=pm25_threshold, branch_threshold=branch_threshold)
        except Exception as e:
            return {"error": f"Failed to parse query: {e}"}
    else:
        return {"error": "Unsupported query format"}
