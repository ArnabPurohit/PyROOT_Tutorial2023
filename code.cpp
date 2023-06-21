#include <iostream>

struct Electron {
  int charge;
  double energy;
  double pt;
};

void Print(const Electron& e){
  std::cout << "Charge: "<< e.charge << ", energy: "<< e.energy <<std::endl;
}
