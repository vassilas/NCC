import numpy as np
import h5py as h5
import keras
import ncc_Model
from keras.layers import  Dense, Flatten, Activation, Dropout, Embedding
from keras.layers import LSTM, GRU, TimeDistributed, Permute,Reshape, Lambda, RepeatVector, Input,Multiply
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import load_model


dhf5_data = h5.File('../datasets/Finalsets/dataset_padded_cutted.hdf5', 'r')
RNA_Sequence = dhf5_data['RNA_Sequence']
RNA_Sequence = np.array(RNA_Sequence)
RNA_Class = dhf5_data['RNA_Class']
RNA_Class = np.array(RNA_Class)
RNA_Class = to_categorical(RNA_Class, 13)

X_train, X_test, Y_train, Y_test = train_test_split(RNA_Sequence, RNA_Class, test_size=0.33, random_state=2, shuffle=True)
print("X_train = "+str(X_train.shape)+" , Y_train = "+str(Y_train.shape))
print("X_test = "+str(X_test.shape)+" , Y_test = "+str(Y_test.shape))



def train():
    m = ncc_Model.ncc_Model_01()

    print("1. MODEL COMPILE")
    m.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])

    print("2. MODEL SUMMARY")
    m.summary() 

    print("2. MODEL FIT")
    batch_size = 128
    epochs = 50
    steps_per_epoch = None
    validation_steps = 3
    print("Batch size : "+str(batch_size))
    print("epochs : "+str(epochs))
    print("steps per epoch : "+str(steps_per_epoch))
    print("validation steps : "+str(validation_steps))
    history = m.fit(x=X_train, y=Y_train, 
                    batch_size= batch_size, 
                    epochs= epochs, 
                    validation_data=(X_test, Y_test),
                    workers=8,
                    shuffle=True,
                    steps_per_epoch=steps_per_epoch, #if not specified = (number of samples)/(batch size) = number of samples
                    validation_steps=validation_steps)

    print("1. MODEL SAVE")
    m.save(ncc_Model.ncc_Model_01.__name__) #Save the model

    return history


def test():
    model = load_model(ncc_Model.ncc_Model_01.__name__)
    model.evaluate(X_test,Y_test)  # Predicting the test set
    Y_predict = model.predict(X_test)  # Predicting the test set
    f = h5.File("Prediction.h5", 'w')  # Save the prediction results
    f.create_dataset('Prediction', data=Y_predict)
    f.create_dataset('Real', data=Y_test)
    return Y_predict, Y_test