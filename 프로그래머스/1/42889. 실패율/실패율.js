function solution(N, stages) {
    var answer = [];
    // 2차원 배열 만드는 방법.. 개 복잡하네
    var fail = new Array(N);
    for(var i = 0; i < fail.length; i++){
      fail[i] = new Array(2);
    }
    stages.sort((a,b)=> a-b);
    let stop_idx = 1;
    // 빈 경우를 고려 못해서 런타임 에러가 났었다.
    let empty = false;
    for(var i = 1; i <= N; i++){
        if(stages.length == 0){
            stop_idx = i;
            empty = true;
            break;
        }
      var len = stages.filter((stage) => stage == i).length;
      let fail_percent = len/stages.length;
      stages.splice(0,len);
      fail[i-1][0] = fail_percent;
      fail[i-1][1] = i;
    }
    if(empty == true){
        for(var i = stop_idx; i <= N; i++){
            fail[i-1][0] = 1-1;
            fail[i-1][1] = i;
        }
    }
    fail.sort((a, b)=>{
      if(a[0] == b[0]){
        return a[1] - b[1];
      }else{
        return b[0] - a[0];
      }
    })
    for(var i = 0; i < N; i++){
      answer.push(fail[i][1]);
    }
    return answer;
}