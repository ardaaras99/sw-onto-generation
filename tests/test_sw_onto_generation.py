import sw_onto_generation


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance(sw_onto_generation.__name__, str)
