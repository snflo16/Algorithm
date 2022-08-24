def solution(survey, choices):
    answer = ''
    score = {}

    
    def add(selection, add_score):
        
        if selection in score:
            score[selection] += add_score
        else:
            score[selection] = add_score
            
            
    for i in range(len(survey)):
        select = choices[i]
        if select < 4:
            add(survey[i][0], abs(4-select))
            add(survey[i][1], 0)
        elif select > 4:
            add(survey[i][1], abs(select-4))
            add(survey[i][0], 0)
    
    
    for can_choice in ("RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"):
        add(can_choice[0], 0)
        add(can_choice[1], 0)
        
        
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer