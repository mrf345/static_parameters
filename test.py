from unittest import TestCase, main
from static_parameters import (
    function_parameters,
    class_parameters
)


class TestingStaticParameters(TestCase):
    @function_parameters
    def toVerify(self, a, b):
        """ 
        Simple function to verify function_parameters
        ((a: str)) ((b: int)) 
        """
        return a * b

    @function_parameters
    def toVerifyFalse(self, a, b):
        """ 
        Simple function to verify false function_parameters
        ((a: False)) ((b: False))
        """
        return a * b
    
    @class_parameters(
        function_parameters
    )
    class toVerifyClass:
        def toVerify(self, a, b):
            """
            Simple function in class to verify 
            class_parameters (( b : int ))
            (( a:int))
            """
            return a + b
    
    def test_function_parameters(self):
        """ to test with the correct input """
        self.assertEqual(
            self.toVerify('a', 3), 'aaa')

    def test_class_parameters(self):
        """ to test with correct input """
        self.assertEqual(
            self.toVerifyClass().toVerify(1, 1),
            2
        )

    def test_function_parameters_false(self):
        """ to test with the false input """
        try:
            self.toVerify(False, False)
        except Exception as e:
            self.assertEqual(type(e), TypeError)

    def test_function_parameters_false_doc(self):
        try:
            self.toVerifyFalse(False, False)
        except Exception as e:
            self.assertEqual(
                type(e), TypeError
            )

    def test_function_parameters_not_callable(self):
        try:
            function_parameters(False)
        except Exception as e:
            self.assertEqual(
                type(e), TypeError
            )

if __name__ == '__main__':
    main()
