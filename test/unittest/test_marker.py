from marker import Marker

class TestMarker(object):
    def test_delete_at_should_return_false_when_guess_not_present(self):
        m = Marker("")
        assert not m.delete_first("5", list("1234"))

    def test_delete_at_should_return_true_when_guess_present(self):
        m = Marker("")
        assert m.delete_first("3", list("1234"))

    def test_delete_at_should_not_delete_when_guess_not_present(self):
        m = Marker("")
        lst = list("1234")
        m.delete_first("5", lst)
        assert list("1234") == lst

    def test_delete_at_should_delete_when_guess_present(self):
        m = Marker("")
        lst = list("1234")
        m.delete_first("3", lst)
        assert list("124") == lst

    def test_exact_match_count_returns_2_for_2_exact_matches(self):
        m = Marker("1234")
        assert m.exact_match_count("1324") == 2

    def test_total_match_count_returns_4_for_4_total_matches(self):
        m = Marker("1234")
        assert m.total_match_count("1324") == 4

    def test_number_match_count_returns_2_for_2_number_matches(self):
        m = Marker("1234")
        assert m.exact_match_count("1324") == 2