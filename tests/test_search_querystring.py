from redis.commands.search.querystring import geo


def test_geo_querystring_order():
    """Verify geo() produces the correct lon,lat order in the RediSearch filter string.

    RediSearch geo filter syntax is: [longitude latitude radius unit].
    The geo() helper takes (lat, lon, ...) in the conventional order and should
    internally produce the RediSearch-expected (lon, lat, ...) order.
    """
    result = geo(40.71, -74.01, 10, "km")
    assert result.to_string() == "[-74.01 40.71 10 km]"
