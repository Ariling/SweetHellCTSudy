function solution(fees, records) {
    var answer = [];
    var money_obj = {};
    // 들어온 시간만 확인
    var temp_obj = {};
    var check_obj = {};
    for(var i = 0; i < records.length; i++){
      var [time, car_num, check] = records[i].split(" ");
      var [hour, min] = time.split(":");
      var time_minute = hour * 60 + min * 1;
      if(check === "IN"){
          if(!money_obj.hasOwnProperty(car_num)){
            money_obj[car_num] = 0;
          }
          check_obj[car_num] = true;
          temp_obj[car_num] = time_minute;
      }
      else if(check === "OUT"){
        check_obj[car_num] = false;
        var val = temp_obj[car_num];
        money_time = time_minute - val;
        money_obj[car_num] += money_time;
      }
    }
    Object.keys(check_obj).forEach((e)=>{
      if(check_obj[e] === true){
        var val = temp_obj[e];
        var time_minute = 23 * 60 + 59 * 1;
        money_time = time_minute - val;
        money_obj[e] += money_time;
      }
    })
    Object.entries(money_obj).sort((a, b) => a[0].localeCompare(b[0]))
      .map((e)=>{
      if(e[1] <= fees[0]){
        answer.push(fees[1]);
      }
      else{
        var plus_time = e[1] - fees[0];

        if(plus_time % fees[2] === 0){
          answer.push(fees[1] + (Math.ceil(plus_time / fees[2]) * fees[3]))
        }else{
          answer.push(fees[1] + (Math.ceil(plus_time / fees[2]) * fees[3]))
        }
      }
    });
    return answer;
}