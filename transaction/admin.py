from typing import Any
from django.contrib import admin
from. models import transactions
from. views import send_transaction_mail

# Register your models here.
@admin.register(transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display=['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve','is_bankrupt']
    def save_model(self, request, obj, form, change):
        if obj.loan_approve==True and obj.is_bankrupt==False:
            obj.account.balance+=obj.amount
            obj.balance_after_transaction=obj.account.balance
            obj.account.save()
            send_transaction_mail(obj.account.user, obj.amount,"Loan Approval","transaction/conform_loan_mail.html")
            super().save_model(request, obj, form, change)
