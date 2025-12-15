from templates.algo_template import AlgorithmName

def test_basic_case():
    algo = AlgorithmName()
    input_data = [1, 2, 3, 4, 5]
    expected_output = 15  
    assert algo.run(input_data) == expected_output

def test_edge_case_empty():
    algo = AlgorithmName()
    assert algo.run([]) == 0