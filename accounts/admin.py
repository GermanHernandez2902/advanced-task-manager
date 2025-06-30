# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # ستون‌های نمایش در لیست
    list_display = ('email', 'username', 'is_staff', 'is_active')
    # فیلتر درکنار صفحه
    list_filter = ('is_staff', 'is_active')
    # فیلدهای قابل جستجو
    search_fields = ('email', 'username')
    ordering = ('email',)
    # اگر فیلدهای اضافی در CustomUser داری، اینجا در fieldsets و add_fieldsets اضافه کن
