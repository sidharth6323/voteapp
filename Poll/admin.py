from django.contrib import admin

# Register your models here.
from models import user,total_votes


@admin.register(user)
class userAdmin(admin.ModelAdmin):
	pass

@admin.register(total_votes)
class total_votesAdmin(admin.ModelAdmin):
	pass