class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=i+"#7617$"
        return result

    def decode(self, s: str) -> List[str]:
        result=s.split("#7617$")
        del result[-1]
        return result

