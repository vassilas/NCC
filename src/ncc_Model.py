from keras.layers import Input, Permute, Multiply, MaxPooling1D
from keras.layers import Dense, Flatten, Dropout, Conv1D
from keras.layers import SimpleRNN, LSTM, GRU, Bidirectional
from keras.models import Model

# accuracy = 0.9885386819484241
# Sensitivity = 0.9859438368042353
# precision = 0.9870469130441977
# f1 = 0.9864626370268229
# mcc = 0.9875355183724713
def ncc_Model_00(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=8,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(512, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model

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
# Notes = Very bad and unstable val-Loss
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


# accuracy = 0.9765616045845272
# Sensitivity = 0.972827572084429
# precision = 0.9736527073544559
# f1 = 0.9732051920174724
# mcc = 0.9745078241394405
#
# Notes = Very bad and unstable val-Loss
#
def ncc_Model_07(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=20, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                        ))(inputs)
    out = Bidirectional(GRU(
                            units=4, 
                            return_sequences=True, 
                            kernel_initializer='RandomNormal', 
                            dropout= 0.3,
                            recurrent_initializer='RandomNormal', 
                            bias_initializer='zero'
                        ))(out)
    out = Flatten()(out)
    out = Dense(500, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# accuracy = 0.9782234957020057
# Sensitivity = 0.9736099823073758
# precision = 0.9764507962100979
# f1 = 0.9749285296605023
# mcc = 0.9763215467234744
def ncc_Model_08(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(LSTM(
                                units=20, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.2,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                        ))(inputs)
    out = Flatten()(out)
    out = Dense(500, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model



# accuracy = 0.9846991404011461
# Sensitivity = 0.9815416873427686
# precision = 0.9834426207290238
# f1 = 0.9824528568288867
# mcc = 0.9833599895349546
def ncc_Model_09(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(LSTM(
                                units=250, 
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




# accuracy = 0.9815472779369627
# Sensitivity = 0.9786113661121363
# precision = 0.9790380969988355
# f1 = 0.9787613414519488
# mcc = 0.9799368950507379
def ncc_Model_10(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(GRU(
                                units=256, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                        ))(inputs)
    out = Conv1D(100, 3, activation='relu')(out)
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


# accuracy = 0.9838968481375359
# Sensitivity = 0.9808776840212237
# precision = 0.9821575307982874
# f1 = 0.9814660914947125
# mcc = 0.9824897624363724
def ncc_Model_11(): # Model
    inputs = Input(shape=(500, 4,))
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


# accuracy = 0.9837249283667622
# Sensitivity = 0.9806403312961769
# precision = 0.9809515193065685
# f1 = 0.9807694169427924
# mcc = 0.9823002506824172
# 
# Change the activation functions
#
def ncc_Model_12(): # Model
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
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='sigmoid')(out)
    out = Dropout(0.4)(out)
    out = Dense(64, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='sigmoid')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model




#
# Simple RRN , training too slow need to modify
#
def ncc_Model_13(): # Model
    inputs = Input(shape=(500, 8,))
    out = Bidirectional(SimpleRNN(
                                units=8, 
                                return_sequences=True, 
                                kernel_initializer='RandomNormal', 
                                dropout= 0.3,
                                recurrent_initializer='RandomNormal', 
                                bias_initializer='zero'
                            ))(inputs)
    out = Flatten()(out)
    out = Dense(500, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(250, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='sigmoid')(out)
    out = Dropout(0.4)(out)
    out = Dense(100, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='sigmoid')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# accuracy = 0.9711747851002865
# Sensitivity = 0.9674674143148547
# precision = 0.9664229396737026
# f1 = 0.9668931361945237
# mcc = 0.9686542983383793
def ncc_Model_14(): # Model
    inputs = Input(shape=(500, 8,))
    out = Flatten()(inputs)
    out = Dense(500, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(250, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='sigmoid')(out)
    out = Dropout(0.4)(out)
    out = Dense(100, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='sigmoid')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model



# accuracy = 0.9841260744985674
# Sensitivity = 0.9816332501131408
# precision = 0.9811856164985385
# f1 = 0.9813987774986781
# mcc = 0.9827359127534064
def ncc_Model_15(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=8,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=8, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(256, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model



# accuracy = 0.9849856733524355
# Sensitivity = 0.9818925842918664
# precision = 0.9836186254198576
# f1 = 0.9827285575583731
# mcc = 0.9836704832311708


# rfam
# accuracy = 0.895
# Sensitivity = 0.895
# precision = 0.8950614785679074
# f1 = 0.8935450572275052
# mcc = 0.8865074655168514
def ncc_Model_16(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=8,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    # ----------------------
    attmech = Permute((2, 1))(out)
    attmech = Dense(123, activation='softmax', kernel_initializer='RandomNormal', bias_initializer='zeros')(attmech)
    attmech =  Permute((2, 1))(attmech)
    out = Multiply()([out, attmech])
    # ----------------------
    out = Flatten()(out)
    out = Dense(512, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# accuracy = 0.9836676217765044
# Sensitivity = 0.9795663462425919
# precision = 0.9830348057871748
# f1 = 0.9811342979577158
# mcc = 0.9822524871358913
def ncc_Model_17(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=40,kernel_size=20,strides=1,activation='relu')(inputs)
    # out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(1000, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(512, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model



# accuracy = 0.9897421203438396
# Sensitivity = 0.9874426132994579
# precision = 0.9885376562601503
# f1 = 0.9879412124220927
# mcc = 0.9888464558716861
def ncc_Model_18(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=8,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(1000, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(512, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# accuracy = 0.9885959885386819
# Sensitivity = 0.9862708251940363
# precision = 0.9868194049785399
# f1 = 0.9865218404706702
# mcc = 0.9875978593901092
def ncc_Model_19(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=3,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model


# Train: dataset_003_08d
# Test: dataset_002_08d
# ---------------------------------------
# accuracy = 0.9142307692307692
# Sensitivity = 0.9142307692307694
# precision = 0.9154401839376296
# f1 = 0.9142229639738342
# mcc = 0.9071868515854054

# NCC
# ---------------------------------------
# accuracy = 0.9897994269340974
# Sensitivity = 0.9870139049819442
# precision = 0.9892415222736667
# f1 = 0.988076055362084
# mcc = 0.9889093245956685
def ncc_Model_20(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=9,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model

# Train: dataset_003_08d
# Test: dataset_002_08d
# ---------------------------------------
# accuracy = 0.9188461538461539
# Sensitivity = 0.9188461538461538
# precision = 0.9215575913843619
# f1 = 0.9172564186196918
# mcc = 0.9126029629566416

# Train: dataset_004_08d
# Test: dataset_002_08d
# ---------------------------------------
# accuracy = 0.926923076923077
# Sensitivity = 0.9269230769230768
# precision = 0.9281730445106077
# f1 = 0.9271264366585444
# mcc = 0.9209059460879675
def ncc_Model_21(): # Model
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=8,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=128, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(1024, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(512, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model

# Train: dataset_003_08d
# Test: dataset_002_08d
# ---------------------------------------
# accuracy = 0.9292307692307692
# Sensitivity = 0.9292307692307691
# precision = 0.931189216261044
# f1 = 0.9293499153046424
# mcc = 0.9234800066296411
def ncc_Model_22():
    inputs = Input(shape=(500, 8,))
    out = Conv1D(filters=32,kernel_size=8,strides=1,activation='relu')(inputs)
    out = MaxPooling1D(pool_size=4)(out)
    out = Bidirectional(GRU(
            units=512, 
            return_sequences=True, 
            kernel_initializer='RandomNormal', 
            dropout= 0.3,
            recurrent_initializer='RandomNormal', 
            bias_initializer='zero'
        ))(out)
    out = Flatten()(out)
    out = Dense(1024, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(512, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(128, kernel_initializer='RandomNormal', bias_initializer='zeros', activation='relu')(out)
    out = Dropout(0.4)(out)
    out = Dense(13, activation='softmax')(out)
    model = Model(inputs=[inputs], outputs=out)
    return model