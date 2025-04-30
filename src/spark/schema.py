# schema_definitions.py

from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType

# This schema matches the Debezium message envelope
debezium_avro_schema = StructType([
    StructField("before", StructType([
        StructField("symbol", StringType(), True),
        StructField("timestamp", StringType(), True),
        StructField("open", DoubleType(), True),
        StructField("high", DoubleType(), True),
        StructField("low", DoubleType(), True),
        StructField("close", DoubleType(), True),
        StructField("volume", DoubleType(), True),
    ]), True),
    StructField("after", StructType([
        StructField("symbol", StringType(), True),
        StructField("timestamp", StringType(), True),
        StructField("open", DoubleType(), True),
        StructField("high", DoubleType(), True),
        StructField("low", DoubleType(), True),
        StructField("close", DoubleType(), True),
        StructField("volume", DoubleType(), True),
    ]), True),
    StructField("source", StructType([
        StructField("version", StringType(), True),
        StructField("connector", StringType(), True),
        StructField("name", StringType(), True),
        StructField("ts_ms", StringType(), True),
        StructField("snapshot", StringType(), True),
        StructField("db", StringType(), True),
        StructField("sequence", StringType(), True),
        StructField("table", StringType(), True),
        StructField("server_id", StringType(), True),
        StructField("gtid", StringType(), True),
        StructField("file", StringType(), True),
        StructField("pos", StringType(), True),
        StructField("row", StringType(), True),
        StructField("thread", StringType(), True),
        StructField("query", StringType(), True),
    ]), True),
    StructField("op", StringType(), True),
    StructField("ts_ms", StringType(), True),
    StructField("transaction", StructType([
        StructField("id", StringType(), True),
        StructField("total_order", StringType(), True),
        StructField("data_collection_order", StringType(), True),
    ]), True),
])
