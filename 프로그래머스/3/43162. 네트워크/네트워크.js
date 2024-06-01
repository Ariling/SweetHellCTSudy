function solution(n, computers) {
  let answer = 0;
  let visited = Array.from({ length: n }, () => false);

  for (let i = 0; i < n; i++) {
    if (!visited[i]) {
      dfs(i, visited, computers);
      answer++;
    }
  }

  return answer;
}

const dfs = (node, visited, computers) => {
  visited[node] = true;
  for (let i = 0; i < computers.length; i++) {
    if (computers[node][i] === 1 && !visited[i]) dfs(i, visited, computers); // dfs로 방문 진행
  }
};