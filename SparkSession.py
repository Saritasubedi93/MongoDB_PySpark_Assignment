# spark_session.py
from pyspark.sql import SparkSession


def create_spark():
    mongo_uri = (
        "mongodb+srv://Admin:Admin1234@cluster0.zckeksp.mongodb.net/"
        "?retryWrites=true&w=majority&appName=Cluster0"
    )

    spark = SparkSession.builder \
        .appName("MongoYoutubeApp") \
        .config("spark.mongodb.input.uri", mongo_uri) \
        .getOrCreate()
    return spark


def get_youtube_df(spark):
    df = spark.read.format("com.mongodb.spark.sql.DefaultSource") \
        .option("uri", "mongodb+srv://Admin:Admin1234@cluster0.zckeksp.mongodb.net/") \
        .option("database", "test") \
        .option("collection", "youtube") \
        .load()
    return df
