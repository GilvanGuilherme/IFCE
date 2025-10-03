from estoque import Estoque
import menu

def main():
    estoque = Estoque()
    menu.exibir_menu(estoque)

if __name__ == "__main__":
    main()
