#include "TApplication.h"
#include "TROOT.h"
#include "TH2F.h"
#include "TF2.h"
#include "TCanvas.h"
#include "TRandom3.h"
#include <iostream>
using namespace std;

void cpp_example2(int samples=10000){
    auto tr = new TRandom3();

    // 2D Gaussian
    auto hist1 = new TH2F("hist1","2D Gaussian;x;y",100,50,150,100,50,150);
    auto fpeak = new TF2("fpeak","exp(-0.5*((x-[0])*(x-[0])/[1]/[1] + (y-[0])*(y-[0])/[1]/[1]))",50,150,50,150);
    fpeak->SetParameters(100,6);
    hist1->FillRandom("fpeak", samples);

    auto tc2 = new TCanvas("c2","Canvas2D");
    tc2->Divide(2,2);

    // Panel 1: original Gaussian
    tc2->cd(1);
    hist1->Draw("COLZ");

    // Panel 2: Gaussian + uniform 2D offset
    auto hist2 = (TH2F*)hist1->Clone("hist2");
    hist2->SetTitle("2D Gaussian+offset;x;y");
    for(int i=0;i<samples/3;++i){
        double x = tr->Uniform(50,150);
        double y = tr->Uniform(50,150);
        hist2->Fill(x,y);
    }
    tc2->cd(2);
    hist2->Draw("COLZ");

    // Panel 3: Gaussian + 1/x^2 baseline in 2D
    auto hist3 = (TH2F*)hist1->Clone("hist3");
    hist3->SetTitle("2D Gaussian+offset2;x;y");
    auto base2 = new TF1("base2","1/x/x",1,11);
    for(int i=0;i<samples*30;++i){
        double x = base2->GetRandom()*10+40;
        double y = base2->GetRandom()*10+40;
        hist3->Fill(x,y);
    }
    tc2->cd(3)->SetLogz();
    hist3->Draw("COLZ");

    // Panel 4: double 2D Gaussian
    auto hist4 = (TH2F*)hist1->Clone("hist4");
    hist4->SetTitle("Double 2D Gaussian;x;y");
    fpeak->SetParameter(1,20);
    hist4->FillRandom("fpeak",samples/2);
    tc2->cd(4);
    hist4->Draw("COLZ");

    tc2->Update();
    tc2->SaveAs("canvas2d_cpp.png");
}

int main(int argc,char **argv){
    int nsamples=10000;
    TApplication theApp("App",&argc,argv);
    if(argc>1) nsamples=atoi(argv[1]);
    cpp_example2(nsamples);
    return 0;
}
