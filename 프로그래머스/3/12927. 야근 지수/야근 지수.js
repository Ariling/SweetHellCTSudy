function solution(n, works) {
  var answer = 0;
  if (n >= works.reduce((acc, cur) => acc + cur)) return 0;
  works.sort((a, b) => b - a);
  while (n != 0) {
    var max = works[0];
    for (var i = 0; i < works.length; i++) {
      if (works[i] >= max) {
        n--;
        works[i]--;
      }
      // 이게 0인지 음수인지 나타내줌
      if (!n) break;
    }
  }
  for (var i = 0; i < works.length; i++) {
    answer += Math.pow(works[i], 2);
  }
  return answer;
}