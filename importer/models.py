from django.db import models


class AccountingGroup(models.Model):
    id = models.AutoField(db_column='accountingGroupTableID', primary_key=True)
    name = models.CharField(db_column='accountGroupName', blank=True, null=True, max_length=500)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'ACCOUNTINGGROUPTABLE'


class AccountType(models.Model):
    id = models.AutoField(db_column='accountTypeTableID', primary_key=True, blank=True)
    name = models.CharField(db_column='accountTypeName', blank=True, null=True, max_length=500)
    accounting_group = models.ForeignKey(
        AccountingGroup, on_delete=models.CASCADE,
        db_column='accountingGroupID', blank=True, null=True
    )

    def __str__(self):
        return f"{self.accounting_group} - {self.name}"

    class Meta:
        managed = False
        db_table = 'ACCOUNTTYPETABLE'


class Account(models.Model):
    id = models.AutoField(db_column='accountsTableID', primary_key=True)
    name = models.CharField(db_column='accountName', blank=True, null=True, max_length=500)
    account_type = models.ForeignKey(
        AccountType, on_delete=models.CASCADE,
        db_column='accountTypeID', blank=True, null=True
    )
    hidden = models.IntegerField(db_column='accountHidden', blank=True, null=True)
    currency = models.CharField(db_column='accountCurrency', blank=True, null=True, max_length=500)
    conversion_rate_new = models.FloatField(db_column='accountConversionRateNew', blank=True, null=True)
    currency_changed = models.IntegerField(db_column='currencyChanged', blank=True, null=True)
    credit_limit = models.IntegerField(db_column='creditLimit', blank=True, null=True)
    cut_off_da = models.IntegerField(db_column='cutOffDa', blank=True, null=True)
    credit_card_due_date = models.IntegerField(db_column='creditCardDueDate', blank=True, null=True)
    cash_based_accounts = models.IntegerField(db_column='cashBasedAccounts', blank=True, null=True)
    selector_visibility = models.IntegerField(db_column='accountSelectorVisibility', blank=True, null=True)
    extra_column_string_1 = models.CharField(
        db_column='accountsExtraColumnString1', blank=True, null=True, max_length=500
    )
    extra_column_string_2 = models.CharField(
        db_column='accountsExtraColumnString2', blank=True, null=True, max_length=500
    )
    extra_column_int_1 = models.CharField(
        db_column='accountsExtraColumnInt1', blank=True, null=True, max_length=500
    )
    extra_column_int_2 = models.CharField(
        db_column='accountsExtraColumnInt2', blank=True, null=True, max_length=500
    )

    def __str__(self):
        return f"{self.name} - {self.currency}"

    class Meta:
        managed = False
        db_table = 'ACCOUNTSTABLE'


class CategoryGroup(models.Model):
    id = models.AutoField(db_column='categoryGroupTableID', primary_key=True)
    name = models.CharField(db_column='categoryGroupName', blank=True, null=True, max_length=500)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = False
        db_table = 'CATEGORYGROUPTABLE'


class ParentCategory(models.Model):
    id = models.AutoField(db_column='parentCategoryTableID', primary_key=True)
    name = models.CharField(db_column='parentCategoryName', blank=True, null=True, max_length=500)
    category_group = models.ForeignKey(
        CategoryGroup, on_delete=models.CASCADE,
        db_column='categoryGroupID', blank=True, null=True
    )
    budget_amount = models.IntegerField(db_column='budgetAmountCategoryParent', blank=True, null=True)
    budget_period = models.IntegerField(db_column='budgetPeriodCategoryParent', blank=True, null=True)
    budget_enabled = models.IntegerField(db_column='budgetEnabledCategoryParent', blank=True, null=True)
    budget_amount_override = models.IntegerField(
        db_column='budgetAmountOverride', blank=True, null=True
    )
    budget_custom_setup = models.CharField(
        db_column='budgetCustomSetupParent', blank=True, null=True, max_length=500
    )
    extra_column_string_1 = models.CharField(
        db_column='categoryParentExtraColumnString1', blank=True, null=True, max_length=500
    )
    extra_column_string_2 = models.CharField(
        db_column='categoryParentExtraColumnString2', blank=True, null=True, max_length=500
    )
    extra_column_int_1 = models.CharField(
        db_column='categoryParentExtraColumnInt1', blank=True, null=True, max_length=500
    )
    extra_column_int_2 = models.CharField(
        db_column='categoryParentExtraColumnInt2', blank=True, null=True, max_length=500
    )

    def __str__(self):
        return f"{self.category_group} - {self.name}"

    class Meta:
        managed = False
        db_table = 'PARENTCATEGORYTABLE'


