from contracts import new_contract


@new_contract
def SMSHandler(x):
    from sms.handlers.base import BaseSMSHandler
    return isinstance(x, BaseSMSHandler)
