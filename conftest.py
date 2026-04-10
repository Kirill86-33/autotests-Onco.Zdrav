import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()



@pytest.fixture
def search_page (driver):
    from pages.main_search import SearchField
    return SearchField (driver)


@pytest.fixture
def side_button (driver):
    from pages.side_menu import SideButton
    return SideButton (driver)



@pytest.fixture
def card_question_answer (driver):
    from pages.qa_map import QuestionAnswer
    return QuestionAnswer (driver)


@pytest.fixture
def chapter_service (driver):
    from pages.service_page import ChapterService
    return ChapterService (driver)



@pytest.fixture
def chapter_onco_atlas (driver):
    from pages.atlas_man import ChapterAtlasOnco
    return ChapterAtlasOnco (driver)



@pytest.fixture
def info_woman_onco_atlas (driver):
    from pages.atlas_woman import WomanAtlasOnco
    return WomanAtlasOnco (driver)


@pytest.fixture
def medical_organizations_search (driver):
    from pages.clinics_search import MedicalOrganizationsSearch
    return MedicalOrganizationsSearch (driver)


@pytest.fixture
def medical_organizations (driver):
    from pages.medical_organizations import MedicalOrganizations
    return MedicalOrganizations (driver)


@pytest.fixture
def medical_organizations_search_city (driver):
    from pages.clinics_city_search import MedicalSearchCity
    return MedicalSearchCity (driver)


@pytest.fixture
def teg_block_specialization (driver):
    from pages.specialization_tag import TegSpecializations
    return TegSpecializations (driver)


@pytest.fixture
def teg_block_med_diagnostics (driver):
    from pages.diagnostics_tag import TegMedicalDiagnostics
    return TegMedicalDiagnostics (driver)



@pytest.fixture
def button_lpu (driver):
    from pages.lpu_clinics import ButtonLpu
    return ButtonLpu (driver)



@pytest.fixture
def chapter_specialists (driver):
    from pages.specialists_page import Specialists
    return Specialists (driver)


@pytest.fixture
def cart_specialists (driver):
    from pages.specialist_card import SpecialistsCart
    return SpecialistsCart (driver)


@pytest.fixture
def doctors_search_city (driver):
    from pages.specialists_city_search import DoctorsSearchCity
    return DoctorsSearchCity (driver)



@pytest.fixture
def doctors_search (driver):
    from pages.specialists_search import DoctorsSearch
    return DoctorsSearch (driver)


@pytest.fixture
def doctors_search_clinic (driver):
    from pages.specialists_clinic_search import DoctorsSearchClinic
    return DoctorsSearchClinic (driver)


@pytest.fixture
def video_page (driver):
    from pages.video_card import VideoPage
    return VideoPage (driver)


@pytest.fixture
def all_materials (driver):
    from pages.all_materials_button import AllMaterials
    return AllMaterials (driver)



@pytest.fixture
def sort_by_name (driver):
    from pages.video_sort_by_name import SortByName
    return SortByName (driver)


@pytest.fixture
def video_button_new (driver):
    from pages.video_new_button import VideoButtonNewPage
    return VideoButtonNewPage (driver)


@pytest.fixture
def video_search_page  (driver):
    from pages.video_search import VideoSearchPage
    return VideoSearchPage (driver)


@pytest.fixture
def teg_block_topic (driver):
    from pages.video_topic_tag import TegTopic
    return TegTopic (driver)


@pytest.fixture
def all_news (driver):
    from pages.news_page import AllNewsPage
    return AllNewsPage (driver)


@pytest.fixture
def button_see_all (driver):
    from pages.news_watch_all_button import ButtonSeeAll
    return ButtonSeeAll (driver)


@pytest.fixture
def search_news (driver):
    from pages.news_search import NewsSearchPage
    return NewsSearchPage (driver)


@pytest.fixture
def teg_new (driver):
    from pages.news_tags import TegNewsPage
    return TegNewsPage (driver)


@pytest.fixture
def button_show_all(driver):
    from pages.news_show_all_button import ButtonShowAll
    return ButtonShowAll (driver)



@pytest.fixture
def button_subscribe (driver):
    from pages.news_subscribe_button import ButtonSubscribe
    return ButtonSubscribe (driver)
