"Aplikasi Spam Email Detector menggunakan Algoritma Support Vector Machine (SVM)"

A. Kode Program kami menggunakan bahasa pemrograman Python dan library scikit-learn untuk implementasi algoritma SVM sekaligus mengintegrasikan dengan aplikasi GUI menggunakan library Tkinter.kode program kami bisa diakses melalui link berikut:

untuk menjalankan aplikasi ini, silakan mengikuti langkah-langkah berikut:
1. pada terminal powershell , ketikkan perintah "venv\Scripts\activate" agar dependensi yang diperlukan bisa dijalankan, kemudian enter. Setelah dienter, maka pada terminal muncul (venv) sebelum folder projek kita contohnya (venv) PS C:\ml>. 
2. Karena kami sudah menguji data emailnya dengan perintah pada terminal yaitu "python model.py" untuk melatih model dari email_spam_indo.csv, maka keluarlah file baru yaitu spam_classifier_svm.pkl dan vectorizer.pkl. Barulah kita menuju ke aplikasinya
3. ketikkan kembali diterminal powershell dengan ada  (venv) PS C:\ml> ketik "python main.py" kemudian muncullah aplikasi GUI yang sudah kita buat. Silakan mengisi form dengan email yang ingin diuji. dan tekan tombol "Detect" untuk mendapatkan hasil prediksi. Jika email tersebut adalah spam, maka akan muncul tulisan "Result : spam" dengan tulisan warna merah dan jika email tersebut bukan spam, maka akan muncul tulisan "Result : not spam" dengan tulisan warna hijau. 
4. Jika ingin menguji email masuk yang lain bisa menekan tombol refresh untuk mengosongkan form dan mengisi kembali email yang ingin diuji.

B. Data yang kami gunakan adalah dataset email_spam_indo.csv yang dapat diakses melalui link berikut:

https://www.kaggle.com/datasets/gevabriel/indonesian-email-spam/data

C. Screenshot implementasi dalam bentuk program berbasis GUI. Untuk Source Kode Program kami dan Screenshot implementasi dalam bentuk program berbasis GUI bisa diakses melalui link berikut:

