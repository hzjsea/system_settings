#!/usr/bin/env python3
# encoding: utf-8
'''
@author: hzj
@file: base36or10encode.py.py
@time: 2020/5/28 4:04 下午
@desc: python进制转换工具
'''


# python 10进制转换36进制
# python 36进制转换10进制

class BaseNumserEncode():

    def base16to10encode(self,integer: str) ->str:
        return int(integer,16)

    def base10to16encode(self,integer: int)->str:
        return hex(integer)

    def base2to10encode(self,integer: str) -> str:
        return int(integer,2)

    def base8to10encode(self,integer:str) -> str:
        return int(integer,8)


    def base2to16encode(self,integer:str)->str:
        # 2 -> 10 -> 16
        # return hex(int(integer,10))
        return hex(self.base2to10encode(integer))

    def base8to16encdeo(self,integer:str)-> str:
        # 8 -> 10 -> 16
        # return hex(int(integer,8))
        return hex(self.base8to10encode(integer))

    def base10to36encode(self,integer: int) -> str:
        """Convert from Base10 to Base36."""
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        sign = '-' if integer < 0 else ''
        integer = abs(integer)
        result = ''

        while integer > 0:
            integer, remainder = divmod(integer, 36)
            result = chars[remainder] + result

        return sign + result

    def base36to10encode(self,nums: str) -> int:
        """Convert from Base36 to Base10"""
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        sign = ""
        if nums.startswith("-"):
            sign = "-"
            nums = nums[1:]

        result = int(nums[0])

        for num in nums[1:]:
            num_index = int(chars.find(num.upper()))
            result = result*36+num_index


        return sign + str(result)

    # 36进制内，任意转换
    def baseNinclude36(self,num, b):
        return ((num == 0) and "0") or (self.baseNinclude36(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

if __name__ == '__main__':
    # chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # nums = 200510
    # xx, yy = divmod(nums, 36)  # xx是商。 yy是余数
    # print(chars[yy], xx)
    # xx, yy = divmod(5569, 36)
    # print(chars[yy], xx)
    # xx, yy = divmod(154, 36)
    # print(chars[yy], xx)


    uu = BaseNumserEncode()
    print(uu.base16to10encode('0xf'))
    print(uu.base10to16encode(20))
    print(uu.base2to10encode('10100111110'))
    print(uu.base8to10encode('17'))
    print(uu.base10to36encode(36))
    print(uu.base36to10encode("10"))
    print(uu.baseNinclude36(36,7))



