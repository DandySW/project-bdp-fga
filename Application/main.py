from turtle import position
import eel
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

eel.init("web")

df = pd.read_csv("SaYoPillow.csv")

# Atribut: snr,rr,t,lm,bo,rem,slr,hr,sl
X = df.drop("sl", axis="columns")
Y = df["sl"]

Xmin = X.min().to_list()
Xmax = X.max().to_list()

stres_level = {0: "low", 1: "medium low",
               2: "medium", 3: "medium high", 4: "high"}

X = MinMaxScaler().fit_transform(X)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, train_size=0.8, random_state=33)

rfc = RandomForestClassifier(n_estimators=99).fit(X_train, Y_train)


@eel.expose
def prediction(user_input):
    array = []
    for idx in range(len(user_input)):
        norm = (float(user_input[idx]) - Xmin[idx]) / (Xmax[idx] - Xmin[idx])
        array.append(norm)
    predict = rfc.predict([array])
    predict = predict[0]
    # print("Hasil prediksi: " + str(predict) + " - " + stres_level[predict])
    return(int(predict), stres_level[predict])


eel.start("index.html", size=(1280, 720))
