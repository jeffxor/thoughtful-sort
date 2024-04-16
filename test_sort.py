from sort import sort

class TestClass:

    def test_package_with_small_dimensions_and_low_mass(self):
        assert sort(10, 10, 10, 10) == 'STANDARD'

    def test_bulky_package_by_dimensions_with_low_mass(self):
        assert sort(200, 200, 200, 5) == 'SPECIAL'

    def test_bulky_package_by_volume_with_low_mass(self):
        assert sort(100, 100, 100, 5) == 'SPECIAL'

    def test_heavy_package_with_small_dimensions(self):
        assert sort(10, 10, 10, 25) == 'SPECIAL'

    def test_heavy_package_with_bulky_dimensions(self):
        assert sort(200, 200, 200, 25) == 'REJECTED'
