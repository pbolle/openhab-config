from shared.helper import rule, getNow, itemStateOlderThen, sendNotification, postUpdate
from core.triggers import ItemStateChangeTrigger, CronTrigger


@rule("test.py")
class MyTestRule:
    def __init__(self):
        self.triggers = [
            CronTrigger("15 * * * * ?")
        ]

    def execute(self, module, input):
        pass

@rule("test.py")
class DoorBellNotificationRule:
    def __init__(self):
        self.triggers = [
#            CronTrigger("15 * * * * ?"),
#            ItemStateChangeTrigger("IncomingCall", state="OPEN")
            ItemStateChangeTrigger("IncomingCall")
        ]

    def execute(self, module, input):

        state = input['event'].getItemState()
        name = input['event'].getItemName()

        self.log.info(u"test {} {}".format(type(state), name))

        #if itemStateOlderThen("pOutdoor_Streedside_Gardendoor_Bell_Last_Change", getNow().minusSeconds(30)):
        #    sendNotification("Klingel", "Es klingelt", "https://smartmarvin.de/cameraStrasseImage" )

        #postUpdate("pOutdoor_Streedside_Gardendoor_Bell_Last_Change", DateTimeType())




