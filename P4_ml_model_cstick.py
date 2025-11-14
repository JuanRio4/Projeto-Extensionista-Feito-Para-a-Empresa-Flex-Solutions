
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Para rodar no Google Colab, você pode precisar fazer upload do arquivo cStick.csv
# ou montar o Google Drive se o arquivo estiver lá.
# from google.colab import files
# uploaded = files.upload()
df = pd.read_csv("cStick.csv")

# Exibir as primeiras linhas do dataset e informações básicas
print("Primeiras 5 linhas do dataset:")
print(df.head())
print("\nInformações do dataset:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificar valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# Imprimir nomes das colunas para depuração
print("\nNomes das colunas:")
print(df.columns)

# Separar features (X) e target (y)
# A coluna alvo é 'Decision ' (com espaço no final)
X = df.drop("Decision ", axis=1)
y = df["Decision "]

# Padronizar as features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

## 1. Support Vector Machine (SVM)

# Inicializar e treinar o modelo SVM
svm_model = SVC(kernel="rbf", random_state=42)
svm_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred_svm = svm_model.predict(X_test)

# Avaliar o modelo SVM
print("\n--- Avaliação do Modelo SVM ---")
print("Matriz de Confusão SVM:")
print(confusion_matrix(y_test, y_pred_svm))
print("\nRelatório de Classificação SVM:")
print(classification_report(y_test, y_pred_svm))

# Visualização da Matriz de Confusão SVM
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred_svm), annot=True, fmt="d", cmap="Blues")
plt.title("Matriz de Confusão do SVM")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()

## 2. k-Nearest Neighbors (k-NN)

# Inicializar e treinar o modelo k-NN
knn_model = KNeighborsClassifier(n_neighbors=5) # k=5 é um valor comum, pode ser otimizado
knn_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred_knn = knn_model.predict(X_test)

# Avaliar o modelo k-NN
print("\n--- Avaliação do Modelo k-NN ---")
print("Matriz de Confusão k-NN:")
print(confusion_matrix(y_test, y_pred_knn))
print("\nRelatório de Classificação k-NN:")
print(classification_report(y_test, y_pred_knn))

# Visualização da Matriz de Confusão k-NN
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt="d", cmap="Greens")
plt.title("Matriz de Confusão do k-NN")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()

## 3. Regressão Logística

# Inicializar e treinar o modelo de Regressão Logística
# solver='liblinear' é bom para datasets pequenos e para problemas multiclasse
logreg_model = LogisticRegression(solver="liblinear", random_state=42, multi_class="ovr")
logreg_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred_logreg = logreg_model.predict(X_test)

# Avaliar o modelo de Regressão Logística
print("\n--- Avaliação do Modelo de Regressão Logística ---")
print("Matriz de Confusão Regressão Logística:")
print(confusion_matrix(y_test, y_pred_logreg))
print("\nRelatório de Classificação Regressão Logística:")
print(classification_report(y_test, y_pred_logreg))

# Visualização da Matriz de Confusão Regressão Logística
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred_logreg), annot=True, fmt="d", cmap="Reds")
plt.title("Matriz de Confusão da Regressão Logística")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.show()

## 4. K-Fold Cross-Validation

# Configurar K-Fold Cross-Validation
num_folds = 5 # Número de folds, um valor comum
kf = KFold(n_splits=num_folds, shuffle=True, random_state=42)

print("\n--- K-Fold Cross-Validation ---")

# Avaliação do SVM com K-Fold
svm_scores = cross_val_score(SVC(kernel="rbf", random_state=42), X_scaled, y, cv=kf, scoring="accuracy")
print(f"Acurácia do SVM (K-Fold): {svm_scores.mean():.4f} (+/- {svm_scores.std():.4f})")

# Avaliação do k-NN com K-Fold
knn_scores = cross_val_score(KNeighborsClassifier(n_neighbors=5), X_scaled, y, cv=kf, scoring="accuracy")
print(f"Acurácia do k-NN (K-Fold): {knn_scores.mean():.4f} (+/- {knn_scores.std():.4f})")

# Avaliação da Regressão Logística com K-Fold
logreg_model = LogisticRegression(solver="liblinear", random_state=42, multi_class="ovr")
logreg_scores = cross_val_score(logreg_model, X_scaled, y, cv=kf, scoring="accuracy")
print(f"Acurácia da Regressão Logística (K-Fold): {logreg_scores.mean():.4f} (+/- {logreg_scores.std():.4f})")

# Comparativo de Acurácias
models = ["SVM", "k-NN", "Regressão Logística"]
accuracies = [svm_scores.mean(), knn_scores.mean(), logreg_scores.mean()]
std_devs = [svm_scores.std(), knn_scores.std(), logreg_scores.std()]

plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, yerr=std_devs, capsize=5, color=["blue", "green", "red"])
plt.ylabel("Acurácia Média")
plt.title("Comparativo de Acurácia Média com K-Fold Cross-Validation")
plt.ylim(0.8, 1.05) # Ajustar limite para melhor visualização
plt.show()


