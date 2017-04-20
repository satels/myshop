from contracts import new_contract


@new_contract
def SMSHandler(x):
    from .handlers.base import SMSHandler
    return isinstance(x, SMSHandler)
