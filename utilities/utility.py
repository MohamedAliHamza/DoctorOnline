
# Choices
SATURDAY = 'SATURDAY'
SUNDAY = 'SUNDAY'
MONDAY = 'MONDAY'
TUSDAY = 'TUSDAY'
WENESDAY = 'WENESDAY'
THURSDAY = 'THURSDAY'
FRIDAY = 'FRIDAY'
choice_day = [
       (SATURDAY,'Saturday'),
       (SUNDAY,'Sunday'),
       (MONDAY,'Monday'),
       (TUSDAY,'Tuesday'),
       (WENESDAY,'Wednesday'),
       (THURSDAY,'Thursday'),
       (FRIDAY,'Friday')
]

# Images
def upload_avatar(instance, filename):
    return 'users/{0}/{1}'.format(instance.id, filename)
