import braintree
from django.conf import settings


if settings.BRAINTREE_SANDBOX:
    braintree_environment = braintree.Environment.Sandbox
else:
    braintree_environment = braintree.Environment.Production

braintree.Configuration.configure(braintree_environment,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)


def get_tr_payment_url():
    return braintree.TransparentRedirect.url()


def get_plans():
    plans = braintree.Plan.all()
    return plans


def get_customers():
    return braintree.Customer.all().items


def get_customer(customer_id):
    return braintree.Customer.find(customer_id)
