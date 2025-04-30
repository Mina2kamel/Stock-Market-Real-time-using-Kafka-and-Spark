from pyspark.sql import SparkSession

class SparkManager:
    def __init__(self, app_name="KafkaSparkApp"):
        self.app_name = app_name
        self.spark = None

    def create_session(self):
        self.spark = SparkSession.builder \
            .appName(self.app_name) \
            .master("spark://spark-master:7077") \
            .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
            .getOrCreate()
        return self.spark
