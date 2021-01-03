from shared.helper import rule, getNow, itemStateOlderThen, sendNotification, postUpdate
from core.triggers import ItemStateChangeTrigger, CronTrigger
from org.eclipse.smarthome.core.library.types import StringListType

@rule("phone.py")
class DoorBellNotificationRule:
    def __init__(self):
        self.triggers = [
            ItemStateChangeTrigger("IncomingCall")
        ]

    def execute(self, module, input):
        state = input['event'].getItemState()
#        self.log.info(u"type {}".format(type(state)))
        if itemStateOlderThen("Gardendoor_Bell_Last_Change", getNow().minusSeconds(30)) and type(state) is StringListType and state.getValue(1) == '4933762979088@192.168.178.1' :
            sendNotification("Klingel", "Es klingelt", "https://bolle.haus/cameraStrasseImage" )
        postUpdate("Gardendoor_Bell_Last_Change", DateTimeType())
