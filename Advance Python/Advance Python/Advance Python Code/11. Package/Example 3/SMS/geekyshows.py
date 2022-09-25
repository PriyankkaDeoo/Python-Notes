# geekyshows Module

# Accessing service module's function from Admin Package
from Admin.service import admin_service
admin_service()

# Accessing product module's function from Admin Package
from Admin.product import admin_product
admin_product()

# Accessing header module's function from Admin Package --> Common Package
from Admin.Common.header import admin_common_header
admin_common_header()

# Accessing footer module's function from Admin Package --> Common Package
from Admin.Common.footer import admin_common_footer
admin_common_footer()

# Accessing profile module's from Tech Package
from Tech.profile import tech_profile
tech_profile()

# Accessing work module's function from Tech Package
from Tech.work import tech_work
tech_work()

# Accessing profile module's function from User Package
from User.profile import user_profile
user_profile()

# Accessing request module from User Package
from User.request import user_request
user_request()

