import ROOT

ROOT.gROOT.ProcessLine('.L code.cpp')

ele = ROOT.Electron

e = ele()

e.charge = -1
e.energy = 55
e.pt = 45

ROOT.TH1F(e)
