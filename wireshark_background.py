import pyshark
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder



label_encoder = LabelEncoder()
model_CNN = tf.keras.models.load_model("../models/actual/model_cnn_lstm.h5")

#Affichage de chaque information pour un paquet en entrée
def print_info_layer(packet):
    try:
        info = [packet.number,packet.sniff_timestamp,packet.ip.src,packet.ip.dst,packet.highest_layer,packet.length,""]
        data = pd.DataFrame([info], columns=["No.","Time","Source","Destination","Protocol","Length","Info"])
        print(data)
        result = label_encoder.fit_transform(model_CNN.predict(data))   
        print(result)
    except AttributeError as e:
        pass

#Nom de l'interface a inspecter celle-ci dois etre changé selon la couche 
name_interface = "Loopback"
#Capture des paquet en temp réel avec un timeout de 10
try:
    print("Start")
    cap = pyshark.LiveCapture(interface=name_interface)
    cap.sniff(packet_count=5)
    cap.apply_on_packets(print_info_layer)
except KeyboardInterrupt:
    print("[-] ERROR PROGRAMME")