# geekyshows Module

# Accessing service module from Admin Package
import Admin.service
Admin.service.admin_service()

# Accessing product module from Admin Package
import Admin.product
Admin.product.admin_product()

# Accessing header module from Admin Package --> Common Package
import Admin.Common.header
Admin.Common.header.admin_common_header()

# Accessing footer module from Admin Package --> Common Package
import Admin.Common.footer
Admin.Common.footer.admin_common_footer()

# Accessing profile module from Tech Package
import Tech.profile
Tech.profile.tech_profile()

# Accessing work module from Tech Package
import Tech.work
Tech.work.tech_work()

# Accessing profile module from User Package
import User.profile
User.profile.user_profile()

# Accessing request module from User Package
import User.request
User.request.user_request()

