# SOURCE ---> http://www.toforge.com/tag/mturk/

from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm,Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer,HTMLQuestion

ACCESS_ID = 'fakefakefake'
SECRET_KEY = 'fnklfjgklfg'
HOST = 'mechanicalturk.sandbox.amazonaws.com'

mtc = MTurkConnection(aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY, host=HOST)

title = 'Give your opinion about a website'
description = ('Visit a website and give us your opinion'
               ' and some personal comments')
keywords = 'website, rating, opinions'

# ratings =[('Very Bad','-2'),
#          ('Bad','-1'),
#          ('Not bad','0'),
#          ('Good','1'),
#          ('Very Good','1')]

# #---------------  BUILD OVERVIEW -------------------

# overview = Overview()
# overview.append_field('Title', 'Give your opinion on this website')
# overview.append(FormattedContent('<a target="_blank"'
#                                  ' href="https://github.com/s4ayub">'
#                                  ' Shabab Ayub Github</a>'))

# #---------------  BUILD QUESTION 1 -------------------

# qc1 = QuestionContent()
# qc1.append_field('Title','How the repos look?')

# fta1 = SelectionAnswer(type='datetime-local',
#                       other=False)

# q1 = Question(identifier='design',
#               content=qc1,
#               answer_spec=AnswerSpecification(fta1),
#               is_required=True)

# #---------------  BUILD QUESTION 2 -------------------

# qc2 = QuestionContent()
# qc2.append_field('Title','Your personal comments')

# fta2 = FreeTextAnswer()

# q2 = Question(identifier="comments",
#               content=qc2,
#               answer_spec=AnswerSpecification(fta2))

# #---------------  BUILD HTMLQuestion -------------------

# qc2 = HTMLQuestion()
# qc2.append_field('Title','Your personal comments')

# fta2 = FreeTextAnswer()

# q2 = Question(identifier="comments",
#               content=qc2,
#               answer_spec=AnswerSpecification(fta2))

# # #--------------- BUILD THE QUESTION FORM -------------------

# # question_form = QuestionForm()
# # question_form.append(overview)
# # question_form.append(q1)
# # question_form.append(q2)

#--------------- BUILD THE HTMLQuestion -------------------

html_form = "<html><head><meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/><script type='text/javascript' src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js'></script></head><body><form name='mturk_form' method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'><input type='hidden' value='' name='assignmentId' id='assignmentId'/><h1>What's up?</h1><img alt='image_url' class='center-block' height='900' src='https://s3.amazonaws.com/turkimportimages/popup2.png' width='600' /><p><input type='datetime-local' name='Input'></p><p><input type='datetime-local' name='Input1'></p><p><input type='submit' id='submitButton' value='Submit' /></p></form><script language='Javascript'>turkSetAssignmentID();</script></body></html>"
frame_height = 600
question_form = HTMLQuestion(html_form, frame_height)

#--------------- CREATE THE HIT -------------------

mtc.create_hit(question=question_form,
               max_assignments=1,
               title=title,
               description=description,
               keywords=keywords,
               duration = 60*5,
               reward=0.05)




# def get_all_reviewable_hits(mtc):
#     page_size = 50
#     hits = mtc.get_reviewable_hits(page_size=page_size)
#     print "Total results to fetch %s " % hits.TotalNumResults
#     print "Request hits page %i" % 1
#     total_pages = float(hits.TotalNumResults)/page_size
#     int_total= int(total_pages)
#     if(total_pages-int_total>0):
#         total_pages = int_total+1
#     else:
#         total_pages = int_total
#     pn = 1
#     while pn < total_pages:
#         pn = pn + 1
#         print "Request hits page %i" % pn
#         temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
#         hits.extend(temp_hits)
#     return hits
# &#91;/python&#93;

# The list of hits returned by the method is a list of boto HITS objects.
# This object doesn't contain the assignments, you have to call another method for get the assignments of a particular HIT id.
# The next step is tho iterate trough this list and for each HIT calls the method <a href="http://boto.cloudhackers.com/ref/mturk.html#boto.mturk.connection.MTurkConnection.get_assignments" target="_blank">get_assignments(hit_id)</a>

