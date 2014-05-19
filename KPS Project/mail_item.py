class  Mail_Item:
    def __init__(self, Origin, Priority, Destination, Weight, Volume, EntryTime,
            costKPS = None, costClient = None, DeliverTime = None):
        self.origin = Origin
        self.destination = Destination
        self.priority = Priority
        self.weight = Weight
        self.volume = Volume
        self.entrytime = EntryTime
        self.costkps = costKPS
        self.costclient = costClient
        self.delivertime = DeliverTime
