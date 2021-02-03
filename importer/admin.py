from django.contrib import admin

# Register your models here.
from .models import (
    Item,
    CategoryGroup,
    ChildCategory,
    Transaction,
    Filter,
    Label,
    Picture,
    AccountingGroup,
    ParentCategory,
    TransactionType,
    Account,
    AccountType,
)


class MultiDBModelAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'bluecoins'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class MultiDBTabularInline(admin.TabularInline):
    using = 'bluecoins'

    def get_queryset(self, request):
        # Tell Django to look for inline objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


class ItemInline(MultiDBTabularInline):
    model = Item


class CategorygrouInline(MultiDBTabularInline):
    model = CategoryGroup


class ChildcategoryInline(MultiDBTabularInline):
    model = ChildCategory


class TransactionsInline(MultiDBTabularInline):
    model = Transaction


class FiltersInline(MultiDBTabularInline):
    model = Filter


class LabelsInline(MultiDBTabularInline):
    model = Label


class PictureInline(MultiDBTabularInline):
    model = Picture


class AccountinggroupInline(MultiDBTabularInline):
    model = AccountingGroup


class ParentcategoryInline(MultiDBTabularInline):
    model = ParentCategory


class TransactiontypeInline(MultiDBTabularInline):
    model = TransactionType


class AccountsInline(MultiDBTabularInline):
    model = Account


class AccounttypeInline(MultiDBTabularInline):
    model = AccountType


class PublisherAdmin(MultiDBModelAdmin):
    inlines = [
        ItemInline,
        CategorygrouInline,
        ChildcategoryInline,
        TransactionsInline,
        FiltersInline,
        LabelsInline,
        PictureInline,
        AccountinggroupInline,
        ParentcategoryInline,
        TransactiontypeInline,
        AccountsInline,
        AccounttypeInline,
    ]

admin.site.register(Item, MultiDBModelAdmin)
admin.site.register(CategoryGroup, MultiDBModelAdmin)
admin.site.register(ChildCategory, MultiDBModelAdmin)
admin.site.register(Transaction, MultiDBModelAdmin)
admin.site.register(Filter, MultiDBModelAdmin)
admin.site.register(Label, MultiDBModelAdmin)
admin.site.register(Picture, MultiDBModelAdmin)
admin.site.register(AccountingGroup, MultiDBModelAdmin)
admin.site.register(ParentCategory, MultiDBModelAdmin)
admin.site.register(TransactionType, MultiDBModelAdmin)
admin.site.register(Account, MultiDBModelAdmin)
admin.site.register(AccountType, MultiDBModelAdmin)
