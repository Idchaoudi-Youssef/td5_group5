from td5_group5.main import greet

def test_greet(capsys):
    # Appel de la fonction à tester
    greet("Alice")
    
    # Capture de la sortie standard (ce qui est affiché dans le terminal)
    captured = capsys.readouterr()
    
    # Vérification (Assertion)
    assert captured.out == "Bonjour, Alice!\n"
