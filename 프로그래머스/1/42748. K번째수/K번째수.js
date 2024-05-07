function solution(array, commands) {
    var answer = [];
    for(var i = 0; i < commands.length; i++){
      var test = array.slice(commands[i][0]-1,commands[i][1]);
      test.sort((a,b)=> a- b);
      answer.push(test[commands[i][2]-1]);
    }
    return answer;
}