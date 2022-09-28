from django.contrib import admin

from app.models import Author, JobPost, Location, Skill
from subscribe.models import Subscribe

class JobAdmin(admin.ModelAdmin):
    list_display=('title', 'salary', 'date')
    list_filter=('date','salary')
    search_fields=("salary",)
    search_help_text="Write your query and hit enter"
    #fields=('title', 'description')
    #exclude=('expiry',)
    fieldsets=(
        ('Basic Information',{'fields':('title', 'description')}
        ),
        ('More Information',{
            'classes':('collapse',),
            'fields':('salary', 'expiry', 'slug')}
        ),
    )
        
# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
admin.site.register(Subscribe)