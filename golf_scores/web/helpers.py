from datetime import date

def calculate_score_to_par(score, golf_course_par):
    score_to_par = score - golf_course_par 
    return score_to_par

def format_date(score_date):
    tmp = score_date.split(".")[::-1]
    score_date = date(int(tmp[0]), int(tmp[1]), int(tmp[2]))
    return score_date

