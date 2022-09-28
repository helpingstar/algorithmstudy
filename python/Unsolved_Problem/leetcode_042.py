from typing import List

class Solution:

    # 풀이 1. 투 포인터를 최대로 이동
    def trap_twoPointer(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[right]

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume




from typing import List

class Solution:
	# 풀이 2. 스택 쌓기
    # height를 스택에 쌓아 가다가 변곡점(현재 보다 높아질 때)을
    # 기준으로 격차만큼 물 높이 volume을 채움
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
           # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)

        return volume
