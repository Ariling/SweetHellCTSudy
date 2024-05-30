var min_cnt = Infinity;
var visited;
var shared_words;
function solution(begin, target, words) {
  var answer = 0;
  var find_word = true;
  // 배열 초기화 방법
  visited = Array.from({ length: words.length }, () => false);
  shared_words = [...words];
  for (var i = 0; i < words.length; i++) {
    if (target === words[i]) {
      find_word = true;
      break;
    }
    find_word = false;
  }
  dfs(begin, target, 0);
  answer = min_cnt;
  if (find_word === false) {
    return 0;
  }
  return answer;
}

function dfs(begin, target, cnt) {
  // 기저조건
  if (visited.every((e) => e === true)) {
    return;
  }
  if (begin === target) {
    min_cnt = Math.min(min_cnt, cnt);
    return;
  }
  for (var i = 0; i < shared_words.length; i++) {
    var dif = 0;
    if (visited[i] === true) continue;
    for (var j = 0; j < shared_words[i].length; j++) {
      if (dif > 1) break;
      if (shared_words[i][j] !== begin[j]) dif++;
    }
    if (dif === 1 && visited[i] === false) {
      // 이거 돌려놓는거 까먹음...
      var tmp = begin;
      visited[i] = true;
      begin = shared_words[i];
      dfs(begin, target, cnt + 1);
      begin = tmp;
      visited[i] = false;
    }
  }
}