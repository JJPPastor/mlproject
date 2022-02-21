from mlproject.distance import haversine

def test_distance():
    assert type(haversine(30, 30, 10, 0)) == float
