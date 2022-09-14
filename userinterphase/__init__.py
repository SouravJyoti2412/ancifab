# default_app_config = 'UserInterphase.apps.UserInterphaseConfig'
# from django.contrib import admin
# from django.contrib.admin import sites

# class USER_INTERPHASE(admin.AdminSite):
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#             "About_us_heading": 1,
#             "About_us_content": 2,
#             "Faqs": 3,
#             "Terms_and_Condition": 4,
#             "Return_refund_policy":5,
#             "contact_details_section":6,
#             "home_carousel":8,
#             "home_collection_banner":9,
#             "All_banner":10
#         }

#         app_dict = self._build_app_dict(request)
#         # a.sort(key=lambda x: b.index(x[0]))
#         # Sort the apps alphabetically.
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

#         # Sort the models alphabetically within each app.
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])

#         return app_list

# mysite = USER_INTERPHASE()
# admin.site = mysite
# sites.site = mysite