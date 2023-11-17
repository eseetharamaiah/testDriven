import pytest
from sparse_recommender import SparseMatrix

def test_sparseMatrix():
    m = SparseMatrix(3, 4)
    assert m.rows == 3
    assert m.coloumns == 4

def test_sparseMatrix1():
    m = SparseMatrix(4, 3)
    assert m.rows == 4
    assert m.coloumns == 3

def test_set_invalidIndex():
    m = SparseMatrix(2, 2)
    with pytest.raises(ValueError):
        m.set(-1, 1, 1)
    
def test_setGet():
    m = SparseMatrix(3, 4)
    m.set(1, 2, 5)
    assert m.get(1, 2) == 5
    assert m.get(0, 0) == 0

def test_recommend():
    m = SparseMatrix(3, 4)
    m.set(0, 0, 3)
    m.set(1, 2, 2)
    vec = [1, 0, 2, 1]
    recommendations = m.recommend(vec)
    assert recommendations == [3, 4, 0]

def test_recommendN():
    m = SparseMatrix(2, 3)
    vec = [0.5, 0]
    with pytest.raises(ValueError):
        m.recommend(vec)

def test_addMovie():
    m1 = SparseMatrix(2, 3)
    m1.set(0, 0, 2)
    m2 = SparseMatrix(2, 3)
    m2.set(1, 2, 3)
    res = m1.add_movie(m2)
    assert res.get(0, 0) == 2
    assert res.get(1, 2) == 3

def test_addMovieN():
    m1 = SparseMatrix(2, 2)
    m2 = SparseMatrix(3, 3)
    with pytest.raises(ValueError):
        m1.add_movie(m2)
def test_toDense():
    m = SparseMatrix(2, 2)
    m.set(0, 1, 1)
    m.set(1, 0, 2)
    dense = m.toDense()
    assert dense == [[0, 1], [2, 0]]

def test_try():
    m = SparseMatrix(2, 2)
    with pytest.raises(ValueError):
        m.set(2, 2, 3)
    with pytest.raises(ValueError):
        m.get(-1, 1)
    vec = [1, 2, 3] 
    with pytest.raises(ValueError):
        m.recommend(vec)

def test_addMovieN1():
    m1 = SparseMatrix(2, 3)
    m2 = SparseMatrix(2, 2)
    with pytest.raises(ValueError):
        m1.add_movie(m2)

if __name__ == "__main__":
    pytest.main()

