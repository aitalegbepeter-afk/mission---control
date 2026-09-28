import unittest
def format_coordinates(lat, lon):
    return f"Lat: {round(float(lat), 2)}, Lon: {round(float(lon), 2)}"
def is_valid_latitude(lat):
    return -90 <= float(lat) <= 90

class TestMissionTools(unittest.TestCase):
   
 def test_format_coordinates(self):
  result = format_coordinates("23.4104", "-102.9556")
  self.assertEqual(result, "Lat: 23.41, Lon: -102.96") 

 def test_valid_latitude(self):
  self.assertTrue(is_valid_latitude("45.0"))
  self.assertFalse(is_valid_latitude("120.0"))

if __name__ == "__main__":
   unittest.main()