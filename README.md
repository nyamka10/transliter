# Инструкция для установки и запуска скриптов на windows

Запустить powershell

```powershell
wsl --install
```

Устанавливаем дистрибутив Ubuntu

```powershell
wsl.exe --install Ubuntu-22.04
```

Запустить обновление wsl

```powershell
wsl --update
```

Перезагружаем систему

Далее запускаем приложение Ubuntu из поиска

и вводим имя пользователя и пароль

Сощдаем виртуальное окружение

```powershell
python3 -m venv venv
```

Если выдает ошибку то выполняем следующий код построчно

```bash
sudo umount /mnt/c
sudo mount -t drvfs C: /mnt/c -o metadata
sudo apt install python3-venv
python3 -m venv venv
chmod +x main.py
```

Запускаем программу
