your_age = 19
has_ticket = True
is_vip = False
event_age_limit = 18

can_enter_standard_event = (your_age >= event_age_limit) and has_ticket
print(f"can enter standard event ? {can_enter_standard_event } # ({your_age} >= {event_age_limit} is {your_age >= event_age_limit}) AND ({has_ticket} is True) -> {can_enter_standard_event}")

can_enter_vip_lounge = is_vip or (your_age >= 21)
print(f"can enter VIP lounge ? {can_enter_vip_lounge }  # ({is_vip} is True) OR ({your_age} >= 21 is {your_age >= 21}) -> {can_enter_vip_lounge}")

is_denied_entry = not (can_enter_standard_event)
print(f"denied entry ? {is_denied_entry }   # NOT ({can_enter_standard_event}) -> {is_denied_entry}")