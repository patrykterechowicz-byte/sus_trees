from sus_trees.data import load_csv


def test_load_csv():
    csv = "0 1 0 0\n1 0 1 0\n0 0 0 1\n"

    table = load_csv(csv=csv)

    assert table.X == [[False, True, False], [True, False, True], [False, False, False]]
    assert table.Y == [False, False, True]
