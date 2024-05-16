var str_arr = ["A", "E", "I", "O", "U"]
var array = [];

function solution(word) {
    var answer = 0;
    search("",0);
    for(var i = 0; i < array.length; i++){
      if(array[i] === word)
        break;
      else answer++;
    }
    return answer;
}

function search(word, num){
  array.push(word);
  if(num === 5)
    return;
  for(var i = 0; i < 5; i++){
    search(word+str_arr[i], num+1);
  }
}