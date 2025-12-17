from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
#actual labels (ground truth)
y_true = [1,0,1,1,0,1,0,0,1,0]

#predicted labels by model
y_pred = [1,0,1,0,0,1,0,1,1,1]

#calculate metrics
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)

f1 = f1_score(y_true, y_pred)

print("Accuracy", accuracy)
print("PRecision:", precision)
print("F1 score:",f1)