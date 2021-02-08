# 문자열을 리스트로 변환하여 풀이
def isPalindrome(self, s):
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
  
  
# re 모듈로 문자열 전처리후 슬라이싱 활용
def isPalindrome(self, s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]
