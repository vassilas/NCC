import keras
from keras.layers import  Dense, Flatten, Dropout
from keras.layers import LSTM, GRU, Input
from keras.models import Model
from keras.layers import  Bidirectional


# accuracy = 0.9852722063037249
# Sensitivity = 0.9827206510263349
# precision = 0.9836097056301122
# f1 = 0.9831257171740228
# mcc = 0.9839845222070254
def ncc_Model_01():
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=256, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    out = Flatten()(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# 0.9843
def ncc_Model_02(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=256, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    # ----------------------
    attmech = Permute((2, 1))(out)
    attmech = Dense(500, activation='softmax', kernel_initializer='RandomNormal', bias_initializer='zeros')(attmech)
    attmech =  Permute((2, 1))(attmech)
    out = Multiply()([out, attmech])
    # ----------------------
    out = Flatten()(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model




# accuracy = 0.9877363896848137
# Sensitivity = 0.9852420331595688
# precision = 0.9857227219900111
# f1 = 0.9853834527549586
# mcc = 0.986670391466567
#
# Notes: In the middle of the training there was a wierd spark and accuracy droped 
#
def ncc_Model_03(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=256, 
                                # return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    out = Flatten()(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    output = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=output)
    return model


# accuracy = 0.9736962750716333
# Sensitivity = 0.9691135203808402
# precision = 0.9711447391876695
# f1 = 0.9700533743698372
# mcc = 0.9713950107196068
def ncc_Model_04(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=4, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    out = Flatten()(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model



# accuracy = 0.9751289398280802
# Sensitivity = 0.9707785539107466
# precision = 0.9721581454914238
# f1 = 0.9714184668760752
# mcc = 0.9729495612084714
def ncc_Model_05(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=8, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    out = Flatten()(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# accuracy = 0.9763323782234957
# Sensitivity = 0.9730065735801431
# precision = 0.972300983557311
# f1 = 0.9725944679713655
# mcc = 0.9742661612097485
#
# Notes = Very bad Loss
#
def ncc_Model_06(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=100, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    
    out = Flatten()(out)
    out = Dense(1000, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dense(500, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model