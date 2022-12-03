from day3 import main 

def test_solution(capfd):
    
    main() 
    out, err = capfd.readouterr()
    assert out == 'The solution to part 1 is 7821\nThe solution to part 2 is 2752\n'
