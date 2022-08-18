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
    print("Hasil prediksi: " + str(predict) + " - " + stres_level[predict])
    # return(array)


eel.start("index.html")

# Predict This!
# prediction([86.84,23.824,90.912,14.28,88.912,97.28,0.912,69.56])  #Medium High
# prediction([54.08,18.816,94.816,8.816,93.224,82.04,5.816,57.04])  #Medium Low
# prediction([80.72,22.192,90.096,12.24,88.096,95.24,0.096,65.48])  #Medium High
# prediction([96.8,26.8,86,17.4,83.2,101,0,77])  #High
# prediction([92.96,25.456,91.728,16.32,89.728,99.32,1.728,73.64])  #Medium High
# prediction([78.24,21.824,93.824,11.824,91.824,94.12,4.736,64.56])  # Medium
# prediction([97.184,27.184,86.48,17.592,83.776,101.48,0,77.96])  # High
# prediction([99.456,29.456,89.32,18.728,87.184,104.32,0,83.64])  # High
# prediction([99.232,29.232,89.04,18.616,86.848,104.04,0,83.08])  # High
# prediction([57.84,19.568,95.568,9.568,94.352,83.92,6.568,58.92])  # Medium Low
