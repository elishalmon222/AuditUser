
class Gender:
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]


class Action:
    DELETED = 'deleted'
    RESTARTED_COMPUTER = 'restarted_computer'
    WENT_RUNNING = 'went_running'
    BAKED_CAKE = 'baked_cake'

    CHOICES = [
        (DELETED, 'Deleted'),
        (RESTARTED_COMPUTER, 'Restarted Computer'),
        (WENT_RUNNING, 'Went Running'),
        (BAKED_CAKE, 'Baked Cake'),
    ]


MAX_USER_ACTION_ROWS = 100
