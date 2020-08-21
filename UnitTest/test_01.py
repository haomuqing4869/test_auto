import unittest
import ddt

# from UnitTest.HelloWorld import hello

# help(unittest)
#
# class Test(unittest.TestCase):
#
#     def test_helloworld(self):
#         result = hello()
#         prospect = 'HelloWorld'
#         self.assertTrue(result == prospect)
#
# if __name__ == '__main__':
#     unittest.main()

data_test = [{"num1":1,"num2":2,"pro":3},{"num1":5,"num2":8,"pro":40}]

@ddt.ddt
class IntegerArithmeticTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("在开始执行测试用例前，只执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("在执行完成测试用例后，只执行一次")

    def setUp(self) -> None:
        print("在每个测试用例执行前，都执行一次")

    def tearDown(self) -> None:
        print("在每个测试用例执行后，都执行一次")

    @ddt.data(*data_test)
    def testAdd(self,test_data):  # test method names begin with 'test'
        """测试加法运算"""
        print("test_add")
        # self.assertEqual((1 + 2), 3)
        # self.assertEqual(0 + 1, 1)
        self.assertEqual(int(test_data['num1'])+int(test_data['num2']),int(test_data['pro']))

    @ddt.data(*data_test)
    def testMultiply(self,test_data):
        """测试乘法运算"""
        print("test_mul")
        # self.assertEqual((0 * 10), 0)
        # self.assertEqual((5 * 8), 40)
        self.assertEqual(int(test_data['num1']) * int(test_data['num2']), int(test_data['pro']))


if __name__ == '__main__':
    unittest.main()
