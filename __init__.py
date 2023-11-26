from mycroft import MycroftSkill, intent_file_handler


class SpaceNerds(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nerds.space.intent')
    def handle_nerds_space(self, message):
        impulse = message.data.get('impulse')

        self.speak_dialog('nerds.space', data={
            'impulse': impulse
        })


def create_skill():
    return SpaceNerds()

