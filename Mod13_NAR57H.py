import unittest
from datetime import datetime

#Symbol
1. symbol: capitalized, 1-7 alpha characters
def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

class TestSymbolValidation(unittest.TestCase):
    
    def test_valid_symbols(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("GOOG"))
        self.assertTrue(validate_symbol("MSFT"))
    
    def test_invalid_symbols(self):
        self.assertFalse(validate_symbol("apple"))
        self.assertFalse(validate_symbol("IBM123"))
        self.assertFalse(validate_symbol("AB"))
        self.assertFalse(validate_symbol("ABCDEFGH"))
if __name__ == '__main__':
    unittest.main()

#Chart Type
2. chart type: 1 numeric character, 1 or 2
def validate_chart_type(chart_type):
    return len(chart_type) == 1 and chart_type.isdigit() and chart_type in ['1', '2']

class TestChartTypeValidation(unittest.TestCase):
    
    def test_valid_chart_types(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))
    
    def test_invalid_chart_types(self):
        self.assertFalse(validate_chart_type("0")) 
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("A")) 
        self.assertFalse(validate_chart_type("12"))
        self.assertFalse(validate_chart_type(" "))

if __name__ == '__main__':
    unittest.main()


#Time Series
3. time series: 1 numeric character, 1 - 4
def validate_time_series(time_series):
    return len(time_series) >= 1 and len(time_series) <= 4 and time_series.isdigit()

class TestTimeSeriesValidation(unittest.TestCase):
    
    def test_valid_time_series(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))
    
    def test_invalid_time_series(self):
        self.assertFalse(validate_time_series(""))
        self.assertFalse(validate_time_series("12345"))
        self.assertFalse(validate_time_series("A")) 
        self.assertFalse(validate_time_series(" "))

if __name__ == '__main__':
    unittest.main()

#Start Date
4. start date: date type YYYY-MM-DD
def validate_start_date(start_date):
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestStartDateValidation(unittest.TestCase):
    
    def test_valid_start_dates(self):
        self.assertTrue(validate_start_date("2024-01-01"))
        self.assertTrue(validate_start_date("2023-12-31"))
    
    def test_invalid_start_dates(self):
        self.assertFalse(validate_start_date("24-01-01")) # Incorrect format
        self.assertFalse(validate_start_date("2024-13-01")) # Invalid month
        self.assertFalse(validate_start_date("2024-12-32")) # Invalid day
        self.assertFalse(validate_start_date("2024/01/01")) # Incorrect delimiter
        self.assertFalse(validate_start_date("2024 01 01")) # Incorrect delimiter

if __name__ == '__main__':
    unittest.main()

#End Date
5. end date: date type YYYY-MM-DD
def validate_end_date(end_date):
    try:
        datetime.strptime(end_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestEndDateValidation(unittest.TestCase):
    
    def test_valid_end_dates(self):
        self.assertTrue(validate_end_date("2024-01-01"))
        self.assertTrue(validate_end_date("2023-12-31"))
    
    def test_invalid_end_dates(self):
        self.assertFalse(validate_end_date("24-01-01")) # Incorrect format
        self.assertFalse(validate_end_date("2024-13-01")) # Invalid month
        self.assertFalse(validate_end_date("2024-12-32")) # Invalid day
        self.assertFalse(validate_end_date("2024/01/01")) # Incorrect delimiter
        self.assertFalse(validate_end_date("2024 01 01")) # Incorrect delimiter

if __name__ == '__main__':
    unittest.main()

