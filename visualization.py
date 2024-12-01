import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# API Base URL
BASE_URL = "http://127.0.0.1:8000"

def fetch_data(endpoint, params=None):
    """
    Fetch data from the API.
    :param endpoint: API endpoint (e.g., '/density').
    :param params: Query parameters (optional).
    :return: DataFrame with the API response.
    """
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)
    response.raise_for_status()  # Raise an error if the request fails
    return pd.DataFrame(response.json())

def visualize_branch_density(data):
    """
    Visualize the distribution of branch density by Census Tract.
    :param data: DataFrame containing branch density data.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data['branch_count'], bins=20, edgecolor='k')
    plt.title('Branch Density Distribution by Census Tract')
    plt.xlabel('Branch Count')
    plt.ylabel('Number of Census Tracts')
    plt.grid(axis='y')
    plt.show()

def visualize_filtered_data(filtered_data):
    """
    Visualize branch counts for filtered Census Tracts.
    :param filtered_data: DataFrame with filtered data.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=filtered_data, x="census_tract", y="branch_count", palette="viridis")
    plt.title('Branch Counts in Census Tracts with PM2.5 > 10 and Branch Count > 5')
    plt.xlabel('Census Tract')
    plt.ylabel('Branch Count')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def correlation_analysis(data):
    """
    Perform correlation analysis and visualize PM2.5 vs. Branch Count.
    :param data: DataFrame containing branch density and PM2.5 levels.
    """
    correlation = data['branch_count'].corr(data['PM2.5'])
    print(f"Correlation between Branch Density and PM2.5 Levels: {correlation:.2f}")

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="branch_count", y="PM2.5", alpha=0.7)
    plt.title(f'Correlation between Branch Density and PM2.5 Levels (Corr: {correlation:.2f})')
    plt.xlabel('Branch Count')
    plt.ylabel('PM2.5 Levels')
    plt.grid(True)
    plt.show()

def main():
    # Fetch all data
    print("Fetching all density data...")
    data = fetch_data("/density")
    if data.empty:
        print("No data retrieved from the API.")
        return

    # Visualize branch density distribution
    print("Visualizing branch density distribution...")
    visualize_branch_density(data)

    # Fetch filtered data for PM2.5 > 10 and Branch Count > 5
    print("Fetching filtered data...")
    filtered_data = fetch_data("/density", params={"pm25_threshold": 10, "branch_threshold": 5})
    if not filtered_data.empty:
        print("Visualizing filtered data...")
        visualize_filtered_data(filtered_data)
    else:
        print("No Census Tracts meet the filtering criteria.")

    # Perform correlation analysis
    print("Performing correlation analysis...")
    correlation_analysis(data)

if __name__ == "__main__":
    main()
