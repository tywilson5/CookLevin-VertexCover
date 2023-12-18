from cnf import CNF

def test_book():
    """
    Test out example in Sipser 7.33
    (x0 V x0 V x1) ^ (not x0 V not x1 V not x1) ^ (not x0 V x1 V x1)
    """
    c = CNF()
    c.add_clause([("x0", True), ("x0", True), ("x1", True)])
    c.add_clause([("x0", False),("x1", False),("x1", False)])
    c.add_clause([("x0", False),("x1", True),("x1",True)])
    cert = c.solve()
    assert(c.is_satisfied(cert))
    cert = {"x0":False, "x1":False, "x2":True}
    assert(not c.is_satisfied(cert))

def test_example1():
    """
    Test out the following formula
    (x0 V not x1 V x2) ^ (x0 V x1 V x2) ^ (not x0 V not x1 V not x2) ^ (not x0)
    """
    c = CNF()
    c.add_clause([("x0", True), ("x1", False), ("x2", True)])
    c.add_clause([("x0", True), ("x1", True), ("x2", True)])
    c.add_clause([("x0", False), ("x1", False), ("x2", False)])
    c.add_clause([("x0", False)])
    cert = c.solve()
    assert(c.is_satisfied(cert))

def test_random():
    """
    Test out a bunch of random clauses with 20 variables
    """
    for seed in range(100):
        c = CNF()
        c.init_random_cnf(20, 30, seed)
        cert = c.solve()
        if len(cert) > 0:
            assert(c.is_satisfied(cert))
        else:
            assert(len(c.solve_brute()) == 0)
    
def test_big():
    """
    Test a large problem that's on the order of the 
    largest problems I'd expect students to test
    """
    N = 20
    c = CNF()
    c.init_random_cnf(N**2, N**3, 1)
    cert = c.solve()
    if len(cert) > 0:
        assert(c.is_satisfied(cert))