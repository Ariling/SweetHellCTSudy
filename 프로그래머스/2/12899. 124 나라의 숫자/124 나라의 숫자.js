function solution(n) {
  let answer = "";
  let num_arr = [4, 1, 2];
  while (n > 0) {
    answer = num_arr[n % 3] + answer;
    // 이 뒤의 n을 어떻게 처리하냐...
    n = parseInt((n - 1) / 3);
  }
  return answer;
}