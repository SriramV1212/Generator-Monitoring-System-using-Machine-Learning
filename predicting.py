# Importing necessary libraries
import pandas as pd
import joblib
import paho.mqtt.client as mqtt
import datetime
import time
# ct stores current time
ct = datetime.datetime.now()

# Load the trained Random Forest model
model_path = 'models/random_forest_model.joblib'  # Adjust the path accordingly
clf = joblib.load(model_path)

# MQTT broker settings for HiveMQ (replace with your broker details)
mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "Status"

# MQTT broker authentication settings (replace with your credentials if required)
mqtt_username = "admin"
mqtt_password = "Sethur2006@"
client = mqtt.Client("RandomForestClient")
# Set MQTT broker credentials
client.username_pw_set(username=mqtt_username, password=mqtt_password)

# Connect to the broker
client.connect(mqtt_broker, mqtt_port, 60)

# New data for prediction (replace this with your actual data) 
datass=[0.00,0.00,0.00,0.00]
new_data = pd.read_csv('inputdata.csv', encoding='unicode_escape')
for i in range(4):
    print(new_data.iloc[0,i])
    datass[i]=new_data.iloc[0,i]

# Make predictions on the new data
predictions = clf.predict(new_data)
print("Predictions:")
if predictions==[1]:
    print("maintenance is required")
    result="Maintenance is required "
else: 
    print("maintenance is Not required")
    result="Maintenance is not required " 



client.publish(mqtt_topic, result)
client.publish("time", str(ct))
client.publish("Battery Voltage (V)", str(datass[0]))
client.publish("Coolant Temperature (°C)", str(datass[1]))
client.publish("Engine Speed (RPM)", str(datass[2]))
client.publish("Generator Avg Frequency (Hz)", str(datass[3]))
print(f"Published: {result}")
time.sleep(5)

