function solution(files) {
    
    var answer = [];
    // file -> {header: header, number: number, tail: tail} 형태로 저장할 리스트
    var files_split = [];
    
    for (var i = 0; i<files.length; i ++) {
        var file = files[i]
        var header = '';
        var number = '';
        var tail = '';
        var j = 0;
        var flag = false; // check flag for number section is over
        while (j < file.length) {
            // blank 값이 아니며, 숫자 구조이며, 아직 number 구간이 끝나지 않았다면 number에 추가
            if ( file[j] != " " && Number.isInteger(parseInt(file[j])) === true && flag === false) {
                number += file[j]
            } 
            // 위가 아님 => number에 해당하지 않으며 아직 tail 구간 진입이 아니라면 header에 추가
            else if (flag === false) {
                header += file[j]
            } 
            // tail 구간에 추가
            else {
                tail += file[j]
            };
            
            // number 길이가 5가 되었다면 tail 구간 진입
            if (number.length >= 5) {
                flag = true;
            };
            // 만일 다음 string이 존재하는데 현재가 숫자였으며 다음 구간이 숫자가 아닌 경우는 tail 진입
            if (j+1 < file.length && Number.isInteger(parseInt(file[j])) === true && Number.isInteger(parseInt(file[j+1])) === false) {
                flag = true;
            };
            
            j++
        };
        files_split.push({'header': header, 'number': number, 'tail': tail})
    };
    
    files_split.sort(function(a, b) { 
        // header(둘 다 upper 처리)와 number이 같다면 순서대로 처리
        if (a.header.toUpperCase() === b.header.toUpperCase() && parseInt(a.number) === parseInt(b.number)) {
            return 1; 
        }
        // header가 같으며 number이 다르면 number 순대로 처리
        if (a.header.toUpperCase() === b.header.toUpperCase()) {
            return parseInt(a.number) - parseInt(b.number); 
        } 
        // header가 다르면 header 순대로 처리
        return a.header.toUpperCase() < b.header.toUpperCase() ? -1 : a.header.toUpperCase() > b.header.toUpperCase() ? 1 : 0; 
    });
    
    for (var i=0; i < files_split.length; i++) {
        var file = files_split[i]
        var name = file['header'] + file['number'] + file['tail']
        answer.push(name)
    }
    
    return answer;
}