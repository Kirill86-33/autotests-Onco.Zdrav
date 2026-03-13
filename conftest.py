import pytest
from selenium import webdriver
from pages.Поле_Поиск_Главная_страница import SearchField
from pages.Боковая_кнопка_для_карточек import SideButton
from pages.Карта_вопрос_ответ import QuestionAnswer
from pages.Раздел_Услуга import ChapterService
from pages.Раздел_Атлас_Онко_Мужчина import ChapterAtlasOnco
from pages.Раздел_Атлас_Онко_Женщина import WomanAtlasOnco
from pages.Раздел_Мед_Организации_поле_Поиск import MedicalOrganizationsSearch
from pages.Раздел_Медицинские_организации import MedicalOrganizations
from pages.Раздел_Мед_Организации_поле_Поиск_по_городу import MedicalSearchCity
from pages.Раздел_Мед_Организация_тег_Специализация import TegSpecializations
from pages.Раздел_Мед_Организация_тег_Метод_диагностики import TegMedicalDiagnostics
from pages.Раздел_Мед_Организации_ЛПУ import ButtonLpu
from pages.Раздел_Специалисты import Specialists
from pages.Раздел_Специалисты_карточка_Специалиста import SpecialistsCart
from pages.Раздел_Специалисты_поле_Поиск_по_городу import DoctorsSearchCity
from pages.Раздел_Специалисты_поле_Поиск import DoctorsSearch
from pages.Раздел_Специалисты_поле_Поиск_по_клинике import DoctorsSearchClinic
from pages.Просмотр_видео import VideoPage
from pages.Кнопка_Все_материалы import AllMaterials
from pages.Видео_Сортировка_по_Названию import SortByName
from pages.Раздел_Видео_кнопка_Новинки import VideoButtonNewPage
from pages.Раздел_Видео_поле_Поиск import VideoSearchPage
from pages.Раздел_Видео_тег_Тема import TegTopic
from pages.Раздел_Все_новости import AllNewsPage
from pages.Раздел_Все_новости_кнопка_Смотреть_все import ButtonSeeAll
from pages.Раздел_Все_новости_поле_Поиск import NewsSearchPage
from pages.Раздел_Все_новости_блок_Теги import TegNewsPage
from pages.Раздел_Все_новости_кнопка_Показать_все import ButtonShowAll
from pages.Раздел_Все_новости_кнопка_Подписаться import ButtonSubscribe







@pytest.fixture # Общие настройки экрана для всех фикстур
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    return SearchField(driver)


@pytest.fixture
def side_button(driver):
    return SideButton(driver)


@pytest.fixture
def card_question_answer(driver):
    page = QuestionAnswer(driver) 
    page.open()
    return page


@pytest.fixture
def chapter_service(driver):
    return ChapterService(driver)


@pytest.fixture
def chapter_onco_atlas(driver):
    return ChapterAtlasOnco(driver)


@pytest.fixture
def info_woman_onco_atlas(driver):
    return WomanAtlasOnco(driver)


@pytest.fixture
def medical_organizations_search(driver):
    return MedicalOrganizationsSearch (driver)


@pytest.fixture
def medical_organizations(driver):
    return MedicalOrganizations (driver)



@pytest.fixture
def medical_organizations_search_city(driver):
    return MedicalSearchCity (driver)



@pytest.fixture
def teg_block_specialization(driver):
    return TegSpecializations (driver)


@pytest.fixture
def teg_block_med_diagnostics(driver):
    return TegMedicalDiagnostics (driver)


@pytest.fixture
def button_lpu(driver):
    return ButtonLpu(driver)


@pytest.fixture
def chapter_specialists(driver):
    return Specialists(driver)


@pytest.fixture
def cart_specialists(driver):
    return SpecialistsCart(driver)


@pytest.fixture
def doctors_search_city(driver):
    return DoctorsSearchCity(driver)


@pytest.fixture
def doctors_search(driver):
    return DoctorsSearch(driver)


@pytest.fixture
def doctors_search_clinic(driver):
    return DoctorsSearchClinic(driver)


@pytest.fixture
def video_page(driver):
    return VideoPage(driver)


@pytest.fixture
def all_materials(driver):
    return AllMaterials(driver)


@pytest.fixture
def sort_by_name(driver):
    return SortByName(driver)


@pytest.fixture
def video_button_new (driver):
    return VideoButtonNewPage(driver)


@pytest.fixture
def video_search_page (driver):
    return VideoSearchPage(driver)


@pytest.fixture
def teg_block_topic(driver):
    return TegTopic(driver)


@pytest.fixture
def all_news(driver):
    return AllNewsPage(driver)


@pytest.fixture
def button_see_all(driver):
    return ButtonSeeAll(driver)


@pytest.fixture
def search_news(driver):
    return NewsSearchPage(driver)


@pytest.fixture
def teg_new(driver):
    return TegNewsPage(driver)


@pytest.fixture
def button_show_all(driver):
    return ButtonShowAll(driver)


@pytest.fixture
def button_subscribe(driver):
    return ButtonSubscribe(driver)