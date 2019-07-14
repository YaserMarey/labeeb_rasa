## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_greet <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## story_intro
* intro{"student_name":"Sam"}
 - utter_ask_course

## story_ask_difficulty
* course
 - utter_ask_difficulty

## story_happy_path_01_01
* intro{"student_name":"Yaser"}  
 - utter_ask_course
* course{"course_name":"Computer Vision"}
 - utter_ask_difficulty

## story_happy_path_01_02
* course{"course_name":"Machine Learning"}
 - utter_ask_difficulty
* difficulty
 - slot{"difficulty_text":"Relatively easy class with some prior knowledge."}
 - action_detect_difficulty_emotions_ask_assignments
* assignments
 - slot{"assignments_text":"The assignment is highly related to the video and well organized. Description of the project are clear."}
 - action_detect_assignments_emotions_ask_mentors
* mentors
 - slot{"mentors_text":"Joyner is a fantastic professor"}
 - action_detect_mentors_emotions_ask_lectures
* lectures
 - slot{"lectures_text":"The lectures were great"}
 - action_detect_lectures_emotions_ask_scale
* scale
 - utter_thanks
* goodbye
 - utter_goodbye
 

## Generated Story -4952663092731812969
* greet
    - utter_greet
* intro{"student_name": "yasser"}
    - slot{"student_name": "yasser"}
    - utter_ask_course
* course{"course_name": "ml"}
    - slot{"course_name": "ml"}
    - utter_ask_difficulty
* difficulty{"difficulty_text": "very difficult indeed"}
    - slot{"difficulty_text": "very difficult indeed"}
    - action_detect_difficulty_emotions_ask_assignments
    - slot{"sentiment_difficulty_score": -0.56789621675}
* assignments{"assignments_text": "assignments were long and required a lot of work"}
    - slot{"assignments_text": "assignments were long and required a lot of work"}
    - action_detect_assignments_emotions_ask_mentors
    - slot{"sentiment_assignments_score": 0.086487919666667}
* assignments{"mentors_text": "instructors were responsive and available all the time on piazza"}
    - slot{"mentors_text": "instructors were responsive and available all the time on piazza"}
    - action_detect_mentors_emotions_ask_lectures
    - slot{"sentiment_mentors_score": 0.242911352}
* lectures{"lectures_text": "lectures were fun but long"}
    - slot{"lectures_text": "lectures were fun but long"}
    - action_detect_lectures_emotions_ask_scale
* scale
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story 2047763984526439356
* stop

## Generated Story -8043430314982040223
* greet
    - utter_greet
* intro{"student_name": "yasser"}
    - slot{"student_name": "yasser"}
    - utter_ask_course
* course{"course_name": "machine learning"}
    - slot{"course_name": "machine learning"}
    - utter_ask_difficulty
* difficulty{"difficulty_text": "difficult"}
    - slot{"difficulty_text": "difficult"}
    - action_detect_difficulty_emotions_ask_assignments
    - slot{"sentiment_difficulty_score": -0.885323353}
* assignments{"assignments_text": "assignments were long and required a lot of effort"}
    - slot{"assignments_text": "assignments were long and required a lot of effort"}
    - action_detect_assignments_emotions_ask_mentors
    - slot{"sentiment_assignments_score": -0.12511969}
* assignments{"mentors_text": "instructors were responsive and available on piazza"}
    - slot{"mentors_text": "instructors were responsive and available on piazza"}
    - action_detect_mentors_emotions_ask_lectures
    - slot{"sentiment_mentors_score": 0.244875432}
* lectures{"lectures_text": "lectures were so many but fun"}
    - slot{"lectures_text": "lectures were so many but fun"}
    - action_detect_lectures_emotions_ask_scale
* scale
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -8695112407933037187
* greet
    - utter_greet
* intro{"student_name": "yaser"}
    - slot{"student_name": "yaser"}
    - utter_ask_course
* course{"course_name": "ml"}
    - slot{"course_name": "ml"}
    - utter_ask_difficulty
* difficulty{"difficulty_text": "very difficult"}
    - slot{"difficulty_text": "very difficult"}
    - action_detect_difficulty_emotions_ask_assignments
    - slot{"sentiment_difficulty_score": -0.56789621675}
* assignments{"assignments_text": "assignments were long"}
    - slot{"assignments_text": "assignments were long"}
    - action_detect_assignments_emotions_ask_mentors
    - slot{"sentiment_assignments_score": -0.087330228}
* lectures{"mentors_text": "ta 's were helpful"}
    - slot{"mentors_text": "ta 's were helpful"}
    - action_detect_mentors_emotions_ask_lectures
    - slot{"sentiment_mentors_score": 0.977358545}
* lectures{"lectures_text": "lectures were fun"}
    - slot{"lectures_text": "lectures were fun"}
    - action_detect_lectures_emotions_ask_scale
* scale
    - utter_thanks
    - utter_goodbye

