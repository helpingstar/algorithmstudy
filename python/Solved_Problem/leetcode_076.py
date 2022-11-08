from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        t_counter = defaultdict(int)
        s_counter = defaultdict(int)
        answer = ""
        answer_len = 1000000

        def is_window_substring(src: defaultdict):
            for k in t_counter.keys():
                if src[k] < t_counter[k]:
                    return False
            return True

        for one_t in t:
            t_counter[one_t] += 1

        s_counter[s[0]] += 1

        # print(f'[debug]  t_counter: {t_counter}')
        # print(f'[debug]  s_counter: {s_counter}')

        while left <= right < len(s):
            # print(f'[debug]  left: {left}, right: {right}')
            if is_window_substring(s_counter):
                # print(f'debug right: {right}, left: {right}, answer_len: {answer_len}')
                if right-left+1 < answer_len:
                    answer = s[left:right+1]
                    answer_len = len(answer)
                s_counter[s[left]] -= 1
                left += 1
            else:
                if right + 1 == len(s):
                    return answer
                s_counter[s[right+1]] += 1
                right += 1
        return answer


s = "ADOBECODEBANC"
t = "ABC"
a = Solution()
print(a.minWindow(s, t))
