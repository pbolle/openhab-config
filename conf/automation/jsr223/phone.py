from shared.helper import rule, getNow, itemStateOlderThen, sendNotification, postUpdate
from core.triggers import ItemStateChangeTrigger, CronTrigger
from org.eclipse.smarthome.core.library.types import StringListType

@rule("phone.py")
class DoorBellNotificationRule:
    def __init__(self):
        self.triggers = [
            ItemStateChangeTrigger("IncomingCall"),
            ItemStateChangeTrigger("OutgoingCall")
        ]

    def execute(self, module, input):
        state = input['event'].getItemState()
        self.log.info(u"tel 0: {}".format(state.getValue(0)))
        self.log.info(u"tel 1: {}".format(state.getValue(1)))
        if  type(state) is StringListType and itemStateOlderThen("Gardendoor_Bell_Last_Change", getNow().minusSeconds(30)) and state.getValue(1) == '99999999' :
            sendNotification("Klingel", "Es klingelt", "https://bolle.haus/cameraStrasseImage" )
            postUpdate("Gardendoor_Bell_Last_Change", DateTimeType())