class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)
       
        # white를 기준으로 세 부분으로 분할하여 정렬합니다.
        while white < blue:
            if nums[white] < 1:  # white 인덱스의 값이 1보다 작으면 red를 의미합니다.
                nums[white], nums[red] = nums[red], nums[white] # white와 red 인덱스 값을 변경합니다.
                # white와 red에 +1을 해줍니다.
                red += 1
                white += 1
            elif nums[white] > 1: # white 인덱스의 값이 1보다 크면 blue를 의미합니다.
                blue -= 1         # blue를 -1 해주고, blue와 white 인덱스에 있는 값을 변경합니다.
                nums[blue], nums[white] = nums[white], nums[blue]
            else:                 # white 인덱스에 있는 값이 1일 때를 의미합니다.
                white += 1        # white에 + 1을 해줍니다.