class ChildCategory(models.Model):
    id = models.AutoField(db_column='categoryTableID', primary_key=True, blank=True)
    name = models.CharField(db_column='childCategoryName', blank=True, null=True, max_length=500)
    parent_category = models.ForeignKey(
        ParentCategory, on_delete=models.CASCADE,
        db_column='parentCategoryID', blank=True, null=True
    )
    budget_amount = models.IntegerField(db_column='budgetAmount', blank=True, null=True)
    budget_period = models.IntegerField(db_column='budgetPeriod', blank=True, null=True)
    budget_enabled = models.IntegerField(
        db_column='budgetEnabledCategoryChild', blank=True, null=True
    )
    icon = models.CharField(
        db_column='childCategoryIcon', blank=True, null=True, max_length=500
    )
    selector_visibility = models.IntegerField(
        db_column='categorySelectorVisibility', blank=True, null=True
    )
    budget_custom_setup = models.CharField(
        db_column='budgetCustomSetup', blank=True, null=True, max_length=500
    )
    extra_column_string_1 = models.CharField(
        db_column='categoryExtraColumnString1', blank=True, null=True, max_length=500
    )
    extra_column_string_2 = models.CharField(
        db_column='categoryExtraColumnString2', blank=True, null=True, max_length=500
    )
    extra_column_int_1 = models.CharField(
        db_column='categoryExtraColumnInt1', blank=True, null=True, max_length=500
    )
    extra_column_int_2 = models.CharField(
        db_column='categoryExtraColumnInt2', blank=True, null=True, max_length=500
    )

    def __str__(self):
        return f"{self.parent_category} - {self.name}"

    class Meta:
        managed = False
        db_table = 'CHILDCATEGORYTABLE'


class Filter(models.Model):
    id = models.AutoField(db_column='filtersTableID', primary_key=True, blank=True)
    name = models.CharField(db_column='filterName', blank=True, null=True, max_length=500)
    json_repr = models.CharField(db_column='filterJSON', blank=True, null=True, max_length=500)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'FILTERSTABLE'


