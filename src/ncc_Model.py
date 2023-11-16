import keras
from keras.layers import  Dense, Flatten, Dropout
from keras.layers import LSTM, GRU, Input
from keras.models import Model
from keras.layers import  Bidirectional


def ncc_Model_01():
    inputs = Input(shape=(500, 8,))
    bi_GRU = Bidirectional(GRU(
                                units=256, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    attention_mul = Flatten()(bi_GRU)
    dense_one = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(attention_mul)
    dense_one = Dropout(0.4)(dense_one)
    dense_two = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(dense_one)
    dense_two = Dropout(0.4)(dense_two)
    dense_3 = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(dense_two)
    dense_3 = Dropout(0.4)(dense_3)
    output = Dense(13, activation='softmax')(dense_3)
    model = Model(inputs=[inputs], outputs=output)
    return model