from app.load_postcodes import load_postcodes

def test_loading_postcodes():
    postcodes = load_postcodes()
    assert len(postcodes) == 38