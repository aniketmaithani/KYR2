# Third Party Stuff
from django.contrib import admin

from .models import Complaints


class ComplaintsAdmin(admin.ModelAdmin):

    '''
    Admin View for Complaints
    '''
    list_display = ('name_of_the_complainee', 'phone_number_of_the_complainee',
                    'description_of_the_problem', 'name_of_the_mp_for_problem_redressal', 'unique_complain_id')
    list_filter = ('unique_complain_id', )
    search_fields = ['name_of_the_complainee', 'phone_number_of_the_complainee',
                     'description_of_the_problem', 'name_of_the_mp_for_problem_redressal', 'unique_complain_id', ]

admin.site.register(Complaints, ComplaintsAdmin)
