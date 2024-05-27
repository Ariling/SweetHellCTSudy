function solution(sequence, k) {
  var answer = [];
  var start = 0;
  var end = 0;
  var sum = 0;
  // 이런게 있다고 함.
  var len = Infinity;
  while (start < sequence.length) {
    if (sum < k && end < sequence.length) {
      sum += sequence[end++];
    } else if (sum >= k || end == sequence.length) {
      sum -= sequence[start++];
    }
    if (sum == k) {
      var dif = end - start - 1;
      if (len > dif) {
        len = dif;
        answer = [start, end -1];
      }
    } else if (len == dif && answer[0] > start) {
      answer = [start, end - 1];
    }
  }
  return answer;
}
