from unittest import mock
from unittest import TestCase, main
from instructor_unit_test_examples import red_or_blue, average_exam_score, increment_line_number


class TestRedOrBlueFunction(TestCase):

    def test_odd_numbers(self):
        expected = 'Red'
        result = red_or_blue(num=3)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        expected = 'Blue'
        result = red_or_blue(num=54)
        self.assertEqual(expected, result)

    def test_range_6_to_20(self):
        expected = 'Red'
        result = red_or_blue(num=12)
        self.assertEqual(expected, result)


class TestAverageExamScore(TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': 8},
        ]
        expected = 7.25  # (8+8+6+7) / 4

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_missing_mark(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha',},
            {'name': 'Zac', 'mark': 8},
        ]
        expected = 6.5  # (8+5+6+7) / 4 --> use 5 if mark is missing

        result = average_exam_score(my_input)
        self.assertEqual(expected, result)

    def test_calculate_average_error_raised(self):
        my_input = [
            {'name': 'Jane', 'mark': 15},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', },
            {'name': 'Zac', 'mark': '8'},
        ]
        with self.assertRaises(ValueError):
            average_exam_score(my_input)


class TestIncrementLineNumber(TestCase):

    @mock.patch('nano.unit_test_examples.get_file_content')
    def test_mock_file_read_function(self, mock_get_file_content):
        content = [
            '1. Hello',
            '2. Hi',
            '3. Good morning',
        ]
        mock_get_file_content.return_value = content
        self.assertEqual(
            increment_line_number('some_file'),
            4
        )


if __name__ == '__main__':
    main()




