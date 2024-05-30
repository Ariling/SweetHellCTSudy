function solution(operations) {
  var answer = [];
  var queue = [];
  for (var i = 0; i < operations.length; i++) {
    var cmd = operations[i].split(" ");
    if (cmd[0] === "I") {
      queue.push(parseInt(cmd[1]));
      queue.sort((a, b) => a - b);
    } else if (cmd[0] === "D") {
      if (cmd[1] === "-1" && queue.length) {
        queue.shift();
      } else if (cmd[1] === "1" && queue.length) {
        queue.pop();
      }
    }
  }
  if (queue.length > 1) {
    answer = [queue.pop(), queue.shift()];
  } else if (queue.length === 1) {
    var a = queue.pop();
    answer = [a, a];
  } else {
    answer = [0, 0];
  }
  return answer;
}