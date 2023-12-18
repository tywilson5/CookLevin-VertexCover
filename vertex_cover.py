"""
Tyler Wilson 
CS373 - Vertex Cover

This program generates a random graph and then solves the vertex cover problem. 
Using the graph, it creates a CNF formula and then uses the glucose solver to solve it.

"""

from cnf import CNF
import numpy as np
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, V, K, seed):
        """
        Initialize a random graph

        Parameters
        ----------
        V: int
            Number of vertices
        seed: int
            Random seed (each seed will give a different graph)
        """
        np.random.seed(seed)
        self.K = K
        self.V = V
        self.edges = set([])
        ## Step 1: Generate a random permutation
        
        perm = np.random.permutation(V)
        for i in range(V):
            # Take out pair of indices in permutation
            i1 = perm[i]
            i2 = perm[(i+1)%V]
            # Add this edge (convention lower index goes first)
            i1, i2 = min(i1, i2), max(i1, i2)
            self.edges.add((i1, i2))

        ## Step 2: Add some additional edges to make the 
        ## problem harder
        
        edges_left = []
        for i in range(V):
            for j in range(i+1, V):
                if (i, j) not in self.edges:
                    edges_left.append((i, j))
        
        E = int(V*(11/2))
        E = min(E, V*(V-1)//2)
        print("{:.3f} %% edges".format(100*E/(V*(V-1)/2)))
        
        for i in range(int(V**(5/4))):
            vertex = np.random.choice(self.K)
            other_vertex = np.random.choice(self.V)
            if (other_vertex != vertex):
                if ((vertex, other_vertex) not in self.edges) & ((other_vertex, vertex) not in self.edges):
                    self.edges.add((vertex, other_vertex))
        
        for i in np.random.permutation(len(edges_left))[0:E-V]:
            self.edges.add(edges_left[i])
        print("E: ", len(self.edges))


    def draw(self, cover=[]):
        """
        Draw the graph, and highlight the vertices in the cover
        
        Parameters
        ----------
        cover: 
            Vertex cover of the graph
        """
        V = self.V
        theta = np.linspace(0, 2*np.pi, V+1)[0:V]
        x = np.cos(theta)
        y = np.sin(theta)
        plt.scatter(x, y, s=100, zorder=100)
        for i in range(V):
            plt.text(x[i]*1.1-0.02, y[i]*1.1-0.05, "{}".format(i))
        ## Draw each edge
        for (i, j) in self.edges:
            plt.plot([x[i], x[j]], [y[i], y[j]], c='k', linewidth=1)
        ## Draw the vertex cover
        for i in range(V):
            if i in cover:
                plt.scatter(x[i], y[i], c='C1', s=100, zorder=101)
        if len(cover) > 0:
            chunk_size = 20
            s = ""
            for k in range(0, len(cover), chunk_size):
                for i in range(min(chunk_size, len(cover)-k)):
                    s += "{}".format(cover[k+i])
                    if k+i < len(cover)-1:
                        s += ","
                s += "\n"
            plt.title(s)
        plt.axis("off")


    def get_at_most_one(self, cnf):
        """
        Fill in the constraint clauses that enforce
        at most one 1 in rows and columns

        Parameters
        ----------
        cnf: CNF
            CNF formula we're building
        """
        V = self.V
        K = self.K
        for i in range(V):
            for j in range(K):
                for k in range(V):
                    # Each row has at most one 1
                    if k != j:
                        cnf.add_clause([((i, j), False), ((i, k), False)])
                    # Each column has at most one 1
                    if k != i and k < K:
                        cnf.add_clause([((i, j), False), ((k, j), False)])


    def get_at_least_one(self, cnf):
        """
        Fill in the constraints that enforce at least one 1 in each row

        Parameters
        ----------
        cnf: CNF
            CNF formula we're building
        """
        V = self.V
        K = self.K
        for i in range(V):
            clause = []
            for j in range(V): #
                clause.append(((i, j), True))
            cnf.add_clause(clause)
    
                    
    def every_edge_covered(self, cnf):
        """
        Fill in the constraints that make sure every edge is covered

        Parameters
        ----------
        cnf: CNF
            CNF formula we're building
        """
        V = self.V
        #not_edges = set([])
        clause = set([]) # use a set so that we don't have opposite literals
        
        for k in range(V-1):
            for (i, j) in self.edges:
                clause.add(((k, i), True)) #X0i V X1i V ... V XV-1i
                clause.add(((k, j), True)) #X0j V X1j V ... V XV-1j
            cnf.add_clause(list(clause)) #for each edge, add a clause
                    
        #cnf.add_clause(clause)      

    def get_cnf_formula(self):
        """
        Do a reduction from this problem to SAT by filling in 
        CNF formulas

        Returns
        -------
        CNF: CNF Formula corresponding to the reduction
        """
        cnf = CNF()
        self.get_at_most_one(cnf)
        self.get_at_least_one(cnf)
        self.every_edge_covered(cnf)
        return cnf

    def solve(self):
        """
        Solve the vertex cover problem using SAT
        
        Returns
        -------
        perm: list
            List of vertices in the vertex cover
        """
        cnf = self.get_cnf_formula()
        cert = cnf.solve_glucose()
        #print(cert)
        
        perm = set([]) # use a set so that we don't have duplicates
        for (i, j), val in cert.items(): 
            if val: 
                perm.add(j) # add j to the vertex cover
                #perm[i] = j

        return list(perm)
    

    def check_cert(self, perm):
        """
        Check if perm is a valid vertex cover

        Parameters
        ----------
        perm: list
            List of vertices in the vertex cover
            
        Returns
        -------
        is_valid: bool
            True if perm is a valid vertex cover, False otherwise
        """
        is_valid = True
        # Step 1: Check that it's a permutation
        if len(np.unique(perm)) != len(perm):
            is_valid = False
            
        # Step 2: Check that every edge is adjacent to at least one vertex
        #for (i, j) in self.edges:
        #    is_valid = is_valid and (i in perm or j in perm)
            
        # Step 3: Check that every vertex not in perm is adjacent to at least one vertex 
        for v in range(self.K):
            if v not in perm:
                is_valid = is_valid and any((v, u) in self.edges or (u, v) in self.edges for u in perm)
            
        return is_valid
        

g = Graph(20,15, 0)
perm = g.solve()
print(g.check_cert(perm))
g.draw(perm)
#CNF.save(g.get_cnf_formula(), "vertex_cover.pkl")
#print(g.get_cnf_formula())
plt.show()