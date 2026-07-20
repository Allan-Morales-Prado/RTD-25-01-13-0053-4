#include <iostream>
#include <string>
#include <stdexcept>
#include <algorithm>
#include <locale>

#ifdef _WIN32
    #include <windows.h>
#endif

class Pelota {
private:
    std::string _color;
    int _tamano;
    std::string _material;

public:
    Pelota(const std::string& color = "Blanco", int tamano = 20, const std::string& material = "Plástico") 
        : _color(color), _material(material) {
        _tamano = std::max(1, tamano);
    }

    std::string getColor() const {
        return _color;
    }

    void setColor(const std::string& valor) {
        if (valor.empty()) {
            throw std::invalid_argument("El color no puede estar vacío");
        }
        _color = valor;
    }

    int getTamano() const {
        return _tamano;
    }

    void setTamano(int valor) {
        _tamano = std::max(1, valor);
    }

    std::string getMaterial() const {
        return _material;
    }

    void setMaterial(const std::string& valor) {
        _material = valor;
    }
};

int main() {
    #ifdef _WIN32
        SetConsoleOutputCP(65001);  // UTF-8 en Windows
    #endif
    std::setlocale(LC_ALL, "es_ES.UTF-8");
    
    try {
        Pelota pelota1("Ñañito", 10, "Caucho");
        Pelota pelota2("Azúl", 15, "Goma");
        
        std::cout << "Pelota 1: " << pelota1.getColor() << ", " 
                  << pelota1.getTamano() << ", " 
                  << pelota1.getMaterial() << std::endl;
        
        pelota1.setColor("Marrón");
        std::cout << "Pelota 1 nuevo color: " << pelota1.getColor() << std::endl;
        
        // Esto lanzará una excepción
        // pelota1.setColor("");

        pelota1.setColor("Gris");
        
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    return 0;
}