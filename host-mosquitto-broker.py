import pymongo
import paho.mqtt.client as mqtt
from datetime import datetime, timezone
import json
from pymongo.server_api import ServerApi

# MongoDB Atlas configuration
uri = "mongodb+srv://admin:test123@cpc357-assignment2-smar.qqfpx.mongodb.net/"

# MongoDB configuration
mongo_client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
db = mongo_client["smarthome"]
collection = db["iot"]

# Send a ping to confirm a successful connection
try:
    mongo_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# MQTT configuration
mqtt_broker_address = "34.71.153.169"  # Local broker address
mqtt_topic = "iot"

# Define the callback function for connection
def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("Successfully connected to MQTT broker")
        client.subscribe(mqtt_topic)
    else:
        print(f"Connection failed with code {reason_code}")

# Define the callback function for ingesting data into MongoDB
def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print(f"Received message: {payload}")
    
    # Add a timestamp to the data
    timestamp = datetime.now(timezone.utc)
    datetime_obj = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    # Insert the data into MongoDB
    document = {"timestamp": datetime_obj, "data": json.loads(payload)}
    collection.insert_one(document)
    print("Data ingested into MongoDB")

if __name__ == "__main__":
    # MQTT client setup
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Start the Mosquitto MQTT broker locally
    print("Starting the MQTT broker...")
    
    # Connect to the local MQTT broker
    client.connect(mqtt_broker_address, 1883, 60)
    
    # Start listening for messages
    print("Listening for MQTT messages...")
    client.loop_forever()
