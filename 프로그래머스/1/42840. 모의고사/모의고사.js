function solution(answers) {
    var answer = [];
    var first = [1,2,3,4,5]; // 5
    var second = [2, 1, 2, 3, 2, 4, 2, 5]; // 8
    var third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]; // 10
    var score = Array(3).fill(0,0,3);
  for(var i = 0; i < answers.length; i++){
    if(first[i % 5] == answers[i]){
      score[0]++;
    }
    if(second[i % 8] == answers[i]){
      score[1]++;
    }
    if(third[i % 10] == answers[i]){
      score[2]++;
    }
  }
    // 이게 최대 구하는 거래 오옹..
    const max = Math.max(...score);
    
    for(var i = 0; i < score.length; i++){
      if(score[i] == max){
        answer.push(i+1);
      }
    }
    return answer;
}
