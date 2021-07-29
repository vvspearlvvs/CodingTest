def letterCombinations(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            for j in dic[digits[i]]:
                dfs(i + 1, path + j) # i는 조합을 위해 문자가 중복되지 않게 선택할 수 있게 해줌.
                # path + j로 넘겼기에 pop이나 join을 해줄 필요가 없다는 장점이있다.
    if not digits:
        return []

    dic = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    dfs(0, "")
    return result
