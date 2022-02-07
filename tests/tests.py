from wrappers.portal_api import users_api
from wrappers.portal_page_objects import login_page

users_api.dev_specific_delete_user("Matt")
users_api.add_user("George")
login_page.login("Alex")
login_page.dev_specific_logout("Maryana")