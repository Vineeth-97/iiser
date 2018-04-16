// Program: A bare bone implementation of MC simulation of the Ising model
// Binning analysis
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <iomanip>
#include "observable.h"

// lattice
const int xsize = 10;
const int ysize = 10;
const int nsite = xsize * ysize;
const int max_nb = 4;
const int half_max_nb = max_nb/2;
const int half_nsites = nsite/2;

// model parameters
double J = 1.0;
double beta = 1.0;

// mc parameters
const int num_samples = 50000;
const int warmup = 50000;
const int max_interval = 30;
const int max_bin = 20;
const int sample_per_bin = num_samples/max_bin;

// acceptance ratio
int moves_attempted = 0;
int moves_accepted = 0;

// basis state
// basis_state;
std::vector<std::vector<int> > nn_table;
std::vector<int> basis_state;

// observables
std::vector<double> Temperature;
std::vector<Observable> Energy;
std::vector<Observable> Magnetization;


// function prototypes
void run_simulation(const double& temp);
void init_nntable(const int& xsize, const int& ysize);
void init_basis_state(void);
void generate_next_state(const double& beta);
void print_basis_state(const int& mcs);
double get_energy(void);
double get_magnetization(void);
void print_observables(void);
/*void generate_next_state(void);
void init_observables(void);
void print_observables(void);
*/

int main(int argc, char const *argv[])
{
  // Lattice 

  // nn table
  init_nntable(xsize, ysize);

  // basis state allocate
  basis_state.resize(nsite);

  // seed RNG
  srandom(time(0));
  srand48(time(0));

  // simulation
  int num_point = 20;
  double T = 1.0;
  double stepT = 0.2;
  for (int i=0; i<num_point; ++i) {
    run_simulation(T);
    T += stepT;
  }

  print_observables();

  return 0;
}

void run_simulation(const double& T)
{

  // observables
  Observable energy, magn;
  int sample = 0;
  int bin_sample = 0;

  // beta
  beta = 1.0/T;

  // initial state
  init_basis_state();
  //print_basis_state(0);

  moves_attempted = 0;
  moves_accepted = 0;

  // MC run
  int counter = max_interval;
  std::cout << " starting simulation for T = " << T << std::endl;
  int mcs = 1;
  while (sample < num_samples) {
    //std::cout << "mcs = " << mcs << std::endl;
    for (int mc_move=0; mc_move<nsite; ++mc_move) {
      generate_next_state(beta);
    }
    //print_basis_state(mcs);

    if (mcs >= warmup) {
      if (moves_accepted > half_nsites || counter==max_interval) {
        // measurement
        energy.add_sample(get_energy());
        magn.add_sample(get_magnetization());

        if (++bin_sample >= sample_per_bin) {
          energy.new_bin();
          magn.new_bin();
          bin_sample = 0;
        }
        bin_sample++;
        sample++; 
        moves_accepted = 0;
        counter = 0;
      }
      else counter++;
    }
    mcs++;
  }

  //double accept_ratio = double(moves_accepted)/moves_attempted;
  //std::cout << "T = " << T << " , accept_ratio = " << accept_ratio << std::endl;

  // store values
  Temperature.push_back(T);
  Energy.push_back(energy);
  Magnetization.push_back(magn);

  std::cout << "  done, total mc steps = " <<  mcs << std::endl;
} // one simulation over


// energy
double get_energy(void) 
{
  int nn; 
  int esum = 0;
  for (int i=0; i<nsite; ++i) {
    for (int nb=0; nb<half_max_nb; ++nb) {
      nn = nn_table[i][nb];
      esum += basis_state[i] * basis_state[nn];
    }
  }
  return double(-J* esum);
}

// magnetization
double get_magnetization(void) 
{
  int msum = 0;
  for (int i=0; i<nsite; ++i) {
    msum += basis_state[i]; 
  }
  return double(abs(msum));
}


