from adapt.intent import IntentBuilder
from mycroft import audio, MycroftSkill, intent_handler
import os
import time

def write_command_fifo(command_string="make it so"):
    filename = '/tmp/snis-natural-language-fifo'
    fifo = open(filename, 'w')
    fifo.write(command_string)
    fifo.close()


class SpaceNerds(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_handler('engage.drive.intent')
    def handle_engage_drive(self, message):
        drive_type = message.data.get('drive_type')

        self.speak_dialog('engage.drive', data={
            'drive_type': drive_type
        })

        audio.wait_while_speaking()
        command_string = "engage {drive_type} drive".format(drive_type=drive_type)
        write_command_fifo(command_string)


    @intent_handler('on.screen.intent')
    def handle_on_screen(self, message):
        station_name = message.data.get('station_name')

        self.speak_dialog('on.screen', data={
            'station_name': station_name
        })

        audio.wait_while_speaking()
        command_string = "{station_name} on screen".format(station_name=station_name)
        write_command_fifo(command_string)


    @intent_handler('shields.intent')
    def handle_shields(self, message):
        raise_lower = message.data.get('raise_lower')

        self.speak_dialog('shields', data={
            'raise_lower': raise_lower
        })

        audio.wait_while_speaking()
        command_string = "{raise_lower} shields".format(raise_lower=raise_lower)
        write_command_fifo(command_string)


    @intent_handler('navigate.to.nearest.intent')
    def handle_navigate_to_nearest(self, message):
        destination = message.data.get('destination')

        self.speak_dialog('navigate.to.nearest', data={
            'destination': destination
        })

        audio.wait_while_speaking()
        command_string = "navigate to nearest {destination}".format(destination=destination)
        write_command_fifo(command_string)


    @intent_handler('begin.patrol.intent')
    def handle_begin_patrol(self, message):
        self.speak_dialog('begin.patrol')
        audio.wait_while_speaking()

        ship_components = [
            "shields",
            "weapons",
            "communications",
            "sensors",
            "impulse drive",
            "maneuvering"
        ]

        # set coolant and power levels
        for component in ship_components:
            command_string = "set {component} coolant to 60%".format(component=component)
            write_command_fifo(command_string)
            time.sleep(2)
            command_string = "set {component} power to 50%".format(component=component)
            write_command_fifo(command_string)
            time.sleep(2)

        # turn lights on
        command_string = "turn lights on"
        write_command_fifo(command_string)
        time.sleep(2)

        # target nearest ship
        command_string = "target nearest ship"
        write_command_fifo(command_string)
        time.sleep(2)

        # turn 30 degrees to port
        command_string = "turn 30 degrees port"
        write_command_fifo(command_string)
        time.sleep(2)

        # set thottle
        command_string = "set impulse drive to 30%"
        write_command_fifo(command_string)
        time.sleep(10)

        # target nearest ship
        command_string = "target nearest ship"
        write_command_fifo(command_string)
        time.sleep(2)

        # cut thottle
        command_string = "set impulse drive to 0%"
        write_command_fifo(command_string)
        time.sleep(10)

        # turn 90 degrees starbaard
        command_string = "turn 90 degrees starboard"
        write_command_fifo(command_string)
        time.sleep(4)

        # set thottle
        command_string = "set impulse drive to 30%"
        write_command_fifo(command_string)
        time.sleep(10)

        # cut thottle
        command_string = "set impulse drive to 0%"
        write_command_fifo(command_string)
        time.sleep(2)

        # target nearest asteroid
        command_string = "target nearest asteroid"
        write_command_fifo(command_string)
        time.sleep(2)

        # navigate to nearest asteroid
        command_string = "navigate to nearest asteroid"
        write_command_fifo(command_string)
        time.sleep(4)

        # set thottle
        command_string = "set impulse drive to 30%"
        write_command_fifo(command_string)
        time.sleep(10)

        # cut thottle
        command_string = "set impulse drive to 0%"
        write_command_fifo(command_string)
        time.sleep(2)

        self.speak_dialog('patrol.complete')
        audio.wait_while_speaking()

    # @intent_handler('red.alert.intent')

    # @intent_handler('prepare.for.warp.intent')

    @intent_handler('disembark.to.direction.intent')
    def handle_disembark_to_direction(self, message):
        port_starboard = message.data.get('port_starboard')

        self.speak_dialog('disembark.to.direction', data={
            'port_starboard': port_starboard
        })

        audio.wait_while_speaking()

        ship_components = [
            "shields",
            "weapons",
            "communications",
            "sensors",
            "impulse drive",
            "maneuvering"
        ]

        # set coolant and power levels
        for component in ship_components:
            command_string = "set {component} coolant to 40%".format(component=component)
            write_command_fifo(command_string)
            time.sleep(2)
            command_string = "set {component} power to 30%".format(component=component)
            write_command_fifo(command_string)
            time.sleep(2)


        # disengage magnets
        command_string = "turn magnets off"
        write_command_fifo(command_string)
        time.sleep(2)

        # turn lights on
        command_string = "turn lights on"
        write_command_fifo(command_string)
        time.sleep(2)

        # reverse throttle
        command_string = "toggle reverse throttle"
        write_command_fifo(command_string)
        time.sleep(2)

        # set thottle
        command_string = "set impulse drive to 20%"
        write_command_fifo(command_string)
        time.sleep(2)

        time.sleep(4)
        command_string = "set impulse drive to 0%"
        write_command_fifo(command_string)
        time.sleep(2)

        command_string = "turn 45 degrees {port_starboard}".format(port_starboard=port_starboard)
        write_command_fifo(command_string)
        time.sleep(2)

        time.sleep(30)

        self.speak_dialog('ready.to.engage', data={'port_starboard': port_starboard})
        audio.wait_while_speaking()


def create_skill():
    return SpaceNerds()

