# https://www.youtube.com/watch?v=Fsua5eN5wSc
"""
ADB инструменты для тестировщика:
1. Эмулятор
        1. - Эмулируем смартфон на компьютере - необходимы хорошие технические характеристики компа.


2. LogCat -> также вкладка в АндроидСтудио
        1. - снятие логов
        2. - нужна специальная версия мобильного приложения

1. AndroidManifest.xml - фал на платформе андроид - описаны функциональные возможности и
   требования приложения к Android
2. Настройки безопасности для установки приложения - получить разрешение
3. Отладка по USB
4. Включить режим разработчика:
   Настройки - Сведения ПО - 7 Тап по Номер сборки - включить отладку по USB
5. Поиск по логам - Ctrl + F
"""

"""
Операционная система «Andriod» имеет встроенный компонент «WebView», позволяющий встраивать веб-страницы в 
мобильные приложения. На основе данной технологии осуществляется быстрая сборка гибридных Android-приложений, 
использующих в качестве источника контента мобильную версию сайта. 

Activity — это фундаментальный компонент каждого Android-приложения. Через этот компонент происходит взаимодействие 
между пользователем и приложением. При помощи него пользователь телефона может «путешествовать» между окнами 
приложения или между разными приложениями.

Порядок вызовов

После onCreate() - onStart()
После onRestart() - onStart()
После onStart() - onResume() или onStop()
После onResume() - onPause()
После onPause() - onResume() или onStop()
После onStop() - onRestart() или onDestroy()
После onDestroy() - ничего
"""

# https://infoit.com.ua/linux/kak-ustanovit-adb-i-fastboot-na-ubuntu-20-04-lts/

"""
install ADB ubuntu
1. sudo apt install android-tools-adb
2. sudo apt install android-tools-fastboot
3. adb version
4. sudo adb devices
"""


# https://www.youtube.com/watch?v=HHN4jFY_Wjs
"""
1. lsusb -> смотреть все устройства подключенные по USB
2. подключаем телефон - берем id телефона
3. редактируем правила -> файл - вставляем id телефона
4. adb devices -> телефон должен отобразиться
"""


