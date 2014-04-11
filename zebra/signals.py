"""
Provides the following signals:

V1

- zebra_webhook_recurring_payment_failed
- zebra_webhook_invoice_ready
- zebra_webhook_recurring_payment_succeeded
- zebra_webhook_subscription_trial_ending
- zebra_webhook_subscription_final_payment_attempt_failed
- zebra_webhook_subscription_ping_sent

v2

- zebra_webhook_charge_succeeded
- zebra_webhook_charge_failed
- zebra_webhook_charge_refunded
- zebra_webhook_charge_disputed
- zebra_webhook_customer_created
- zebra_webhook_customer_updated
- zebra_webhook_customer_deleted
- zebra_webhook_customer_subscription_created
- zebra_webhook_customer_subscription_updated
- zebra_webhook_customer_subscription_deleted
- zebra_webhook_customer_subscription_trial_will_end
- zebra_webhook_customer_discount_created
- zebra_webhook_customer_discount_updated
- zebra_webhook_customer_discount_deleted
- zebra_webhook_invoice_created
- zebra_webhook_invoice_updated
- zebra_webhook_invoice_payment_succeeded
- zebra_webhook_invoice_payment_failed
- zebra_webhook_invoiceitem_created
- zebra_webhook_invoiceitem_updated
- zebra_webhook_invoiceitem_deleted
- zebra_webhook_plan_created
- zebra_webhook_plan_updated
- zebra_webhook_plan_deleted
- zebra_webhook_coupon_created
- zebra_webhook_coupon_updated
- zebra_webhook_coupon_deleted
- zebra_webhook_transfer_created
- zebra_webhook_transfer_failed
- zebra_webhook_ping
"""
import django.dispatch

WEBHOOK_ARGS = ["customer", "full_json"]

zebra_webhook_recurring_payment_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_invoice_ready = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_recurring_payment_succeeded = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_trial_ending = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_final_payment_attempt_failed = django.dispatch.Signal(providing_args=WEBHOOK_ARGS)
zebra_webhook_subscription_ping_sent = django.dispatch.Signal(providing_args=[])

# v2 webhooks
WEBHOOK2_ARGS = ["full_json"]

zebra_webhook_charge_succeeded = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_charge_failed = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_charge_refunded = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_charge_disputed = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_deleted = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_deleted = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_trial_will_end = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_discount_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_discount_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_discount_deleted = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_payment_succeeded = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_payment_failed = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoiceitem_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoiceitem_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoiceitem_deleted = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_plan_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_plan_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_plan_deleted = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_coupon_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_coupon_updated = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_coupon_deleted = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_transfer_created = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_transfer_failed = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_ping = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)

WEBHOOK_MAP = {
    'charge_succeeded': zebra_webhook_charge_succeeded,
    'charge_failed': zebra_webhook_charge_failed,
    'charge_refunded': zebra_webhook_charge_refunded,
    'charge_disputed': zebra_webhook_charge_disputed,
    'customer_created': zebra_webhook_customer_created,
    'customer_updated': zebra_webhook_customer_updated,
    'customer_deleted': zebra_webhook_customer_deleted,
    'customer_subscription_created': zebra_webhook_customer_subscription_created,
    'customer_subscription_updated': zebra_webhook_customer_subscription_updated,
    'customer_subscription_deleted': zebra_webhook_customer_subscription_deleted,
    'customer_subscription_trial_will_end': zebra_webhook_customer_subscription_trial_will_end,
    'customer_discount_created': zebra_webhook_customer_discount_created,
    'customer_discount_updated': zebra_webhook_customer_discount_updated,
    'customer_discount_deleted': zebra_webhook_customer_discount_deleted,
    'invoice_created': zebra_webhook_invoice_created,
    'invoice_updated': zebra_webhook_invoice_updated,
    'invoice_payment_succeeded': zebra_webhook_invoice_payment_succeeded,
    'invoice_payment_failed': zebra_webhook_invoice_payment_failed,
    'invoiceitem_created': zebra_webhook_invoiceitem_created,
    'invoiceitem_updated': zebra_webhook_invoiceitem_updated,
    'invoiceitem_deleted': zebra_webhook_invoiceitem_deleted,
    'plan_created': zebra_webhook_plan_created,
    'plan_updated': zebra_webhook_plan_updated,
    'plan_deleted': zebra_webhook_plan_deleted,
    'coupon_created': zebra_webhook_coupon_created,
    'coupon_updated': zebra_webhook_coupon_updated,
    'coupon_deleted': zebra_webhook_coupon_deleted,
    'transfer_created': zebra_webhook_transfer_created,
    'transfer_failed': zebra_webhook_transfer_failed,
    'ping': zebra_webhook_ping,
}

