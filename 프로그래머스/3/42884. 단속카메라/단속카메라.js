function solution(routes) {
  var answer = 0;
  var arr = routes.sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]));
  var camera_pos = -30001; // 이 이상 안 준다고 하니깐..
  for (var i = 0; i < arr.length; i++) {
    if (camera_pos < arr[i][0]) {
      answer += 1;
      camera_pos = arr[i][1];
    }
  }
  return answer;
}