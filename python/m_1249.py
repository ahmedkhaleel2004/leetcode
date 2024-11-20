class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l_count = r_count = 0

        string_builder = []

        for char in s:
            if char == "(":
                l_count += 1
                string_builder.append(char)
            elif char == ")":
                if l_count > r_count:
                    r_count += 1
                    string_builder.append(char)
            else:
                string_builder.append(char)

        if l_count == r_count:
            return "".join(string_builder)
        else:
            res = []

            for char in string_builder[::-1]:
                if char == "(":
                    if l_count <= r_count:
                        res.append(char)
                    else:
                        l_count -= 1
                elif char == ")":
                    res.append(char)
                else:
                    res.append(char)

            return "".join(res[::-1])
