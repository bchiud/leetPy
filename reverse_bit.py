class Solution:
    def reverseBitsBitByBit(self, n: int) -> int:
        """
        time: 1 (fixed at 32)
        space: 1
        """
        ans, shift = 0, 31
        while n:
            ans += (n & 1) << shift
            n >>= 1
            shift -= 1
        return ans

    def reverseBitsBinarySearch(self, n):
        """
        time: 1
        space: 1

        Step 0.
        abcd efgh ijkl mnop qrst uvwx yzAB CDEF <-- n

        Step 1.
                            abcd efgh ijkl mnop <-- n >> 16, same as (n & 0xffff0000) >> 16
        qrst uvwx yzAB CDEF                     <-- n << 16, same as (n & 0x0000ffff) << 16
        qrst uvwx yzAB CDEF abcd efgh ijkl mnop <-- after OR

        Step 2.
                  qrst uvwx           abcd efgh <-- (n & 0xff00ff00) >> 8
        yzAB CDEF           ijkl mnop           <-- (n & 0x00ff00ff) << 8
        yzAB CDEF qrst uvwx ijkl mnop abcd efgh <-- after OR

        Step 3.
             yzAB      qrst      ijkl      abcd <-- (n & 0xf0f0f0f0) >> 4
        CDEF      uvwx      mnop      efgh      <-- (n & 0x0f0f0f0f) << 4
        CDEF yzAB uvwx qrst mnop ijkl efgh abcd <-- after OR

        Step 4.
          CD   yz   uv   qr   mn   ij   ef   ab <-- (n & 0xcccccccc) >> 2
        EF   AB   wx   st   op   kl   gh   cd   <-- (n & 0x33333333) << 2
        EFCD AByz wxuv stqr opmn klij ghef cdab <-- after OR

        Step 5.
         E C  A y  w u  s q  o m  k i  g e  c a <-- (n & 0xaaaaaaaa) >> 1
        F D  B z  x v  t r  p n  l j  h f  d b  <-- (n & 0x55555555) << 1
        FEDC BAzy xwvu tsrq ponm lkji hgfe dcba <-- after OR
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


if __name__ == '__main__':
    s = Solution()

    # 00000010100101000001111010011100 => 43261596, 00111001011110000010100101000000 => 964176192
    # 11111111111111111111111111111101 => 4294967293, 10111111111111111111111111111111 => 3221225471

    assert s.reverseBitsBitByBit(int("00000010100101000001111010011100", 2)) == 964176192
    assert s.reverseBitsBitByBit(int("11111111111111111111111111111101", 2)) == 3221225471

    assert s.reverseBitsBinarySearch(int("00000010100101000001111010011100", 2)) == 964176192
    assert s.reverseBitsBinarySearch(int("11111111111111111111111111111101", 2)) == 3221225471
