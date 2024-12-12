import tkinter as tk
from tkinter import messagebox
import joblib


model = joblib.load('spam_classifier_svm.pkl') 
vectorizer = joblib.load('vectorizer.pkl')  


def predict_spam():
    email = email_text.get("1.0", tk.END) 
    if email.strip() == "":
        messagebox.showwarning("Input Error", "Harap masukkan konten email!")
        return

    vectorized_email = vectorizer.transform([email])
    prediction = model.predict(vectorized_email)[0]

    result = 'Spam' if prediction == 1 else 'Not Spam'
    result_label.config(text=f"Result: {result}", fg="green" if result == 'Not Spam' else "red")

def refresh():
    email_text.delete("1.0", tk.END)  
    result_label.config(text="Result: ", fg="black")  


root = tk.Tk()
root.title("Spam Email Detector")
root.geometry("500x400")


title_label = tk.Label(root, text="Spam Email Detector", font=("Arial", 16))
title_label.pack(pady=10)


email_text = tk.Text(root, height=10, width=50)
email_text.pack(pady=10)

detect_button = tk.Button(root, text="Detect", command=predict_spam, bg="green", fg="white", font=("Arial", 14))
detect_button.pack(pady=10)



refresh_button = tk.Button(root, text="Refresh", command=refresh, bg="blue", fg="white", font=("Arial", 14))
refresh_button.pack(pady=5)


result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)


root.mainloop()