void init_basis_state(void)
{
  // random state
  for (int i=0; i<nsite; ++i) 
    if (drand48() < 0.5) basis_state[i] = 1; 
    else basis_state[i] = -1;
}

void generate_next_state(const double& beta) 
{
  int nb, site, select_site, isum;
  double W, dE;
  // suggest a new state
  select_site = random()%nsite;
  // transition proby
  isum = 0;
  for (nb=0; nb<max_nb; ++nb) {
    site = nn_table[select_site][nb];
    isum += basis_state[site];
  }
  dE = 2.0 * J * isum * basis_state[select_site];
  W = exp(-beta * dE);
  // acceptance
  moves_attempted++;
  if (drand48() < W) {
    basis_state[select_site] = -basis_state[select_site]; 
    moves_accepted++;
  }
}

void init_nntable(const int& xsize, const int& ysize)
{

  // Numbering scheme for the 2D lattice:
  /*
  *   12   13   14   15      
  *    8    9   10   11      
  *    4    5    6    7     
  *    0    1    2    3    
  *-----------------------------------------*/

  enum nn_dir {right_nn, top_nn, left_nn, bottom_nn};

  // allocate
  int i, nsite; 
  nsite = xsize * ysize;
  nn_table.resize(nsite);
  for (i=0; i<nsite; ++i) nn_table[i].resize(max_nb);

  // Right NNs
  for (i=0; i<nsite; ++i) nn_table[i][right_nn] = i+1;
  // Top NNs
  for (i=0; i<nsite; ++i) nn_table[i][top_nn] = i+xsize;
  // Left NNs
  for (i=0; i<nsite; ++i) nn_table[i][left_nn] = i-1;
  // Bottom NNs
  for (i=0; i<nsite; ++i) nn_table[i][bottom_nn] = i-xsize;

  // Take care of the boundary points
  int xsize_m1 = xsize-1; 
  int m = xsize * (ysize-1);

  // bottom line
  for (i=0; i<xsize; ++i) nn_table[i][bottom_nn] = i + m;
  // right line
  for (i=xsize_m1; i<nsite; i += xsize) nn_table[i][right_nn] = i - xsize_m1;
  // top line
  for (i=m; i<nsite; ++i) nn_table[i][top_nn] = i - m;
  // left line
  for (i=0; i<nsite; i += xsize) nn_table[i][left_nn] = i + xsize_m1;
  // print
  /*for (i=0; i<nsite; ++i) {
    std::cout << "nn_table[i][nn] = " << i << " " << nn_table[i][0] << " " << nn_table[i][1] << " "
    << nn_table[i][2] << " " << nn_table[i][3] << std::endl;
  }*/
}

void print_basis_state(const int& mcs)
{
  int s;
  std::cout << "|state>_"; 
  std::cout << std::left << std::setw(6);
  if (mcs >= 0) std::cout << mcs << std::right;
  else std::cout << ' ' << std::right;
  std::cout << " = |"; 
  //std::cout << "|state> = |"; 
  for (int i=0; i<nsite; ++i) {
    std::cout << std::setw(3) << basis_state[i];
  }
  std::cout << " >" << std::endl; 
}

// #include <iomanip>
void print_observables(void)
{
  std::ofstream fout("results.txt");
  fout << "# Temperature   mag         err        energy         err         samples\n";
  fout << std::fixed << std::showpoint;
  for (int i=0; i<Temperature.size(); ++i) {
    fout << std::setw(12) << Temperature[i];
    fout << std::setw(12) << Magnetization[i].mean()/nsite;
    fout << std::setw(12) << Magnetization[i].stddev()/nsite;
    fout << std::setw(12) << Energy[i].mean()/nsite;
    fout << std::setw(12) << Energy[i].stddev()/nsite;
    fout << std::setw(12) << Energy[i].sample_size();
    fout << std::endl;
  }
  fout.close();
}

