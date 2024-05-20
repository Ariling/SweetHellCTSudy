function solution(numbers) {
    var answer = numbers.map(e => String(e))
                        .sort((a, b) => (b+a) - (a+b))
                        .join('');
    // 괄호 까먹지 말기! 그리고 배열 할당도!
    return answer[0] === "0" ? "0" : answer;
}