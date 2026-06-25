from abc import ABC, abstractmethod

#16.1

def ordenar_ultima_letra(lista_palavras: list) -> list:
    return sorted(lista_palavras, key=lambda palavra: palavra[-1].lower() if palavra else "")

if __name__ == "__main__": 
    palavras = ["Java", "Python", "C", "JavaScript", "Ruby", "Go", "HTML"]
    palavras_ordenadas = ordenar_ultima_letra(palavras)
    print(palavras_ordenadas)

#16.2

class ClassGenerator(ABC):
    def generate_class(self) -> str:
        linhas_codigo = []
        linhas_codigo.append(f"public class {self.get_class_name()}{self.get_extends_clause()} {{")

        atributos = self.get_attributes()
        if atributos:
            linhas_codigo.append(atributos)
        linhas_codigo.append(self.get_methods())
        linhas_codigo.append("}")
        retunr "\n".join(linhas_codigo)

