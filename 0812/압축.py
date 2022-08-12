def solution(msg):
    
    # 정답 배열
    answer = []
    # 사전dict  {'A': 1, 'B': 2, ...}
    words = {}
    
    # 한글자 A~Z 알파벳 색인 번호 정보를 사전 dict에 추가
    for i in range(ord('Z') - ord('A') + 1):
        words[(chr(i+65))] = i+1
    
    # while 통해 단어를 확인
    i = 0
    while i < len(msg):
        
        # 현재 위치 시작 지점 알파벳을 우선 word로 지정
        word = msg[i]
        # j는 다음 위치 알파벳을 포함한 단어가 words에 있는지 확인하기 위한 변수
        j = 1
        # 다음 알파벳이 존재하며 알파벳을 추가한 단어가 사전에 있을 때까지 다음 알파벳 추가
        while i+j < len(msg) and word in words:
            word += msg[i+j]
            j += 1
        
        # 만일 단어가 words에 있는 단어라면 answer에 해당 단어의 색인 번호를 넣고
        if word in words:
            answer.append(words[word])
            # 그 단어만큼을 뛰어서 msg 확인
            i += len(word)
        # 만일 단어가 words에 없다면
        else:
            # 현재 words에서 가장 큰 색인 번호를 추출해 해당 단어를 max 색인 번호 + 1에 추가
            max_val = max(words.values())+1
            words[word] = max_val
            # 그리고 마지막 한 자리를 뺀 단어의 색인 번호를 answer에 추가
            answer.append(words[word[:len(word)-1]])
            # 한 자리 뺀 단어의 길이만큼 뛰어서 msg 확인
            i += len(word)-1
    
    return answer