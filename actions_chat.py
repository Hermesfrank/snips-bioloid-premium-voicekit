#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.ontology import *
import actions_leds
import time


def when_born(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "My brain was created in July of two thousand nineteen", "")


def creator(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "I was created by my Master", "")


def belong_to(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "I belong to my Master", "")


def wink(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Sure, I can wink", "")

    # Wink
    time.sleep(1)
    actions_leds.wink()


def smile(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "Sure, I can smile, can you", "")

    # smile
    time.sleep(1)
    actions_leds.smile()
    time.sleep(1)
    actions_leds.straight_face()


def frown(hermes, intent_message):
    # terminate the session first if not continue
    hermes.publish_end_session(intent_message.session_id, "")

    # action code goes here...
    print('[Received] intent: {}'.format(intent_message.intent.intent_name))

    # if need to speak the execution result by tts
    hermes.publish_start_session_notification(intent_message.site_id, "I will frown if I am sad", "")

    # frown
    time.sleep(1)
    actions_leds.frown()
    time.sleep(1)
    actions_leds.straight_face()
