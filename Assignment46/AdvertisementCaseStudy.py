# Design Machine Learning Application which uses the classification technique

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score


border = "-" * 70
def LoadData(filename):
   

    df = pd.read_csv(filename)

    print(border)
    print("Step 1 : Load the Data")
    print(border)

    print("Dataset Loaded Sucessfully")
    print(df.head())

    print(border)


# Step 2 : Data Preprocessing 
 
    print("Step 2 : Data Preprocessing")
    print(border)

    if "Unamed: 0" in df.columns:
        df = df.drop(columns = ["Unamed: 0"])

    print(df.head())

    print(border)
    print("Check the Missing Value : ")
    print(df.isnull().sum())
    print(border)

# Step 3 : Statistical Report 

    print("Step 3 :Statistical report:")
    print(border)

    print(df.describe())
    print(border)


# Step 4 : Seperate Independent and Dependent Variable

    print(" Step 4 : Seperate Independent and Dependent Variable")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)

    print("Independent Variable : ")
    print(X.head())

    print("Dependent Variable : ")
    print(Y.head())

    print(border)

# Step 5 : Split Data 

    print("Step 5 : Split the dataset")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
    )

    print("Dataset Spliting Completed Sucessfully")

    print("X_train:",X_train.shape)
    print("X_test:",X_test.shape)

    print("Y_train:",Y_train.shape)
    print("Y_test:",Y_test.shape)

    print(border)

# Step 6 : Create the model

    print("Step 6 : Create the model")
    

    Model = LinearRegression()

    print("Model created succesfully...")

    print(border)



# Step 7 : Train Model

    print("Step 7 : Train Mode")
    


    Model = Model.fit(X_train,Y_train)

    print("Model Train Sucessfully...")

    print(border)

#  Step 8 : Test the model  

    print("Step 8 : Test the model  ")
    print(border)

    Y_pred = Model.predict(X_test)

    print("Accurate ans:")
    print(Y_test[:3])

    print("Predicted ans:")
    print(Y_pred[:3])

    print(border)


# Step 9 : Evaluate Model

    print("Step 9 : Evaluate the model")
    print(border)

    mrc = mean_squared_error(Y_test,Y_pred)

    rmsc = np.sqrt(mrc)

    r2 = r2_score(Y_test,Y_pred)

    print("MSC : ",mrc)
    print("RMSC :",rmsc)
    print("R2 : ",r2)


def main():

   LoadData("Advertising.csv")

if __name__ == "__main__":
    main()