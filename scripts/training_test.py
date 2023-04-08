import pandas as pd
from scipy.io import arff
import numpy as np
import tensorflow as tf
from tensorflow import keras

# data set de https://www.kaggle.com/datasets/jacobvs/ddos-attack-network-logs
# tuto : https://www.tensorflow.org/tutorials/load_data/csv

# convertir les données arff en csv avant ########################################
train = pd.read_csv("./final-dataset-short.csv")
#train = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
print(train.head())
# la colonne qui nous intéresse : PKT_class (type) # le truc qui marche dataset de base
ddos_features = train.copy()
ddos_labels = ddos_features.pop('PKT_CLASS')
#ddos_labels = ddos_features.pop('survived') # le truc qui marche : data set de base

# Build un model preprocessing (car col de type different : numeric et string) #############
inputs = {}

for name, column in ddos_features.items():
  dtype = column.dtype
  if dtype == object:
    dtype = tf.string
  else:
    dtype = tf.float32
  inputs[name] = tf.keras.Input(shape=(1,), name=name, dtype=dtype)

inputs

# pour les inputs numeric : on les concat ensemble
numeric_inputs = {name:input for name,input in inputs.items()
                  if input.dtype==tf.float32}
x = keras.layers.Concatenate()(list(numeric_inputs.values()))
norm = keras.layers.Normalization()
norm.adapt(np.array(train[numeric_inputs.keys()]))
all_numeric_inputs = norm(x)

all_numeric_inputs

#collectionner les résultats preprocessing pr concat plus tard
preprocessed_inputs = [all_numeric_inputs]

# pour les string inputs : utiliser CategoryEncoding pr convertir en float
for name, input in inputs.items():
  if input.dtype == tf.float32: # ignorer si ce sont des float
    continue

  lookup = keras.layers.StringLookup(vocabulary=np.unique(ddos_features[name]))
  one_hot = keras.layers.CategoryEncoding(num_tokens=lookup.vocabulary_size())

  x = lookup(input)
  x = one_hot(x)
  preprocessed_inputs.append(x)

# concat les inputs ensemble et build model qui handle le preprocessing
preprocessed_inputs_cat = keras.layers.Concatenate()(preprocessed_inputs)
ddos_preprocessing = tf.keras.Model(inputs, preprocessed_inputs_cat)

#plot_model(model = ddos_preprocessing , rankdir="LR", dpi=72, show_shapes=True)

# convertir en un dictionnaire de tensors
ddos_features_dict = {name: np.array(value)
                         for name, value in ddos_features.items()}

features_dict = {name: values[:1] for name, values in ddos_features_dict.items()}

# Build model tensorflow ########################################"###

# Fonction pr création model
def ddos_model(preprocessing_head, inputs):
  body = tf.keras.Sequential([
    keras.layers.Dense(64),
    keras.layers.Dense(1)
  ])

  preprocessed_inputs = preprocessing_head(inputs)
  result = body(preprocessed_inputs)
  model = tf.keras.Model(inputs, result)

  model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                optimizer=tf.keras.optimizers.Adam())
  return model

# Création model
ddos_model = ddos_model(ddos_preprocessing, inputs)

# Check summary
ddos_model.summary()
# Train model

ddos_model.fit(x=ddos_features_dict, y=ddos_labels, epochs=5)
#ddos_model.save('./ddos_model_test')

# reloaded = tf.keras.models.load_model('./ddos_model_test')