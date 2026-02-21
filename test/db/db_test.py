import allure

from db.db_functions import *


def preparing():
    if select_by_id(id=11) is not None:
        delete_by_id(id=11)
    create_new(id=11, name='санаторий парус 2', image='accommodation_img/parus_80MrPZw.jpg',
               short_desc='анапский санаторий с романтичным названием «Парус', description='большое описание',
               availability=20, price=2000, room_desc='описание номера', is_active=1, country_id=1, region_id=1)


@allure.title("Проверка создания записи")
def test_create_row():
    preparing()
    row = select_by_id(id=11)
    delete_by_id(id=11)
    assert row


# def test_accomodation_delete():
#     preparing()
#     result_before = select_all()
#     delete_by_id(id=11)
#     result_after = select_all()
#     delete_by_id(id=11)
#     assert len(result_before) != len(result_after)
#
#
# def test_accomodation_update():
#     preparing()
#     row_before = select_by_id(id=11)
#     update_by_id(name='санаторий парус 3', id=11)
#     row_after = select_by_id(id=11)
#     delete_by_id(id=11)
#     assert row_before['name'] != row_after['name']
#
#
# def test_active_accomodations():
#     result = select_all()
#     lst = [el['is_active'] for el in result]
#     assert 0 not in lst
#
#
# def test_select_by_id():
#     assert select_by_id(id=1) is not None
#
#
# def test_select_by_id_not():
#     assert select_by_id(id=11) is None
