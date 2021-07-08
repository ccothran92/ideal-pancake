class Plant(object):
    def __init__(self, desired_moisture_percentage: int, dry_period_in_hours: int):
        self.desired_moisture_percentage = desired_moisture_percentage
        self.dry_period_in_hours = dry_period_in_hours