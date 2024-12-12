import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

# 1. Load Dataset
data = pd.read_csv('email_spam_indo.csv', delimiter=',', encoding='utf-8')

# 2. Preprocessing
data = data[data['Kategori'].isin(['spam', 'ham'])]
data['Kategori'] = data['Kategori'].map({'spam': 1, 'ham': 0})  # Spam = 1, Ham = 0

# Pisahkan fitur dan label
X = data['Pesan']
y = data['Kategori']

# 3. Text Vectorization
vectorizer = CountVectorizer(stop_words=None)  # Tidak menggunakan stop words karena bahasa Indonesia
X_vectorized = vectorizer.fit_transform(X)

# 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# 5. Train SVM Model
model = SVC(kernel='linear', C=1)
model.fit(X_train, y_train)

# 6. Evaluate Model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# 7. Save Model and Vectorizer
joblib.dump(model, 'spam_classifier_svm.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved successfully!")