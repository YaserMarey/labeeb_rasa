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
 

## story_ask_difficulty_01
* course
 - utter_ask_difficulty

## story_ask_difficulty_02
* course{"course_name":"CV"}
 - utter_ask_difficulty

## story_ask_difficulty_03_01
* course{"course_name":"Computational Photography"}
 - utter_ask_difficulty

## story_ask_difficulty_03_02
* course{"course_name":"6475"}
 - utter_ask_difficulty

## story_ask_difficulty_03_03
* course{"course_name":"CS-6475"}
 - utter_ask_difficulty
 
## story_ask_difficulty_03_04
* course{"course_name":"Computer Networks"}
 - utter_ask_difficulty

## story_ask_difficulty_03_05
* course{"course_name":"CN"}
 - utter_ask_difficulty

## story_ask_difficulty_03_06
* course{"course_name":"6250"}
 - utter_ask_difficulty

## story_ask_difficulty_03_07
* course{"course_name":"CS-6250"}
 - utter_ask_difficulty


## story_ask_difficulty_03_08
* course{"course_name":"Intro to Operating Systems"}
 - utter_ask_difficulty

## story_ask_difficulty_03_09
* course{"course_name":"Human-Computer Interaction"}
 - utter_ask_difficulty

## story_ask_difficulty_03_10
* course{"course_name":"HCI"}
 - utter_ask_difficulty

## story_ask_difficulty_03_11
* course{"course_name":"Software Development Process"}
 - utter_ask_difficulty

## story_ask_difficulty_03_12
* course{"course_name":"SDP"}
 - utter_ask_difficulty

## story_ask_difficulty_03_13
* course{"course_name":"6300"}
 - utter_ask_difficulty

## story_ask_difficulty_03_14
* course{"course_name":"Knowledge-Based AI"}
 - utter_ask_difficulty

## story_ask_difficulty_03_15
* course{"course_name":"KBAI"}
 - utter_ask_difficulty


## story_ask_assignments_1
* difficulty
 - utter_ask_assignments

## story_ask_mentors_1
* assignments
 - utter_ask_mentors

## story_ask_lectures_1
* mentors
 - utter_ask_lectures


## story_happy_path_01_01
* intro{"student_name":"Yaser"}  
 - utter_ask_course
* course{"course_name":"Computer Vision"}
 - utter_ask_difficulty

## story_happy_path_01_02
* course{"course_name":"Machine Learning"}
 - utter_ask_difficulty
* difficulty
 - slot{"difficulty_text":""}

## story_happy_path_01_03
* difficulty
 - slot{"difficulty_text":""}
 - action_detect_emotions_ask_assignments
* assignments
 - slot{"assignments_text":""}
 - action_detect_emotions_ask_mentors
* mentors
 - slot{"mentors_text":""}
 - action_detect_emotions_ask_lectures
* lectures
 - slot{"lectures_text":""}
 - action_detect_emotions_ask_scale
* scale
 - utter_thanks
* goodbye
 - utter_goodbye

## story_happy_path_01_05
* scale
 - utter_thanks
* goodbye
 - utter_goodbye



## story_happy_path_01
* intro{"student_name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_ask_course
* course{"course_name":"CV"}
 - utter_ask_review
* review{"review_text":"Overall, I will say this is a very good course. It's tedious, somewhat vague, and frustrating at times. However, I feel it largely depends on the effort you put into it."}
 - slot{"review_text":"Overall, I will say this is a very good course. It's tedious, somewhat vague, and frustrating at times. However, I feel it largely depends on the effort you put into it."}
 - action_detect_emotions_ask_scale
* scale
 - utter_thanks
* goodbye
 - utter_goodbye

## story_happy_path_02
* intro{"student_name":"Yaser"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_ask_course
* course{"course_name":"Machine Learning"}
 - utter_ask_review
* review{"review_text":"The lectures were great, but the Head TA Ronnie Howard is the absolute worst TA or instructor I've ever experienced. He just doesn't give a fudge."}
 - slot{"review_text":"The lectures were great, but the Head TA Ronnie Howard is the absolute worst TA or instructor I've ever experienced. He just doesn't give a fudge."}
 - action_detect_emotions_ask_scale
* scale
 - utter_thanks
 - utter_goodbye

## story_happy_path_03
* intro{"student_name":"Ken"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_ask_course
* course{"course_name":"6264"}
 - utter_ask_review
* review{"review_text":"Love the class, it is well organized and the assignment instruction is clear."}
 - slot{"review_text":"Love the class, it is well organized and the assignment instruction is clear."}
 - action_detect_emotions_ask_scale
* scale
 - utter_thanks
* goodbye
 - utter_goodbye

## story_happy_path_04
* intro{"student_name":"Yaser Marey"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_ask_course
* course{"course_name":"EduTeck"}
 - utter_ask_review
* review{"review_text":"Easy but a super good class. The assignment is highly related to the video and well organized. Description of the project are clear."}
 - slot{"review_text":"Easy but a super good class. The assignment is highly related to the video and well organized. Description of the project are clear."}
 - action_detect_emotions_ask_scale
* scale
 - utter_thanks
* goodbye
 - utter_goodbye
