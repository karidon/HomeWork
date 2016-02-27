from django.contrib import admin
from .models import Question, Choise


# Register your models here.


# class ChoiseInline(admin.StackedInline):
class ChoiseInline(
	admin.TabularInline):  # TabularInline делает компакнее вопросы
	'''
	Формируте форму ответов
	'''
	model = Choise
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		# collapse - для схлопывания редко редактироваемого поля
		(
			'Date information',
			{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiseInline]  # Добовляет форму

	# выводим списоа полей
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = [
		'pub_date']  # Добовляет фильтр по полю pub_date в боковой панели
	search_fields = ['question_text']  # Добовляет поиск по полю question_text
# list_per_page = 50    # определяет количество объектов на одной странице по умолчанию 100



admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choise)

