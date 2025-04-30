#!/bin/bash

# Register Debezium MySQL source connector
echo "Registering Debezium connector..."
curl -i -X POST http://localhost:8083/connectors/ \
  -H "Accept:application/json" \
  -H "Content-Type:application/json" \
  --data @connector-config.json

# Optional: Wait for the connector to initialize
sleep 5

# Create Kafka topic (only if auto topic creation is disabled)
echo "Creating Kafka topic..."
docker exec -it kafka kafka-topics \
  --create \
  --topic mysql-server.stocks.stock_intraday \
  --bootstrap-server kafka:9092 \
  --replication-factor 1 \
  --partitions 3