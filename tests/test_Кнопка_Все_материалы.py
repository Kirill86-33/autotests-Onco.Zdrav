class TestMaterialsPage:
    
    def test_all_materials(self, all_materials ):  
        all_materials.open()
        all_materials.click_button_all_materials()