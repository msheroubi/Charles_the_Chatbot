import tagNtokenize
import correlation_cf as cf
import time
from os.path import dirname, join
import pickle

current_dir = dirname(__file__)
file_path = join(current_dir, 'question_answers.pickle')
with open(file_path, 'rb') as f:
        question_answers= pickle.load(f)


current_milli_time = lambda: int(round(time.time() * 1000))

def getResponse(uIn, sub):
    global question_answers
    tagtime = current_milli_time()
    tagged = tagNtokenize.tagNtokenize(uIn, True)
    tagtime = current_milli_time() - tagtime

    max_u = 0.6
    str_ans = "Sorry I don't quite know how to answer that!"

    corrtime = current_milli_time()

    # If in subquestions
    if(sub =="1"):
        str_ans = "That's interesting"
        sub = ""
    elif(sub != ""):
            for quest in question_answers[sub]:
                tagged2 = tagNtokenize.tagNtokenize(quest)
                temp_u = cf.correlate(tagged,tagged2)
##                      print("u= " + str(temp_u))
                if(temp_u>max_u):
                        try:
                                str_ans = question_answers[sub][quest]
##                                      print(tagged2)
                                max_u=temp_u
                        except:
                                print("Error in Sub referencing")
                                sub = ""
                            
    for quest in question_answers:
##                print("\n"+quest)
            tagged2 = tagNtokenize.tagNtokenize(quest)
            temp_u = cf.correlate(tagged,tagged2)
##                print("u= " + str(temp_u))
            if(temp_u>max_u):
                    max_u=temp_u
                    str_ans = question_answers[quest]['ans']
##                        print(tagged2)
                    sub = quest
    corrtime = current_milli_time() - corrtime

    if(max_u <= 0.6):
        for t in tagged:
            if "NN" in t[1]:
                namedEntity = tagNtokenize.NER([(t[0],t[1])])
                for n in namedEntity:
                    if("PERSON" in n):
                        str_ans = "Who is " + t[0] + "?"
                        sub = ""
                    elif("GPE" in n):
                        str_ans = "Where is " + t[0] + "?"
                        sub = "!"

    return [str_ans, sub]