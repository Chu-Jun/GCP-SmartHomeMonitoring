# Import required libraries
import paho.mqtt.client as mqtt
import json
import time

# MQTT configuration
mqtt_broker_address = <External IP for VM>  # Broker address (You are required to change the <External IP for VM> to the external IP for VM instance created)
mqtt_topic = "iot"

# Publish dummy data to MQTT broker
def publish_dummy_data(mqtt_client, topic):
    # Dummy data
    dummy_data = [
        {
            "timestamp": "2023-08-18 00:00:00",
            "temperature_salon": 29.0,
            "humidity_salon": 59.6,
            "temperature_chambre": 28.3,
            "humidity_chambre": 60.7,
            "temperature_bureau": 28.3,
            "humidity_bureau": 59.9
        },
        {
            "timestamp": "2023-08-18 00:15:00",
            "temperature_salon": 27.9,
            "humidity_salon": 53.6,
            "temperature_chambre": 28.3,
            "humidity_chambre": 62.1,
            "temperature_bureau": 27.9,
            "humidity_bureau": 55.7
        },
        {
            "timestamp": "2023-08-18 00:30:00",
            "temperature_salon": 28.9,
            "humidity_salon": 52.6,
            "temperature_chambre": 29.3,
            "humidity_chambre": 63.1,
            "temperature_bureau": 26.9,
            "humidity_bureau": 56.7
        },
        {
            "timestamp": "2023-08-18 00:45:00",
            "temperature_salon": 25.9,
            "humidity_salon": 55.6,
            "temperature_chambre": 29.3,
            "humidity_chambre": 65.1,
            "temperature_bureau": 24.9,
            "humidity_bureau": 53.7
        },
        {
            "timestamp": "2023-08-18 01:00:00",
            "temperature_salon": 26.9,
            "humidity_salon": 54.6,
            "temperature_chambre": 28.5,
            "humidity_chambre": 62.6,
            "temperature_bureau": 26.8,
            "humidity_bureau": 54.9
        }
    ]
    
    # Publish each row as a JSON message
    for row in dummy_data:
        mqtt_client.publish(topic, json.dumps(row))
        print(f"Published message: {row}")
        time.sleep(1)  # Simulate a delay for real-time publishing

if __name__ == "__main__":
    # MQTT client setup
    client = mqtt.Client()
    
    # Connect to the MQTT broker
    client.connect(mqtt_broker_address, 1883, 60)
    
    # Publish dummy data to MQTT broker
    publish_dummy_data(client, mqtt_topic)
    
    print("Finished publishing dummy data")
