# ^ You can ignore this line - it is used to help check your code

# YOUR CODE HERE
if subj_age == 'old' and score > 25:
    subj_status = 'Super Ager'
elif subj_age == 'old' and score <=25:
    subj_status = 'Normal Ager'
elif subj_age == 'young' and score > 25:
    subj_status = 'Normal Youth'
elif subj_age == 'young' and score <= 25:
    subj_status = 'Bad Youth'