Чтобы установить *пакет* нужно:
1. Открыть командную строку.
2. Ввести команду: **pip install git+https://github.com/Alexzhyliuk/my_project.git**.
3. Убедитесь, что пакет установлен: **pip freeze**. Если в списке есть **-e git+https://github.com/Alexzhyliuk/my_project.git@df4a2710a7645f13e40200b3dc00356859d51870#egg=cardsgames**, значит пакет установлен.
4. Чтобы использовать его в коде нужно импортирова модули из cardsgames: **from cardsgames import set_game**
5. Чтобы импортировать тесты нужно импортировать их из tests: **from tests import test_set_game**


| Функция                 | Описание        |
| ----------------------- |:---------------:|
| set_game.check_set      | проверяет сет   |
| set_game.create_cards   | создает карточки|