# VERIFIED EVENTS
zebra_webhook_charge_succeeded_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_charge_failed_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_charge_refunded_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_charge_disputed_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_deleted_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_deleted_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_subscription_trial_will_end_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_discount_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_discount_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_customer_discount_deleted_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_payment_succeeded_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoice_payment_failed_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoiceitem_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoiceitem_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_invoiceitem_deleted_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_plan_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_plan_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_plan_deleted_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_coupon_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_coupon_updated_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_coupon_deleted_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_transfer_created_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_transfer_failed_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)
zebra_webhook_ping_verified = django.dispatch.Signal(providing_args=WEBHOOK2_ARGS)

WEBHOOK_MAP.update({
    'charge_succeeded_verified': zebra_webhook_charge_succeeded_verified,
    'charge_failed_verified': zebra_webhook_charge_failed_verified,
    'charge_refunded_verified': zebra_webhook_charge_refunded_verified,
    'charge_disputed_verified': zebra_webhook_charge_disputed_verified,
    'customer_created_verified': zebra_webhook_customer_created_verified,
    'customer_updated_verified': zebra_webhook_customer_updated_verified,
    'customer_deleted_verified': zebra_webhook_customer_deleted_verified,
    'customer_subscription_created_verified': zebra_webhook_customer_subscription_created_verified,
    'customer_subscription_updated_verified': zebra_webhook_customer_subscription_updated_verified,
    'customer_subscription_deleted_verified': zebra_webhook_customer_subscription_deleted_verified,
    'customer_subscription_trial_will_end_verified': zebra_webhook_customer_subscription_trial_will_end_verified,
    'customer_discount_created_verified': zebra_webhook_customer_discount_created_verified,
    'customer_discount_updated_verified': zebra_webhook_customer_discount_updated_verified,
    'customer_discount_deleted_verified': zebra_webhook_customer_discount_deleted_verified,
    'invoice_created_verified': zebra_webhook_invoice_created_verified,
    'invoice_updated_verified': zebra_webhook_invoice_updated_verified,
    'invoice_payment_succeeded_verified': zebra_webhook_invoice_payment_succeeded_verified,
    'invoice_payment_failed_verified': zebra_webhook_invoice_payment_failed_verified,
    'invoiceitem_created_verified': zebra_webhook_invoiceitem_created_verified,
    'invoiceitem_updated_verified': zebra_webhook_invoiceitem_updated_verified,
    'invoiceitem_deleted_verified': zebra_webhook_invoiceitem_deleted_verified,
    'plan_created_verified': zebra_webhook_plan_created_verified,
    'plan_updated_verified': zebra_webhook_plan_updated_verified,
    'plan_deleted_verified': zebra_webhook_plan_deleted_verified,
    'coupon_created_verified': zebra_webhook_coupon_created_verified,
    'coupon_updated_verified': zebra_webhook_coupon_updated_verified,
    'coupon_deleted_verified': zebra_webhook_coupon_deleted_verified,
    'transfer_created_verified': zebra_webhook_transfer_created_verified,
    'transfer_failed_verified': zebra_webhook_transfer_failed_verified,
    'ping_verified': zebra_webhook_ping_verified,
})