from django.contrib import admin
from .models import LabourUser,NormalUser,ProductImage,ServiceImage,questions,quiz,Answer

admin.site.register(LabourUser)
admin.site.register(NormalUser)
admin.site.register(ProductImage)
admin.site.register(ServiceImage)

admin.site.register(quiz)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(questions,QuestionAdmin)
admin.site.register(Answer)  

# Register your models here.