class Item(models.Model):
    id = models.AutoField(db_column='itemTableID', primary_key=True)
    name = models.CharField(db_column='itemName', blank=True, null=True, max_length=500)
    auto_fill_visibility = models.IntegerField(db_column='itemAutoFillVisibility', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'ITEMTABLE'


class TransactionType(models.Model):
    id = models.AutoField(db_column='transactionTypeTableID', primary_key=True, blank=True)
    name = models.CharField(db_column='transactionTypeName', blank=True, null=True, max_length=500)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'TRANSACTIONTYPETABLE'


class Transaction(models.Model):
    id = models.AutoField(db_column='transactionsTableID', primary_key=True, blank=True)
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE,
        db_column='itemID', blank=True, null=True
    )
    amount = models.IntegerField(blank=True, null=True)
    currency = models.CharField(
        db_column='transactionCurrency', blank=True, null=True, max_length=500
    )
    conversion_rate_new = models.FloatField(db_column='conversionRateNew', blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    transaction_type = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE,
        db_column='transactionTypeID', blank=True, null=True
    )
    category = models.ForeignKey(
        ChildCategory, on_delete=models.CASCADE,
        db_column='categoryID', blank=True, null=True
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        related_name="from+", db_column='accountID',
        blank=True, null=True
    )
    notes = models.CharField(blank=True, null=True, max_length=500)
    status = models.IntegerField(blank=True, null=True)
    account_reference = models.IntegerField(db_column='accountReference', blank=True, null=True)
    account_pair = models.ForeignKey(
        Account, on_delete=models.CASCADE,
        related_name="to+", db_column='accountPairID',
        blank=True, null=True
    )
    uid_pair = models.ForeignKey(
        "self", on_delete=models.CASCADE,
        db_column='uidPairID', blank=True, null=True
    )
    deleted = models.IntegerField(db_column='deletedTransaction', blank=True, null=True)
    new_split = models.IntegerField(db_column='newSplitTransactionID', blank=True, null=True)
    transfer_group = models.IntegerField(
        db_column='transferGroupID',
        blank=True,
        null=True
    )
    has_photo = models.IntegerField(db_column='hasPhoto', blank=True, null=True)
    label_count = models.IntegerField(db_column='labelCount', blank=True, null=True)
    reminder_transaction = models.IntegerField(db_column='reminderTransaction', blank=True,
                                               null=True)
    reminder_group = models.IntegerField(db_column='reminderGroupID', blank=True, null=True)
    reminder_frequency = models.IntegerField(db_column='reminderFrequency', blank=True, null=True)
    reminder_repeat_every = models.IntegerField(db_column='reminderRepeatEvery', blank=True, null=True)
    reminder_ending_type = models.IntegerField(db_column='reminderEndingType', blank=True, null=True)
    reminder_start_date = models.DateTimeField(db_column='reminderStartDate', blank=True, null=True)
    reminder_end_date = models.DateTimeField(db_column='reminderEndDate', blank=True, null=True)
    reminder_after_no_of_occurrences = models.IntegerField(
        db_column='reminderAfterNoOfOccurences', blank=True, null=True
    )
    reminder_automatic_log_transaction = models.IntegerField(
        db_column='reminderAutomaticLogTransaction', blank=True, null=True
    )
    reminder_repeating = models.IntegerField(db_column='reminderRepeating', blank=True, null=True)
    reminder_repeat_by_day_of_month = models.IntegerField(
        db_column='reminderRepeatByDayOfMonth', blank=True, null=True
    )
    reminder_exclude_weekend = models.IntegerField(
        db_column='reminderExcludeWeekend', blank=True, null=True
    )
    reminder_week_day_move_setting = models.IntegerField(
        db_column='reminderWeekDayMoveSetting', blank=True, null=True
    )
    reminder_un_billed = models.IntegerField(db_column='reminderUnbilled', blank=True, null=True)
    credit_card_installment = models.IntegerField(db_column='creditCardInstallment', blank=True, null=True)
    reminder_version = models.IntegerField(db_column='reminderVersion', blank=True, null=True)
    data_extra_column_string1 = models.CharField(db_column='dataExtraColumnString1', blank=True, null=True,
                                                 max_length=500)

    def __str__(self):
        extra_text = f" TO {self.account_pair}" if self.account != self.account_pair else ""
        return f"{self.item} - {self.account}{extra_text}"

    class Meta:
        managed = False
        db_table = 'TRANSACTIONSTABLE'


class Label(models.Model):
    id = models.AutoField(db_column='labelsTableID', primary_key=True, blank=True)
    name = models.CharField(db_column='labelName', blank=True, null=True, max_length=500)
    transaction = models.ForeignKey(
        Transaction, on_delete=models.CASCADE,
        db_column='transactionIDLabels', blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        db_table = 'LABELSTABLE'


class Picture(models.Model):
    id = models.AutoField(db_column='pictureTableID', primary_key=True, blank=True)
    filename = models.CharField(db_column='pictureFileName', blank=True, null=True, max_length=500)
    transaction = models.ForeignKey(
        Transaction, on_delete=models.CASCADE,
        db_column='transactionID', blank=True, null=True
    )

    def __str__(self):
        return f"{self.filename}"

    class Meta:
        managed = False
        db_table = 'PICTURETABLE'



