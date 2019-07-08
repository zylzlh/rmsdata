from django.contrib import admin
from .models import accident
from .models import acmodel
from .models import data_source
from .models import data_address
from term.models import term
from term.models import term_category

# decorator
@admin.register(accident)
class accident_Admin(admin.ModelAdmin):
    list_display = ('title','date','content','acmodel')
    list_filter = ('date','acmodel')
    search_fields = ('title','content')
    date_hierarchy = 'date'
    ordering = ('date','acmodel')

admin.site.register(acmodel)

@admin.register(term)
class term_Admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'acmodel', 'tag')
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(term_category)
class term_category_Admin(admin.ModelAdmin):
    list_display = ('name','slug')
    list_filter = ('name',)
    search_fields = ('name',)
    
@admin.register(data_source)
class data_source_Admin(admin.ModelAdmin):
    list_display = ('title', 'acmodel', 'source_interpretation')
    list_filter = ('title',)
    search_fields = ('title','source_interpretation')
    
@admin.register(data_address) 
class data_address_Admin(admin.ModelAdmin):
    list_display = ('title', 'date', 'data_source')
    list_filter = ('title',)
    search_fields = ('title',)
