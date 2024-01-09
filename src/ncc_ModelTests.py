from keras.models import load_model
from keras.utils import to_categorical
import h5py as h5
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt



class_dict = {
    0       :   '5S_rRNA'    ,
    1       :   '5_8S_rRNA'  ,
    2       :   'tRNA'       ,
    3       :   'ribozyme'   ,
    4       :   'CD-box'     ,
    5       :   'miRNA'      ,
    6       :   'Intron_gpI' ,
    7       :   'Intron_gpII',
    8       :   'HACA-box'   ,
    9       :   'riboswitch' ,
    10      :   'IRES'       ,
    11      :   'leader'     ,
    12      :   'scaRNA'
}

labels = [  '5S_rRNA'    ,
            '5_8S_rRNA'  ,
            'tRNA'       ,
            'ribozyme'   ,
            'CD-box'     ,
            'miRNA'      ,
            'Intron_gpI' ,
            'Intron_gpII',
            'HACA-box'   ,
            'riboswitch' ,
            'IRES'       ,
            'leader'     ,
            'scaRNA']


def read_XY_HDF5_dataset(dataset_path:str) -> []:
    dhf5_data = h5.File(dataset_path, 'r')
    RNA_Sequence = dhf5_data['RNA_Sequence']
    RNA_Sequence = np.array(RNA_Sequence)
    RNA_Class = dhf5_data['RNA_Class']
    RNA_Class = np.array(RNA_Class)
    RNA_Class = to_categorical(RNA_Class, 13)
    return RNA_Sequence,RNA_Class


def prediction(model, X_test) -> []:
    Y_predict = model.predict(X_test)
    return Y_predict

def convert_true_categorical_class_to_class(Y_true: []) ->[]:
    Y_true_class = []
    for class_array in Y_true:
        for i in range(len(class_array)):
            if class_array[i] == 1:
                Y_true_class.append(class_dict[i])
    return Y_true_class


def convert_predictions_to_resulted_class(Y_predicted: []) ->[]:
    Y_pred_class = []
    for class_array in Y_predicted:
        index: int = 0
        max:float = 0.0
        for i in range(0,len(class_array)):
            element = class_array[i]
            float_element = float(element)
            if float_element > max:
                max = float_element
                index = i
        Y_pred_class.append(class_dict[index])
    return Y_pred_class

def evaluate_model(Y_true_class: [], Y_pred_class: []):
    accuracy    = metrics.accuracy_score(y_true=Y_true_class,y_pred=Y_pred_class)
    f1          = metrics.f1_score(y_true=Y_true_class,y_pred=Y_pred_class,average = 'micro')
    precision   = metrics.precision_score(y_true=Y_true_class,y_pred=Y_pred_class,average = 'micro')
    sensitivity = metrics.recall_score(y_true=Y_true_class,y_pred=Y_pred_class,average = 'micro')
    mcc         = metrics.matthews_corrcoef(y_true=Y_true_class,y_pred=Y_pred_class)
    return [accuracy, sensitivity, precision, f1, mcc]

def display_confusion_matrix(Y_true_class, Y_pred_class):
    confusion_matrix = metrics.confusion_matrix(Y_true_class, Y_pred_class, labels=labels)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix,
                                            display_labels = labels)
    cm_display.plot()
    plt.xticks(rotation=90)
    plt.show()

def print_evaluation_metrics(Y_true_class: [], Y_pred_class: []):
    [accuracy, sensitivity, precision, f1, mcc] = evaluate_model(Y_true_class, Y_pred_class)
    print("accuracy \t= " + str(accuracy))
    print("Sensitivity \t= " + str(sensitivity))
    print("precision \t= " + str(precision))
    print("f1 \t\t= " + str(f1))
    print("mcc \t\t= " + str(mcc))




if __name__ == '__main__':
    model_name = "model_20_Train_001"
    model_path = "../Models/" + model_name
    dataset_path = "../datasets/Finalsets/ribozyme_padded_cutted.hdf5"

    print("> Load model : [" + model_name + "]")
    model = load_model(model_path)

    print("> Load dataset from ["+ dataset_path +"]")
    [X_test,Y_true] = read_XY_HDF5_dataset(dataset_path)
    
    print("> Prediction")
    Y_predict = prediction(model,X_test)

    print("> Convert numerical values to RNA classes")
    Y_true_class = convert_true_categorical_class_to_class(Y_true)
    Y_pred_class = convert_predictions_to_resulted_class(Y_predict)

    print("> Print the evaluation of the model / metrics")
    print_evaluation_metrics(Y_true_class, Y_pred_class)
    
    print("> Display Confusion Matrix")
    display_confusion_matrix(Y_true_class, Y_pred_class)