# https://dev.to/plotegor/adb-fastboot-3mgf
"""
Команды ADB
    adb devices – вывод списка подключенных устройств;
    adb reboot – перезагрузка устройства;
    adb reboot recovery – перезагрузка устройства в режим восстановления (recovery);
    adb reboot bootloader – перезагрузка устройства в режим fastboot для дальнейшего выполнения fastboot-команд;
    adb install app.apk – установка приложения на карту памяти (необходимо предварительно загрузить .apk-файл 
                          в папку с ADB либо указать полный путь к нему);
    adb install -f app.apk – установка приложения во внутреннюю память;
    adb install -t app.apk – установка приложения для тестирования;
    adb install -r app.apk – переустановка приложения с сохранением пользовательских данных;
    adb uninstall com.app.example – удаление приложения;
    adb shell – вызов консоли Android (shell) для выполнения Linux-команд;
    adb shell screencap /sdcard/screenshot.png – создание скриншота (больше подробностей в написанном мною руководстве 
                                                 по созданию скриншотов на смартфонах Samsung);
    adb shell screenrecord /sdcard/video.mp4 – запись скринкаста (захват изображения с экрана);
    adb shell dumpsys package com.app.example – вывод информации о приложении;
    adb shell pm list packages – вывод списка установленных приложений;
    adb shell pm grant com.app.example android.permission.SEND_SMS – выдача разрешения приложению 
                                                                     (в конкретном случае на отправку сообщений);
    adb shell pm revoke com.app.example android.permission.CAMERA – блокировка доступа приложению 
                                                                    (в конкретном случае к камере);
    adb backup -apk -shared -all -f C:\backup.ab – создание резервной копии данных, включая установленные приложения и 
                                                   файлы, хранящиеся на карте памяти (имя файла создаваемого бэкапа и 
                                                   путь к нему можно изменить);
    adb restore C:\backup.ab – восстановление данных из созданной резервной копии;
    adb tcpip 5555 – установка соединения по протоколу TCP/IP через порт 5555;
    adb connect 192.168.0.100 – подключение к устройству (узнать IP-адрес устройства можно в 
                                                          настройках в разделе «О телефоне»);
    adb disconnect 192.168.0.100 – отключение от устройства;
    adb sideload /sdcard/firmware.zip – установка прошивки, когда устройство загружено в recovery;
    adb push C:\app.apk /sdcard/Download – отправка файла с компьютера на смартфон (возможна отправка каталогов);
    adb pull /sdcard/video.mp4 C:\Users\Overclocker\Downloads – копирование файла с компьютера на 
                                                                смартфон (возможно копирование каталогов);
    adb start-server – перезапуск демона;
    adb kill-server – остановка демона.

Команды Fastboot
    fastboot devices – вывод списка подключенных устройств, загруженных в режиме fastboot;
    fastboot reboot – перезагрузка устройства, запуск Android;
    fastboot reboot recovery – перезагрузка устройства в режим восстановления (recovery);
    fastboot oem device-info – проверка состояния загрузчика;
    fastboot oem unlock – разблокировка загрузчика на старых устройствах, например, на всех моделях Google Nexus;
    fastboot flashing unlock – разблокировка загрузчика на новых устройствах, например, на всех моделях Google Pixel;
    fastboot oem unlock **************** – разблокировка загрузчика на устройствах, которые требуют прохождения 
                                           процедуры получения кода. К таким устройствам относятся смартфоны и планшеты 
                                           Xiaomi, Sony, HTC, Huawei, Honor и многих других производителей. Количество 
                                           символов в коде подтверждения может отличаться;
    fastboot oem lock – блокировка загрузчика на старых устройствах;
    fastboot flashing lock – блокировка загрузчика на новых устройствах;
    fastboot oem relock **************** – блокировка загрузчика на устройствах, которые требуют прохождения 
                                           процедуры получения кода;
    fastboot getvar all – вывод технической информации об устройстве, которая включает данные об IMEI, серийном номере, 
                          версии загрузчика, состоянии батареи и прочие сведения.

Очистка разделов перед прошивкой:
    fastboot erase system;
    fastboot erase userdata;
    fastboot erase recovery;
    fastboot erase boot;
    fastboot erase cache;
    fastboot erase radio;
    fastboot -w – сброс настроек, очистка раздела /data.

Прошивка разделов:
    fastboot flash system system-filename.img;
    fastboot flash userdata userdata-filename.img;
    fastboot flash recovery recovery-filename.img;
    fastboot flash boot boot-filename.img;
    fastboot flash cache cache-filename.img;
    fastboot flash radio radio-filename.img;
    flash-all – прошивка всех разделов (необходимо предварительно загрузить файлы прошивки в папку с Fastboot, при этом 
                среди них должен быть .bat-файл с названием flash-all);
    fastboot flashall – аналогичная предыдущей команда;
    fastboot update firmware-filename.zip – установка прошивки в формате .zip.
"""

"""
Fastboot отличается от ADB тем, что fastboot работает на более низком уровне (более низкий уровень означает большую 
близость к железу устройства, к фундаментальному уровню) и чтобы работать с ним, вам будет необходимо, 
в отличие от ADB, перейти в особый режим.
"""

# https://www.youtube.com/watch?v=5CSK_SAFGsA
"""
Логирование:
    1. Verbose - дебаг - инфо - ассерты - видим все
       - подключаем устройство по USD + переводим в режим разработчика
       - выбираем необходимое устройство
       - логи в файл - сохраняем
       
    2. через терминал
       - переходим в папку (где приложение)
       - ./adb -> смотрим команды
       - ./abd devices -> смотрим все подключенные девайсы
       - ./abd logcat -d -v time > ./log.txt -> создаем файл для логов  
       - ./adb logcat -c -> очищаем логи
       - ./adb -s [name of device] logcat -> смотрим все логи устройства - логи выводятся в консоль
"""