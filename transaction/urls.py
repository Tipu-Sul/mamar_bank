from django.urls import path
from.views import DepositeMoneyView,WithdrawMoneyView,TransationReportView,LoanListView,PayLoanView,LoanRequstView

urlpatterns = [
    path('deposite/', DepositeMoneyView.as_view(),name='deposite_money'),
    path('report/', TransationReportView.as_view(),name='transaction_report'),
    path('withdraw/', WithdrawMoneyView.as_view(),name='withdraw_money'),
    path('loan_request/', LoanRequstView.as_view(),name='loan_request'),
    path('loans/', LoanListView.as_view(),name='loan_list'),
    path('loan/<int:loan_id>/', PayLoanView.as_view(),name='pay'),
   
]



