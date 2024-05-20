function solution(record) {
  const answer = [];
  const userInfo = {};
  //userInfo를 {} 객체로 생성하여 이름과 값 쌍을로 구성 -> 이게 낫네... 괜히 객체배열로 하느니...

  for (let i = 0; i < record.length; i++) {
    const list = record[i].split(" ");
    if (list[0] === "Enter") {
      userInfo[list[1]] = list[2];
      answer.push(`${list[1]}님이 들어왔습니다.`);
    } else if (list[0] === "Leave") {
      answer.push(`${list[1]}님이 나갔습니다.`);
    } else if (list[0] === "Change") {
      userInfo[list[1]] = list[2];
    }
  }

  // replace로 이름으로 변경하기
  for (let i = 0; i < answer.length; i++) {
    const uid = answer[i].split("님이")[0];
    answer[i] = answer[i].replace(uid, userInfo[uid]);
  }

  return answer;
}