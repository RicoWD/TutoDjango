from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# admin.site.register(Question)


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text", "place_holder_3"]


class ChoiceAdmin(admin.ModelAdmin):
    fields = ["question", "choice_text", "votes"]
    list_display = ("choice_text", "votes", "question")


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
        ("Place Holder 3", {"fields": ["place_holder_3"]}),
    ]
    list_display = ["question_text", "pub_date"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)


# ICI : Vous pouvez améliorer cela en appliquant le décorateur display() à cette méthode (dans polls/models.py), comme ceci :
