# SOURCE ---------> http://scottlobdell.me/2015/03/use-mechanical-turk-python-boto-crowdsource-tasks/


import os
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
from boto.mturk.price import Price

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

if os.environ.get("I_AM_IN_DEV_ENV"):
    HOST = 'mechanicalturk.sandbox.amazonaws.com'
else:
    HOST = 'mechanicalturk.amazonaws.com'

connection = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                             host=HOST)

url = "https://mturk-demonstration.herokuapp.com/"
title = "Describe a picture in your own words (COMPLETE THIS TASK ONLY ONCE!)"
description = "COMPLETE THIS TASK ONLY ONCE! All submissions after the first will be rejected"
keywords = ["easy"]
frame_height = 800
amount = 0.05

questionform = ExternalQuestion(url, frame_height)

for _ in xrange(60):
    create_hit_result = connection.create_hit(
        title=title,
        description=description,
        keywords=keywords,
        max_assignments=1,
        question=questionform,
        reward=Price(amount=amount),
        response_groups=('Minimal', 'HITDetail'),  # I don't know what response groups are
    )

# SERVER SIDE CODE

if os.environ.get("I_AM_IN_DEV_ENV"):
    AMAZON_HOST = "https://workersandbox.mturk.com/mturk/externalSubmit"
else:
    AMAZON_HOST = "https://www.mturk.com/mturk/externalSubmit"


def home(request):
    if request.GET.get("assignmentId") == "ASSIGNMENT_ID_NOT_AVAILABLE":
        # worker hasn't accepted the HIT (task) yet
        pass
    else:
        # worked accepted the task
        pass

    worker_id = request.GET.get("workerId", "")
    if worker_id in get_worker_ids_past_tasks():
        # you might want to guard against this case somehow
        pass

    render_data = {
        "worker_id": request.GET.get("workerId", ""),
        "assignment_id": request.GET.get("assignmentId", ""),
        "amazon_host": AMAZON_HOST,
        "hit_id": request.GET.get("hitId", ""),
    }

    response = render_to_response("base.html", render_data)
    # without this header, your iFrame will not render in Amazon
    response['x-frame-options'] = 'this_can_be_anything'
    return response

# CLIENT SIDE CODE

# <html>
#     <head>
#         {% include "_js_scripts.html" %}
#     </head>
#     <body>
#     <h3>Using your own words, describe this man however you want.</h3>
#         <form action="{{ amazon_host }}" method="POST">
#             <textarea rows="4" cols="50" name="user-input">
#             </textarea>
#             <input type="hidden" id="assignmentId" value="{{ assignment_id }}" name="assignmentId"/>
#             <br/>
#             <input type="hidden" id="workerId" value="{{ worker_id }}" name="workerId"/>
#             <input type="hidden" id="hitId" value="{{ hit_id }}" name="hitId"/>
#             <input type="submit">
#         </form>
#         <div>
#             <img src="https://s3.amazonaws.com/lobbdawg/mturk/broome1.jpg" style="width: 30%;">
#             <img src="https://s3.amazonaws.com/lobbdawg/mturk/broome2.jpg" style="width: 30%;">
#             <img src="https://s3.amazonaws.com/lobbdawg/mturk/broome3.jpg" style="width: 30%;">
#             <img src="https://s3.amazonaws.com/lobbdawg/mturk/broome4.jpg" style="width: 30%;">
#             <img src="https://s3.amazonaws.com/lobbdawg/mturk/broome5.jpg" style="width: 30%;">
#             <img src="https://s3.amazonaws.com/lobbdawg/mturk/broome6.jpg" style="width: 30%;">
#         </div>
#     </body>
# </html>

# MANIPULATING HITs

all_hits = [hit for hit in connection.get_all_hits()]

for hit in all_hits:
    assignments = connection.get_assignments(hit.HITId)
    for assignment in assignments:
        # don't ask me why this is a 2D list
        question_form_answers = assignment.answers[0]
        for question_form_answer in question_form_answers:
            # "user-input" is the field I created and the only one I care about
            if question_form_answer.qid == "user-input":
                user_response = question_form_answer.fields[0]
                print user_response
                print "\n"
        # connection.approve_assignment(assignment.AssignmentId)
