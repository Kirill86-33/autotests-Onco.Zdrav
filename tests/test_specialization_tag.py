from testit_python_commons.decorators import externalId, displayName
class TestBlockSpecialization:
    @externalId("test_block_specialization")
    @displayName("Блок специализации")
    def test_block_specialization(self, teg_block_specialization ):  
        teg_block_specialization.open()
        teg_block_specialization.click_tag()