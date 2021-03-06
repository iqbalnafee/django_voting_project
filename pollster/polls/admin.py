from django.contrib import admin

from .models import Question, choice

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"  # browser tab site_title
admin.site.index_title = "Welcome to the Pollster admin area"

# To show choices below Questions in admin side


class ChoiceBelowQuestion(admin.TabularInline):
    model = choice
    extra = 3  # number of choices


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets consists of tuples
    fieldsets = [

        # tuple structure: first parameter is name of tuple,2nd param is an object with actual field name
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']})



    ]
    inlines = [ChoiceBelowQuestion]


# Register your models here.

admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(choice)
