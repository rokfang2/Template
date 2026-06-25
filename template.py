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
        return "\n".join(linhas_codigo)

    @abstractmethod
    def get_class_name(self) -> str:
        """Passo abstrato: Cada subclasse deve fornecer seu próprio nome."""
        pass

    @abstractmethod
    def get_methods(self) -> str:
        """Passo abstrato: Cada subclasse deve implementar seus próprios métodos."""
        pass

    def get_extends_clause(self) -> str:
        return ""

    def get_attributes(self) -> str:
        return ""
    
    #16.3

    