# This method will return all the answers to your hits.
# Below the complete script for print to screen all the assignments of your hits.


# from boto.mturk.connection import MTurkConnection

# ACCESS_ID ='your access id'
# SECRET_KEY = 'your key'
# HOST = 'mechanicalturk.sandbox.amazonaws.com'

# def get_all_reviewable_hits(mtc):
#     page_size = 50
#     hits = mtc.get_reviewable_hits(page_size=page_size)
#     print "Total results to fetch %s " % hits.TotalNumResults
#     print "Request hits page %i" % 1
#     total_pages = float(hits.TotalNumResults)/page_size
#     int_total= int(total_pages)
#     if(total_pages-int_total>0):
#         total_pages = int_total+1
#     else:
#         total_pages = int_total
#     pn = 1
#     while pn < total_pages:
#         pn = pn + 1
#         print "Request hits page %i" % pn
#         temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
#         hits.extend(temp_hits)
#     return hits

# mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
#                       aws_secret_access_key=SECRET_KEY,
#                       host=HOST)

# hits = get_all_reviewable_hits(mtc)

# for hit in hits:
#     assignments = mtc.get_assignments(hit.HITId)
#     for assignment in assignments:
#         print "Answers of the worker %s" % assignment.WorkerId
#         for question_form_answer in assignment.answers&#91;0&#93;:
#             for key, value in question_form_answer.fields:
#                 print "%s: %s" % (key,value)
#         print "--------------------"
# &#91;/python&#93;

# # As you can see the scripts call the get_assignments method for each hit id and after that iterate trough it for fetching the answers.
# # In the line 36 you see an answer&#91;0&#93;, maybe you are thinking "why don't iterate trough all answers ?"
# # For try to give a clear explanation first let's give some definition thaw will be valid on the next rows.
# # <ul>
# #     <li>A "question form answer" is the single answer to a single question of your form.</li>
# #     <li>An "answer" element is the set of all the "question form answer" of your QuestionForm</li>
# #     <li>An "assignment" is the set of all the "answer<strong>s</strong>" of the same worker</li>
# # </ul>
# # In practice each worker can give just 1 "answer" to the hit, for that the assignment will contain always just one "answer".
# # "answer<strong>s</strong>" element is just a reflection of the xml structure, boto translate it as array of one element.
# # If this explanation has been clear, you just have to know which method use for accept and refuse payments to the workers.
# # The operations of pay and refuse have do be done on the "assignments" unit, in fact they accept the assignment id as a parameter.

# # <tt>approve_assignment</tt><big>(</big><em>assignment_id</em>, <em>feedback=None</em><big>)</big>

# # <tt>reject_assignment</tt><big>(</big><em>assignment_id</em>, <em>feedback=None</em><big>)</big>

# # Both methods accept also a feedback string, this is the message that the workers will receive as explanation for the approved/rejected assignment, be kind <img draggable="false" class="emoji" alt="😀" src="https://s.w.org/images/core/emoji/72x72/1f600.png"> .
# # When you don't need anymore an hits you can "delete" it from mturk by calling the method

# # <tt>disable_hit</tt><big>(</big><em>hit_id</em>, <em>response_groups=None</em><big>)</big>

# # I suggest you to read the <a href="http://boto.cloudhackers.com/ref/mturk.html#boto.mturk.connection.MTurkConnection.disable_hit" target="_blank">documentation</a> about disable_hit method.
# # I leave you with an edited version of the loop that pay all workers and disable the hits.
# # See you soon <img draggable="false" class="emoji" alt="😉" src="https://s.w.org/images/core/emoji/72x72/1f609.png">


# for hit in hits:
#     assignments = mtc.get_assignments(hit.HITId)
#     for assignment in assignments:
#         print "Answers of the worker %s" % assignment.WorkerId
#         for question_form_answer in assignment.answers[0]:
#             for key, value in question_form_answer.fields:
#                 print "%s: %s" % (key,value)
#         mtc.approve_assignment(assignment.AssignmentId)
#         print "--------------------"
#     mtc.disable_hit(hit.HITId)
