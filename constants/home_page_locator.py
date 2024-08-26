from selenium.webdriver.common.by import By

BASE_URL = "https://www.dr.com.tr/"

COOKIES = (By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
ELECTRONIC_CATALOG_HOVER = (By.CSS_SELECTOR,"li:nth-of-type(3) > .pointer-events-auto > span")
SUBCATEGORY = (By.CSS_SELECTOR,"li:nth-of-type(3) > .sub-menu  .sub-menu-wrapper > ul > li:nth-of-type(1) > a[target='_self']")
SUBCATEGORY_TEXT = (By.CSS_SELECTOR,".breadcrumb.js-breadcrumb-list.pt-20 > .font-weight-bold")
FIRST_PRODUCT = (By.CSS_SELECTOR,".facet__products-list.js-facet-product-list > div:nth-of-type(1) .js-prd-img-first")
FIRST_PRODUCT_PAGE_CONTROL = (By.CSS_SELECTOR,".d-block.font-weight-600.mb-10.w-100")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,".btn.col-12.d-block.fs-5.js-add-basket.js-btn-detail-basket.py-10.text-c255.text-center")
ADD_TO_CART_ITEM_CONTROL = (By.CSS_SELECTOR,".basket-modal__title.fs-5.js-popup-title.text-center")
GO_TO_CART_BUTTON = (By.LINK_TEXT,"Sepete Git")