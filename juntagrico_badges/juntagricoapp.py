from juntagrico.util import addons
import juntagrico_badges


addons.config.register_user_menu('jbg/menu.html')
addons.config.register_admin_menu('jbg/admin_menu.html')
addons.config.register_version(juntagrico_badges.name, juntagrico_badges.version)
