# MongoDB–PySpark YouTube Sample

This project implements a small end‑to‑end pipeline using MongoDB Atlas and PySpark with the MongoDB Spark Connector. It loads a sample YouTube API response into MongoDB, reads it into a Spark DataFrame, and extracts only the `regionCode` for a specific `channelId`. [file:1][web:5]

## Assignment Description

The assignment requirements are: [file:1]

- Insert a provided YouTube JSON sample into a MongoDB collection named `youtube` in the `test` database.
- Write a MongoDB query to return only the `regionCode` for documents where `channelId` is `UCJowOS1R0FnhipXVqEnYU1A`.
- Write PySpark code to:
  - Read this YouTube document into a Spark DataFrame.
  - Return only the `regionCode` for rows where the nested `channelId` equals `UCJowOS1R0FnhipXVqEnYU1A`.

## Approach

- **MongoDB insertion (Python / PyMongo)**  
  A Python script connects to MongoDB Atlas using the SRV URI and inserts the YouTube JSON document into the `test.youtube` collection. [web:65][file:1]

- **Spark session configuration**  
  A helper module creates a `SparkSession` configured with the MongoDB Spark Connector (via `--packages`) and the Atlas connection URI. [web:23][web:5]

- **DataFrame creation and transformation (PySpark)**  
  Another script:
  - Reads `test.youtube` into a Spark DataFrame using the MongoDB connector.
  - Explodes the `items` array and filters by `item.id.channelId`.
  - Selects only the distinct `regionCode` field to satisfy the assignment query. [file:1]

## File Overview

- `insert_youtube.py`
  - Connects to MongoDB Atlas with `MongoClient`.  
  - Inserts the sample YouTube JSON document into `test.youtube`. [file:1][web:65]

- `spark_session.py`  
  - Creates and returns a configured `SparkSession` with the MongoDB connection URI.  
  - Provides a `get_youtube_df(spark)` helper that reads the `youtube` collection into a DataFrame. [web:5]

- `youtube_region_code.py`  
  - Uses `spark_session.create_spark()` and `get_youtube_df()` to get the DataFrame.  
  - Explodes `items`, filters by `channelId`, and returns only the `regionCode`. [file:1]

## Prerequisites

- MongoDB Atlas cluster with a user (e.g. `Admin`) and Network Access configured for your IP. [web:31]  
- Python 3, `pymongo`, and PySpark installed in the environment. [web:67]  
- Access to Spark submit (`spark-submit`).  
- MongoDB Spark Connector for Scala 2.12 (e.g. `mongo-spark-connector_2.12:3.0.2`). [web:23]

## Configuration

Update the MongoDB URI in both Python files:

```python
# Example URI (replace password and appName as needed)
MONGO_URI = (
    "mongodb+srv://Admin:<password>@clustername.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Cluster0"
)
