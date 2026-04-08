# Automated Weather Data Pipeline 🌦️

A modern data engineering pipeline that extracts weather data from an API, orchestrates the workflow with Airflow, and transforms the data using dbt and PostgreSQL.

## 🚀 Project Architecture
The pipeline follows a standard Medallion architecture:
1.  **Extract & Load:** A Python script fetches real-time weather data and loads it into a `raw` PostgreSQL table.
2.  **Orchestration:** Apache Airflow manages the task dependencies and scheduling.
3.  **Transformation (dbt):**
    * **Staging:** Deduplicates raw data and handles timezone offsets.
    * **Marts:** Creates aggregated daily averages and reporting-ready tables.
4.  **Visualization:** Data is served to Apache Superset for dashboarding.

## 🛠️ Tech Stack
* **Orchestration:** Apache Airflow
* **Transformation:** dbt (data build tool)
* **Database:** PostgreSQL
* **Containerization:** Docker & Docker Compose
* **Language:** Python

## 📂 Project Structure
* `airflow/dags/`: Airflow DAG definitions.
* `api-request/`: Python scripts for data ingestion.
* `dbt/`: dbt models, sources, and configurations.
* `docker/`: Initialization scripts and configurations for Superset and Postgres.

## 🏁 Getting Started

### Prerequisites
* Docker and Docker Compose
* A WeatherStack API Key (or equivalent)

## 🖼️ Pipeline in Action

### Airflow DAG Status
Data Pipeline Orchestration: This view shows the Airflow DAG successfully managing the workflow. You can see the transition from initial failures to a consistent 'Success' state (green) for both the ingestion and transformation tasks after the SQL and data type issues were resolved.
<img width="1915" height="759" alt="image" src="https://github.com/user-attachments/assets/f1b3edea-b432-4350-ba0e-19752d38195d" />
*Figure 1: Airflow successfully orchestrating the 'Extract' and 'Transform' steps every 12 hours.*

### Superset Visualization
Live Weather Dashboard: A visualization of the processed data in Apache Superset. This chart tracks the temperature and wind speed trends for Tashkent, pulling directly from the dbt-transformed mart tables in PostgreSQL.
<img width="1905" height="738" alt="image" src="https://github.com/user-attachments/assets/a4e1344a-93e7-425c-844d-bc840a41b454" />
*Figure 2: Final dashboard showing weather trends for Tashkent, processed through the Medallion architecture.*

### Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kaido-coder/automated-data-pipeline.git](https://github.com/kaido-coder/automated-data-pipeline.git)
   cd automated-data-pipeline


