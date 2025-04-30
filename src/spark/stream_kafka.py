# kafka_stream_processor.py

from spark_manager import SparkKafkaManager
from pyspark.sql.functions import expr

class KafkaStreamProcessor:
    def __init__(self, kafka_bootstrap_servers, topic):
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.topic = topic
        self.spark_manager = SparkKafkaManager()

    def read_from_kafka(self, kafka_bootstrap_servers, topic):
        return self.spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
            .option("subscribe", topic) \
            .option("startingOffsets", "earliest") \
            .load()

    def process_stream(self):
        # Read from Kafka
        raw_df = self.spark_manager.read_from_kafka(self.kafka_bootstrap_servers, self.topic)
        
        # Parse the Kafka message value as a string
        value_df = raw_df.selectExpr("CAST(value AS STRING)")

        # Here, apply your transformation logic as per your schema
        # Example: You could use `split`, `json`, or other transformations on the value column
        transformed_df = value_df.select(expr("value"))

        # Write the processed stream to the console or a file
        query = transformed_df.writeStream \
            .outputMode("append") \
            .format("console") \
            .start()

        query.awaitTermination()

    def stop(self):
        self.spark_manager.stop()
