 #!/usr/bin/python3
 """
 Matrix Multiplication Module
 """"


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")


def matrix_mul(m_a, m_b):
        """
        Matrix Multiplication Function
        """
        if type(m_a) != list:
            raise TypeError("m_a must be a list")
        if type(m_b) != list:
            raise TypeError("m_b must be a list")
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")
        