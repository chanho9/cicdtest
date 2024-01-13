# 테스트 코드 예시
import unittest
import os
import sys
# 파이썬 인터프리터는 상위폴더를 인식할 수 없음으로 다음과 같이 수정해서 사용 필요
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from my_module.function import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -2), -3)

    def test_add_positive_and_negative_number(self):
        self.assertEqual(add_numbers(-1, 2), 1)

# 테스트 실행
def run_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestAddNumbers)
    unittest.TextTestRunner().run(test_suite)

run_tests()  # 테스트 실행 함수 호출
