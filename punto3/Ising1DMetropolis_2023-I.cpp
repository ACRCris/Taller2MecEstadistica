//Muestreo Monte Carlo del modelo de Ising2D en equilibrio canónico usando Metrópolis
// J=1 kb=1
#include <iostream>
#include <cmath>
#include "Random64.h"
using namespace std;

const double kB=1;
const double J=1;

const int N=128;

class SpinSystem{
private:
  int s[N],E,M;
public:
  void InicieTodosAbajo(void);
  void UnPasoDeMetropolis(double Beta,Crandom & Ran64);
  double GetE(void){return E;};
  double GetM(void){return fabs(M);};
};
void SpinSystem::InicieTodosAbajo(void){
  for(int i=0;i<N;i++)  
    s[i]=-1;
  M=-N; E=-N*J;
}
void SpinSystem::UnPasoDeMetropolis(double Beta,Crandom & Ran64){
  int n,i,j; double dE;
  //Escojo un espin al azar;
  i=(int) N*Ran64.r();
  //Calculo el dE que se produciría si lo volteo;
  dE=2*J*s[i]*(s[(i+1)%N]+s[(i+N-1)%N]);
  //Implemento la rata de aceptacion A(x'|x)
  if(dE<=0)
    {s[i]*=-1; E+=dE; M+=2*s[i];} //lo volteo;
  else if(Ran64.r()<exp(-Beta*dE))
    {s[i]*=-1; E+=dE; M+=2*s[i];} //lo volteo;
}

double EpromTeo(double Beta){
  return -J*tanh(Beta);
}

const int teq=3000;//teq=(int)(300*pow(L/8.0,2.125));
const int tcorr=250;//tcorr=(int)(50*pow(L/8.0,2.125));
const int Nmuestras=1000;


int main(void){
  SpinSystem Ising;
  Crandom Ran64(1902);
  double kT,Beta;
  int mcs,mcss,teq,cmuestras;
  double E,M,sumM,sumM2,sumM4,sumE,sumE2;
  double Mprom,M2prom,M4prom,Eprom,E2prom;
  double Cv,Xs,Ubinder;
  
  for(Beta=0.05;Beta<3.5;Beta+=0.25){ //Para cada temperatura
    kT=1.0/Beta;
    //Inicio el sistema
    Ising.InicieTodosAbajo();
    
    //Llegar hasta el equilibrio
    for(mcss=0;mcss<teq;mcss++)
      for(mcs=0;mcs<N;mcs++) // 1 mcss
	Ising.UnPasoDeMetropolis(Beta,Ran64);
    
    //Tomar Nmuestras
    sumM=sumM2=sumM4=sumE=sumE2=0;//Inicio los acumuladores en cero
    for(cmuestras=0;cmuestras<Nmuestras;cmuestras++){
      //Tomo 1 Muestra
      E=Ising.GetE(); M=Ising.GetM();
      //Cargo en los acumuladores
      sumM+=M;   sumM2+=M*M;   sumM4+=M*M*M*M;   sumE+=E;   sumE2+=E*E;
      //Avanzar hasta la siguiente muestra
      for(mcss=0;mcss<tcorr;mcss++)
	for(mcs=0;mcs<N;mcs++) // 1 mcss
	  Ising.UnPasoDeMetropolis(Beta,Ran64);
    }
    
    //Imprimir los resultados
    //Hacer promedios
    Mprom=sumM/Nmuestras; M2prom=sumM2/Nmuestras; M4prom=sumM4/Nmuestras;
    Eprom=sumE/Nmuestras; E2prom=sumE2/Nmuestras;
    //Calcular las cantidades que quiero imprimir
    Cv=kB/(kT*kT)*(E2prom-Eprom*Eprom);
    Xs=Beta*(M2prom-Mprom*Mprom);
    Ubinder=1.0-1.0/3*M4prom/(M2prom*M2prom);
    //Tmprimo
    cout<<Beta<<" "<<Eprom/N<<" "<<EpromTeo(Beta)<<" "<<Mprom<<" "<<Cv<<" "<<Xs<<" "<<Ubinder<<endl;
  } 
  return 0;
}
