from django.contrib import admin

from .models import Question,Choice

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to Admin Area"

class ChoiceInline(admin.TabularInline):
    model =  Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ('question_text',)}), ('Date Information',{"fields":('pub_date',), "classes":('collapse',"wide",'extrapretty',)}) )
    inlines = [ChoiceInline]
    


admin.site.register(Question, QuestionAdmin)



# fieldsets can be omitted
# Notice that "fields" tuples take an ending comma. would throw an error otherwise.
# Tuples ; () can be replaced with lists ; []