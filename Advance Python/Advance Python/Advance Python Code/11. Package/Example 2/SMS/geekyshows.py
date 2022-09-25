# geekyshows Module

# Accessing service module from Admin Package
from Admin import service
service.admin_service()

# Accessing product module from Admin Package
from Admin import product
product.admin_product()

# Accessing header module from Admin Package --> Common Package
from Admin.Common import header
header.admin_common_header()

# Accessing footer module from Admin Package --> Common Package
from Admin.Common import footer
footer.admin_common_footer()

# Accessing profile module from Tech Package
from Tech import profile
profile.tech_profile()

# Accessing work module from Tech Package
from Tech import work
work.tech_work()

# Accessing profile module from User Package
from User import profile
profile.user_profile()

# Accessing request module from User Package
from User import request
request.user_request()

