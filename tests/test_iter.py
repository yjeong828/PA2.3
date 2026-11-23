from pathlib import Path

def test_iter():
    """Test that the iteration notebook prints the points for each team."""
    notebook = (Path(__file__).parents[1] / "1_iter.ipynb").read_text(
        encoding="utf-8"
    )
    assert "Team green has 5 points." in notebook, \
        "Expected 'Team green has 5 points.' in the notebook output"
    assert "Team red has 9 points." in notebook, \
        "Expected 'Team red has 9 points.' in the notebook output"
    assert "Team blue has 7 points." in notebook, \
        "Expected 'Team blue has 7 points.' in the notebook output"
