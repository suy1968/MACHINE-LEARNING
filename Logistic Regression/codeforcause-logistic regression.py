import numpy as np
from sklearn.datasets import make_blobs
from sklearn.linear_momdel import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X,y = make_blobs(n=smaples=1000, centers=2 ,random_state=42)

X_train,X_test,y_train,y_test= train_test_split(X,y,random_state=42)

model=LogisticReggression()

model.fit(X_train,y_train)

model.ceof_,model.intercept_

x1_sample= np.linspace(-6,7)

colors = ["red","blue"]
y_colors =list(map(lambda c: colors[c],y))

y_colors[:5],y[:5]

plt.scatter(X[:,0],X[:1],c=y)
for i, (coef, intercept) in enumerate(zip(model.coef_, model.intercept_)):
    x2_sample = -coef[0]/coef[1] * x1_sample - intercept/coef[1]
    plt.plot(x1_sample, x2_sample, color=color[i])
model.score(X_test, y_test)
