function solution(arr)
{
    var answer = [];
    answer.push(arr[0]);
    var num = arr[0];
    // var에서 헷갈림
    for(var i = 1; i < arr.length; i++){
      if(num == arr[i]){
        continue;
      }else{
        num = arr[i];
        answer.push(arr[i]);
      }
    }
    
    return answer;
}