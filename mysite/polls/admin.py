from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    #默认提供3个空白的Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #字段分组显示，也可指定该字段的HTML样式类
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    # django界面默认显示str（）返回的内容，如果要自定义则传递list_display字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    #添加过滤器
    list_filter = ['pub_date']
    #限制搜索字段
    search_fields = ['question_text']
    #高效的关联Choice方式
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)