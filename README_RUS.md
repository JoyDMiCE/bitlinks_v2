##  Что за программа
   ### Это программа делает битлинки, может посчитать клики по **_БИТЛИНКАМ_**

## Окружение
   Требования к окружению можете посмотреть в requirements.txt, если вы не видете файл *.env* - это нормально ведь, он скрыт от вас(там хранится токен для программы), *requests* - нужен, чтобы делать _битлинки_.

## Как начать
   Что бы запустить программу надо написать в консоль (terminal)
```
   python main.py "ссылка"
```
   .

### Примеры
   Пример:
                                          ```
   python main.py https://dvmn.org/modules
                                          ```
    - будет выводить битлинк(ссылку можно поменять).

   Получаем: `bit.ly/3bKvkyD`.

   (_Вы можете сами проверить работает-ли ссылка_).

   2. Пример: 
```
      python main.py bit.ly/3bKvkyD
``` 
- посчитает сколько кликов было сделано по БИТЛИНКУ, который вы сделали сверху.

   Получаем: `bit.ly/3bKvkyD.
   1`
### Bitly токен

Если вы не любите читать то вот видеогайд - https://www.youtube.com/watch?v=6fNButYLNyM

Чтобы получить bitly токен(который вам понадобится).

Заходите на сайт https://bitly.com/ 

После чего, регистрируйтесь.

Найдите свою иконку(она справа сверху) и кликните по ней.

|--- Profile Settings ----- GENERIC ACCESS TOKEN и водите там свой пароль.

Теперь нажимайте на оранжевую кнопку "GENERIC TOKEN".

Вам выдало токен который вы копируете и вставляете(пример: sd7f87hhjd9ffj454jjef8884s3).

Заходите в папку проекта(bitlinks_v2).

И создавайте файл .env.

Заходите через него любым редактором которой вам удобен.

   *И ПИШИТЕ РОВНО ТАК КАК НАПИСАНО ТУТ*.
   
   ```
   BITLY_TOKEN=sd7f87hhjd9ffj454jjef8884s3
   ```
(токен который у вас).
   
   Поздравляем, теперь у вас всё работает.
