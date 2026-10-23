
from django.contrib import admin
from .models import Project, Skill, ContactMesssage, Experience, Education


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "is_featured", "created_at")
    search_fields = ("title", "tech_stack")
    list_filter = ("is_featured",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "display_order")
    search_fields = ("name", "category")
    list_filter = ("category", "proficiency")


@admin.register(ContactMesssage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "is_read", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("is_read", "created_at")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "is_current")
    search_fields = ("title", "organization")
    list_filter = ("is_current",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("qualification", "institute", "year")
    search_fields = ("qualification", "institute")
