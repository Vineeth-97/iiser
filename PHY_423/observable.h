#include <iostream>
#include <string>
#include <cstdlib>
#include <iomanip>

class Observable 
{
private:
  int this_bin;
  int num_bin;
  std::vector<int> num_sample;
  std::vector<double> ssum;
  int total_samples;
  double mean_;
  double stddev_;
  bool finalized;

  void finalize(void);
public:
  Observable();
  ~Observable() {};
  void create_bin(void);
  void new_bin(void);
  void clear(void);
  void add_sample(const double& sample);
  double mean(void);
  double stddev(void);
  int sample_size(void);
};

Observable::Observable()
{
  create_bin();
}

void Observable::create_bin(void)
{
  this_bin = 0;
  num_bin = 0;
  total_samples = 0;
  num_sample.push_back(0);
  ssum.push_back(0.0);
  finalized = false;
}

void Observable::new_bin(void)
{
  this_bin++;
  num_sample.push_back(0);
  ssum.push_back(0.0);
}

void Observable::clear(void)
{
  create_bin();
}

void Observable::add_sample(const double& sample)
{
  num_sample[this_bin] += 1;
  ssum[this_bin] += sample;
}

double Observable::mean(void)
{
  if (!finalized) finalize();
  return mean_;
}

double Observable::stddev(void)
{
  if (!finalized) finalize();
  return stddev_;
}

int Observable::sample_size(void)
{
  total_samples = 0;
  for (int bin=0; bin<num_bin; ++bin) 
    total_samples += num_sample[bin];
  return total_samples;
}

void Observable::finalize(void)
{
  num_bin = this_bin + 1;
  // bin averages
  for (int bin=0; bin<num_bin; ++bin) {
    if (num_sample[bin] > 0) ssum[bin] /= num_sample[bin];
  }

  mean_ = 0.0;
  stddev_ = 0.0;
  for (int bin=0; bin<num_bin; ++bin) {
    mean_ += ssum[bin];
    stddev_ += ssum[bin] * ssum[bin];
  }
  mean_ /= num_bin;
  stddev_ /= num_bin;
  if (num_bin > 1)
    stddev_ = sqrt((stddev_ - mean_*mean_)/(num_bin-1));
  else stddev_ = 0.0;
  
  finalized = true;
}



