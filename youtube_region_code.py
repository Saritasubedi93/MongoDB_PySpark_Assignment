# youtube_region_code.py
from pyspark.sql.functions import explode, col
from SparkSession import create_spark, get_youtube_df


def get_region_code_for_channel(df, channel_id):
    items_df = df.select(
        "regionCode",
        explode("items").alias("item")
    )

    filtered_df = items_df.filter(
        col("item.id.channelId") == channel_id
    )

    result_df = filtered_df.select("regionCode").distinct()
    return result_df


def main():
    spark = create_spark()
    df = get_youtube_df(spark)

    df.printSchema()
    df.show(truncate=False)

    channel_id = "UCJowOS1R0FnhipXVqEnYU1A"
    result_df = get_region_code_for_channel(df, channel_id)
    result_df.show()  # shows only regionCode


if __name__ == "__main__":
    main()
