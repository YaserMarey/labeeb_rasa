# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

logger = logging.getLogger(__name__)


class ActionDetectDifficultyEmotionsAskAssignments(Action):
    def name(self):
        return 'action_detect_difficulty_emotions_ask_assignments'

    def run(self, dispatcher, tracker, domain):

        logger.info(('difficulty text is:{}'.format(tracker.get_slot('difficulty_text'))))

        msg = "{}"
        score = 0.0

        if tracker.get_slot('difficulty_text') is not None:

            logger.info('difficulty_text is not: None')

            res = requests.post("https://twinword-sentiment-analysis-v1.p.rapidapi.com/analyze/",
                                headers={
                                    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
                                    "X-RapidAPI-Key": "X-RapidAPI-Key", # TODO replace with your own API KEY
                                    # TODO this needs to be enhanced to use environment variables
                                    "Content-Type": "application/x-www-form-urlencoded"
                                },
                                data={
                                    "text": tracker.get_slot('difficulty_text')
                                }
                                )

            logger.info(('res.json is :{}'.format(res.json())))
            score = float(res.json()['score'])
            logger.info('score is :{}'.format(score))

            if score > 0.3:
                msg = "Good to know that :simple_smile:, {}"
            elif score >= 0.1:
                msg = "Alright :neutral_face:, {}"
            elif score < -0.3:
                msg = "Oh sorry to hear that :worried:, {}"
            elif score <= -0.1:
                msg = "Hmmm :neutral_face:, {}"

        dispatcher.utter_message(msg.format("how do you describe the assignments of this course?"))

        return [SlotSet('sentiment_difficulty_score', score)]

class ActionDetectAssignmentsEmotionsAskMentors(Action):
    def name(self):
        return 'action_detect_assignments_emotions_ask_mentors'

    def run(self, dispatcher, tracker, domain):

        logger.info(('assignments text is:{}'.format(tracker.get_slot('assignments_text'))))

        msg = "{}"
        score = 0.0

        if tracker.get_slot('assignments_text') is not None:

            logger.info('assignments_text is not: None')

            res = requests.post("https://twinword-sentiment-analysis-v1.p.rapidapi.com/analyze/",
                                headers={
                                    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
                                    "X-RapidAPI-Key": "X-RapidAPI-Key", # TODO replace with your own API KEY
                                    # TODO this needs to be enhanced to use environment variables
                                    "Content-Type": "application/x-www-form-urlencoded"
                                },
                                data={
                                    "text": tracker.get_slot('assignments_text')
                                }
                                )

            logger.info(('res.json is :{}'.format(res.json())))
            score = float(res.json()['score'])
            logger.info('score is :{}'.format(score))

            if score > 0.3:
                msg = "Nice :simple_smile:, {}"
            elif score >= 0.1:
                msg = "Alright :neutral_face:, {}"
            elif score < -0.3:
                msg = "Too bad :worried:, {}"
            elif score <= -0.1:
                msg = "Hmmm :neutral_face:, {}"


        dispatcher.utter_message(msg.format("how do you describe the course TA's and Professors ?"))
        return [SlotSet('sentiment_assignments_score', score)]

class ActionDetectMentorsEmotionsAskLectures(Action):
    def name(self):
        return 'action_detect_mentors_emotions_ask_lectures'

    def run(self, dispatcher, tracker, domain):

        logger.info(('mentors text is:{}'.format(tracker.get_slot('mentors_text'))))

        msg = "{}"
        score = 0.0

        if tracker.get_slot('mentors_text') is not None:

            logger.info('mentors_text is not: None')

            res = requests.post("https://twinword-sentiment-analysis-v1.p.rapidapi.com/analyze/",
                                headers={
                                    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
                                    "X-RapidAPI-Key": "X-RapidAPI-Key", # TODO replace with you own API KEY
                                    # TODO this needs to be enhanced to use environment variables
                                    "Content-Type": "application/x-www-form-urlencoded"
                                },
                                data={
                                    "text": tracker.get_slot('mentors_text')
                                }
                                )

            logger.info(('res.json is :{}'.format(res.json())))
            score = float(res.json()['score'])
            logger.info('score is :{}'.format(score))

            if score > 0.3:
                msg = "Good good :simple_smile:, {}"
            elif score >= 0.1:
                msg = "Alright :neutral_face:, {}"
            elif score < -0.3:
                msg = "Sorry to know that :worried:, {}"
            elif score <= -0.1:
                msg = "Hmmm :neutral_face:, {}"

        dispatcher.utter_message(msg.format("Alright, and how do you describe the lectures ?"))
        return [SlotSet('sentiment_mentors_score', score)]

class ActionDetectLecturesEmotionsAskScale(Action):
    def name(self):
        return 'action_detect_lectures_emotions_ask_scale'

    def run(self, dispatcher, tracker, domain):

        logger.info(('lecture text is:{}'.format(tracker.get_slot('lectures_text'))))


        if tracker.get_slot('lectures_text') is not None:

            logger.info('lectures_text is not: None')

            res = requests.post("https://twinword-sentiment-analysis-v1.p.rapidapi.com/analyze/",
                                headers={
                                    "X-RapidAPI-Host": "twinword-sentiment-analysis.p.rapidapi.com",
                                    "X-RapidAPI-Key": "X-RapidAPI-Key", # TODO replace with your own API KEY
                                    # TODO this needs to be enhanced to use environment variables
                                    "Content-Type": "application/x-www-form-urlencoded"
                                },
                                data={
                                    "text": tracker.get_slot('lectures_text')
                                }
                                )

            logger.info(('res.json is :{}'.format(res.json())))
            sentiment_lecture_score = float(res.json()['score'])
            avg_sentiment_score = (float(tracker.get_slot('sentiment_assignments_score')) + \
                                  float(tracker.get_slot('sentiment_mentors_score')) + \
                                  float(tracker.get_slot('sentiment_difficulty_score')) + \
                                  sentiment_lecture_score)/4

            # logger.info('score is :{}'.format(score))
            if avg_sentiment_score > 0.3:
                msg = "It seems that you like this course very much"
            elif avg_sentiment_score >= 0.1:
                msg = "It seems that you like this course"
            elif avg_sentiment_score < -0.3:
                msg = "It seems that you don't like this course at all"
            elif avg_sentiment_score <= -0.1:
                msg = "It seems that you don't like this course"
            else:
                msg = "It seems that you have some likes and dislikes about this course"

            response = msg + ", ok this is the last question, I promise :smile: , so on a scale form 1 to 5 where 1 is the worst, and 5 is the best, " \
                             "how do you rate this course"
        else:
            response = "Alright, this is the last question, I promise :), " \
                       "on a scale form 1 to 5 where 1 is the worst, and 5 is the best, how do " \
                       "you rate this course"

        logger.info(('response is :{}'.format(response)))

        dispatcher.utter_message(response)
        return []
