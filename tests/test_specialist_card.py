from testit_python_commons.decorators import externalId, displayName
class TestCartSpecialistsPage:
    @externalId("test_cart")
    @displayName("Карточка специалиста")
    def test_cart(self, cart_specialists ):  
        cart_specialists.open()
        cart_specialists.click_cart_specialists()
       