from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Informações dos votos', {'fields': ['pub_date']}),
    ]
    list_display = ['get_question_text', 'get_pub_date']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

    def get_question_text(self, obj):
        return obj.question_text
    get_question_text.short_description = 'Pergunta'

    def get_pub_date(self, obj):
        return obj.pub_date
    get_pub_date.short_description = 'Data de Criação'

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question', 'choice_text']}),
        ('Informações sobre os votos', {'fields': ['votes']}),
    ]
    list_display = ['get_choice_text', 'get_votes', 'get_question_text', 'get_pub_date']

    def get_choice_text(self, obj):
        return obj.choice_text
    get_choice_text.short_description = 'Escolha'

    def get_votes(self, obj):
        return obj.votes
    get_votes.short_description = 'Quantidade de Votos'

    def get_question_text(self, obj):
        return obj.question.question_text
    get_question_text.short_description = 'Pergunta'

    def get_pub_date(self, obj):
        return obj.question.pub_date
    get_pub_date.short_description = 'Data de Criação'