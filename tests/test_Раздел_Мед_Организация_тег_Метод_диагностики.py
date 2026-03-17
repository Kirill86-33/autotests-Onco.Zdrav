from testit_python_commons.decorators import externalId, displayName
class TestBlockMedDiagnostics:
    @externalId("test_block_med_diagnostics")
    @displayName("Блок методов диагностики")
    def test_block_med_diagnostics(self, teg_block_med_diagnostics):  
        teg_block_med_diagnostics.open()
        teg_block_med_diagnostics.click_button_block_diagnostics()