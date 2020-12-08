# task 2.2.2 Работа с кодом: модули и импорт
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода
# simplecrypt.encrypt.
# Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать,
# какой из паролей служит ключом для расшифровки файла с интересной информацией.
# Ответом для данной задачи служит расшифрованная интересная информация Алисы.
from simplecrypt import decrypt
# with open("passwords.txt", "r") as inf_password:
#     passwords = inf_password.read().split('\n')
with open("encrypted.bin", "rb") as inf_data:
    encrypted = inf_data.read()
# for password in passwords:
password = 'RVrF2qdMpoq6Lib'
print(decrypt(password, encrypted))
