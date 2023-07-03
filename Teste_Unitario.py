def verifPalind(sentence):
    for l in "!?',;. ":
        sentence = sentence.replace(l, '')
    
    sentence = sentence.lower()
    
    invertido = sentence[::-1]

    if (sentence == invertido):
        palindromo = True
    else:
        palindromo = False
    
    return palindromo

import unittest


### Testes unitarios ###
class TestPalindromo(unittest.TestCase):
    def test_palavra(self):
        self.assertTrue(verifPalind("arara"))
        self.assertFalse(verifPalind("banana"))

    def test_frase(self):
        self.assertTrue(verifPalind("A base do teto desaba"))
        self.assertFalse(verifPalind("Nao e palindromo"))


### Teste automatizado - Pytest ###
def test_palindromo_True():
    assert verifPalind("arara") == True
    assert verifPalind("A base do teto desaba") == True
    
def test_palindromo_False():
    assert verifPalind("banana") == False
    assert verifPalind("Nao e banana") == False



        
        
if __name__ == '__main__':
    unittest.main()
    