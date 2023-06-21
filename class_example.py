import ROOT

cpp_code = """
int sq(int i) {return i*i;}

class Electron{
   private:
      int pdgid = 11;
   public:
      Electron(){std::cout<<"I am an Electron. My PDG ID is "<<pdgid<<"."<<std::endl;}
};
"""

ROOT.gInterpreter.ProcessLine(cpp_code)

a = ROOT.sq(4)
print(a)

x = ROOT.Electron()
