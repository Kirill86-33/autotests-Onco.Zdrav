from testit_python_commons.decorators import externalId, displayName
class TestMaterialsPage:
    @externalId("test_all_materials")
    @displayName("Кнопка 'Все материалы'")
    def test_all_materials(self, all_materials ):  
        all_materials.open()
        all_materials.click_button_materials()